import re
from bs4 import BeautifulSoup
from google import search
import urllib


def getqtype(q):
    words = q.split()
    if "who" in words or "Who" in words:
        return "who"
    elif "when" in words or "When" in words:
        return "when"

def get_urls(q):
    results = []
    for url in search(q, tld = 'com', lang = 'en', num=10, start=0, stop=10, pause=0.0):
        results.append(url)
    return results

def get_names(results, question):
    names_dict = {}
    f = open("static/first_names.csv", "r")
    first_names = f.read()
    f.close()
    first_names.split()
    for url in results:
        url_txt = urllib.urlopen(url)
        html = url_txt.read()
        soup = BeautifulSoup(html)
        text = soup.get_text()
        names = re.findall( '[A-Z][a-z]+\s[A-Z][a-z]+', text, flags=0)
        for name in names:
            first_name = name.split(" ")[0]
            if first_name in first_names and (first_name != "The") and (name.lower() not in question.lower()):
                if name in names_dict:
                    names_dict[name] += 1
                else:
                    names_dict[name] = 1
    return names_dict



   

    
        
    




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


