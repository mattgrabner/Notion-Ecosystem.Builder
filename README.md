# 🌐 Notion Ecosystem Map Automation Tool

## Overview 📜

🚀 Streamline the creation and maintenance of a corporate ecosystem landscape with this automated solution. It seamlessly updates a Notion database with rich company profiles, harnessing the power of web scraping and OpenAI's GPT model to provide summaries. Your Notion workspace becomes a dynamic repository of company information, with minimal manual intervention required.

## Requirements 📋

- Python 3.x
- Pip (Python package installer)
- Notion account with API integration
- OpenAI account with an API key

## Installation 🔧

1. Clone the repository to your local machine.
2. Install the necessary Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Change `.env.example` to `.env`.
4. Populate the `.env` with your Notion and OpenAI credentials:

    ```
    NOTION_API_KEY=your_notion_api_key_here
    OPENAI_API_KEY=your_openai_api_key_here
    ```

## Notion Database Configuration 🗃️

Your Notion database should have these specific columns:

- `URL`: Links to company pages for data extraction
- `Description`: Stores the full scraped content
- `Summary`: GPT-4 generated company summaries go here
- `Company / Organization`: Official company name
- `Category`: Business sector or industry type
- `Active`: Company's operational status

## Usage 🛠️

To initiate the updating process, run the `run.py` script:

    ```
    python run.py
    ```

After inputting your Notion Database ID:

- The script scrapes content from each `URL`.
- The `Description` column gets updated with the new content.
- Summaries crafted by OpenAI's GPT are added to the `Summary` column.

## Important Notes 📝

- Verify that your Notion API token can access the targeted database.
- Safeguard your API keys at all times.

## Notion Page Custom Styling with CSS 🎨

Included is a `style.css` file designed to enhance Notion pages with the elegant aesthetic of the XR Landscape Austria website.

<p align="center">
  <img src="https://assets.super.so/d8fa3248-0b58-4287-a142-d579e10bbd53/uploads/cover/7f5853bc-3fde-48b2-971f-f8a7394856c7.png" alt="XR Landscape Austria Style Preview" width="400">
</p>

### How to Apply the Custom CSS in Super.so

1. Create or access your account at [Super.so](https://super.so/).
2. Link your Notion page to Super.so to make a new site.
3. Within the Super.so site settings, find the **Custom Code** area.
4. Copy the contents of `style.css` from our repository.
5. Paste it into the **Custom CSS** field in the Super.so settings.
6. Save your settings and revel in your Notion page's new look!

## Contributing 🤝

👥 Community contributions are invaluable! Feel free to fork this project and submit pull requests to enhance the tool's capabilities.

## License 📄

The code is released under the MIT License.

> 🚨 Remember to insert real API keys in place of `your_notion_api_key_here` and never commit your `.env` to public repositories.
