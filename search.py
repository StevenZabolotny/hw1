import re
from bs4 import BeautifulSoup
import google
## Reads in text files
f = open('text.txt')
text = f.read()
f.close()
## Finds occurences of Firstname Lastname
names = re.findall( '[A-Z][a-z]*\s[A-Z][a-z]*', text, flags=0)
## Creates dictionary with name as value and frequency in text as key
names_dict = {}
r = google.search("who played spiderman", tld = 'com', lang = 'en', num = 10, start = 0, stop = 10, pause = 0.0)
for name in names:
    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

if __name__ == "__main__":
    print names_dict
