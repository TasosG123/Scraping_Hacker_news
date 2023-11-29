import requests
from bs4 import BeautifulSoup
from pprint import pprint



res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2') # results for the second page as well

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser') # results for the second page as well

links = soup.select('.titleline > a') 
subtext = soup.select('.subtext')

links2 = soup2.select('.titleline > a') # results for the second page as well
subtext2 = soup2.select('.subtext')

mega_links = links + links2 # results for the second page as well
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True) #function to sort by votes

def create_custom_hn(links , subtext):
    hn = []
    for idx , item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint(create_custom_hn(mega_links , mega_subtext))
