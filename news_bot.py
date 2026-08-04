import os
import requests
from bs4 import BeautifulSoup

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

URL = "https://al-ain.com/country/egypt/"

def fetch_latest_news():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = soup.find_all('h3')
            
            news_list = []
            for title in titles[:3]:
                text = title.get_text(strip=True)
                if text and text not in news_list:
                    news_list.append(text)
            
            if news_list:
                formatted_news = "🚨 **تنبيه إخباري: تم تشغيل نظام الأتمتة وجلب الأخبار بنجاح!**\n\n**أحدث أخبار مصر (العين الإخبارية):**\n\n"
                for i, news in enumerate(news_list, 1):
                    formatted_news += f"{i}. {news}\n\n"
                return formatted_news
                
        return "🚨 تنبيه إخباري: تم تشغيل نظام الأتمتة، ولكن لم يتم العثور على عناوين جديدة حالياً."
    except Exception as e:
        return f"🚨 حدث خطأ أثناء سحب الأخبار: {e}"

def send_telegram_message(message):
    if not message:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    news = fetch_latest_news()
    send_telegram_message(news)
