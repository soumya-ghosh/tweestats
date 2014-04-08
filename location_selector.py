locselector = """
<form name="locselector" action="/results" method="post">
      <select id="location-list" name="location">
        <optgroup label="">
            <option  selected  value="Worldwide">Worldwide</option>
          </optgroup><optgroup label="Algeria">
            <option  value="Algeria">Algeria</option><option  value="Algiers">Algiers</option>
          </optgroup><optgroup label="Argentina">
            <option  value="Argentina">Argentina</option><option  value="Buenos Aires">Buenos Aires</option><option  value="Córdoba">Córdoba</option><option  value="Mendoza">Mendoza</option><option  value="Rosario">Rosario</option>
          </optgroup><optgroup label="Australia">
            <option  value="Australia">Australia</option><option  value="Adelaide">Adelaide</option><option  value="Brisbane">Brisbane</option><option  value="Canberra">Canberra</option><option  value="Darwin">Darwin</option><option  value="Melbourne">Melbourne</option><option  value="Perth">Perth</option><option  value="Sydney">Sydney</option>
          </optgroup><optgroup label="Austria">
            <option  value="Austria">Austria</option><option  value="Vienna">Vienna</option>
          </optgroup><optgroup label="Bahrain">
            <option  value="Bahrain">Bahrain</option>
          </optgroup><optgroup label="Belarus">
            <option  value="Belarus">Belarus</option><option  value="Brest">Brest</option><option  value="Gomel">Gomel</option><option  value="Grodno">Grodno</option><option  value="Minsk">Minsk</option>
          </optgroup><optgroup label="Belgium">
            <option  value="Belgium">Belgium</option>
          </optgroup><optgroup label="Brazil">
            <option  value="Brazil">Brazil</option><option  value="Belém">Belém</option><option  value="Belo Horizonte">Belo Horizonte</option><option  value="Brasília">Brasília</option><option  value="Campinas">Campinas</option><option  value="Curitiba">Curitiba</option><option  value="Fortaleza">Fortaleza</option><option  value="Goiânia">Goiânia</option><option  value="Guarulhos">Guarulhos</option><option  value="Manaus">Manaus</option><option  value="Porto Alegre">Porto Alegre</option><option  value="Recife">Recife</option><option  value="Rio de Janeiro">Rio de Janeiro</option><option  value="Salvador">Salvador</option><option  value="São Luís">São Luís</option><option  value="São Paulo">São Paulo</option>
          </optgroup><optgroup label="Canada">
            <option  value="Canada">Canada</option><option  value="Calgary">Calgary</option><option  value="Edmonton">Edmonton</option><option  value="Montreal">Montreal</option><option  value="Ottawa">Ottawa</option><option  value="Quebec">Quebec</option><option  value="Toronto">Toronto</option><option  value="Vancouver">Vancouver</option><option  value="Winnipeg">Winnipeg</option>
          </optgroup><optgroup label="Chile">
            <option  value="Chile">Chile</option><option  value="Concepcion">Concepcion</option><option  value="Santiago">Santiago</option><option  value="Valparaiso">Valparaiso</option>
          </optgroup><optgroup label="Colombia">
            <option  value="Colombia">Colombia</option><option  value="Barranquilla">Barranquilla</option><option  value="Bogotá">Bogotá</option><option  value="Cali">Cali</option><option  value="Medellín">Medellín</option>
          </optgroup><optgroup label="Denmark">
            <option  value="Denmark">Denmark</option>
          </optgroup><optgroup label="Dominican Republic">
            <option  value="Dominican Republic">Dominican Republic</option><option  value="Santo Domingo">Santo Domingo</option>
          </optgroup><optgroup label="Ecuador">
            <option  value="Ecuador">Ecuador</option><option  value="Guayaquil">Guayaquil</option><option  value="Quito">Quito</option>
          </optgroup><optgroup label="Egypt">
            <option  value="Egypt">Egypt</option><option  value="Alexandria">Alexandria</option><option  value="Cairo">Cairo</option><option  value="Giza">Giza</option>
          </optgroup><optgroup label="France">
            <option  value="France">France</option><option  value="Bordeaux">Bordeaux</option><option  value="Lille">Lille</option><option  value="Lyon">Lyon</option><option  value="Marseille">Marseille</option><option  value="Montpellier">Montpellier</option><option  value="Nantes">Nantes</option><option  value="Paris">Paris</option><option  value="Rennes">Rennes</option><option  value="Strasbourg">Strasbourg</option><option  value="Toulouse">Toulouse</option>
          </optgroup><optgroup label="Germany">
            <option  value="Germany">Germany</option><option  value="Berlin">Berlin</option><option  value="Bremen">Bremen</option><option  value="Cologne">Cologne</option><option  value="Dortmund">Dortmund</option><option  value="Dresden">Dresden</option><option  value="Dusseldorf">Dusseldorf</option><option  value="Essen">Essen</option><option  value="Frankfurt">Frankfurt</option><option  value="Hamburg">Hamburg</option><option  value="Leipzig">Leipzig</option><option  value="Munich">Munich</option><option  value="Stuttgart">Stuttgart</option>
          </optgroup><optgroup label="Ghana">
            <option  value="Ghana">Ghana</option><option  value="Accra">Accra</option><option  value="Kumasi">Kumasi</option>
          </optgroup><optgroup label="Greece">
            <option  value="Greece">Greece</option><option  value="Athens">Athens</option><option  value="Thessaloniki">Thessaloniki</option>
          </optgroup><optgroup label="Guatemala">
            <option  value="Guatemala">Guatemala</option><option  value="Guatemala City">Guatemala City</option>
          </optgroup><optgroup label="India">
            <option  value="India">India</option><option  value="Ahmedabad">Ahmedabad</option><option  value="Amritsar">Amritsar</option><option  value="Bangalore">Bangalore</option><option  value="Bhopal">Bhopal</option><option  value="Chennai">Chennai</option><option  value="Delhi">Delhi</option><option  value="Hyderabad">Hyderabad</option><option  value="Indore">Indore</option><option  value="Jaipur">Jaipur</option><option  value="Kanpur">Kanpur</option><option  value="Kolkata">Kolkata</option><option  value="Lucknow">Lucknow</option><option  value="Mumbai">Mumbai</option><option  value="Nagpur">Nagpur</option><option  value="Patna">Patna</option><option  value="Pune">Pune</option><option  value="Rajkot">Rajkot</option><option  value="Ranchi">Ranchi</option><option  value="Srinagar">Srinagar</option><option  value="Surat">Surat</option><option  value="Thane">Thane</option>
          </optgroup><optgroup label="Indonesia">
            <option  value="Indonesia">Indonesia</option><option  value="Bandung">Bandung</option><option  value="Bekasi">Bekasi</option><option  value="Depok">Depok</option><option  value="Jakarta">Jakarta</option><option  value="Makassar">Makassar</option><option  value="Medan">Medan</option><option  value="Palembang">Palembang</option><option  value="Pekanbaru">Pekanbaru</option><option  value="Semarang">Semarang</option><option  value="Surabaya">Surabaya</option><option  value="Tangerang">Tangerang</option>
          </optgroup><optgroup label="Ireland">
            <option  value="Ireland">Ireland</option><option  value="Cork">Cork</option><option  value="Dublin">Dublin</option><option  value="Galway">Galway</option>
          </optgroup><optgroup label="Israel">
            <option  value="Israel">Israel</option><option  value="Haifa">Haifa</option><option  value="Jerusalem">Jerusalem</option><option  value="Tel Aviv">Tel Aviv</option>
          </optgroup><optgroup label="Italy">
            <option  value="Italy">Italy</option><option  value="Bologna">Bologna</option><option  value="Genoa">Genoa</option><option  value="Milan">Milan</option><option  value="Naples">Naples</option><option  value="Palermo">Palermo</option><option  value="Rome">Rome</option><option  value="Turin">Turin</option>
          </optgroup><optgroup label="Japan">
            <option  value="Japan">Japan</option><option  value="Chiba">Chiba</option><option  value="Fukuoka">Fukuoka</option><option  value="Hamamatsu">Hamamatsu</option><option  value="Hiroshima">Hiroshima</option><option  value="Kawasaki">Kawasaki</option><option  value="Kitakyushu">Kitakyushu</option><option  value="Kobe">Kobe</option><option  value="Kumamoto">Kumamoto</option><option  value="Kyoto">Kyoto</option><option  value="Nagoya">Nagoya</option><option  value="Niigata">Niigata</option><option  value="Okayama">Okayama</option><option  value="Okinawa">Okinawa</option><option  value="Osaka">Osaka</option><option  value="Sagamihara">Sagamihara</option><option  value="Saitama">Saitama</option><option  value="Sapporo">Sapporo</option><option  value="Sendai">Sendai</option><option  value="Takamatsu">Takamatsu</option><option  value="Tokyo">Tokyo</option><option  value="Yokohama">Yokohama</option>
          </optgroup><optgroup label="Jordan">
            <option  value="Jordan">Jordan</option><option  value="Amman">Amman</option>
          </optgroup><optgroup label="Kenya">
            <option  value="Kenya">Kenya</option><option  value="Mombasa">Mombasa</option><option  value="Nairobi">Nairobi</option>
          </optgroup><optgroup label="Korea">
            <option  value="Korea">Korea</option><option  value="Ansan">Ansan</option><option  value="Bucheon">Bucheon</option><option  value="Busan">Busan</option><option  value="Changwon">Changwon</option><option  value="Daegu">Daegu</option><option  value="Daejeon">Daejeon</option><option  value="Goyang">Goyang</option><option  value="Gwangju">Gwangju</option><option  value="Incheon">Incheon</option><option  value="Seongnam">Seongnam</option><option  value="Seoul">Seoul</option><option  value="Suwon">Suwon</option><option  value="Ulsan">Ulsan</option><option  value="Yongin">Yongin</option>
          </optgroup><optgroup label="Kuwait">
            <option  value="Kuwait">Kuwait</option>
          </optgroup><optgroup label="Latvia">
            <option  value="Latvia">Latvia</option><option  value="Riga">Riga</option>
          </optgroup><optgroup label="Lebanon">
            <option  value="Lebanon">Lebanon</option>
          </optgroup><optgroup label="Malaysia">
            <option  value="Malaysia">Malaysia</option><option  value="Hulu Langat">Hulu Langat</option><option  value="Ipoh">Ipoh</option><option  value="Johor Bahru">Johor Bahru</option><option  value="Kajang">Kajang</option><option  value="Klang">Klang</option><option  value="Kuala Lumpur">Kuala Lumpur</option><option  value="Petaling">Petaling</option>
          </optgroup><optgroup label="Mexico">
            <option  value="Mexico">Mexico</option><option  value="Acapulco">Acapulco</option><option  value="Aguascalientes">Aguascalientes</option><option  value="Chihuahua">Chihuahua</option><option  value="Ciudad Juarez">Ciudad Juarez</option><option  value="Culiacán">Culiacán</option><option  value="ecatepec-de-morelos">Ecatepec de Morelos</option><option  value="guadalajara">Guadalajara</option><option  value="Hermosillo">Hermosillo</option><option  value="León">León</option><option  value="Mérida">Mérida</option><option  value="Mexicali">Mexicali</option><option  value="Mexico City">Mexico City</option><option  value="Monterrey">Monterrey</option><option  value="Morelia">Morelia</option><option  value="Naucalpan de Juárez">Naucalpan de Juárez</option><option  value="Nezahualcóyotl">Nezahualcóyotl</option><option  value="Puebla">Puebla</option><option  value="Querétaro">Querétaro</option><option  value="Saltillo">Saltillo</option><option  value="San Luis Potosí">San Luis Potosí</option><option  value="Tijuana">Tijuana</option><option  value="Toluca">Toluca</option><option  value="Zapopan">Zapopan</option>
          </optgroup><optgroup label="Netherlands">
            <option  value="Netherlands">Netherlands</option><option  value="Amsterdam">Amsterdam</option><option  value="Den Haag">Den Haag</option><option  value="Rotterdam">Rotterdam</option><option  value="Utrecht">Utrecht</option>
          </optgroup><optgroup label="New Zealand">
            <option  value="New Zealand">New Zealand</option><option  value="Auckland">Auckland</option>
          </optgroup><optgroup label="Nigeria">
            <option  value="Nigeria">Nigeria</option><option  value="Benin City">Benin City</option><option  value="Ibadan">Ibadan</option><option  value="Kaduna">Kaduna</option><option  value="Kano">Kano</option><option  value="Lagos">Lagos</option><option  value="Port Harcourt">Port Harcourt</option>
          </optgroup><optgroup label="Norway">
            <option  value="Norway">Norway</option><option  value="Bergen">Bergen</option><option  value="Oslo">Oslo</option>
          </optgroup><optgroup label="Oman">
            <option  value="Oman">Oman</option><option  value="Muscat">Muscat</option>
          </optgroup><optgroup label="Pakistan">
            <option  value="Pakistan">Pakistan</option><option  value="Faisalabad">Faisalabad</option><option  value="Karachi">Karachi</option><option  value="Lahore">Lahore</option><option  value="Multan">Multan</option><option  value="Rawalpindi">Rawalpindi</option>
          </optgroup><optgroup label="Panama">
            <option  value="Panama">Panama</option>
          </optgroup><optgroup label="Peru">
            <option  value="Peru">Peru</option><option  value="Lima">Lima</option>
          </optgroup><optgroup label="Philippines">
            <option  value="Philippines">Philippines</option><option  value="Antipolo">Antipolo</option><option  value="Cagayan de Oro">Cagayan de Oro</option><option  value="Calocan">Calocan</option><option  value="Cebu City">Cebu City</option><option  value="Davao City">Davao City</option><option  value="Makati">Makati</option><option  value="Manila">Manila</option><option  value="Pasig">Pasig</option><option  value="Quezon City">Quezon City</option><option  value="Taguig">Taguig</option><option  value="Zamboanga City">Zamboanga City</option>
          </optgroup><optgroup label="Poland">
            <option  value="Poland">Poland</option><option  value="Gdansk">Gdansk</option><option  value="Kraków">Kraków</option><option  value="Lodz">Lodz</option><option  value="Poznan">Poznan</option><option  value="Warsaw">Warsaw</option><option  value="Wroclaw">Wroclaw</option>
          </optgroup><optgroup label="Portugal">
            <option  value="Portugal">Portugal</option>
          </optgroup><optgroup label="Puerto Rico">
            <option  value="Puerto Rico">Puerto Rico</option>
          </optgroup><optgroup label="Qatar">
            <option  value="Qatar">Qatar</option>
          </optgroup><optgroup label="Russia">
            <option  value="Russia">Russia</option><option  value="Chelyabinsk">Chelyabinsk</option><option  value="Irkutsk">Irkutsk</option><option  value="Kazan">Kazan</option><option  value="Khabarovsk">Khabarovsk</option><option  value="Krasnodar">Krasnodar</option><option  value="Krasnoyarsk">Krasnoyarsk</option><option  value="Moscow">Moscow</option><option  value="Nizhny Novgorod">Nizhny Novgorod</option><option  value="Novosibirsk">Novosibirsk</option><option  value="Omsk">Omsk</option><option  value="Perm">Perm</option><option  value="Rostov-on-Don">Rostov-on-Don</option><option  value="Saint Petersburg">Saint Petersburg</option><option  value="Samara">Samara</option><option  value="Ufa">Ufa</option><option  value="Vladivostok">Vladivostok</option><option  value="Volgograd">Volgograd</option><option  value="Voronezh">Voronezh</option><option  value="Yekaterinburg">Yekaterinburg</option>
          </optgroup><optgroup label="Saudi Arabia">
            <option  value="Saudi Arabia">Saudi Arabia</option><option  value="Ahsa">Ahsa</option><option  value="Dammam">Dammam</option><option  value="Jeddah">Jeddah</option><option  value="Mecca">Mecca</option><option  value="Medina">Medina</option><option  value="Riyadh">Riyadh</option>
          </optgroup><optgroup label="Singapore">
            <option  value="Singapore">Singapore</option>
          </optgroup><optgroup label="South Africa">
            <option  value="South Africa">South Africa</option><option  value="Cape Town">Cape Town</option><option  value="Durban">Durban</option><option  value="Johannesburg">Johannesburg</option><option  value="Port Elizabeth">Port Elizabeth</option><option  value="Pretoria">Pretoria</option><option  value="Soweto">Soweto</option>
          </optgroup><optgroup label="Spain">
            <option  value="Spain">Spain</option><option  value="Barcelona">Barcelona</option><option  value="Bilbao">Bilbao</option><option  value="Las Palmas">Las Palmas</option><option  value="Madrid">Madrid</option><option  value="Malaga">Malaga</option><option  value="Murcia">Murcia</option><option  value="Palma">Palma</option><option  value="Seville">Seville</option><option  value="Valencia">Valencia</option><option  value="Zaragoza">Zaragoza</option>
          </optgroup><optgroup label="Sweden">
            <option  value="Sweden">Sweden</option><option  value="Gothenburg">Gothenburg</option><option  value="Stockholm">Stockholm</option>
          </optgroup><optgroup label="Switzerland">
            <option  value="Switzerland">Switzerland</option><option  value="Geneva">Geneva</option><option  value="Lausanne">Lausanne</option><option  value="Zurich">Zurich</option>
          </optgroup><optgroup label="Thailand">
            <option  value="Thailand">Thailand</option><option  value="Bangkok">Bangkok</option>
          </optgroup><optgroup label="Turkey">
            <option  value="Turkey">Turkey</option><option  value="Adana">Adana</option><option  value="Ankara">Ankara</option><option  value="Antalya">Antalya</option><option  value="Bursa">Bursa</option><option  value="Diyarbakr">Diyarbakir</option><option  value="Eskisehir">Eskisehir</option><option  value="Gaziantep">Gaziantep</option><option  value="Istanbul">Istanbul</option><option  value="Izmir">Izmir</option><option  value="Kayseri">Kayseri</option><option  value="Konya">Konya</option><option  value="Mersin">Mersin</option>
          </optgroup><optgroup label="Ukraine">
            <option  value="Ukraine">Ukraine</option><option  value="Dnipropetrovsk">Dnipropetrovsk</option><option  value="Donetsk">Donetsk</option><option  value="Kharkiv">Kharkiv</option><option  value="Kyiv">Kyiv</option><option  value="Lviv">Lviv</option><option  value="Odesa">Odesa</option><option  value="Zaporozhye">Zaporozhye</option>
          </optgroup><optgroup label="United Arab Emirates">
            <option  value="United Arab Emirates">United Arab Emirates</option><option  value="Abu Dhabi">Abu Dhabi</option><option  value="Dubai">Dubai</option><option  value="Sharjah">Sharjah</option>
          </optgroup><optgroup label="United Kingdom">
            <option  value="United Kingdom">United Kingdom</option><option  value="Belfast">Belfast</option><option  value="Birmingham">Birmingham</option><option  value="Blackpool">Blackpool</option><option  value="Bournemouth">Bournemouth</option><option  value="Brighton">Brighton</option><option  value="Bristol">Bristol</option><option  value="Cardiff">Cardiff</option><option  value="Coventry">Coventry</option><option  value="Derby">Derby</option><option  value="Edinburgh">Edinburgh</option><option  value="Glasgow">Glasgow</option><option  value="Hull">Hull</option><option  value="Leeds">Leeds</option><option  value="Leicester">Leicester</option><option  value="Liverpool">Liverpool</option><option  value="London">London</option><option  value="Manchester">Manchester</option><option  value="Middlesbrough">Middlesbrough</option><option  value="Newcastle">Newcastle</option><option  value="Nottingham">Nottingham</option><option  value="Plymouth">Plymouth</option><option  value="Portsmouth">Portsmouth</option><option  value="Preston">Preston</option><option  value="Sheffield">Sheffield</option><option  value="Stoke-on-Trent">Stoke-on-Trent</option><option  value="Swansea">Swansea</option>
          </optgroup><optgroup label="United States">
            <option  value="United States">United States</option><option  value="Albuquerque">Albuquerque</option><option  value="Atlanta">Atlanta</option><option  value="Austin">Austin</option><option  value="Baltimore">Baltimore</option><option  value="Baton Rouge">Baton Rouge</option><option  value="Birmingham">Birmingham</option><option  value="Boston">Boston</option><option  value="Charlotte">Charlotte</option><option  value="Chicago">Chicago</option><option  value="Cincinnati">Cincinnati</option><option  value="Cleveland">Cleveland</option><option  value="Colorado Springs">Colorado Springs</option><option  value="Columbus">Columbus</option><option  value="Dallas-ft. Worth">Dallas-Ft. Worth</option><option  value="Denver">Denver</option><option  value="Detroit">Detroit</option><option  value="El Paso">El Paso</option><option  value="Fresno">Fresno</option><option  value="Greensboro">Greensboro</option><option  value="Harrisburg">Harrisburg</option><option  value="Honolulu">Honolulu</option><option  value="Houston">Houston</option><option  value="Indianapolis">Indianapolis</option><option  value="Jackson">Jackson</option><option  value="Jacksonville">Jacksonville</option><option  value="Kansas City">Kansas City</option><option  value="Las Vegas">Las Vegas</option><option  value="Long Beach">Long Beach</option><option  value="Los Angeles">Los Angeles</option><option  value="Louisville">Louisville</option><option  value="Memphis">Memphis</option><option  value="Mesa">Mesa</option><option  value="Miami">Miami</option><option  value="Milwaukee">Milwaukee</option><option  value="Minneapolis">Minneapolis</option><option  value="Nashville">Nashville</option><option  value="New Haven">New Haven</option><option  value="New Orleans">New Orleans</option><option  value="New York">New York</option><option  value="Norfolk">Norfolk</option><option  value="Oklahoma City">Oklahoma City</option><option  value="Omaha">Omaha</option><option  value="Orlando">Orlando</option><option  value="Philadelphia">Philadelphia</option><option  value="Phoenix">Phoenix</option><option  value="Pittsburgh">Pittsburgh</option><option  value="Portland">Portland</option><option  value="Providence">Providence</option><option  value="Raleigh">Raleigh</option><option  value="Richmond">Richmond</option><option  value="Sacramento">Sacramento</option><option  value="Salt Lake City">Salt Lake City</option><option  value="San Antonio">San Antonio</option><option  value="San Diego">San Diego</option><option  value="San Francisco">San Francisco</option><option  value="San Jose">San Jose</option><option  value="Seattle">Seattle</option><option  value="St. Louis">St. Louis</option><option  value="Tallahassee">Tallahassee</option><option  value="Tampa">Tampa</option><option  value="Tucson">Tucson</option><option  value="Virginia Beach">Virginia Beach</option><option  value="Washington">Washington</option>
          </optgroup><optgroup label="Venezuela">
            <option  value="Venezuela">Venezuela</option><option  value="BarcelonaV">Barcelona</option><option  value="Barquisimeto">Barquisimeto</option><option  value="Caracas">Caracas</option><option  value="Ciudad Guayana">Ciudad Guayana</option><option  value="Maracaibo">Maracaibo</option><option  value="Maracay">Maracay</option><option  value="Maturin">Maturín</option><option  value="Turmero">Turmero</option><option  value="Valencia">Valencia</option>
          </optgroup><optgroup label="Vietnam">
            <option  value="Vietnam">Vietnam</option><option  value="Can Tho">Can Tho</option><option  value="Da Nang">Da Nang</option><option  value="Hai Phong">Hai Phong</option><option  value="hanoi">Hanoi</option><option  value="Ho Chi Minh City">Ho Chi Minh City</option>
          </optgroup>
      </select>
      <input class="submit" type="submit" value="Fetch">
      </form>
"""