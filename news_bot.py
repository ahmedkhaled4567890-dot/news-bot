import os
import requests
from bs4 import BeautifulSoup

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# رابط قسم مصر من موقع العين الإخبارية
URL = "https://al-ain.com/country/egypt/"

def fetch_latest_news():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # البحث عن عناوين المقالات (عادة تكون داخل وسوم h3 أو روابط العناوين في هذا الموقع)
            # هنبحث عن الـ h3 أو العناصر اللي تحمل عناوين الأخبار
            titles = soup.find_all('h3')
            
            news_list = []
            for title in titles[:3]: # سحب أحدث 3 عناوين مثلاً
                text = title.get_text(strip=True)
                if text and text not in news_list:
                    news_list.append(text)
            
            if news_list:
                formatted_news = "🚨 **أحدث أخبار مصر (العين الإخبارية):**\n\n"
                for i, news in enumerate(news_list, 1):
                    formatted_news += f"{i}. {news}\n\n"
                return formatted_news
                
        return None
    except Exception as e:
        print(f"خطأ في السحب: {e}")
        return None

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
    if news:
        send_telegram_message(news)
    else:
        print("مفيش أخبار جديدة أو لم يتم جلب العناوين.")
