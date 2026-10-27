# ═══════════════════════════════════════════════════════════════
#   ɴxᴄ x ᴍᴜꜱɪᴄ
#   Licensed under the MIT License — see LICENSE.
# ═══════════════════════════════════════════════════════════════

import asyncio


async def watchdog() -> None:
    """No-op — watchdog disabled to keep bot running 24/7."""
    while True:
        await asyncio.sleep(3600)  # sleep forever, do nothing
