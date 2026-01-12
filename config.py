import os

API_ID = 39256507

API_HASH = os.environ.get("API_HASH", "d9f88a9d3d207b8f6dfb08b762c30965")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7959445535:AAH6cQtHpNBDfx8b8MGkdrxeM3imLZ1LFHg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "7517872227"))

LOG = int(os.environ.get("LOG", "1"))

PORT = os.environ.get("PORT", "8080")

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7376514183").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
