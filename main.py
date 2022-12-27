from bs4 import BeautifulSoup
import requests
import json





def searchReddit(query):
    query.replace(' ', "%20")
    url = f"https://www.reddit.com/search/?q={query}"
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    req = requests.get(url, headers=head)
    htmlFile = BeautifulSoup(req.text,"html.parser")
    info = []
    cards = htmlFile.find_all('div', attrs={'class': '_2i5O0KNpb9tDq0bsNOZB_Q'})
    for card in cards:
        particular = {}
        particular['title'] = card.find('a').find('h3').text
        spans = card.find_all('span')
        temp = []
        for span in spans:
            temp.append(span.text)
        particular['upvotes'] = temp[-3].replace('upvotes', '').strip()
        particular['comments'] = temp[-2].replace('comments', '').strip()
        particular['awards'] = temp[-1].replace('awards', '').strip()
        info.append(particular)
    return info



query = "india"
data = searchReddit(query)
fileName = "output"
with open(fileName + '.json', 'w') as f:
    json.dump(data,f,indent=4)





# info['title'] = card.find('a').find('h3').text
# subreddit = card.find('a', attrs={'data-testid':"subreddit-name"})
# print(subreddit)

