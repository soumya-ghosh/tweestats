# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

import sys
from socket import timeout
from threading import Thread
from time import sleep
import urllib2

from tweepy2.models import Status
from tweepy2.api import API
from tweepy2.error import TweepError

from tweepy2.utils import import_simplejson, urlencode_noplus
json = import_simplejson()

STREAM_VERSION = 1


class StreamListener(object):

    def __init__(self, api=None):
        self.api = api or API()

    def on_data(self, data):
        """Called when raw data is received from connection.

        Override this method if you wish to manually handle
        the stream data. Return False to stop stream and close connection.
        """

        if 'in_reply_to_status_id' in data:
            status = Status.parse(self.api, json.loads(data))
            if self.on_status(status) is False:
                return False
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False

    def on_status(self, status):
        """Called when a new status arrives"""
        return

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        return

    def on_limit(self, track):
        """Called when a limitation notice arrvies"""
        return

    def on_error(self, status_code):
        """Called when a non-200 status code is returned"""
        return False

    def on_timeout(self):
        """Called when stream connection times out"""
        return


class Stream(object):

    host = 'stream.twitter.com'

    def __init__(self, auth, listener, **options):
        self.auth = auth
        self.listener = listener
        self.running = False
        self.timeout = options.get("timeout", 300.0)
        self.retry_count = options.get("retry_count")
        self.retry_time = options.get("retry_time", 10.0)
        self.snooze_time = options.get("snooze_time", 5.0)
        self.buffer_size = options.get("buffer_size", 1500)
        self.scheme = "https"
        self.proxy_url = options.get("proxy_url", None)

        self.api = API()
        self.headers = options.get("headers") or {}
        self.parameters = None
        self.body = None

    def _run(self):
        # Authenticate
        url = "%s://%s%s" % (self.scheme, self.host, self.url)

        # Connect and process the stream
        error_counter = 0
        exception = None
        resp = None
        while self.running:
            if self.retry_count is not None and error_counter > self.retry_count:
                # quit if error count greater than retry count
                break
            try:
                if self.body:
                    method = 'POST'
                else:
                    method = 'GET'
                self.auth.apply_auth(url, method, self.headers, self.parameters)
                req = urllib2.Request(url, data=self.body, headers=self.headers)
                if self.proxy_url:
                    proxy_url = 'http://%s' % self.proxy_url
                    proxy_handler = urllib2.ProxyHandler({'http': proxy_url, 'https': proxy_url})
                    opener = urllib2.build_opener(proxy_handler)
                    if sys.version_info >= (2, 6, 0):
                        resp = opener.open(req, timeout=self.timeout)
                    else:
                        resp = opener.open(req)
                else:
                    if sys.version_info >= (2, 6, 0):
                        resp = urllib2.urlopen(req, timeout=self.timeout)
                    else:
                        resp = urllib2.urlopen(req)
                error_counter = 0
                self._read_loop(resp)
            except urllib2.HTTPError, e:
                if self.listener.on_error(e.code) is False:
                    break
                error_counter += 1
                if error_counter > self.retry_count:
                    self.running = False
                    raise e
                sleep(self.retry_time)
            except urllib2.URLError, e:
                if isinstance(e.reason, timeout):
                    if self.listener.on_timeout() is False:
                        break
                    sleep(self.snooze_time)
                else:
                    break
            except Exception, exception:
                # any other exception is fatal, so kill loop
                break
            finally:
                if resp:
                    resp.close()
                resp = None

        # cleanup
        self.running = False

        if exception:
            raise exception

    def _read_loop(self, resp):

        while self.running and not resp.isclosed():

            # Note: keep-alive newlines might be inserted before each length value.
            # read until we get a digit...
            c = '\n'
            while c == '\n' and self.running and not resp.isclosed():
                c = resp.read(1)
            delimited_string = c

            # read rest of delimiter length..
            d = ''
            while d != '\n' and self.running and not resp.isclosed():
                d = resp.read(1)
                delimited_string += d

            # read the next twitter status object
            if delimited_string.strip().isdigit():
                next_status_obj = resp.read( int(delimited_string) )
                self._data(next_status_obj)

            # read data and pass into listener
            if self.listener.on_data(data) is False:
                self.running = False

    def _start(self, async):
        self.running = True
        if async:
            Thread(target=self._run).start()
        else:
            self._run()

    def userstream(self, count=None, async=False):
        self.parameters = {'delimited': 'length'}
        if self.running:
            raise TweepError('Stream object already connected!')
        self.url = '/2/user.json?delimited=length'
        self.host='userstream.twitter.com'
        self._start(async)

    def firehose(self, count=None, async=False):
        self.parameters = {'delimited': 'length'}
        if self.running:
            raise TweepError('Stream object already connected!')
        self.url = '/%i/statuses/firehose.json?delimited=length' % STREAM_VERSION
        if count:
            self.url += '&count=%s' % count
        self._start(async)

    def retweet(self, async=False):
        self.parameters = {'delimited': 'length'}
        if self.running:
            raise TweepError('Stream object already connected!')
        self.url = '/%i/statuses/retweet.json?delimited=length' % STREAM_VERSION
        self._start(async)

    def sample(self, count=None, async=False):
        self.parameters = {'delimited': 'length'}
        if self.running:
            raise TweepError('Stream object already connected!')
        self.url = '/%i/statuses/sample.json?delimited=length' % STREAM_VERSION
        if count:
            self.url += '&count=%s' % count
        self._start(async)

    def filter(self, follow=None, track=None, async=False, locations=None, count=None):
        self.parameters = {}
        self.headers['Content-type'] = "application/x-www-form-urlencoded"
        if self.running:
            raise TweepError('Stream object already connected!')
        self.url = '/%i/statuses/filter.json?delimited=length' % STREAM_VERSION
        if follow:
            self.parameters['follow'] = ','.join(map(str, follow))
        if track:
            self.parameters['track'] = ','.join(map(str, track))
        if locations and len(locations) > 0:
            assert len(locations) % 4 == 0
            self.parameters['locations'] = ','.join(['%.2f' % l for l in locations])
        if count:
            self.parameters['count'] = count
        self.body = urlencode_noplus(self.parameters)
        self.parameters['delimited'] = 'length'
        self._start(async)

    def disconnect(self):
        if self.running is False:
            return
        self.running = False