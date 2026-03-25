from telethon import TelegramClient, events
from datetime import datetime, timezone
import asyncio

# 🔑 YOUR API
api_id = 33213300
api_hash = "a75cec1d75321e310763fb28353ced42"

# 📡 CHANNEL MAP
channel_map = {
    -1002034302956: -1003610042240,
    -1002439392027: -1003610042240,
    -1001538202326: -1003610042240,
    -1002481683835: -1003610042240,

    -1001854773639: -1003568924734,
    -1001514009598: -1003779852810,
    -1003771386369: -1003893624542,
    -1002315207640: -1003526708899,
    -1001918806676: -1003881584533,
    -1001805277811: -1003851114959,
    -1001958158065: -1003890157454,
    -1001804131088: -1003648168935,
    -1002127440209: -1003585710863,
}

client = TelegramClient("session", api_id, api_hash)

# 📅 TODAY CHECK
def is_today(msg_date):
    return msg_date.date() == datetime.now(timezone.utc).date()

# 🚀 FAST FETCH (TODAY POSTS)
async def fetch_today_messages():
    print("⚡ Fast fetching started...")

    for source_id, target_id in channel_map.items():
        print(f"🔎 Checking: {source_id}")

        async for msg in client.iter_messages(source_id, limit=100):  # 🔥 limit added (FAST)
            if is_today(msg.date):

                try:
                    if msg.media:
                        await client.send_file(
                            target_id,
                            msg.media,
                            caption=msg.text or ""
                        )
                    else:
                        if msg.text:
                            await client.send_message(
                                target_id,
                                msg.text
                            )
                except Exception as e:
                    print("Error:", e)

            else:
                break  # stop early = fast

# 🚀 LIVE POSTS
@client.on(events.NewMessage(chats=list(channel_map.keys())))
async def handler(event):
    msg = event.message

    if not is_today(msg.date):
        return

    source_id = event.chat_id
    target_id = channel_map[source_id]

    try:
        if msg.media:
            await client.send_file(
                target_id,
                msg.media,
                caption=msg.text or ""
            )
        else:
            if msg.text:
                await client.send_message(
                    target_id,
                    msg.text
                )
    except Exception as e:
        print("Error:", e)

# ▶️ MAIN
async def main():
    await client.start()
    print("🔥 FAST BOT RUNNING 🔥")

    await fetch_today_messages()
    await client.run_until_disconnected()

# ▶️ RUN
asyncio.run(main())
