import requests
from bs4 import BeautifulSoup

# Base URL for Wowhead Classic quests
BASE_URL = 'https://www.wowhead.com/classic/quest='

quests_list = []
comment_list = []

# Iterate over the range of quest IDs to fetch data
for i in range(1, 901):
    quest_url = f'{BASE_URL}{i}'
    
    try:
        # Send a GET request to the quest URL
        response = requests.get(quest_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract quest title (example: <h1 class="heading-size-1">Quest Title</h1>)
        quest_title_tag = soup.find('h1', class_='heading-size-1')
        quest_title = quest_title_tag.text.strip() if quest_title_tag else f"Quest {i}"

        # Extract comments (example structure: <div class="comment">Comment text</div>)
        comments = []
        comment_tags = soup.find_all('div', class_='comment')
        for tag in comment_tags:
            comments.append(tag.text.strip())

        # Add the quest and its details to the lists
        quests_list.append({
            'quest_id': i,
            'quest_title': quest_title,
            'quest_url': quest_url,
            'comments': comments
        })

        # Add comments to the global comment list (optional, if needed)
        comment_list.extend(comments)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching quest {i}: {e}")
    
# Output the data (replace this with saving to a file or database as needed)
for quest in quests_list:
    print(f"Quest ID: {quest['quest_id']}")
    print(f"Title: {quest['quest_title']}")
    print(f"URL: {quest['quest_url']}")
    print("Comments:")
    for comment in quest['comments']:
        print(f"- {comment}")
    print("\n--------------------\n")