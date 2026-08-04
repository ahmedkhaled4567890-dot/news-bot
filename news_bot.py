import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("تم إرسال الرسالة بنجاح!")
    else:
        print(f"فشل الإرسال: {response.text}")

if __name__ == "__main__":
    news_text = "🚨 **تنبيه إخباري:** تم تشغيل نظام الأتمتة وجلب الأخبار بنجاح عبر سكريبت بايثون الجديد!"
    send_telegram_message(news_text)
