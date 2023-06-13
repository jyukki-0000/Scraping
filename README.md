# Tonamel Shadowverse大会情報Bot

Tonamel Shadowverse大会情報Botは、Tonamel上で開催されるShadowverseの大会情報を自動的に抽出し、Discordに通知するBotです。特定の日付の大会情報をスクレイピングし、取得した情報をDiscordの指定したチャンネルに送信します。

## 🎯 主な機能

- TonamelからShadowverseの大会情報を自動的にスクレイピングします。
- スクレイピングした大会情報をDiscordの指定チャンネルに通知します。
- Discordに投稿された新しいメッセージを自動的に公開します。

## 🚀 使い方

1. このリポジトリをクローンします。
    ```bash
    git clone https://github.com/<your-github-username>/Tonamel-Shadowverse-Tournament-Bot.git
    ```

2. 必要なパッケージをインストールします。パッケージには、selenium、requests、discordが必要です。
    ```bash
    pip install selenium requests discord
    ```

3. Chromedriverのパスを記載します。具体的には、`if __name__ == "__main__":`以下にある部分を修正します。
    ```python
    s = Service('/path/to/your/chromedriver')  # Chromedriverのパスを指定
    ```

4. DiscordのWebhook URLとチャンネルIDを設定します。

5. Discord Botのトークンを設定します。

6. Pythonのスクリプトを実行します。

## 📖 コード解説

### scraping.py

- `get_today_date()`

    現在の日付を'YYYY/MM/DD'の形式で取得します。

- `scrape_tonamel(driver, url)`

    指定したURLから大会情報をスクレイピングします。10個の大会情報を取得し、その日の大会情報のみをリストに追加します。

- `send_to_discord(url, tournaments)`

    大会情報をDiscordに送信します。大会情報がない場合はその旨を通知し、大会情報がある場合はその情報を送信します。

### share.py

- `on_ready()`

    Botがログインしたときに実行されるイベントハンドラです。

- `on_message(message)`

    新しいメッセージが投稿されたときに実行されるイベントハンドラです。指定したチャンネルIDに新しいメッセージが投稿されたとき、そのメッセージを自動的に公開します。
