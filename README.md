# ɴxᴄ x ᴍᴜꜱɪᴄ

Telegram voice-chat music bot — audio & video streaming, queue, autoplay, playlists, effects and channel play.

Built with [Pyrogram/Kurigram](https://github.com/kurigram-org/kurigram), [Py-TgCalls](https://github.com/pytgcalls/pytgcalls), [richgram](https://pypi.org/project/richgram/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp). No external download API is needed.

## Environment variables

Required: `API_ID`, `API_HASH`, `BOT_TOKEN`, `OWNER_ID`, `STRING_SESSION`, `MONGO_DB_URL`

Optional:

| Variable | Purpose |
|---|---|
| `BOT_NAME` | Name shown in the bot (default: ɴxᴄ x ᴍᴜꜱɪᴄ) |
| `BOT_LINK` | `https://t.me/<bot>` (auto-detected if empty) |
| `SUPPORT_GROUP` | Support link — button hidden if empty |
| `UPDATES_CHANNEL` | Updates link — button hidden if empty |
| `LOGGER_ID` | Log group/channel ID |
| `START_VIDEO` | Video on /start (default `assets/start.mp4`, path or URL) |
| `START_VIDEO_SPOILER` | `true` = video is hidden until tapped |
| `START_PHOTOS` | Optional comma-separated image URLs |
| `PING_IMG_URL` | Optional image for /ping |
| `YT_COOKIES_FILE` | Path to YouTube cookies (default `cookies.txt`) |

## YouTube cookies

Datacenter IPs are often blocked by YouTube. Put an exported `cookies.txt` (Netscape format) in the project root and downloads will use it automatically.

## Run

```bash
pip install -r requirements.txt
python3 -m NxcMusic
```

Or with Docker: `docker build -t nxcmusic . && docker run --env-file .env nxcmusic`

## Commands

Playback: `/play` `/vplay` `/playforce` `/pause` `/resume` `/skip` `/stop` `/clear` `/autoplay` `/thumbnail`
Seek & effects: `/seek` `/seekback` `/speed` `/speedreset` `/bass` `/bassoff` `/effecton` `/effectoff` `/effects`
Playlists: `/pcreate` `/padd` `/premove` `/pview` `/pplay` `/pdelete`
Channel: `/addchannel` `/delchannel` `/cplay` `/cvplay` `/cpause` `/cresume` `/cskip` `/cstop`
General: `/start` `/help` `/ping` `/id` `/language`
Owner: `/stats` `/speedtest` `/broadcast` `/logger` `/gblock` `/gunblock` `/ublock` `/uunblock` `/blocklist` `/reboot`

## License

MIT — see `LICENSE`.
