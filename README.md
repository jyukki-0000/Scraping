# Tonamel Shadowverse Tournament Bot

Tonamel Shadowverse Tournament Bot is a Python bot that automatically extracts tournament information for Shadowverse held on Tonamel and sends notifications to Discord. It scrapes tournament information for a specific date and sends the information obtained to a designated channel on Discord.

## 🎯 Main Features

- Automatically scrapes tournament information for Shadowverse from Tonamel.
- Sends scraped tournament information to a designated channel on Discord.

## 🚀 Usage

1. Clone this repository.
    ```bash
    git clone https://github.com/<your-github-username>/Tonamel-Shadowverse-Tournament-Bot.git
    ```

2. Install the necessary packages, including selenium and requests.
    ```bash
    pip install selenium requests
    ```

3. Specify the path to your chromedriver. Specifically, modify the section under `if __name__ == "__main__":`.
    ```python
    s = Service('/path/to/your/chromedriver')  # Specify the path to your chromedriver
    ```

4. Set your Discord webhook URL and channel ID.

5. Run the Python script.

## 📖 Code Explanation

- `get_today_date()`

    Gets the current date in 'YYYY/MM/DD' format.

- `scrape_tonamel(driver, url)`

    Scrapes tournament information from the specified URL. It retrieves 10 tournament information and only adds the tournament information of the day to the list.

- `send_to_discord(url, tournaments)`

    Sends tournament information to Discord. If there is no tournament information, it sends a notification to that effect, and if there is tournament information, it sends that information.

## 📝 License

This project is released under the MIT license.

## ⚠️ Disclaimer

This script retrieves information from published web pages. If the specifications of the web page change, there may be a possibility that the script does not work as expected. Also, if inappropriate use is made, the website administrator may take measures such as access restrictions, so please use it with caution.

## 👤 Author

[jyukki-](https://github.com/jyukki-)

If you find any problems or have any questions, please feel free to open an issue.
