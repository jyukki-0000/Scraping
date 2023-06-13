#!/usr/bin/env python3
import subprocess
import datetime
import time
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Tonamel Shadowverseの検索URL
SHADOWVERSE_URL = "https://tonamel.com/competitions?game=shadowverse&date="

# DiscordのWebhook URLとチャンネルID
WEBHOOK_URL = "WEBHOOK_URL"
CHANNEL_ID = "CHANNEL_ID"

def get_today_date():
    """
    現在の日付をYYYY/MM/DD形式で取得
    """
    return datetime.datetime.now().strftime('%Y/%m/%d')

def scrape_tonamel(driver, url):
    """
    大会情報を取得
    """
    driver.get(url)
    time.sleep(3)

    # 大会情報を抽出
    tournaments = []
    for i in range(1, 11):  # 10個の大会情報を取得
        tournament = {}
        tournament["title"] = driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[{i}]/div/div/a/span').text
        tournament["url"] = driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div[1]/div/div/div[2]/ul/li[{i}]/div/div/a').get_attribute("href")

        # 大会詳細ページに移動して日付を取得
        driver.get(tournament["url"])
        time.sleep(3)
        tournament["date"] = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/dl[1]/dd[1]/span').text

        # 大会一覧に戻るためのURL
        driver.get(url)
        time.sleep(3)

        # 取得した大会の日付が現在の日付と同じ場合のみ、リストに追加
        if tournament["date"].startswith(get_today_date()):
            tournaments.append(tournament)
        else:
            break

    return tournaments

def send_to_discord(url, tournaments):
    """
    大会情報をDiscordに送信
    """
    headers = {"Content-Type": "application/json"}

    # 大会情報がない場合、その旨をDiscordに送信
    if not tournaments:
        payload = {
            "content": "**本日の大会はありません**",
            "tts": False,
        }
        requests.post(url, headers=headers, data=json.dumps(payload))
        return

    # 大会情報がある場合、それぞれをDiscordに送信
    color_list = [0xEE2044, 0xED3B39, 0xEF4836, 0xFF6235]
    embeds = []
    for index, tournament in enumerate(tournaments):
        content = f"{tournament['date']}\n[{tournament['title']}]({tournament['url']})"
        color = color_list[index] if index < len(color_list) else color_list[-1]  # 4つ目以降の色はリストの最後の色に設定
        embeds.append({"color": color, "description": content})

    payload = {
        "embeds": embeds,
    }
    requests.post(url, headers=headers, data=json.dumps(payload))

if __name__ == "__main__":
    s = Service('/path/chromedriver')  # Chromedriverのパスを指定
    driver = webdriver.Chrome(service=s)

    filtered_url = SHADOWVERSE_URL

    if filtered_url:
        tournaments = scrape_tonamel(driver, filtered_url)
        send_to_discord(WEBHOOK_URL, tournaments)

    driver.quit()

subprocess.run(["/usr/local/bin/python3", "/path/share.py"])