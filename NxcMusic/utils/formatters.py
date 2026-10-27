# ═══════════════════════════════════════════════════════════════
#   ɴxᴄ x ᴍᴜꜱɪᴄ
#   Licensed under the MIT License — see LICENSE.
# ═══════════════════════════════════════════════════════════════

import isodate
import math


def fmt_time(seconds: float) -> str:
    """Convert seconds → H:MM:SS or M:SS string."""
    s = int(seconds)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def parse_dur(s: str) -> int:
    """Parse ISO 8601 duration or MM:SS / H:MM:SS string → seconds."""
    try:
        return int(isodate.parse_duration(s).total_seconds())
    except Exception:
        pass
    if ":" in s:
        try:
            parts = [int(x) for x in s.split(":")]
            if len(parts) == 2:
                return parts[0] * 60 + parts[1]
            if len(parts) == 3:
                return parts[0] * 3600 + parts[1] * 60 + parts[2]
        except Exception:
            pass
    return 0


def iso_to_sec(iso: str) -> int:
    """ISO 8601 duration → seconds."""
    try:
        return int(isodate.parse_duration(iso).total_seconds())
    except Exception:
        return 0


def iso_to_human(iso: str) -> str:
    """ISO 8601 duration → human-readable H:MM:SS string."""
    try:
        t = int(isodate.parse_duration(iso).total_seconds())
        h, r = divmod(t, 3600)
        m, s = divmod(r, 60)
        return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"
    except Exception:
        return "?"


def sec_to_iso(sec: int) -> str:
    """Seconds → ISO 8601 duration string."""
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"PT{h}H{m}M{s}S" if h else f"PT{m}M{s}S"


def short(title: str, n: int = 22) -> str:
    """Truncate title to n characters."""
    return title if len(title) <= n else title[: n - 1] + "…"


def progress_bar(elapsed: float, total: float) -> str:
    """Clean progress bar:  1:23  ━━━━●─────  3:34"""

    if total <= 0:
        return "N/A"

    slots = 10
    pos = min(slots - 1, int((elapsed / total) * slots)) if total else 0
    bar = "━" * pos + "●" + "─" * (slots - 1 - pos)
    return f"{fmt_time(elapsed)}  {bar}  {fmt_time(total)}"
