import cgi

from google.appengine.api import users

import webapp2
from tweepy2 import *
from location_selector import *
from location_data import *
from Authenticate import *

import csv


GO_BACK = """\
<input type="submit" value="Try for another city/country" 
        onclick="window.location='/';" />
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
      	self.response.write('<html><body>')
        self.response.write(locselector)
        self.response.write('</html></body>')



class Guestbook(webapp2.RequestHandler):

    def post(self):
        auth = OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = API(auth_handler = auth)
        location = self.request.get('location')
        woeid = locations_to_woeid[location]
        data = api.trends_place(woeid)
        trends = data[0]['trends']
        # names = ['<a href=' + trend['url'] + '>' trend['name'] + '</a>' for trend in trends]
        names = [trend['name'] for trend in trends]
        trends_names = '<br/>'.join(names)
        self.response.write('<html><body><h2>You selected: ')
        self.response.write(cgi.escape(location))
        self.response.write('<br/>Woeid is : ' + str(woeid) + '</h2><br/>')
        self.response.write('<hr><h3/>' + trends_names +'</h3><hr>')
        self.response.write(GO_BACK)
        self.response.write('</body></html>')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/results', Guestbook)
], debug=True)
