import os
import requests
import sys
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def scrape_url_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup.get_text()

def update_notion_page(page_id, description):
    NOTION_API_KEY = os.getenv('NOTION_API_KEY')
    if NOTION_API_KEY is None:
        raise ValueError("No Notion API key provided. Please set the NOTION_API_KEY environment variable.")
    headers = {
        "Authorization": "Bearer " + NOTION_API_KEY,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }
    update_url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "properties": {
            "Description": {
                "type": "rich_text",
                "rich_text": [{"type": "text", "text": {"content": description}}]
            }
        }
    }
    res = requests.patch(update_url, headers=headers, json=payload)
    res.raise_for_status()

def iterate_notion_database(database_id):
    NOTION_API_KEY = os.getenv('NOTION_API_KEY')
    if NOTION_API_KEY is None:
        raise ValueError("No Notion API key provided. Please set the NOTION_API_KEY environment variable.")

    print(f"Using Notion API key: {NOTION_API_KEY}")

    headers = {
        "Authorization": "Bearer " + NOTION_API_KEY,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }
    
    query_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    print(f"Querying Notion database with ID: {database_id}")

    try:
        res = requests.post(query_url, headers=headers)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while querying the Notion database: {e}")
        sys.exit(1)

    pages = data.get('results', [])
    if not pages:
        print("No pages found in the database.")
        return

    for page in pages:
        page_id = page.get('id')
        print(f"Processing page: {page_id}")

        properties = page.get('properties', {})
        description_data = properties.get('Description', {}).get('rich_text', [])
        description = description_data[0].get('plain_text', '') if description_data else ''

        # Check for the URL under the "super:Link" property
        url = properties.get('super:Link', {}).get('url', '')
        if not description and url:
            print(f"Scraping content from URL: {url}")
            try:
                scraped_content = scrape_url_content(url)
                print(f"Updating Notion page {page_id} with scraped content.")
                update_notion_page(page_id, scraped_content)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while scraping URL content: {e}")
        elif not description:
            print(f"No 'super:Link' URL found for page {page_id}, skipping.")
        else:
            print(f"Page {page_id} already has a description, skipping.")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scrape-summary.py <Notion Database ID>")
        print("Please provide the Notion Database ID as an argument when calling the script.")
        sys.exit(1)
    database_id = sys.argv[1]
    iterate_notion_database(database_id)
