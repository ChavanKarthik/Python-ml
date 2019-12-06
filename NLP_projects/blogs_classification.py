import urllib.request
from urllib.request import urlopen

from bs4 import BeautifulSoup


def getAllDoxyDonkeyPosts(url, links):
    request1 = urllib.request.Request(url)
    response = urlopen(request1)
    soup = BeautifulSoup(response, "lxml")
    print(soup.find_all('a'))
    for a in soup.find_all('a'):
        try:
            url = a['href']
            title = a['title']
            if title == 'Older Posts':
                print(title, url)
                links.append(url)
                getAllDoxyDonkeyPosts(url, links)
        except:
            title = ""
    return


blogUrl = "http://sur.ly/o/doxydonkey.blogspot.in/AA000014"
links = []
getAllDoxyDonkeyPosts(blogUrl, links)

print(links)
