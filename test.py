import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

urlhand = urllib.request.urlopen("https://en.wikipedia.org/wiki/JoJo%27s_Bizarre_Adventure")

# succesful http request returns a 200
print(urlhand.getcode())

# creates a BeautifulSoup class object that takes in 2 instance attributes, the url handler which opens the url and the html parser
soup = BeautifulSoup(urlhand, "lxml")

# we can now access attributes of the the BeautifulSoup class object via dot notation
print(soup.title.text)

print(soup.prettify())

# figure out how to parse main content text using BeautifulSoup
