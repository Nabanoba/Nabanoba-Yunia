import asyncio
import schedule
import time
import datetime
from telegram import Bot
from transformers import pipeline

# === Config ===
BOT_TOKEN = '8107552443:AAGz3lbiD-PleVgAujzoDZydP3n8HEt2YLw'  # Replace with secure method later
CHAT_ID = -4703939610
POST_TIME = "09:42"

# === Daily Topics ===
TOPICS = {
    "Monday": "climate change and agriculture",
    "Tuesday": "rising sea levels and their impact",
    "Wednesday": "deforestation and global warming",
    "Thursday": "climate change facts and stats",
    "Friday": "renewable energy solutions",
    "Saturday": "youth voices in climate action",
    "Sunday": "how to fight climate change at home"
}

# === Initialize Telegram bot ===
bot = Bot(token=BOT_TOKEN)

# === Initialize local AI generator (GPT-2) ===
generator = pipeline("text-generation", model="gpt2")

def generate_post(topic):
    prompt = f"Write a short engaging Telegram post about {topic}."
    try:
        response = generator(
            prompt,
            max_length=80,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            num_return_sequences=1
        )
        text = response[0]['generated_text'].strip()

        # Fallback if low quality
        if text.lower().count("tweet") > 5 or len(text) < 40:
            raise ValueError("Bad generation output.")

        return text

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return f"🌍 Let's talk about {topic}. Every action counts. #ClimateAction"

async def send_post(topic):
    content = generate_post(topic)
    await bot.send_message(chat_id=CHAT_ID, text=content)
    print(f"✅ Posted on {datetime.datetime.now().strftime('%A')}: {topic}")
    print(content)

def job():
    today = datetime.datetime.today().strftime('%A')
    topic = TOPICS.get(today, "climate change")
    asyncio.run(send_post(topic))

def main():
    print(f"📅 Scheduling daily post at {POST_TIME}")
    schedule.every().day.at(POST_TIME).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
