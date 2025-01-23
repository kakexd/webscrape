import requests
from bs4 import BeautifulSoup
import csv
import sys
import time

# Base URL for Wowhead Classic quests
BASE_URL = 'https://www.wowhead.com/classic/quest='

quests_list = []
comment_list = []

# Function to display a loading bar
def display_loading_bar(current, total, bar_length=40):
    progress = current / total
    block = int(bar_length * progress)
    bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\rProgress: [{bar}] {current}/{total} quests")
    sys.stdout.flush()

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
    
    # Update the loading bar
    display_loading_bar(i, 900)
    time.sleep(0.01)  # Optional delay to make progress more noticeable

# Export data to CSV
csv_file = 'wowhead_quests.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Quest ID', 'Quest Title', 'Quest URL', 'Comments'])

    # Write the quest data
    for quest in quests_list:
        comments_joined = " | ".join(quest['comments'])  # Join comments with a delimiter
        writer.writerow([quest['quest_id'], quest['quest_title'], quest['quest_url'], comments_joined])

print(f"\nData exported to {csv_file}")
