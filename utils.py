import re
from bs4 import BeautifulSoup
from google import search


def getqtype(q):
    words = q.split()
    if "who" in words or "Who" in words:
        return "who"
    elif "when" in words or "When" in words:
        return "when"

def get_urls(q):
    results = []
    for url in search(q, tld = 'com', lang = 'en', num=10, start=0, stop=10, pause=2.0):
        print url
        results.append(url)
    return results




# ## Reads in text files
# f = open('text.txt')
# text = f.read()
# # f.close()

# ## Finds occurences of Firstname Lastname
# names = re.findall( '[A-Z][a-z]*\s[A-Z][a-z]*', text, flags=0)

# ## Creates dictionary with name as value and frequency in text as key
# names_dict = {}
# r = google.search("who played spiderman", tld = 'com', lang = 'en', num = 10, start = 0, stop = 10, pause = 0.0)
# for name in names:
#     if name in names_dict:
#         names_dict[name] += 1
#     else:
#         names_dict[name] = 1


