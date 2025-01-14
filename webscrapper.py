
import requests
from bs4 import BeautifulSoup




quests_list = []

for i in range(1, 901):
    # url goes like this www.wowhead.com/classic/quest=207/*quest-name#comments to read the comments from the quest's url.
    url = 'https://www.wowhead.com/classic/quests'
    html = urlopen(url)

    r = requests.get(url)

    soup = BeautifulSoup(r.html, 'html.parser')
    comment_list = []

    # Code here


    # End work of the code
    comment = [Comments]
    comment_list.append(comment)
