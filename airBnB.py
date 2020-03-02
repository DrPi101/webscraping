#!/usr/bin/python3

from bs4 import BeautifulSoup

import urllib.request



county = 'South-West-England--UK'

checkin = '2019-12-30'

checkout = '2019-12-31'

adults = '/homes?adults=2&children=0&infants=0'



url = 'https://www.airbnb.co.uk/s/' +county+  '/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&source=$



request = urllib.request.Request(url)

response = urllib.request.urlopen(request)



soup = BeautifulSoup(response.read(),features="html.parser")



print ("County : " + county)

print ("Checkin : " + checkin)

print ("Checkout : " + checkout)



list2 = soup.findAll('div', attrs={'class': "_1ebt2xej"})

for i in list2:

 print(i.text)



for url in soup.findAll('a', class_ ="_i24ijs"):

  print("https://airbnb.co.uk" + url['href'])
