from playwright.sync_api import sync_playwright
import csv
import sys
# Base URL
BASE_URL = 'https://www.wowhead.com/classic/quest='

quests_list = []
total_quests = 10

# Function to display a loading bar
def display_loading_bar(current, total, bar_length=40):
    progress = current / total
    block = int(bar_length * progress)
    bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\rProgress: [{bar}] {current}/{total} quests")
    sys.stdout.flush()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for i in range(1, 11):  # Adjust range as needed
        quest_url = f"{BASE_URL}{i}"
        try:
            page.goto(quest_url)
            page.wait_for_timeout(3000)  # Allow time for JavaScript to execute

            # Extract the quest title
            quest_title = page.locator("h1.heading-size-1").inner_text().strip()

            # Extract comments
            comment_elements = page.locator("div.text.comment-body.comment-high-rating")
            comments = [comment.inner_text().strip() for comment in comment_elements.all()]

            # Store the quest data
            quests_list.append({
                'quest_id': i,
                'quest_title': quest_title,
                'quest_url': quest_url,
                'comments': comments
            })

            print(f"Scraped Quest {i}: {quest_title}")

            display_loading_bar(i, total_quests)

        except Exception as e:
            print(f"Error scraping Quest {i}: {e}")

    browser.close()

# Export to CSV
csv_file = 'wowhead_quests_playwright.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quest ID', 'Quest Title', 'Quest URL', 'Comments'])

    for quest in quests_list:
        comments_joined = " | ".join(quest['comments'])
        writer.writerow([quest['quest_id'], quest['quest_title'], quest['quest_url'], comments_joined])

print(f"Data exported to {csv_file}")
