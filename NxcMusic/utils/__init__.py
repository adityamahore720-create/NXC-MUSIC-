# ═══════════════════════════════════════════════════════════════
#   ɴxᴄ x ᴍᴜꜱɪᴄ
#   Licensed under the MIT License — see LICENSE.
# ═══════════════════════════════════════════════════════════════

from NxcMusic.utils.permissions import is_user_authorized
from NxcMusic.utils.decorators import register_block_middleware

__all__ = [
    "is_user_authorized",
    "register_block_middleware",
]
