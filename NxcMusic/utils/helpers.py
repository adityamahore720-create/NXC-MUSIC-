# ═══════════════════════════════════════════════════════════════
#   ɴxᴄ x ᴍᴜꜱɪᴄ
#   Licensed under the MIT License — see LICENSE.
# ═══════════════════════════════════════════════════════════════

import os


def delete_file(path: str) -> None:
    """Silently delete a file if it exists."""
    try:
        if path and os.path.exists(path):
            os.remove(path)
    except Exception:
        pass


# ── Optional start image ──────────────────────────────────────────────────────
import random as _random


def pick_photo() -> str:
    """Random START_PHOTOS entry, or '' when none configured."""
    import config
    return _random.choice(config.START_PHOTOS) if config.START_PHOTOS else ""


def opt_img(url: str) -> str:
    """rich_img() that returns '' for an empty url."""
    if not url:
        return ""
    from richgram import rich_img
    return rich_img(url)
