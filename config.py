"""
config.py — All environment variables in one place.
Copy sample.env → .env and fill in your values.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ── Required ──────────────────────────────────────────────────────────────────
API_ID          = int(os.environ["API_ID"])
API_HASH        = os.environ["API_HASH"]
BOT_TOKEN       = os.environ["BOT_TOKEN"]
STRING_SESSION  = os.environ["STRING_SESSION"]
MONGO_DB_URL    = os.environ["MONGO_DB_URL"]
OWNER_ID        = int(os.environ["OWNER_ID"])

# ── Optional ──────────────────────────────────────────────────────────────────
BOT_NAME         = os.getenv("BOT_NAME", "ɴxᴄ x ᴍᴜꜱɪᴄ")
BOT_LINK         = os.getenv("BOT_LINK", "")   # auto-detected from the bot username when empty
UPDATES_CHANNEL  = os.getenv("UPDATES_CHANNEL", "")   # button is hidden when empty
SUPPORT_GROUP    = os.getenv("SUPPORT_GROUP", "")   # button is hidden when empty
LOGGER_ID        = int(os.getenv("LOGGER_ID", "0"))
PING_IMG_URL     = os.getenv("PING_IMG_URL", "")   # optional image for /ping
SESSION_NAME     = os.getenv("SESSION_NAME", "NxcMusic")
PORT             = int(os.getenv("PORT", 10000))

# ── Download config (yt-dlp, no external API) ────────────────────────────────
DOWNLOAD_DIR          = "downloads"
YT_TOKEN_TIMEOUT  = 10    # seconds — fetch download token
YT_STREAM_TIMEOUT = 900   # 15 min  — stream long songs

# ── NSFW Moderation API ─────────────────────────────────────────────────────
#NSFW_API_URL = os.getenv("NSFW_API_URL", "https://ai-moderation-api-khyr.onrender.com")
#NSFW_API_KEY = os.getenv("NSFW_API_KEY", "nsfwBad")

# Custom detection thresholds — sent with every /detect/upload call.
#NSFW_THRESHOLDS = {
#    "porn": float(os.getenv("NSFW_THRESHOLD_PORN", "0.7")),
#    "sexy": float(os.getenv("NSFW_THRESHOLD_SEXY", "0.8")),
#}

#── Start ───────────────────────────────────────────────────────────────────────
# Optional start images (comma separated URLs). Leave empty for none.
START_PHOTOS = [u.strip() for u in os.getenv("START_PHOTOS", "").split(",") if u.strip()]

# Video shown on /start in private chat. Local path or direct URL.
START_VIDEO         = os.getenv("START_VIDEO", "assets/start.mp4")
START_VIDEO_SPOILER = os.getenv("START_VIDEO_SPOILER", "true").lower() in ("1", "true", "yes")  # hidden until tapped

# ── Limits ────────────────────────────────────────────────────────────────────
MAX_DURATION_SECONDS = 1800   # 30 minutes
QUEUE_LIMIT          = 20
COOLDOWN             = 10     # seconds between /play per chat

# ── Playlist limits ───────────────────────────────────────────────────────────
PLAYLIST_LIMIT       = 10     # playlists per user
PLAYLIST_SONG_LIMIT  = 50     # songs per playlist


#BLOCKED_EXTENSIONS = [
#    ".zip",
#    ".rar",
#    ".7z",
#    ".apk",
#    ".exe",
#    ".py",
#    ".js",
#    ".go",
#    ".php",
#]
