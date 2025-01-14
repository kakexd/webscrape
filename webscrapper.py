
import requests
from bs4 import BeautifulSoup


# possible meta pick from the website in example: <meta property="og:url" content="https://www.wowhead.com/classic/quest=626/cortellos-riddle">

quests_list = []

# Splitting URL query into proper layer
quest_src = soup.find('meta property', content='https://www.wowhead.com/classic/quest=')
quest_id = quest_src.split('/')[4]
quest_link = f'https://www.wowhead.com/classic/quest={quest_id}'

for i in range(1, 901):
    # url goes like this www.wowhead.com/classic/quest=207/*quest-name#comments to read the comments from the quest's url.
    url = 'https://www.wowhead.com/classic/quests'
    html = urlopen(url)

    r = requests.get(url)

    soup = BeautifulSoup(r.html, 'html.parser')
    comment_list = []
    quests_list = []

    # Code here


    # End work of the code
    comment = [Comments]
    comment_list.append(comment)
    # quest_ID = []
