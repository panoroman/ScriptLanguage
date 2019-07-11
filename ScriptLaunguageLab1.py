import requests
from bs4 import BeautifulSoup
from collections import deque

start_page = "https://en.wikipedia.org/wiki/Special:Random"
end_page = "https://en.wikipedia.org/wiki/Special:Random"

def get_links(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'html.parser')
    base_url = page[:page.find('/wiki/')]
    links = list({base_url + a['href'] for a in soup.select('p a[href]') if a['href'].startswith('/wiki/')})
    return links

def path(start, end):
    path = {}
    path[start] = [start]
    Q = deque([start])

    while len(Q) != 0:
        page = Q.popleft()
        links = get_links(page)

        for link in links:

            if link == end:
                return path[page] + [link]

            if (link not in path) and (link != page):
                path[link] = path[page] + [link]
                Q.append(link)

            # if len(links) > 10:
            #     print("FAIL")
            #     break
    return None

print(path(start_page, end_page))
print(path(end_page, start_page))