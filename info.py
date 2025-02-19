
import os
import re
from pyrogram import Client, filters
from pymongo import MongoClient

# Configuration
API_ID = 22125271  # Replace with your API ID
API_HASH = "ee54ed0f27ef14430e653aa620b5e828"  # Replace with your API Hash
BOT_TOKEN = "7825304144:AAHoL-LiXNYlBKpOpfk1nFt__HGVCU01jGE"  # Replace with your Bot Token
MONGO_URI = "mongodb+srv://rajhamraj45:rajhamraj@hemraj.fygnq.mongodb.net/?retryWrites=true&w=majority&appName=hemraj"  # Replace with your MongoDB URI
CHANNEL_ID = -1002495162924  # Replace with your Channel/Group ID

# Initialize Bot
bot = Client("AutoFilterBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["autofilter_db"]
collection = db["files"]

# Function to clean text
def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).lower()

# Handler to store files
@bot.on_message(filters.document | filters.video | filters.audio)
def save_file(client, message):
    file_name = clean_text(message.caption or message.document.file_name)
    file_id = message.document.file_id

    # Save file details to MongoDB
    collection.insert_one({"file_name": file_name, "file_id": file_id})
    message.reply_text(f"✅ File saved: {message.document.file_name}")

# Handler for search queries
@bot.on_message(filters.text & filters.private)
def search_file(client, message):
    query = clean_text(message.text)
    results = collection.find({"file_name": {"$regex": query, "$options": "i"}})

    response = ""
    for result in results:
        response += f"📂 {result['file_name']}\n🎯 File ID: `{result['file_id']}`\n\n"

    if response:
        message.reply_text(response)
    else:
        message.reply_text("❌ No results found.")

# Start the bot
print("Bot is running...")
bot.run()
#---------------------------------------------------------------
#---------------------------------------------------------------
SETTINGS = {
            'spell_check': SPELL_CHECK,
            'auto_filter': AUTO_FILTER,
            'file_secure': PROTECT_CONTENT,
            'auto_delete': AUTO_DELETE,
            'template': IMDB_TEMPLATE,
            'caption': FILE_CAPTION,
            'tutorial': TUTORIAL,
            'shortner': SHORTENER_WEBSITE,
            'api': SHORTENER_API,
            'shortner_two': SHORTENER_WEBSITE2,
            'api_two': SHORTENER_API2,
            'log': LOG_VR_CHANNEL,
            'imdb': IMDB,
            'link': LINK_MODE, 
            'is_verify': IS_VERIFY, 
            'verify_time': TWO_VERIFY_GAP,
            'shortner_three': SHORTENER_WEBSITE3,
            'api_three': SHORTENER_API3,
            'third_verify_time': THREE_VERIFY_GAP
}
