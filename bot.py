from telethon import TelegramClient, events
from datetime import datetime, timezone
import asyncio

# 🔑 YOUR API (same as your file)
api_id = 36861954
api_hash = "b92c5c41a893cf06212c3d61d9828a26"

# 📱 PHONE NUMBER
phone = "+918658252025"  # 👈 YAHAN APNA NUMBER DALNA HAI

# 📡 CHANNEL MAP (same as your file)
channel_map = {
    -1002034302956: -1003514525404,
    -1002439392027: -1003514525404,
    -1001538202326: -1003514525404,
    -1002481683835: -1003514525404,

    -1001854773639: -1003679880003,
    -1001514009598: -1003830782292,
    -1003771386369: -1003838262416,
    -1002356483627: -1003798361118,
    -1001918806676: -1003758406148,
    -1001805277811: -1003770821220,
    -1001958158065: -1003607766894,
    -1001804131088: -1003722026423,
    -1002127440209: -1003790590314,
}

client = TelegramClient("session", api_id, api_hash)

# 📅 TODAY CHECK
def is_today(msg_date):
    return msg_date.date() == datetime.now(timezone.utc).date()

# 🚀 FAST FETCH
async def fetch_today_messages():
    print("⚡ Fast fetching started...")

    for source_id, target_id in channel_map.items():
        print(f"🔎 Checking: {source_id}")

        async for msg in client.iter_messages(source_id, limit=100):
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
                break

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
    await client.start(phone)  # 👈 FIXED (NO INPUT ISSUE)
    print("🔥 FAST BOT RUNNING 🔥")

    await fetch_today_messages()
    await client.run_until_disconnected()

# ▶️ RUN
asyncio.run(main())
