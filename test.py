import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

urlhand = urllib.request.urlopen("https://en.wikipedia.org/wiki/JoJo%27s_Bizarre_Adventure") # using urllib.request library to handle opening a URL

print(urlhand.getcode()) # succesful http request returns a 200

soup = BeautifulSoup(urlhand, "lxml") # creates a BeautifulSoup class object that takes in 2 instance arguments, the url handler which opens the url (the variable containing all the html information to parse) and the html parser

print(soup.title.text)
print(soup.find("body")) # we can now access attributes of the the BeautifulSoup class object via dot notation
