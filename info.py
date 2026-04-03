import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'Royal_movies')   
API_ID = int(environ.get('API_ID', '0')) # डिप्लॉय करते समय सर्वर में असली ID डालेंगे
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# ============================
# Channel & Group Links Configuration
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+gjEckl3TjepjZTA1') 
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/+gjEckl3TjepjZTA1') 
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/movieuniverse224') 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+gjEckl3TjepjZTA1') 

# ============================
# Admin and Database Settings
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-100'))
URL = environ.get('URL', '')
DREAMXBOTZ_IMAGE_FETCH = environ.get('DREAMXBOTZ_IMAGE_FETCH', '')
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
MOVIE_UPDATE_CHANNEL = environ.get('MOVIE_UPDATE_CHANNEL', '')
LINK_PREVIEW = environ.get('LINK_PREVIEW', 'False')
ABOVE_PREVIEW = environ.get('ABOVE_PREVIEW', 'False')
BAD_WORDS = set(environ.get('BAD_WORDS', '').split())
LANDSCAPE_POSTER = environ.get('LANDSCAPE_POSTER', 'False')
TMDB_POSTER = environ.get('TMDB_POSTER', 'False')

DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_URI2 = environ.get('DATABASE_URI2', DATABASE_URI)
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'royal_files')

# ============================
# Payment Configuration
# ============================
QR_CODE = environ.get('QR_CODE', 'YOUR_QR_CODE_LINK_HERE')    
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'YOUR_UPI_ID_HERE')

# ============================
# File Limit & Referral Quota Settings
# ============================
FREE_FILE_LIMIT = int(environ.get('FREE_FILE_LIMIT', 10)) 
REFER_BONUS_FILES = int(environ.get('REFER_BONUS_FILES', 15)) 

# ============================
# Miscellaneous Configuration
# ============================
SESSION_NAME = str(environ.get('SESSION_NAME', 'Royal_movies'))
name = str(environ.get('name', 'Royal movies'))
AUTO_DELETE = True
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))
IMDB = True
TMDB_API_KEY = environ.get('TMDB_API_KEY', '')
Bot_cmds = []
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS', 0))
