# ═══════════════════════════════════════════════════════════════
#   ɴxᴄ x ᴍᴜꜱɪᴄ
#   Licensed under the MIT License — see LICENSE.
# ═══════════════════════════════════════════════════════════════

import config
from NxcMusic.utils.db import is_logger_enabled


def logger_active() -> bool:
    return bool(config.LOGGER_ID) and is_logger_enabled()
