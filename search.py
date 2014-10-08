import re
from bs4 import BeautifulSoup
## Reads in text files
f = open('text.txt')
text = f.read()
f.close()
## Finds occurences of Firstname Lastname
names = re.findall( '[A-Z][a-z]*\s[A-Z][a-z]*', text, flags=0)
## Creates dictionary with name as value and frequency in text as key
names_dict = {}
for name in names:
    if name in names_dict:
        names_dict[name] += 1
    else:
        names_dict[name] = 1

if __name__ == "__main__":
    print names_dict
