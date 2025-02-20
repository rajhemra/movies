from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Hemraj:Hemraj@hemraj.igyty.mongodb.net/?retryWrites=true&w=majority&appName=hemraj"
client = MongoClient(MONGO_URI)

try:
    client.admin.command('ping')  # MongoDB se connection verify karega
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
