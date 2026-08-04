import os
import requests

# جلب بيانات الاعتماد من أسرار جيت هب (GitHub Secrets) أو القيم المباشرة
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def send_telegram_message(message):
  """دالة لإرسال الرسائل عبر بوت تليجرام"""
  if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    print("خطأ: لم يتم ضبط توكن البوت أو معرف الشات في البيئة.")
    return

  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
  payload = {
      "chat_id": TELEGRAM_CHAT_ID,
      "text": message,
      "parse_mode": "Markdown",
  }

  try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
      print("تم إرسال الرسالة بنجاح إلى تليجرام!")
    else:
      print(f"فشل الإرسال، الكود: {response.status_code}, الرد: {response.text}")
  except Exception as e:
    print(f"حدث خطأ أثناء الاتصال بتليجرام: {e}")


if __name__ == "__main__":
  # رسالة الاختبار أو محتوى الخبر الذي سيصلك
  news_message = (
      "🚀 *تنبيه من روبوت الأخبار*\n\nتم تشغيل البوت بنجاح عبر GitHub Actions!"
  )
  send_telegram_message(news_message)
