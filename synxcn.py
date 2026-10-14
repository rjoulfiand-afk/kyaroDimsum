#!/usr/bin/env python3
"""
SYNXCN :: OPERATIONS DECK
Single-file offline terminal theater & cybersecurity training simulation.
100% Python stdlib-only. Zero network calls. Deterministic registry.
"""

from __future__ import annotations

import argparse
import ast
import atexit
from dataclasses import dataclass
import datetime
import hashlib
import inspect
import math
import os
import random
import re
import shutil
import sys
import time
from typing import Callable, Dict, List, Optional, Sequence, Tuple

# ============================================================================
# [SECTION 01] CLI FLAGS & RUNTIME CONFIG
# ============================================================================


@dataclass
class RuntimeConfig:
    fast: bool = False
    auto: bool = False
    skip_intro: bool = False
    sound: bool = False
    color_256: bool = False
    seed: int = 2026
    selftest: bool = False

    @property
    def speed_mult(self) -> float:
        return 2.5 if self.fast else 1.0


CFG = RuntimeConfig()


def nap(seconds: float) -> None:
    if seconds <= 0:
        return
    factor = 2.5 if CFG.fast else 1.0
    if CFG.auto:
        factor *= 2.0
    time.sleep(max(0.001, seconds / factor))


def beep() -> None:
    if CFG.sound:
        sys.stdout.write("\a")
        sys.stdout.flush()


# ============================================================================
# [SECTION 02] FICTIONAL NAMESPACE & DETERMINISTIC GENERATORS
# ============================================================================

ORG_NAMES: Tuple[str, ...] = (
    "NEXORA DYNAMICS",
    "VELTRIX LOGISTICS",
    "HALCYON BIOTECH",
    "OBSIDIAN FINANCIAL GRID",
    "AETHER TELECOM",
    "KRONOS SHIPPING NET",
    "LUMEN MEDIA GROUP",
    "PRAXIS ROBOTICS",
    "ZEPHYR AIRWORKS",
    "MERIDIAN BANKCHAIN",
    "IRONCLAD DEFENSE SYS",
    "SOLSTICE ENERGY GRID",
    "CASCADE WATERWORKS",
    "VANTAGE RETAIL NET",
    "ONYX PHARMA LABS",
    "TRIDENT MARITIME OPS",
    "GLASSPEAK MEDIA",
    "FERROUS INDUSTRIAL",
    "NORTHSTAR INSURANCE",
    "COBALT MINING CORP",
)

WORD_BANK: Tuple[str, ...] = (
    "NULL",
    "GHOST",
    "RAVEN",
    "CIPHER",
    "SHADOW",
    "ECHO",
    "VOID",
    "CRIMSON",
    "OBSIDIAN",
    "QUARTZ",
    "SPECTRE",
    "UMBRA",
    "NOVA",
    "GLITCH",
    "PHANTOM",
    "STATIC",
    "VECTOR",
    "ONYX",
    "TITAN",
    "WRAITH",
    "PULSE",
    "DRIFT",
    "ASH",
    "IRON",
)

DATA_NOUNS: Tuple[str, ...] = (
    "shipment_manifest",
    "unit_cost_model",
    "vendor_roster",
    "project_roadmap",
    "capacity_forecast",
    "maintenance_log",
    "routing_table",
    "inventory_snapshot",
    "budget_draft",
    "facility_map",
    "asset_registry",
    "telemetry_dump",
    "contract_draft",
    "onboarding_plan",
    "incident_report",
    "quarterly_brief",
    "schema_backup",
    "access_matrix",
    "build_pipeline",
    "sensor_feed",
)

PROTOCOLS: Dict[str, str] = {
    "MESHLINE": "ENCRYPTED MESH CHAT PROTOCOL",
    "VAULTMAIL": "SECURE MAIL BACKBONE",
    "GRIDNET": "SYNTHETIC INFRASTRUCTURE MESH",
}

ALLOWED_TLDS: Tuple[str, ...] = (
    ".example",
    ".test",
    ".invalid",
    ".local",
    ".internal",
    ".lan",
)

CATEGORIES: Tuple[str, ...] = (
    "RECON",
    "INTRUSION",
    "SOCIAL",
    "CRYPTO VAULT",
    "TRAINING SIM",
    "ARCHIVE",
)

HOST_ROLES: Tuple[str, ...] = (
    "edge-01",
    "edge-04",
    "db-core",
    "gw-north",
    "auth-node",
    "cache-07",
    "kms-vault",
    "bus-relay",
    "sync-hub",
    "telemetry-02",
    "proxy-ring",
    "ledger-09",
)

VULN_TEMPLATES: Tuple[Tuple[str, str], ...] = (
    ("SYN-DESYNC-04", "Gridnet Frame Alignment Drift"),
    ("BUFFER-ECHO-19", "Transient Heap Echo in Telemetry Bus"),
    ("TOKEN-SKEW-08", "Session Nonce Clock Skew Window"),
    ("MESH-LEAK-27", "Unmasked Header Metadata Reflection"),
    ("CIPHER-PAD-12", "Legacy Block Padding Oracle Simulation"),
    ("ROUTE-LOOP-33", "Synthetic BGP Prefix Reflection Fault"),
    ("CACHE-GHOST-41", "Stale Shadow Line in Edge Directory"),
    ("VAULT-RACE-06", "Concurrent Lock Latch Timing Anomaly"),
)

MORSE_TABLE: Dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

SECURITY_TRIVIA_BANK: Tuple[Tuple[str, Tuple[str, str, str, str], int, str], ...] = (
    (
        "Metode 2FA (Two-Factor Authentication) mana yang paling tahan terhadap serangan phishing real-time?",
        (
            "A. Kode SMS 6-digit standar",
            "B. Hardware Security Key / Passkey (FIDO2)",
            "C. Pertanyaan keamanan nama hewan peliharaan",
            "D. Link verifikasi via email sekunder",
        ),
        1,
        "TIP NYATA: Gunakan FIDO2/Passkey atau aplikasi authenticator; hindari SMS OTP bila memungkinkan karena rentan SIM-swap.",
    ),
    (
        "Indikator paling kuat bahwa sebuah pesan darurat merupakan upaya social engineering / phishing adalah:",
        (
            "A. Menciptakan urgensi palsu agar melewati prosedur verifikasi standar",
            "B. Dikirim pada jam kerja normal",
            "C. Menggunakan tanda baca formal",
            "D. Menyertakan nomor tiket internal biasa",
        ),
        0,
        "TIP NYATA: Selalu verifikasi permintaan sensitif melalui jalur komunikasi kedua (out-of-band) sebelum bertindak.",
    ),
    (
        "Praktik manajemen kredensial terbaik untuk menjaga keamanan banyak akun adalah:",
        (
            "A. Satu password rumit yang dipakai ulang di semua layanan",
            "B. Mengganti angka terakhir password setiap bulan",
            "C. Password Manager dengan passphrase unik & panjang di tiap layanan",
            "D. Menyimpan daftar password di file teks biasa di desktop",
        ),
        2,
        "TIP NYATA: Panjang & keunikan passphrase (16+ karakter unik via Password Manager) jauh lebih krusial daripada rotasi paksa.",
    ),
    (
        "Apa fungsi utama VPN yang sebenarnya saat menggunakan jaringan Wi-Fi publik?",
        (
            "A. Membuat perangkat kebal sepenuhnya terhadap malware dari file unduhan",
            "B. Mengenkripsi lalu lintas antara perangkat dan server VPN dari penyadapan lokal",
            "C. Menghapus semua jejak login di situs tempat kamu masuk akun",
            "D. Mempercepat perangkat keras prosesor secara otomatis",
        ),
        1,
        "TIP NYATA: VPN mengamankan jalur transit jaringan lokal, namun tidak menggantikan HTTPS, 2FA, dan kehati-hatian saat mengunduh file.",
    ),
    (
        "Dalam strategi pencadangan data '3-2-1 Backup Rule', angka '1' merujuk pada:",
        (
            "A. Cukup 1 kali backup seumur hidup",
            "B. Hanya menyimpan 1 file penting saja",
            "C. Minimal 1 salinan backup disimpan off-site / terpisah secara fisik atau cloud terisolasi",
            "D. Menggunakan 1 flashdisk yang selalu menancap di laptop",
        ),
        2,
        "TIP NYATA: Terapkan aturan 3-2-1 (3 salinan data, 2 media berbeda, 1 salinan off-site/offline) untuk proteksi terhadap ransomware.",
    ),
    (
        "Mengapa menjalankan aplikasi harian menggunakan akun Administrator/root penuh berisiko tinggi?",
        (
            "A. Karena kode berbahaya yang tereksekusi otomatis mewarisi hak akses penuh sistem",
            "B. Karena membuat layar monitor lebih cepat redup",
            "C. Karena membatasi jumlah tab terminal yang bisa dibuka",
            "D. Karena menonaktifkan fitur salin-tempel",
        ),
        0,
        "TIP NYATA: Terapkan Principle of Least Privilege (PoLP); gunakan akun standar harian dan eskalasi hak akses hanya saat diperlukan.",
    ),
)


def stable_seed(text: str, master_seed: int = 2026) -> int:
    digest = hashlib.sha256(f"{master_seed}::{text}".encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big")


def slugify_org(org_name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", org_name.lower()).strip("-")


def make_callsign(rng: random.Random) -> str:
    w1, w2 = rng.sample(WORD_BANK, 2)
    num = rng.randint(10, 99)
    return f"{w1}{w2}-{num:02d}"


def make_fictional_domain(org_name: str, rng: random.Random) -> str:
    suffix = rng.choice((".internal", ".example", ".local", ".lan"))
    return f"{slugify_org(org_name)}{suffix}"


def make_safe_ip(rng: random.Random) -> str:
    pool = rng.randint(0, 5)
    if pool == 0:
        return f"10.{rng.randint(1, 250)}.{rng.randint(1, 250)}.{rng.randint(2, 250)}"
    if pool == 1:
        return f"172.{rng.randint(16, 31)}.{rng.randint(1, 250)}.{rng.randint(2, 250)}"
    if pool == 2:
        return f"192.168.{rng.randint(1, 250)}.{rng.randint(2, 250)}"
    if pool == 3:
        return f"192.0.2.{rng.randint(2, 250)}"
    if pool == 4:
        return f"198.51.100.{rng.randint(2, 250)}"
    return f"203.0.113.{rng.randint(2, 250)}"


def is_valid_safe_ip(ip_str: str) -> bool:
    parts = ip_str.split(".")
    if len(parts) != 4:
        return False
    try:
        octets = [int(p) for p in parts]
    except ValueError:
        return False
    if any(o < 0 or o > 255 for o in octets):
        return False
    a, b, c, _ = octets
    if a == 10:
        return True
    if a == 172 and 16 <= b <= 31:
        return True
    if a == 192 and b == 168:
        return True
    if a == 192 and b == 0 and c == 2:
        return True
    if a == 198 and b == 51 and c == 100:
        return True
    if a == 203 and b == 0 and c == 113:
        return True
    return False


# ============================================================================
# [SECTION 03] CROSS-PLATFORM TERMINAL INPUT & COLOR ENGINE
# ============================================================================

IS_WINDOWS = os.name == "nt"
if IS_WINDOWS:
    import msvcrt
else:
    import select
    import termios
    import tty

_OLD_TERMIOS = None
_TERMINAL_ACTIVE = False


def init_terminal() -> None:
    global _OLD_TERMIOS, _TERMINAL_ACTIVE
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        return
    if IS_WINDOWS:
        os.system("")
    else:
        try:
            fd = sys.stdin.fileno()
            _OLD_TERMIOS = termios.tcgetattr(fd)
            tty.setcbreak(fd)
        except Exception:
            _OLD_TERMIOS = None
    sys.stdout.write("\x1b[?1049h\x1b[?25l\x1b[2J\x1b[H")
    sys.stdout.flush()
    _TERMINAL_ACTIVE = True


def restore_terminal() -> None:
    global _OLD_TERMIOS, _TERMINAL_ACTIVE
    if _TERMINAL_ACTIVE:
        sys.stdout.write("\x1b[0m\x1b[?25h\x1b[?1049l")
        sys.stdout.flush()
        _TERMINAL_ACTIVE = False
    if not IS_WINDOWS and _OLD_TERMIOS is not None:
        try:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, _OLD_TERMIOS)
        except Exception:
            pass
        _OLD_TERMIOS = None


atexit.register(restore_terminal)


def kbhit() -> bool:
    if not sys.stdin.isatty():
        return False
    if IS_WINDOWS:
        return msvcrt.kbhit()
    dr, _, _ = select.select([sys.stdin], [], [], 0.0)
    return bool(dr)


def getch() -> str:
    if not sys.stdin.isatty():
        return ""
    if IS_WINDOWS:
        ch = msvcrt.getch()
        if ch in (b"\x00", b"\xe0"):
            ch2 = msvcrt.getch()
            win_map = {
                b"H": "UP",
                b"P": "DOWN",
                b"K": "LEFT",
                b"M": "RIGHT",
                b"Z": "SHIFT_TAB",
            }
            return win_map.get(ch2, "")
        if ch == b"\x03":
            raise KeyboardInterrupt
        if ch in (b"\r", b"\n"):
            return "ENTER"
        if ch == b"\x1b":
            return "ESC"
        if ch == b"\t":
            return "TAB"
        if ch in (b"\x08", b"\x7f"):
            return "BACKSPACE"
        try:
            return ch.decode("utf-8", errors="ignore")
        except Exception:
            return ""
    else:
        fd = sys.stdin.fileno()
        ch = os.read(fd, 1)
        if not ch:
            return ""
        if ch == b"\x03":
            raise KeyboardInterrupt
        if ch in (b"\r", b"\n"):
            return "ENTER"
        if ch == b"\t":
            return "TAB"
        if ch in (b"\x7f", b"\x08"):
            return "BACKSPACE"
        if ch == b"\x1b":
            dr, _, _ = select.select([sys.stdin], [], [], 0.015)
            if not dr:
                return "ESC"
            seq = os.read(fd, 2)
            if seq == b"[A":
                return "UP"
            if seq == b"[B":
                return "DOWN"
            if seq == b"[C":
                return "RIGHT"
            if seq == b"[D":
                return "LEFT"
            if seq == b"[Z":
                return "SHIFT_TAB"
            return "ESC"
        try:
            return ch.decode("utf-8", errors="ignore")
        except Exception:
            return ""


def drain_keys() -> None:
    while kbhit():
        getch()


def rgb_to_256(r: int, g: int, b: int) -> int:
    if r == g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232
    rc = round(r / 255 * 5)
    gc = round(g / 255 * 5)
    bc = round(b / 255 * 5)
    return 16 + 36 * rc + 6 * gc + bc


def rgb(r: int, g: int, b: int, bg: bool = False) -> str:
    if CFG.color_256:
        idx = rgb_to_256(r, g, b)
        return f"\x1b[{48 if bg else 38};5;{idx}m"
    return f"\x1b[{48 if bg else 38};2;{r};{g};{b}m"


class Palette:
    RESET = "\x1b[0m"

    @staticmethod
    def bg_dark() -> str:
        return rgb(8, 12, 18, bg=True)

    @staticmethod
    def bg_panel() -> str:
        return rgb(14, 20, 30, bg=True)

    @staticmethod
    def bg_highlight() -> str:
        return rgb(24, 48, 42, bg=True)

    @staticmethod
    def bg_vault_hi() -> str:
        return rgb(34, 24, 58, bg=True)

    @staticmethod
    def green() -> str:
        return rgb(40, 245, 140)

    @staticmethod
    def green_dim() -> str:
        return rgb(22, 125, 75)

    @staticmethod
    def cyan() -> str:
        return rgb(65, 225, 250)

    @staticmethod
    def purple() -> str:
        return rgb(185, 115, 255)

    @staticmethod
    def amber() -> str:
        return rgb(255, 190, 55)

    @staticmethod
    def red() -> str:
        return rgb(255, 75, 90)

    @staticmethod
    def white() -> str:
        return rgb(230, 242, 248)

    @staticmethod
    def muted() -> str:
        return rgb(105, 125, 145)


def category_color(category: str) -> str:
    if category in ("RECON", "INTRUSION", "SOCIAL"):
        return Palette.green()
    if category == "CRYPTO VAULT":
        return Palette.cyan()
    if category == "TRAINING SIM":
        return Palette.purple()
    return Palette.amber()


def clearance_color(level: int) -> str:
    mapping = {
        1: Palette.green(),
        2: Palette.cyan(),
        3: Palette.purple(),
        4: Palette.amber(),
        5: Palette.red(),
    }
    return mapping.get(level, Palette.white())


# ============================================================================
# [SECTION 04] SCREEN BUFFER, BRAILLE CANVAS & TYPIST ENGINE
# ============================================================================

SCREEN_W = 120
SCREEN_H = 34


@dataclass
class Cell:
    ch: str = " "
    fg: str = ""
    bg: str = ""


class Screen:
    def __init__(self, width: int = SCREEN_W, height: int = SCREEN_H) -> None:
        self.width = width
        self.height = height
        default_fg = Palette.white()
        default_bg = Palette.bg_dark()
        self.buf: List[List[Cell]] = [
            [Cell(" ", default_fg, default_bg) for _ in range(width)]
            for _ in range(height)
        ]
        self.old: List[List[Cell]] = [
            [Cell("", "", "") for _ in range(width)] for _ in range(height)
        ]
        self.jitter_row: int = -1
        self.jitter_shift: int = 0

    def clear(self, bg: Optional[str] = None) -> None:
        fill_bg = bg if bg is not None else Palette.bg_dark()
        fg = Palette.white()
        for y in range(self.height):
            row = self.buf[y]
            for x in range(self.width):
                c = row[x]
                c.ch = " "
                c.fg = fg
                c.bg = fill_bg
        self.jitter_row = -1
        self.jitter_shift = 0

    def invalidate(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.old[y][x].ch = ""

    def put(
        self,
        x: int,
        y: int,
        ch: str,
        fg: Optional[str] = None,
        bg: Optional[str] = None,
    ) -> None:
        if 0 <= x < self.width and 0 <= y < self.height and ch:
            cell = self.buf[y][x]
            cell.ch = ch[0]
            if fg is not None:
                cell.fg = fg
            if bg is not None:
                cell.bg = bg

    def fill_rect(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        ch: str = " ",
        fg: Optional[str] = None,
        bg: Optional[str] = None,
    ) -> None:
        for ry in range(max(0, y), min(self.height, y + h)):
            for rx in range(max(0, x), min(self.width, x + w)):
                self.put(rx, ry, ch, fg, bg)

    def text(
        self,
        x: int,
        y: int,
        s: str,
        fg: Optional[str] = None,
        bg: Optional[str] = None,
        max_w: Optional[int] = None,
    ) -> None:
        if not (0 <= y < self.height):
            return
        limit = self.width if max_w is None else min(self.width, x + max_w)
        cx = x
        for ch in s:
            if cx >= limit:
                break
            if cx >= 0:
                self.put(cx, y, ch, fg, bg)
            cx += 1

    def draw_markup(
        self,
        x: int,
        y: int,
        s: str,
        default_fg: Optional[str] = None,
        default_bg: Optional[str] = None,
    ) -> None:
        if not (0 <= y < self.height):
            return
        cur_fg = default_fg if default_fg is not None else Palette.white()
        cur_bg = default_bg if default_bg is not None else None
        tag_map = {
            "green": Palette.green(),
            "gdim": Palette.green_dim(),
            "cyan": Palette.cyan(),
            "purple": Palette.purple(),
            "amber": Palette.amber(),
            "red": Palette.red(),
            "white": Palette.white(),
            "muted": Palette.muted(),
            "reset": default_fg if default_fg is not None else Palette.white(),
        }
        i = 0
        cx = x
        n = len(s)
        while i < n and cx < self.width:
            if s[i] == "{":
                end = s.find("}", i + 1)
                if end != -1:
                    tag = s[i + 1 : end]
                    if tag in tag_map:
                        cur_fg = tag_map[tag]
                        i = end + 1
                        continue
            if s[i] == "\x1b" and i + 1 < n and s[i + 1] == "[":
                end = s.find("m", i + 2)
                if end != -1:
                    seq = s[i : end + 1]
                    if seq == "\x1b[0m":
                        cur_fg = default_fg if default_fg is not None else Palette.white()
                    else:
                        cur_fg = seq
                    i = end + 1
                    continue
            if cx >= 0:
                self.put(cx, y, s[i], cur_fg, cur_bg)
            cx += 1
            i += 1

    def draw_box(
        self,
        x: int,
        y: int,
        w: int,
        h: int,
        title: str = "",
        style: str = "single",
        fg: Optional[str] = None,
        bg: Optional[str] = None,
        fill: bool = False,
    ) -> None:
        if w < 2 or h < 2:
            return
        box_fg = fg if fg is not None else Palette.green_dim()
        if fill and bg is not None:
            self.fill_rect(x, y, w, h, " ", box_fg, bg)
        if style == "double":
            tl, tr, bl, br, hz, vt = "╔", "╗", "╚", "╝", "═", "║"
        else:
            tl, tr, bl, br, hz, vt = "┌", "┐", "└", "┘", "─", "│"

        self.put(x, y, tl, box_fg, bg)
        self.put(x + w - 1, y, tr, box_fg, bg)
        self.put(x, y + h - 1, bl, box_fg, bg)
        self.put(x + w - 1, y + h - 1, br, box_fg, bg)
        for cx in range(x + 1, x + w - 1):
            self.put(cx, y, hz, box_fg, bg)
            self.put(cx, y + h - 1, hz, box_fg, bg)
        for cy in range(y + 1, y + h - 1):
            self.put(x, cy, vt, box_fg, bg)
            self.put(x + w - 1, cy, vt, box_fg, bg)
        if title:
            label = f" {title} "
            self.text(x + 2, y, label, Palette.white(), bg, max_w=w - 4)

    def hbar(
        self,
        x: int,
        y: int,
        w: int,
        ratio: float,
        fg: str,
        bg_empty: Optional[str] = None,
    ) -> None:
        clamped = max(0.0, min(1.0, ratio))
        filled = int(round(w * clamped))
        empty_color = bg_empty if bg_empty is not None else Palette.muted()
        for i in range(w):
            if i < filled:
                self.put(x + i, y, "█", fg)
            else:
                self.put(x + i, y, "░", empty_color)

    def trigger_glitch(self, rng: random.Random) -> None:
        if rng.random() < 0.22:
            self.jitter_row = rng.randint(4, self.height - 4)
            self.jitter_shift = rng.choice((-1, 1))
        else:
            self.jitter_row = -1
            self.jitter_shift = 0

    def present(self) -> None:
        if not sys.stdout.isatty():
            return
        out: List[str] = []
        last_fg = ""
        last_bg = ""
        for y in range(self.height):
            shift = self.jitter_shift if y == self.jitter_row else 0
            for x in range(self.width):
                src_x = max(0, min(self.width - 1, x - shift))
                c = self.buf[y][src_x]
                o = self.old[y][x]
                if c.ch != o.ch or c.fg != o.fg or c.bg != o.bg:
                    out.append(f"\x1b[{y + 1};{x + 1}H")
                    if c.bg != last_bg and c.bg:
                        out.append(c.bg)
                        last_bg = c.bg
                    if c.fg != last_fg and c.fg:
                        out.append(c.fg)
                        last_fg = c.fg
                    out.append(c.ch)
                    o.ch = c.ch
                    o.fg = c.fg
                    o.bg = c.bg
        if out:
            out.append(Palette.RESET)
            sys.stdout.write("".join(out))
            sys.stdout.flush()


class BrailleCanvas:
    """Unicode Braille (U+2800..U+28FF) high-density subpixel canvas."""

    DOT_MAP = (
        (0x01, 0x08),
        (0x02, 0x10),
        (0x04, 0x20),
        (0x40, 0x80),
    )

    def __init__(self, char_w: int, char_h: int) -> None:
        self.char_w = char_w
        self.char_h = char_h
        self.px_w = char_w * 2
        self.px_h = char_h * 4
        self.grid: List[List[int]] = [
            [0 for _ in range(char_w)] for _ in range(char_h)
        ]
        self.colors: List[List[Optional[str]]] = [
            [None for _ in range(char_w)] for _ in range(char_h)
        ]

    def clear(self) -> None:
        for cy in range(self.char_h):
            for cx in range(self.char_w):
                self.grid[cy][cx] = 0
                self.colors[cy][cx] = None

    def set(self, px: int, py: int, color: Optional[str] = None) -> None:
        if 0 <= px < self.px_w and 0 <= py < self.px_h:
            cx, dx = divmod(px, 2)
            cy, dy = divmod(py, 4)
            self.grid[cy][cx] |= self.DOT_MAP[dy][dx]
            if color is not None:
                self.colors[cy][cx] = color

    def line(
        self,
        x0: int,
        y0: int,
        x1: int,
        y1: int,
        color: Optional[str] = None,
    ) -> None:
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        cx, cy = x0, y0
        while True:
            self.set(cx, cy, color)
            if cx == x1 and cy == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                cx += sx
            if e2 <= dx:
                err += dx
                cy += sy

    def arc(
        self,
        cx: int,
        cy: int,
        radius: float,
        start_deg: float = 0.0,
        end_deg: float = 360.0,
        color: Optional[str] = None,
    ) -> None:
        steps = max(16, int(radius * 6))
        for step in range(steps + 1):
            deg = start_deg + (end_deg - start_deg) * (step / steps)
            rad = math.radians(deg)
            px = int(round(cx + radius * math.cos(rad)))
            py = int(round(cy + radius * math.sin(rad)))
            self.set(px, py, color)

    def render(
        self,
        screen: Screen,
        sx: int,
        sy: int,
        default_fg: str,
        bg: Optional[str] = None,
    ) -> None:
        for cy in range(self.char_h):
            for cx in range(self.char_w):
                mask = self.grid[cy][cx]
                if mask:
                    ch = chr(0x2800 + mask)
                    fg = self.colors[cy][cx] or default_fg
                    screen.put(sx + cx, sy + cy, ch, fg, bg)


class Typist:
    """Typewriter reveal engine with punctuation pauses and instant skip."""

    @staticmethod
    def reveal_lines(
        screen: Screen,
        x: int,
        y: int,
        lines: Sequence[Tuple[str, str]],
        base_delay: float = 0.008,
    ) -> None:
        skipped = CFG.auto
        for row_idx, (line_text, fg) in enumerate(lines):
            cur_y = y + row_idx
            if skipped:
                screen.text(x, cur_y, line_text, fg)
                continue
            for col_idx, ch in enumerate(line_text):
                if kbhit():
                    key = getch()
                    if key in (" ", "ENTER", "ESC"):
                        skipped = True
                        screen.text(x, cur_y, line_text, fg)
                        break
                screen.put(x + col_idx, cur_y, ch, fg)
                if col_idx + 1 < len(line_text):
                    screen.put(x + col_idx + 1, cur_y, "█", Palette.white())
                screen.present()
                delay = base_delay
                if ch in ".,:;!":
                    delay *= 3.2
                elif ch == " ":
                    delay *= 0.5
                nap(delay)
            screen.text(x, cur_y, line_text + " ", fg)
        screen.present()


def check_terminal_size(min_cols: int = SCREEN_W, min_rows: int = SCREEN_H) -> None:
    if not sys.stdout.isatty() or CFG.selftest or CFG.auto:
        return
    while True:
        sz = shutil.get_terminal_size((min_cols, min_rows))
        if sz.columns >= min_cols and sz.lines >= min_rows:
            return
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.write(
            f"{Palette.amber()}SYNXCN :: TERMINAL DIMENSION CHECK{Palette.RESET}\n\n"
            f"Ukuran terminal saat ini : {sz.columns}x{sz.lines}\n"
            f"Ukuran minimal wajib     : {min_cols}x{min_rows}\n\n"
            "Silakan perbesar jendela terminal kamu (atau tekan [Enter] untuk lanjut paksa)..."
        )
        sys.stdout.flush()
        if kbhit():
            k = getch()
            if k in ("ENTER", " ", "ESC"):
                return
        time.sleep(0.15)


def draw_hud(screen: Screen, subtitle: str = "OPERATIONS DECK") -> None:
    t = time.time()
    cpu_pct = int(38 + 24 * math.sin(t * 0.9) + 9 * math.cos(t * 2.3))
    mem_pct = int(62 + 11 * math.sin(t * 0.35))
    clock_str = datetime.datetime.now().strftime("%H:%M:%S")
    hud_bg = rgb(16, 26, 38, bg=True)
    screen.fill_rect(0, 0, SCREEN_W, 1, " ", Palette.white(), hud_bg)
    screen.text(1, 0, "◈ SYNXCN", Palette.green(), hud_bg)
    screen.text(10, 0, f"// {subtitle}", Palette.cyan(), hud_bg)

    cpu_bar = "▮" * (cpu_pct // 12) + "▯" * (8 - (cpu_pct // 12))
    mem_bar = "▮" * (mem_pct // 12) + "▯" * (8 - (mem_pct // 12))
    metrics = (
        f"GRID:ONLINE  CPU[{cpu_bar}]{cpu_pct:02d}%  "
        f"MEM[{mem_bar}]{mem_pct:02d}%  CLK {clock_str}"
    )
    screen.text(SCREEN_W - len(metrics) - 1, 0, metrics, Palette.amber(), hud_bg)
    for x in range(SCREEN_W):
        screen.put(x, 1, "─", Palette.green_dim())


# ============================================================================
# [SECTION 05] BOOT GLITCH & SYNXCN LOGO REVEAL
# ============================================================================

LOGO_SYNXCN: Tuple[str, ...] = (
    "  ███████╗██╗   ██╗███╗   ██╗██╗  ██╗ ██████╗███╗   ██╗  ",
    "  ██╔════╝╚██╗ ██╔╝████╗  ██║╚██╗██╔╝██╔════╝████╗  ██║  ",
    "  ███████╗ ╚████╔╝ ██╔██╗ ██║ ╚███╔╝ ██║     ██╔██╗ ██║  ",
    "  ╚════██║  ╚██╔╝  ██║╚██╗██║ ██╔██╗ ██║     ██║╚██╗██║  ",
    "  ███████║   ██║   ██║ ╚████║██╔╝ ██╗╚██████╗██║ ╚████║  ",
    "  ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═══╝  ",
)

RAIN_GLYPHS = "0123456789ABCDEFｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"


def run_boot_and_reveal(screen: Screen, master_seed: int) -> None:
    if CFG.skip_intro:
        return
    rng = random.Random(master_seed ^ 0x5A17)
    cols = [rng.randint(-SCREEN_H, 0) for _ in range(SCREEN_W)]
    speeds = [rng.randint(1, 3) for _ in range(SCREEN_W)]
    rain_frames = 28 if not CFG.fast else 14

    for _ in range(rain_frames):
        if kbhit():
            getch()
            return
        screen.clear()
        for x in range(SCREEN_W):
            head = cols[x]
            for trail in range(10):
                ry = head - trail
                if 0 <= ry < SCREEN_H:
                    ch = rng.choice(RAIN_GLYPHS)
                    if trail == 0:
                        fg = Palette.white()
                    elif trail < 3:
                        fg = Palette.green()
                    elif trail < 6:
                        fg = Palette.cyan()
                    else:
                        fg = Palette.green_dim()
                    screen.put(x, ry, ch, fg)
            cols[x] += speeds[x]
            if cols[x] - 10 > SCREEN_H:
                cols[x] = rng.randint(-12, 0)
        screen.text(
            42,
            SCREEN_H // 2,
            "[ INITIALIZING KERNEL TELEMETRY ... ]",
            Palette.amber(),
        )
        screen.present()
        nap(0.055)

    # Reveal Phase: Gradient green -> purple top-to-bottom
    gradient = [
        rgb(45, 250, 145),
        rgb(65, 230, 175),
        rgb(95, 205, 210),
        rgb(130, 175, 235),
        rgb(165, 140, 248),
        rgb(195, 110, 255),
    ]
    logo_w = len(LOGO_SYNXCN[0])
    logo_x = (SCREEN_W - logo_w) // 2
    logo_y = 9

    for step in range(14):
        if kbhit():
            getch()
            return
        screen.clear()
        draw_hud(screen, "BOOT SEQUENCE // VERIFYING OFFLINE MATRICES")
        screen.draw_box(16, 6, 88, 22, "SYNXCN CORELOADER", "double", Palette.cyan())
        for row_idx, line in enumerate(LOGO_SYNXCN):
            fg = gradient[row_idx % len(gradient)]
            rendered = []
            for ch in line:
                if ch == " " or step >= 10 or rng.random() < (step / 10.0):
                    rendered.append(ch)
                else:
                    rendered.append(rng.choice(RAIN_GLYPHS))
            screen.text(logo_x, logo_y + row_idx, "".join(rendered), fg)

        sub1 = ":: OPERATIONS DECK ::"
        sub2 = "v1.0 :: 100% OFFLINE SIMULATION"
        screen.text((SCREEN_W - len(sub1)) // 2, 17, sub1, Palette.white())
        screen.text((SCREEN_W - len(sub2)) // 2, 19, sub2, Palette.muted())

        bar_w = 50
        bx = (SCREEN_W - bar_w) // 2
        screen.hbar(bx, 22, bar_w, (step + 1) / 14.0, Palette.green())
        status = (
            "SYSTEM ONLINE // MODULE DECK READY"
            if step >= 11
            else "MOUNTING 16 TACTICAL & VAULT ENGINES..."
        )
        screen.text(
            (SCREEN_W - len(status)) // 2,
            24,
            status,
            Palette.green() if step >= 11 else Palette.amber(),
        )
        screen.present()
        nap(0.065)
    beep()
    nap(0.35)


# ============================================================================
# [SECTION 06] DATA-DRIVEN MODULE REGISTRY (150-220 MODULES)
# ============================================================================


@dataclass(frozen=True)
class ModuleDef:
    id: str
    category: str
    engine: str
    display_name: str
    clearance: int
    blurb: str
    seed: int


OPS_ENGINE_META: Tuple[Tuple[str, str, str], ...] = (
    (
        "NETMAP",
        "RECON",
        "Pemetaan topologi node & sub-grid internal organisasi via Braille vector radar",
    ),
    (
        "VULNSWEEP",
        "RECON",
        "Pemindaian indeks eksposur permukaan protokol sintetis & matriks anomali",
    ),
    (
        "FIREBREACH",
        "INTRUSION",
        "Simulasi penetrasi perimeter berlapis melalui injeksi paket tekanan tinggi",
    ),
    (
        "EXFILRUN",
        "INTRUSION",
        "Akuisisi terindeks arsip dokumen korporat fiksi melewati kanal terenkripsi",
    ),
    (
        "PAYLOADFORGE",
        "INTRUSION",
        "Kompilasi & kalibrasi urutan instruksi rakitan sintetis di sandbox memori",
    ),
    (
        "MESHTAP",
        "SOCIAL",
        "Intersepsi transkrip kanal komunikasi terenkripsi MESHLINE antar callsign",
    ),
    (
        "VAULTCRACK",
        "SOCIAL",
        "Indeksasi struktur direktori surat elektronik internal pada backbone VAULTMAIL",
    ),
    (
        "GHOSTROUTE",
        "SOCIAL",
        "Perutean pantulan multi-hop melewati simpul proxy callsign hingga jejak nol",
    ),
)

VAULT_ENGINE_META: Tuple[Tuple[str, str, str, str], ...] = (
    (
        "CIPHERLOCK",
        "CRYPTO VAULT",
        "SEKUENS",
        "Dekripsi sandi geser Caesar pada token otorisasi terkunci secara real-time",
    ),
    (
        "SIGDECODE",
        "CRYPTO VAULT",
        "PULSA",
        "Translasi gelombang sinyal titik-garis menjadi kata kunci protokol",
    ),
    (
        "HEXCAL",
        "CRYPTO VAULT",
        "VEKTOR",
        "Kalibrasi cepat konversi alamat memori biner, heksadesimal, dan desimal",
    ),
    (
        "PATTERNBREACH",
        "TRAINING SIM",
        "MATRIKS",
        "Sinkronisasi memori urutan gerbang sinyal beruntun ala Simon-says",
    ),
    (
        "KEYRUSH",
        "TRAINING SIM",
        "OVERRIDE",
        "Uji kecepatan & akurasi pengetikan instruksi konsol darurat (WPM & akurasi)",
    ),
    (
        "LOGICGATE",
        "TRAINING SIM",
        "SIRKUIT",
        "Pemecahan pola deret angka & logika pengunci mekanisme gerbang",
    ),
    (
        "INTELGRID",
        "TRAINING SIM",
        "DOKTRIN",
        "Evaluasi literasi keamanan siber nyata: 2FA, anti-phishing, backup, dan VPN",
    ),
    (
        "DOSSIERGEN",
        "ARCHIVE",
        "ARSIP",
        "Generator kartu identitas operatif lengkap dengan callsign, pangkat, & statistik",
    ),
)


def build_registry(
    target_count: int = 200,
    master_seed: int = 2026,
) -> List[ModuleDef]:
    target_count = max(150, min(220, target_count))
    rng = random.Random(master_seed)
    registry: List[ModuleDef] = []

    ops_quota = int(round(target_count * 0.60))
    vault_quota = target_count - ops_quota

    # Distribute OPS quota evenly across 8 OPS engines
    base_ops = ops_quota // len(OPS_ENGINE_META)
    rem_ops = ops_quota % len(OPS_ENGINE_META)
    ops_idx = 1

    for eng_i, (engine, category, blurb_prefix) in enumerate(OPS_ENGINE_META):
        count = base_ops + (1 if eng_i < rem_ops else 0)
        orgs_pool = list(ORG_NAMES)
        rng.shuffle(orgs_pool)
        for k in range(count):
            org = orgs_pool[k % len(orgs_pool)]
            mod_id = f"OPS-{ops_idx:03d}"
            ops_idx += 1
            seed_val = stable_seed(mod_id, master_seed)
            item_rng = random.Random(seed_val)
            clearance = item_rng.randint(1, 5)
            dom = make_fictional_domain(org, item_rng)
            display_name = f"{engine} :: {org}"
            blurb = f"{blurb_prefix} untuk target {org} ({dom})."
            registry.append(
                ModuleDef(
                    id=mod_id,
                    category=category,
                    engine=engine,
                    display_name=display_name,
                    clearance=clearance,
                    blurb=blurb,
                    seed=seed_val,
                )
            )

    # Distribute VAULT quota across 8 VAULT engines
    base_vlt = vault_quota // len(VAULT_ENGINE_META)
    rem_vlt = vault_quota % len(VAULT_ENGINE_META)
    vlt_idx = 1

    for eng_i, (engine, category, tag_word, blurb_prefix) in enumerate(
        VAULT_ENGINE_META
    ):
        count = base_vlt + (1 if eng_i < rem_vlt else 0)
        for k in range(1, count + 1):
            mod_id = f"VLT-{vlt_idx:03d}"
            vlt_idx += 1
            seed_val = stable_seed(mod_id, master_seed)
            item_rng = random.Random(seed_val)
            clearance = item_rng.randint(1, 5)
            codename = item_rng.choice(WORD_BANK)
            display_name = f"{engine} :: {tag_word}-{k:02d} [{codename}]"
            blurb = f"{blurb_prefix} // Paket latihan {tag_word}-{k:02d} ({codename})."
            registry.append(
                ModuleDef(
                    id=mod_id,
                    category=category,
                    engine=engine,
                    display_name=display_name,
                    clearance=clearance,
                    blurb=blurb,
                    seed=seed_val,
                )
            )

    return registry


# ============================================================================
# [SECTION 07] DETERMINISTIC SCENE DATA & UNIFORM DEBRIEF GENERATOR
# ============================================================================


def generate_module_context(mod: ModuleDef) -> Dict[str, object]:
    """Generate 100% deterministic mission/puzzle parameters from mod.seed."""
    rng = random.Random(mod.seed)
    org = rng.choice(ORG_NAMES)
    if "::" in mod.display_name and mod.category in ("RECON", "INTRUSION", "SOCIAL"):
        candidate = mod.display_name.split("::", 1)[1].strip()
        if candidate in ORG_NAMES:
            org = candidate

    domain = make_fictional_domain(org, rng)
    primary_ip = make_safe_ip(rng)
    callsign_a = make_callsign(rng)
    callsign_b = make_callsign(rng)

    node_count = rng.randint(5, 9)
    hosts = rng.sample(HOST_ROLES, node_count)
    nodes = []
    for h in hosts:
        nodes.append(
            {
                "host": f"{h}.{domain}",
                "short": h,
                "ip": make_safe_ip(rng),
                "x": rng.randint(6, 56),
                "y": rng.randint(4, 52),
            }
        )

    vuln_count = rng.randint(4, 6)
    picked_vulns = rng.sample(VULN_TEMPLATES, vuln_count)
    vulns = [
        {"code": code, "title": title, "sev": rng.randint(42, 96)}
        for code, title in picked_vulns
    ]
    exposure_index = int(sum(v["sev"] for v in vulns) / len(vulns))

    exfil_count = rng.randint(6, 9)
    picked_nouns = rng.sample(DATA_NOUNS, exfil_count)
    records = [
        {
            "name": noun,
            "size_kb": rng.randint(24, 940),
            "stamp": f"CYC-{rng.randint(10, 99):02d} // T+{rng.randint(10, 59):02d}s",
        }
        for noun in picked_nouns
    ]
    total_records = rng.randint(140, 890)

    hop_count = rng.randint(5, 7)
    hops = [
        {"callsign": make_callsign(rng), "ip": make_safe_ip(rng), "ms": rng.randint(4, 48)}
        for _ in range(hop_count)
    ]

    plain_word = rng.choice(WORD_BANK)
    shift = rng.randint(2, 7)
    cipher_word = "".join(
        chr((ord(c) - 65 + shift) % 26 + 65) for c in plain_word
    )

    morse_word = rng.choice([w for w in WORD_BANK if 4 <= len(w) <= 6])
    morse_code = "   ".join(MORSE_TABLE[c] for c in morse_word)

    hex_questions = []
    for _ in range(3):
        val = rng.randint(10, 63)
        mode = rng.choice(("HEX2DEC", "BIN2DEC", "DEC2HEX"))
        if mode == "HEX2DEC":
            q_str = f"Konversi alamat 0x{val:02X} ke Desimal"
            a_str = str(val)
        elif mode == "BIN2DEC":
            q_str = f"Konversi biner 0b{val:06b} ke Desimal"
            a_str = str(val)
        else:
            q_str = f"Konversi desimal {val} ke Heksadesimal (tanpa 0x)"
            a_str = f"{val:X}"
        hex_questions.append((q_str, a_str))

    pattern_seq = [rng.randint(1, 4) for _ in range(4)]

    override_noun = rng.choice(DATA_NOUNS)
    override_phrase = f"sync {override_noun} --node {hosts[0]} --lock"

    seq_base = rng.randint(2, 5)
    seq_step = rng.randint(3, 7)
    logic_nums = [seq_base + i * seq_step for i in range(4)]
    logic_ans = str(seq_base + 4 * seq_step)

    trivia_indices = rng.sample(range(len(SECURITY_TRIVIA_BANK)), 3)
    trivia_items = [SECURITY_TRIVIA_BANK[idx] for idx in trivia_indices]

    dossier_stats = {
        "rank": rng.choice(("VANGUARD-I", "SPECTRE-II", "ARCHON-III", "PRIME-IV")),
        "stealth": rng.randint(68, 99),
        "crypt": rng.randint(70, 99),
        "sigcraft": rng.randint(65, 98),
    }

    return {
        "org": org,
        "domain": domain,
        "primary_ip": primary_ip,
        "callsign_a": callsign_a,
        "callsign_b": callsign_b,
        "nodes": nodes,
        "vulns": vulns,
        "exposure_index": exposure_index,
        "records": records,
        "total_records": total_records,
        "hops": hops,
        "plain_word": plain_word,
        "shift": shift,
        "cipher_word": cipher_word,
        "morse_word": morse_word,
        "morse_code": morse_code,
        "hex_questions": hex_questions,
        "pattern_seq": pattern_seq,
        "override_phrase": override_phrase,
        "logic_nums": logic_nums,
        "logic_ans": logic_ans,
        "trivia_items": trivia_items,
        "dossier_stats": dossier_stats,
    }


def render_debrief_lines(
    mod: ModuleDef,
    ctx: Optional[Dict[str, object]] = None,
    runtime_result: Optional[Dict[str, str]] = None,
) -> List[str]:
    """
    Deterministic debrief text builder.
    Calling twice with the same ModuleDef & seed guarantees 100% identical text.
    """
    if ctx is None:
        ctx = generate_module_context(mod)
    res = runtime_result or {}
    eng = mod.engine
    org = str(ctx["org"])
    dom = str(ctx["domain"])

    if eng == "NETMAP":
        nodes = ctx["nodes"]  # type: ignore[assignment]
        top_pairs = ", ".join(
            f"{n['short']}={n['ip']}" for n in nodes[:3]  # type: ignore[index]
        )
        return [
            f"TARGET GRID     : {org} ({dom})",
            f"NODES MAPPED    : {len(nodes)} host aktif terpetakan via GRIDNET",  # type: ignore[arg-type]
            f"NODE TABLE      : {top_pairs}",
            "STATUS AKHIR    : topology snapshot locked (simulated)",
        ]
    if eng == "VULNSWEEP":
        vulns = ctx["vulns"]  # type: ignore[assignment]
        v0 = vulns[0]["code"]  # type: ignore[index]
        return [
            f"SURFACE TARGET  : {org} // {ctx['primary_ip']}",
            f"TEMUAN UTAMA    : {len(vulns)} anomali sintetis ({v0})",  # type: ignore[arg-type]
            f"HASIL ANALISIS  : exposure index: {ctx['exposure_index']}/100",
        ]
    if eng == "FIREBREACH":
        return [
            f"PERIMETER NODE  : gw-core.{dom} [{ctx['primary_ip']}]",
            f"OPERATOR TAG    : {ctx['callsign_a']} via GRIDNET",
            "STATUS OPERASI  : perimeter down (simulated)",
        ]
    if eng == "EXFILRUN":
        recs = ctx["records"]  # type: ignore[assignment]
        sample_names = ", ".join(r["name"] for r in recs[:3])  # type: ignore[index]
        return [
            f"SUMBER ARSIP    : {org} ({dom})",
            f"MANIFEST SAMPEL : {sample_names}",
            f"HASIL AKUISISI  : {ctx['total_records']} records captured",
        ]
    if eng == "PAYLOADFORGE":
        return [
            f"SANDBOX TARGET  : {org} // {ctx['primary_ip']}",
            f"OPERATOR BUILD  : {ctx['callsign_a']} -> stage-4 verified",
            "STATUS KOMPILASI: payload armed (simulated)",
        ]
    if eng == "MESHTAP":
        return [
            f"PROTOKOL KANAL  : MESHLINE // {dom}",
            f"PARTISIPAN SESI : {ctx['callsign_a']} <-> {ctx['callsign_b']}",
            "STATUS INTERSEP : transcript archived",
        ]
    if eng == "VAULTCRACK":
        recs = ctx["records"]  # type: ignore[assignment]
        return [
            f"BACKBONE TARGET : VAULTMAIL // {org} ({dom})",
            f"SUBJEK TERINDEKS: {recs[0]['name']} & {recs[1]['name']}",  # type: ignore[index]
            "STATUS DIREKTORI: inbox indexed",
        ]
    if eng == "GHOSTROUTE":
        hops = ctx["hops"]  # type: ignore[assignment]
        chain = " -> ".join(h["callsign"] for h in hops[:3])  # type: ignore[index]
        return [
            f"RUTE RELAY      : {chain} (+{len(hops) - 3} hops)",  # type: ignore[arg-type]
            f"EXIT ENDPOINT   : {ctx['primary_ip']} ({dom})",
            "HASIL TELEMETRI : trace confidence: 0%",
        ]
    if eng == "CIPHERLOCK":
        verdict = res.get("verdict", f"SOLVED // KUNCI: {ctx['plain_word']}")
        score = res.get("score", "100/100")
        return [
            f"SANDI CAESAR    : {ctx['cipher_word']} (geser +{ctx['shift']})",
            f"VERIFIKASI      : {verdict}",
            f"SKOR VAULT      : {score}",
        ]
    if eng == "SIGDECODE":
        verdict = res.get("verdict", f"DECODED // SINYAL: {ctx['morse_word']}")
        score = res.get("score", "100/100")
        return [
            f"POLA GELOMBANG  : {ctx['morse_code']}",
            f"HASIL DEKODE    : {verdict}",
            f"SKOR VAULT      : {score}",
        ]
    if eng == "HEXCAL":
        score = res.get("score", "3/3 alamat terkalibrasi (100%)")
        return [
            f"MODUL KALIBRASI : {mod.display_name}",
            f"HASIL KONVERSI  : {score}",
            "STATUS MEMORI   : register offset tervalidasi",
        ]
    if eng == "PATTERNBREACH":
        score = res.get("score", "4/4 gerbang sinkron (100%)")
        return [
            f"SEKUENS GERBANG : {ctx['pattern_seq']}",
            f"HASIL MEMORI    : {score}",
            "STATUS SIMULASI : pola neural terkunci",
        ]
    if eng == "KEYRUSH":
        score = res.get("score", "78 WPM // Akurasi 100%")
        return [
            f"VEKTOR KOMANDO  : {ctx['override_phrase']}",
            f"METRIK KETIK    : {score}",
            "STATUS OVERRIDE : manual console sync complete",
        ]
    if eng == "LOGICGATE":
        verdict = res.get("verdict", f"UNLOCKED // Jawaban: {ctx['logic_ans']}")
        return [
            f"DERET MEKANISME : {ctx['logic_nums']} -> [{ctx['logic_ans']}]",
            f"HASIL LOGIKA    : {verdict}",
            "STATUS GERBANG  : latch terbuka",
        ]
    if eng == "INTELGRID":
        items = ctx["trivia_items"]  # type: ignore[assignment]
        tip = items[0][3]  # type: ignore[index]
        score = res.get("score", "3/3 jawaban tepat (100%)")
        return [
            f"SKOR LITERASI   : {score}",
            f"EVALUASI        : Doktrin pertahanan siber terverifikasi",
            f"{tip}",
        ]
    # DOSSIERGEN
    stats = ctx["dossier_stats"]  # type: ignore[assignment]
    return [
        f"OPERATIVE ID    : {ctx['callsign_a']} // RANK {stats['rank']}",  # type: ignore[index]
        f"DIVISI ARSIP    : {org} ({dom})",
        "STATUS DOKUMEN  : dossier card minted (offline archive)",
    ]


# ============================================================================
# [SECTION 08] SCENE BRIEFING, 16 ENGINE RUNNERS & DEBRIEF MODAL
# ============================================================================


def prompt_line_input(
    screen: Screen,
    x: int,
    y: int,
    prompt_label: str,
    auto_answer: str,
    max_len: int = 44,
) -> str:
    drain_keys()
    buf: List[str] = []
    if CFG.auto:
        for ch in auto_answer:
            buf.append(ch)
            screen.text(
                x,
                y,
                f"{prompt_label}{''.join(buf)}█",
                Palette.cyan(),
                max_w=max_len + len(prompt_label) + 2,
            )
            screen.present()
            nap(0.03)
        return "".join(buf)

    while True:
        display = f"{prompt_label}{''.join(buf)}█" + (" " * (max_len - len(buf)))
        screen.text(x, y, display, Palette.cyan(), max_w=max_len + len(prompt_label) + 2)
        screen.present()
        if kbhit():
            key = getch()
            if key == "ESC":
                return ""
            if key == "ENTER":
                return "".join(buf).strip()
            if key == "BACKSPACE":
                if buf:
                    buf.pop()
            elif len(key) == 1 and 32 <= ord(key) <= 126 and len(buf) < max_len:
                buf.append(key)
        time.sleep(0.02)


def run_scene_briefing(screen: Screen, mod: ModuleDef, ctx: Dict[str, object]) -> None:
    screen.clear()
    draw_hud(screen, f"MISSION BRIEFING // {mod.id}")
    col = category_color(mod.category)
    screen.draw_box(6, 3, 108, 9, f"BRIEFING :: {mod.display_name}", "double", col)
    lines = [
        (
            f"MODULE ID : {mod.id}   |   CATEGORY : {mod.category}   |   ENGINE : {mod.engine}   |   CLEARANCE : LVL-{mod.clearance}",
            Palette.white(),
        ),
        (
            f"NAMESPACE : {ctx['org']} ({ctx['domain']})   |   ENDPOINT : {ctx['primary_ip']}",
            Palette.cyan(),
        ),
        (
            f"CALLSIGNS : {ctx['callsign_a']} // {ctx['callsign_b']}   |   MODE : 100% OFFLINE THEATER",
            Palette.muted(),
        ),
        (
            f"OBJECTIVE : {mod.blurb}",
            Palette.amber(),
        ),
    ]
    Typist.reveal_lines(screen, 9, 5, lines, base_delay=0.005)


def run_engine_netmap(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    canvas = BrailleCanvas(62, 15)
    nodes = ctx["nodes"]  # type: ignore[assignment]
    rng = random.Random(mod.seed)
    for idx in range(len(nodes)):  # type: ignore[arg-type]
        if kbhit() and getch() == "ESC":
            break
        screen.trigger_glitch(rng)
        screen.draw_box(
            6, 13, 66, 17, "BRAILLE TOPOLOGY RADAR [GRIDNET]", "single", Palette.green()
        )
        screen.draw_box(
            74, 13, 40, 17, "DISCOVERED NODES", "single", Palette.cyan()
        )
        cur = nodes[idx]  # type: ignore[index]
        canvas.arc(cur["x"], cur["y"], 3.0, 0, 360, Palette.green())
        if idx > 0:
            prev = nodes[idx - 1]  # type: ignore[index]
            canvas.line(prev["x"], prev["y"], cur["x"], cur["y"], Palette.cyan())
        canvas.render(screen, 8, 14, Palette.green())
        for j in range(idx + 1):
            nd = nodes[j]  # type: ignore[index]
            lx = 8 + min(52, nd["x"] // 2)
            ly = 14 + min(13, nd["y"] // 4)
            screen.text(lx, ly, f"●{nd['short']}", Palette.white())
            screen.text(
                76,
                15 + j,
                f"{j + 1:02d}. {nd['short']:<12} {nd['ip']}",
                Palette.green() if j == idx else Palette.white(),
            )
        screen.present()
        nap(0.18)
    return {}


def run_engine_vulnsweep(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    vulns = ctx["vulns"]  # type: ignore[assignment]
    screen.draw_box(
        6, 13, 108, 17, "SYNTHETIC VULNERABILITY SWEEP", "single", Palette.green()
    )
    for step in range(1, 21):
        if kbhit() and getch() == "ESC":
            break
        ratio = step / 20.0
        for i, v in enumerate(vulns):  # type: ignore[arg-type]
            ry = 15 + i * 2
            cur_sev = int(v["sev"] * min(1.0, ratio * (1.2 - i * 0.1)))
            screen.text(
                9, ry, f"[{v['code']}] {v['title']:<40}", Palette.white()
            )
            bar_col = Palette.red() if v["sev"] >= 80 else Palette.amber()
            screen.hbar(68, ry, 30, cur_sev / 100.0, bar_col)
            screen.text(100, ry, f"{cur_sev:02d}/100", bar_col)
        screen.present()
        nap(0.06)
    return {}


def run_engine_firebreach(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6,
        13,
        108,
        17,
        "PERIMETER OVERLOAD // MASH ANY KEY TO BREACH",
        "single",
        Palette.green(),
    )
    progress = 0.15
    ticks = 0
    while progress < 1.0 and ticks < 90:
        ticks += 1
        if CFG.auto:
            progress += 0.09
        else:
            pressed = False
            while kbhit():
                k = getch()
                if k == "ESC":
                    progress = 1.0
                    break
                pressed = True
                progress += 0.11
            if not pressed:
                progress = max(0.05, progress - 0.012)
                if ticks > 35:
                    progress += 0.045
        clamped = min(1.0, progress)
        screen.text(
            10,
            16,
            f"TARGET GATEWAY : gw-core.{ctx['domain']} ({ctx['primary_ip']})",
            Palette.cyan(),
        )
        screen.text(
            10,
            18,
            "INSTRUKSI      : Tekan tombol beruntun untuk menembus lapisan barikade!",
            Palette.amber(),
        )
        screen.hbar(10, 21, 86, clamped, Palette.green())
        screen.text(98, 21, f"{int(clamped * 100):3d}%", Palette.white())
        for gate in range(4):
            g_open = clamped >= (gate + 1) * 0.25
            lbl = f"GATE-0{gate + 1}: {'[OPEN]' if g_open else '[LOCKED]'}"
            screen.text(
                10 + gate * 24,
                24,
                lbl,
                Palette.green() if g_open else Palette.red(),
            )
        screen.present()
        nap(0.05)
    return {}


def run_engine_exfilrun(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    recs = ctx["records"]  # type: ignore[assignment]
    screen.draw_box(
        6, 13, 108, 17, "EXFILTRATION STREAM [GRIDNET TUNNEL]", "single", Palette.green()
    )
    screen.text(
        9,
        15,
        f"{'IDX':<5} {'RECORD ARTIFACT':<30} {'VOLUME':<14} {'CYCLE STAMP':<24} {'STATE'}",
        Palette.cyan(),
    )
    for idx, r in enumerate(recs):  # type: ignore[arg-type]
        if kbhit() and getch() == "ESC":
            break
        ry = 17 + idx
        if ry < 28:
            screen.text(
                9,
                ry,
                f"#{idx + 1:02d}   {r['name']:<30} {r['size_kb']:>4d} KB        {r['stamp']:<24} CAPTURED",
                Palette.green(),
            )
        screen.hbar(9, 28, 100, (idx + 1) / len(recs), Palette.cyan())  # type: ignore[arg-type]
        screen.present()
        nap(0.12)
    return {}


def run_engine_payloadforge(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    rng = random.Random(mod.seed ^ 0x99)
    screen.draw_box(
        6, 13, 108, 17, "SYNTHETIC PAYLOAD FORGE // ASM PIPELINE", "single", Palette.green()
    )
    ops = ("MOV", "XOR", "LEA", "ROL", "CMP", "CALL", "JMP", "AND")
    regs = ("RAX", "RBX", "RCX", "RDX", "R8", "R9", "R11", "RSP")
    for i in range(11):
        if kbhit() and getch() == "ESC":
            break
        addr = 0x401000 + i * 16
        op = rng.choice(ops)
        r1, r2 = rng.sample(regs, 2)
        imm = rng.randint(0x10, 0xFF)
        hex_bytes = " ".join(f"{rng.randint(0, 255):02X}" for _ in range(6))
        line = f"0x{addr:06X}  |  {hex_bytes:<18}  |  {op:<5} {r1}, [{r2}+0x{imm:02X}]   // stage-{i + 1:02d} ok"
        screen.text(9, 15 + i, line, Palette.green() if i % 2 == 0 else Palette.cyan())
        screen.hbar(9, 27, 100, (i + 1) / 11.0, Palette.amber())
        screen.present()
        nap(0.09)
    return {}


def run_engine_meshtap(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "MESHLINE ENCRYPTED PACKET TRANSCRIPT", "single", Palette.green()
    )
    ca = str(ctx["callsign_a"])
    cb = str(ctx["callsign_b"])
    recs = ctx["records"]  # type: ignore[assignment]
    n0 = recs[0]["name"]  # type: ignore[index]
    n1 = recs[1]["name"]  # type: ignore[index]
    transcript = [
        (ca, f"[MESH-PKT#01] Kanal ke {ctx['domain']} sudah sinkron?"),
        (cb, f"[MESH-PKT#02] Positif. Berkas {n0} sudah di-staging di node lokal."),
        (ca, f"[MESH-PKT#03] Lampirkan juga {n1} sebelum jendela audit ditutup."),
        (cb, f"[MESH-PKT#04] Diterima. Checksum terverifikasi, siap rotasi kunci."),
        (ca, "[MESH-PKT#05] Terminasi sesi MESHLINE dalam 3 detik. Keluar."),
    ]
    for i, (speaker, msg) in enumerate(transcript):
        if kbhit() and getch() == "ESC":
            break
        ry = 15 + i * 2
        col = Palette.cyan() if speaker == ca else Palette.green()
        screen.text(9, ry, f"<{speaker}>", col)
        Typist.reveal_lines(screen, 28, ry, [(msg, Palette.white())], base_delay=0.006)
        nap(0.10)
    return {}


def run_engine_vaultcrack(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, f"VAULTMAIL BACKBONE INDEXER :: {ctx['org']}", "single", Palette.green()
    )
    folders = ("[INBOX-CORE]", "[DISPATCH-GRID]", "[AUDIT-VAULT]", "[ARCHIVE-NODE]")
    recs = ctx["records"]  # type: ignore[assignment]
    for i in range(6):
        if kbhit() and getch() == "ESC":
            break
        fld = folders[i % len(folders)]
        rec = recs[i % len(recs)]  # type: ignore[index]
        subj = f"RE: Sinkronisasi {rec['name']} kuartal berjalan ({ctx['domain']})"
        screen.text(
            9,
            15 + i * 2,
            f"{fld:<16} | FROM: {ctx['callsign_b']:<16} | {subj}",
            Palette.white() if i % 2 else Palette.cyan(),
        )
        screen.present()
        nap(0.12)
    return {}


def run_engine_ghostroute(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    hops = ctx["hops"]  # type: ignore[assignment]
    canvas = BrailleCanvas(56, 14)
    screen.draw_box(
        6, 13, 60, 17, "PROXY BOUNCE VECTOR", "single", Palette.green()
    )
    screen.draw_box(
        68, 13, 46, 17, "CALLSIGN RELAY CHAIN", "single", Palette.cyan()
    )
    pts = [(8 + i * 16, 10 + ((i * 23) % 34)) for i in range(len(hops))]  # type: ignore[arg-type]
    for i, hop in enumerate(hops):  # type: ignore[arg-type]
        if kbhit() and getch() == "ESC":
            break
        px, py = pts[i]
        canvas.arc(px, py, 2.5, 0, 360, Palette.cyan())
        if i > 0:
            p0x, p0y = pts[i - 1]
            canvas.line(p0x, p0y, px, py, Palette.green())
        canvas.render(screen, 8, 14, Palette.green())
        screen.text(
            70,
            15 + i * 2,
            f"HOP-{i + 1} :: {hop['callsign']:<15} {hop['ip']:<15} ({hop['ms']}ms)",
            Palette.green(),
        )
        screen.present()
        nap(0.16)
    return {}


def run_engine_cipherlock(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "CIPHERLOCK // CAESAR SUBSTITUTION VAULT", "single", Palette.cyan()
    )
    plain = str(ctx["plain_word"])
    cipher = str(ctx["cipher_word"])
    shift = int(ctx["shift"])  # type: ignore[arg-type]
    screen.text(10, 15, f"CIPHERTEXT TERKUNCI :  {cipher}", Palette.amber())
    screen.text(
        10,
        17,
        f"PARAMETER GESER     :  +{shift} posisi alfabet (petunjuk huruf awal: '{plain[0]}')",
        Palette.white(),
    )
    screen.text(
        10,
        19,
        "ALFABET REFERENSI   :  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
        Palette.muted(),
    )
    ans = prompt_line_input(
        screen, 10, 22, "KETIK HASIL DEKODE > ", plain, max_len=24
    ).upper()
    ok = ans == plain
    return {
        "verdict": f"{'BENAR' if ok else 'SALAH'} (Input: {ans or '-'} | Kunci: {plain})",
        "score": "100/100" if ok else "0/100",
    }


def run_engine_sigdecode(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "SIGDECODE // MORSE PULSE TRANSLATOR", "single", Palette.cyan()
    )
    word = str(ctx["morse_word"])
    code = str(ctx["morse_code"])
    screen.text(10, 15, f"SINYAL MASUK  :   {code}", Palette.amber())
    ref1 = "  ".join(f"{k}:{MORSE_TABLE[k]}" for k in word)
    screen.text(10, 17, f"KAMUS PULSA   :   {ref1}", Palette.green())
    screen.text(
        10,
        19,
        "INSTRUKSI     :   Terjemahkan deret titik-garis di atas menjadi kata utuh.",
        Palette.white(),
    )
    ans = prompt_line_input(
        screen, 10, 22, "DEKODE SINYAL > ", word, max_len=24
    ).upper()
    ok = ans == word
    return {
        "verdict": f"{'TEPAT' if ok else 'MELESET'} (Input: {ans or '-'} | Sinyal: {word})",
        "score": "100/100" if ok else "0/100",
    }


def run_engine_hexcal(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "HEXCAL // MEMORY ADDRESS CALIBRATION", "single", Palette.cyan()
    )
    questions = ctx["hex_questions"]  # type: ignore[assignment]
    correct = 0
    for idx, (q_str, a_str) in enumerate(questions):  # type: ignore[arg-type]
        ry = 15 + idx * 4
        screen.text(10, ry, f"REGISTER #{idx + 1}: {q_str}", Palette.amber())
        ans = prompt_line_input(
            screen, 10, ry + 1, "NILAI KALIBRASI > ", a_str, max_len=16
        ).upper()
        if ans == a_str.upper():
            correct += 1
            screen.text(55, ry + 1, "[TERKALIBRASI]", Palette.green())
        else:
            screen.text(55, ry + 1, f"[MISSMATCH -> {a_str}]", Palette.red())
        screen.present()
    pct = int(round((correct / len(questions)) * 100))  # type: ignore[arg-type]
    return {"score": f"{correct}/{len(questions)} alamat terkalibrasi ({pct}%)"}  # type: ignore[arg-type]


def run_engine_patternbreach(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "PATTERNBREACH // SIMON SEQUENCE MATRIX", "single", Palette.purple()
    )
    seq = ctx["pattern_seq"]  # type: ignore[assignment]
    labels = {
        1: ("1:▲ RED", Palette.red()),
        2: ("2:◆ CYN", Palette.cyan()),
        3: ("3:● GRN", Palette.green()),
        4: ("4:■ AMB", Palette.amber()),
    }
    screen.text(
        10,
        15,
        "PERHATIKAN URUTAN 4 SINYAL BERIKUT, LALU KETIK ANGKA 1-4 BERURUTAN:",
        Palette.white(),
    )
    for step_idx, gate in enumerate(seq):  # type: ignore[arg-type]
        for k, (txt, col) in labels.items():
            hi = k == gate
            screen.draw_box(
                10 + (k - 1) * 24,
                17,
                20,
                4,
                txt,
                "double" if hi else "single",
                col if hi else Palette.muted(),
            )
        screen.text(
            10, 22, f"TRANSMISI PULSA KE-{step_idx + 1} DARI 4...", Palette.amber()
        )
        screen.present()
        nap(0.32)

    expected = "".join(str(x) for x in seq)  # type: ignore[union-attr]
    ans = prompt_line_input(
        screen, 10, 25, "ULANGI 4 DIGIT URUTAN (mis 1234) > ", expected, max_len=8
    )
    clean = "".join(ch for ch in ans if ch.isdigit())[:4]
    matches = sum(1 for a, b in zip(clean, expected) if a == b)
    return {"score": f"{matches}/4 gerbang sinkron ({matches * 25}%)"}


def run_engine_keyrush(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "KEYRUSH // MANUAL CONSOLE OVERRIDE", "single", Palette.purple()
    )
    target = str(ctx["override_phrase"])
    screen.text(10, 16, "KETIK KOMANDO OVERRIDE BERIKUT DENGAN CEPAT & TEPAT:", Palette.white())
    screen.text(10, 18, target, Palette.amber())
    t0 = time.time()
    typed = prompt_line_input(
        screen, 10, 21, "OVERRIDE > ", target, max_len=len(target) + 6
    )
    elapsed = max(0.5, time.time() - t0)
    words = max(1.0, len(target) / 5.0)
    wpm = int(round((words / elapsed) * 60))
    if CFG.auto:
        wpm = 84
    correct_chars = sum(1 for a, b in zip(typed, target) if a == b)
    acc = int(round((correct_chars / max(1, len(target))) * 100))
    return {"score": f"{wpm} WPM // Akurasi {acc}%"}


def run_engine_logicgate(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    screen.draw_box(
        6, 13, 108, 17, "LOGICGATE // SEQUENCE LOCK MECHANISM", "single", Palette.purple()
    )
    nums = ctx["logic_nums"]  # type: ignore[assignment]
    ans_expected = str(ctx["logic_ans"])
    seq_display = "  ->  ".join(str(n) for n in nums) + "  ->  [ ? ]"  # type: ignore[union-attr]
    screen.text(10, 16, "ANALISIS POLA DERET PENGUNCI SIRKUIT BERIKUT:", Palette.white())
    screen.text(10, 18, seq_display, Palette.amber())
    ans = prompt_line_input(
        screen, 10, 22, "MASUKKAN ANGKA PENGUNCI BERIKUTNYA > ", ans_expected, max_len=12
    )
    ok = ans == ans_expected
    return {
        "verdict": f"{'UNLOCKED' if ok else 'LOCKED'} (Input: {ans or '-'} | Kunci: {ans_expected})"
    }


def run_engine_intelgrid(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    items = ctx["trivia_items"]  # type: ignore[assignment]
    correct = 0
    letters = ("A", "B", "C", "D")
    for idx, (question, choices, ans_idx, _tip) in enumerate(items):  # type: ignore[arg-type]
        screen.fill_rect(6, 13, 108, 17, " ")
        screen.draw_box(
            6,
            13,
            108,
            17,
            f"INTELGRID // CYBERSECURITY DOCTRINE [{idx + 1}/{len(items)}]",  # type: ignore[arg-type]
            "single",
            Palette.purple(),
        )
        screen.text(9, 15, question[:102], Palette.amber())
        for c_i, choice_str in enumerate(choices):
            screen.text(11, 17 + c_i * 2, choice_str[:100], Palette.white())
        expected_letter = letters[ans_idx]
        ans = prompt_line_input(
            screen, 11, 26, "PILIH JAWABAN (A/B/C/D) > ", expected_letter, max_len=4
        ).upper()
        if ans == expected_letter:
            correct += 1
    pct = int(round((correct / len(items)) * 100))  # type: ignore[arg-type]
    return {"score": f"{correct}/{len(items)} jawaban tepat ({pct}%)"}  # type: ignore[arg-type]


def run_engine_dossiergen(
    screen: Screen, mod: ModuleDef, ctx: Dict[str, object]
) -> Dict[str, str]:
    stats = ctx["dossier_stats"]  # type: ignore[assignment]
    screen.draw_box(
        6, 13, 108, 17, "ARCHIVE // OPERATIVE DOSSIER GENERATOR", "double", Palette.amber()
    )
    screen.draw_box(10, 15, 46, 13, "SYNXCN CREDENTIAL CARD", "single", Palette.cyan())
    screen.text(13, 17, f"CALLSIGN   : {ctx['callsign_a']}", Palette.green())
    screen.text(13, 19, f"CLEARANCE  : LEVEL-0{mod.clearance} // {stats['rank']}", Palette.amber())  # type: ignore[index]
    screen.text(13, 21, f"ASSIGNMENT : {ctx['org']}", Palette.white())
    screen.text(13, 23, f"SUBNET ID  : {ctx['domain']}", Palette.cyan())
    screen.text(13, 25, f"NODE IP    : {ctx['primary_ip']}", Palette.muted())

    metrics = [
        ("STEALTH INDEX", int(stats["stealth"]), Palette.green()),  # type: ignore[index]
        ("CRYPTANALYSIS", int(stats["crypt"]), Palette.cyan()),  # type: ignore[index]
        ("SIGNAL CRAFT ", int(stats["sigcraft"]), Palette.purple()),  # type: ignore[index]
    ]
    for i, (label, val, col) in enumerate(metrics):
        ry = 17 + i * 3
        screen.text(60, ry, f"{label:<15} {val:02d}/100", Palette.white())
        screen.hbar(60, ry + 1, 46, val / 100.0, col)
    screen.present()
    nap(0.45)
    return {}


ENGINE_RUNNERS: Dict[
    str, Callable[[Screen, ModuleDef, Dict[str, object]], Dict[str, str]]
] = {
    "NETMAP": run_engine_netmap,
    "VULNSWEEP": run_engine_vulnsweep,
    "FIREBREACH": run_engine_firebreach,
    "EXFILRUN": run_engine_exfilrun,
    "PAYLOADFORGE": run_engine_payloadforge,
    "MESHTAP": run_engine_meshtap,
    "VAULTCRACK": run_engine_vaultcrack,
    "GHOSTROUTE": run_engine_ghostroute,
    "CIPHERLOCK": run_engine_cipherlock,
    "SIGDECODE": run_engine_sigdecode,
    "HEXCAL": run_engine_hexcal,
    "PATTERNBREACH": run_engine_patternbreach,
    "KEYRUSH": run_engine_keyrush,
    "LOGICGATE": run_engine_logicgate,
    "INTELGRID": run_engine_intelgrid,
    "DOSSIERGEN": run_engine_dossiergen,
}


def run_debrief_modal(
    screen: Screen,
    mod: ModuleDef,
    ctx: Dict[str, object],
    runtime_result: Dict[str, str],
) -> None:
    col = category_color(mod.category)
    lines = render_debrief_lines(mod, ctx, runtime_result)
    box_x, box_y, box_w, box_h = 14, 10, 92, 13
    screen.draw_box(
        box_x,
        box_y,
        box_w,
        box_h,
        f"DEBRIEF :: {mod.id} // {mod.engine} [{mod.category}]",
        "double",
        col,
        Palette.bg_panel(),
        fill=True,
    )
    for idx, line in enumerate(lines[:4]):
        screen.text(
            box_x + 4,
            box_y + 3 + idx * 2,
            line,
            Palette.amber() if "TIP NYATA" in line else Palette.white(),
            Palette.bg_panel(),
            max_w=box_w - 8,
        )
    footer = "[ Tekan tombol apa saja -> kembali ke DECK ]"
    screen.text(
        box_x + (box_w - len(footer)) // 2,
        box_y + box_h - 2,
        footer,
        col,
        Palette.bg_panel(),
    )
    screen.present()
    beep()
    if CFG.auto:
        nap(0.35)
        return
    drain_keys()
    while True:
        if kbhit():
            getch()
            return
        time.sleep(0.03)


def execute_module_scene(
    screen: Screen, mod: ModuleDef, visited_ids: set
) -> None:
    ctx = generate_module_context(mod)
    run_scene_briefing(screen, mod, ctx)
    runner = ENGINE_RUNNERS[mod.engine]
    runtime_result = runner(screen, mod, ctx)
    visited_ids.add(mod.id)
    run_debrief_modal(screen, mod, ctx, runtime_result)


# ============================================================================
# [SECTION 09] MODULE DECK UI (120x34 MAIN INTERFACE)
# ============================================================================


def wrap_text(text: str, width: int) -> List[str]:
    words = text.split()
    lines: List[str] = []
    cur = ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render_deck(
    screen: Screen,
    registry: Sequence[ModuleDef],
    cat_idx: int,
    filtered: Sequence[ModuleDef],
    sel_idx: int,
    scroll_top: int,
    visited_ids: set,
    search_mode: bool,
    search_query: str,
) -> None:
    screen.clear()
    draw_hud(screen, f"OPERATIONS DECK // COMPLETED: {len(visited_ids)}/{len(registry)}")

    # Row 2: Category Tabs
    tx = 2
    for idx, cat in enumerate(CATEGORIES):
        active = idx == cat_idx
        col = category_color(cat)
        cat_count = sum(1 for m in registry if m.category == cat)
        label = f" {cat} ({cat_count}) "
        bg = Palette.bg_highlight() if active else Palette.bg_panel()
        fg = Palette.white() if active else col
        screen.text(tx, 2, label, fg, bg)
        tx += len(label) + 2

    # Left Panel: Module List (cols 2..72, rows 4..30)
    active_cat = CATEGORIES[cat_idx]
    left_title = f"MODULES :: {active_cat}"
    if search_query or search_mode:
        left_title += f" [FILTER: '{search_query}']"
    screen.draw_box(
        2, 4, 70, 27, left_title, "single", category_color(active_cat)
    )

    visible_rows = 24
    if not filtered:
        screen.text(
            6,
            15,
            "Tidak ada modul yang cocok dengan filter pencarian.",
            Palette.amber(),
        )
    else:
        for row_offset in range(visible_rows):
            item_idx = scroll_top + row_offset
            if item_idx >= len(filtered):
                break
            m = filtered[item_idx]
            ry = 5 + row_offset
            is_sel = item_idx == sel_idx
            row_bg = (
                Palette.bg_highlight()
                if (is_sel and active_cat in ("RECON", "INTRUSION", "SOCIAL"))
                else (Palette.bg_vault_hi() if is_sel else Palette.bg_dark())
            )
            screen.fill_rect(3, ry, 68, 1, " ", Palette.white(), row_bg)
            ptr = "▸" if is_sel else " "
            chk = "✓" if m.id in visited_ids else "·"
            chk_col = Palette.green() if m.id in visited_ids else Palette.muted()
            screen.put(4, ry, ptr, Palette.amber() if is_sel else Palette.muted(), row_bg)
            screen.put(6, ry, chk, chk_col, row_bg)
            screen.text(8, ry, m.id, Palette.cyan(), row_bg)
            screen.text(
                17,
                ry,
                m.display_name,
                Palette.white() if is_sel else Palette.muted(),
                row_bg,
                max_w=44,
            )
            clr_tag = f"[C{m.clearance}]"
            screen.text(65, ry, clr_tag, clearance_color(m.clearance), row_bg)

    # Right Panel: Preview Panel (cols 74..118, rows 4..30)
    screen.draw_box(
        74, 4, 44, 27, "TACTICAL PREVIEW", "double", Palette.cyan()
    )
    if filtered and 0 <= sel_idx < len(filtered):
        cur_mod = filtered[sel_idx]
        ctx = generate_module_context(cur_mod)
        screen.text(76, 6, f"ID        : {cur_mod.id}", Palette.white())
        screen.text(76, 7, f"ENGINE    : {cur_mod.engine}", category_color(cur_mod.category))
        screen.text(76, 8, f"CATEGORY  : {cur_mod.category}", Palette.cyan())
        clr_bar = "■" * cur_mod.clearance + "□" * (5 - cur_mod.clearance)
        screen.text(
            76,
            9,
            f"CLEARANCE : {clr_bar} LVL-{cur_mod.clearance}",
            clearance_color(cur_mod.clearance),
        )
        status_txt = (
            "VISITED (SESSION COMPLETE)"
            if cur_mod.id in visited_ids
            else "READY FOR EXECUTION"
        )
        screen.text(
            76,
            10,
            f"STATUS    : {status_txt}",
            Palette.green() if cur_mod.id in visited_ids else Palette.amber(),
        )
        screen.text(76, 12, f"ORG       : {ctx['org']}", Palette.white(), max_w=40)
        screen.text(76, 13, f"DOMAIN    : {ctx['domain']}", Palette.muted(), max_w=40)
        screen.text(76, 14, f"ENDPOINT  : {ctx['primary_ip']}", Palette.green(), max_w=40)
        screen.text(76, 15, f"OPERATIVE : {ctx['callsign_a']}", Palette.purple(), max_w=40)

        screen.text(76, 17, "BRIEFING SUMMARY:", Palette.amber())
        wrapped = wrap_text(cur_mod.blurb, 40)
        for w_i, w_line in enumerate(wrapped[:4]):
            screen.text(76, 18 + w_i, w_line, Palette.white())

        # Mini Braille telemetry widget inside preview panel
        mini = BrailleCanvas(38, 5)
        rng = random.Random(cur_mod.seed)
        pts = [(rng.randint(4, 70), rng.randint(2, 17)) for _ in range(5)]
        for p_i in range(len(pts) - 1):
            mini.line(
                pts[p_i][0],
                pts[p_i][1],
                pts[p_i + 1][0],
                pts[p_i + 1][1],
                category_color(cur_mod.category),
            )
        screen.draw_box(76, 23, 40, 7, "SIGNAL SIGNATURE", "single", Palette.muted())
        mini.render(screen, 77, 24, category_color(cur_mod.category))

    # Footer (rows 32..33)
    pos_str = f"POS {sel_idx + 1 if filtered else 0}/{len(filtered)} (TOTAL {len(registry)})"
    if search_mode:
        prompt_str = f"SEARCH FILTER > {search_query}█   [Enter: Terapkan | Esc: Batal/Reset]"
        screen.text(2, 32, prompt_str, Palette.amber())
    else:
        keys_str = (
            "[↑/↓ j/k] Pilih  [←/→ Tab] Kategori  [/] Cari  [Enter] Jalankan  [Ctrl+C] Keluar"
        )
        screen.text(2, 32, keys_str, Palette.green())
    screen.text(SCREEN_W - len(pos_str) - 2, 32, pos_str, Palette.cyan())
    screen.present()


def run_module_deck(screen: Screen, registry: Sequence[ModuleDef]) -> None:
    cat_idx = 0
    sel_idx = 0
    scroll_top = 0
    visited_ids: set = set()
    search_mode = False
    search_query = ""
    visible_rows = 24

    if CFG.auto:
        # Automated demo across categories then exit cleanly
        for demo_cat in range(min(3, len(CATEGORIES))):
            cat_idx = demo_cat
            cat_mods = [m for m in registry if m.category == CATEGORIES[cat_idx]]
            if cat_mods:
                render_deck(
                    screen, registry, cat_idx, cat_mods, 0, 0, visited_ids, False, ""
                )
                nap(0.25)
                execute_module_scene(screen, cat_mods[0], visited_ids)
        return

    while True:
        active_cat = CATEGORIES[cat_idx]
        cat_mods = [m for m in registry if m.category == active_cat]
        if search_query:
            q_low = search_query.lower()
            filtered = [
                m
                for m in cat_mods
                if q_low in m.display_name.lower() or q_low in m.id.lower()
            ]
        else:
            filtered = cat_mods

        if not filtered:
            sel_idx = 0
            scroll_top = 0
        else:
            sel_idx = max(0, min(sel_idx, len(filtered) - 1))
            if sel_idx < scroll_top:
                scroll_top = sel_idx
            elif sel_idx >= scroll_top + visible_rows:
                scroll_top = sel_idx - visible_rows + 1

        render_deck(
            screen,
            registry,
            cat_idx,
            filtered,
            sel_idx,
            scroll_top,
            visited_ids,
            search_mode,
            search_query,
        )

        # Wait briefly for input while keeping HUD clock & CPU bars alive
        wait_loops = 0
        while not kbhit() and wait_loops < 10:
            time.sleep(0.04)
            wait_loops += 1

        if not kbhit():
            continue

        key = getch()
        if search_mode:
            if key == "ESC":
                search_mode = False
                search_query = ""
                sel_idx = 0
            elif key == "ENTER":
                search_mode = False
            elif key == "BACKSPACE":
                search_query = search_query[:-1]
                sel_idx = 0
            elif len(key) == 1 and 32 <= ord(key) <= 126 and len(search_query) < 28:
                search_query += key
                sel_idx = 0
            continue

        if key in ("UP", "k", "K"):
            sel_idx = max(0, sel_idx - 1)
        elif key in ("DOWN", "j", "J"):
            if filtered:
                sel_idx = min(len(filtered) - 1, sel_idx + 1)
        elif key in ("RIGHT", "TAB"):
            cat_idx = (cat_idx + 1) % len(CATEGORIES)
            sel_idx = 0
            scroll_top = 0
        elif key in ("LEFT", "SHIFT_TAB"):
            cat_idx = (cat_idx - 1) % len(CATEGORIES)
            sel_idx = 0
            scroll_top = 0
        elif key == "/":
            search_mode = True
        elif key == "ESC":
            search_query = ""
        elif key == "ENTER" and filtered:
            execute_module_scene(screen, filtered[sel_idx], visited_ids)
            screen.invalidate()


# ============================================================================
# [SECTION 10] COMPREHENSIVE SELFTEST SUITE (--selftest)
# ============================================================================


def run_selftest(master_seed: int = 2026) -> int:
    print("SYNXCN :: RUNNING SELF-VERIFICATION SUITE (9 CHECKS)")
    source_code = inspect.getsource(sys.modules[__name__])
    tree = ast.parse(source_code)

    # 1. Registry bounds (150-220), unique IDs, all fields populated
    reg = build_registry(target_count=200, master_seed=master_seed)
    assert 150 <= len(reg) <= 220, f"Invalid registry count: {len(reg)}"
    ids = [m.id for m in reg]
    assert len(ids) == len(set(ids)), "Duplicate module IDs detected"
    for m in reg:
        assert m.id and m.category and m.engine and m.display_name and m.blurb
        assert 1 <= m.clearance <= 5 and isinstance(m.seed, int)
    print(f"[PASS 1/9] Registry count={len(reg)} (in 150..220), all IDs unique & populated.")

    # 2. Every engine referenced in registry has a registered runner
    used_engines = {m.engine for m in reg}
    assert used_engines.issubset(set(ENGINE_RUNNERS.keys())), "Unregistered engine found"
    assert len(ENGINE_RUNNERS) == 16 and len(used_engines) == 16
    print(f"[PASS 2/9] All {len(used_engines)} engines registered and active.")

    # 3. AST scan: zero network imports (socket, requests, urllib, subprocess, etc.)
    banned_roots = {
        "socket",
        "requests",
        "urllib",
        "subprocess",
        "http",
        "ftplib",
        "poplib",
        "imaplib",
        "smtplib",
        "telnetlib",
        "xmlrpc",
    }
    imported_names: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_names.append(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_names.append(node.module.split(".")[0])
    bad_imports = [name for name in imported_names if name in banned_roots]
    assert not bad_imports, f"Forbidden network imports found: {bad_imports}"
    print("[PASS 3/9] AST scan verified: 0 network/subprocess imports.")

    # Collect all string literals from AST + all generated text across all 200 modules
    string_literals: List[str] = [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    ]
    generated_blobs: List[str] = []
    for m in reg:
        ctx = generate_module_context(m)
        debrief = "\n".join(render_debrief_lines(m, ctx))
        generated_blobs.append(f"{m.id} {m.display_name} {m.blurb} {debrief} {ctx}")
    all_texts = string_literals + generated_blobs

    # 4. IPv4 Regex scan: every IPv4 must be in RFC 1918 private or RFC 5737 doc ranges
    ip_regex = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    found_ips: List[str] = []
    for blob in all_texts:
        for match in ip_regex.findall(blob):
            found_ips.append(match)
            assert is_valid_safe_ip(match), f"Unsafe IPv4 address detected: {match}"
    assert len(found_ips) > 0, "Expected safe IPs to be validated"
    print(f"[PASS 4/9] IPv4 scan verified: {len(found_ips)} IP occurrences all within safe RFC ranges.")

    # 5. Domain-like Regex scan: ([a-z0-9-]+\.[a-z]{2,}) -> TLD must be in ALLOWED_TLDS
    dom_regex = re.compile(r"\b[a-z0-9-]+\.([a-z]{2,})\b", re.IGNORECASE)
    found_domains = 0
    for blob in all_texts:
        for m_obj in dom_regex.finditer(blob):
            full_dom = m_obj.group(0).lower()
            tld = "." + m_obj.group(1).lower()
            assert tld in ALLOWED_TLDS, f"Disallowed domain/TLD '{full_dom}' (TLD {tld})"
            found_domains += 1
    assert found_domains > 0, "Expected fictional domains to be validated"
    print(f"[PASS 5/9] Domain scan verified: {found_domains} occurrences all use reserved TLDs.")

    # 6. Case-insensitive forbidden brand scan across entire source & generated outputs
    # Encoded in hex so the source code itself never contains forbidden brand strings
    forbidden_hex = (
        "7768617473617070",  # forbidden token 1
        "676d61696c",        # forbidden token 2
        "676f6f676c65",      # forbidden token 3
        "74656c656772616d",  # forbidden token 4
        "696e7374616772616d",# forbidden token 5
        "66616365626f6f6b",  # forbidden token 6
        "74696b746f6b",      # forbidden token 7
        "70617970616c",      # forbidden token 8
    )
    forbidden_brands = [bytes.fromhex(h).decode("ascii") for h in forbidden_hex]
    combined_lower = (source_code + "\n" + "\n".join(generated_blobs)).lower()
    for brand in forbidden_brands:
        assert brand not in combined_lower, f"Forbidden brand detected: {brand}"
    print("[PASS 6/9] Brand safety scan verified: 0 real platform/brand occurrences.")

    # 7. Phone number pattern scan across all string literals & generator outputs
    phone_regex = re.compile(r"\+?\d{1,3}[-\s]?\d{3}[-\s]?\d{3,4}[-\s]?\d{3,4}")
    for blob in all_texts:
        m_phone = phone_regex.search(blob)
        assert m_phone is None, f"Phone-like digit sequence detected: {m_phone.group(0)}"
    print("[PASS 7/9] Phone pattern scan verified: 0 matches in literals or generators.")

    # 8. Registry determinism: build_registry(master_seed=2026) called twice -> identical
    reg_a = build_registry(target_count=200, master_seed=2026)
    reg_b = build_registry(target_count=200, master_seed=2026)
    assert repr(reg_a) == repr(reg_b), "Registry generation is not deterministic!"
    print("[PASS 8/9] Registry determinism verified: identical across repeated builds.")

    # 9. Debrief determinism: rendering DEBRIEF twice for same module & seed -> identical
    for m_a, m_b in zip(reg_a, reg_b):
        deb_a = "\n".join(render_debrief_lines(m_a))
        deb_b = "\n".join(render_debrief_lines(m_b))
        assert deb_a == deb_b and len(deb_a) > 20, f"Debrief mismatch on {m_a.id}"
    print(f"[PASS 9/9] Debrief determinism verified across all {len(reg_a)} modules.")
    print("ALL 9 SELFTEST CHECKS PASSED SUCCESSFULLY.")
    return 0


def parse_args(argv: Optional[Sequence[str]] = None) -> RuntimeConfig:
    parser = argparse.ArgumentParser(
        prog="SYNXCN",
        description="SYNXCN :: Operations Deck (100% Offline Terminal Simulation)",
    )
    parser.add_argument("--fast", action="store_true", help="Speed multiplier x2.5")
    parser.add_argument("--auto", action="store_true", help="Automated hands-free demo")
    parser.add_argument("--skip-intro", action="store_true", help="Skip boot & reveal")
    parser.add_argument("--sound", action="store_true", help="Enable terminal bell")
    parser.add_argument("--256", dest="color_256", action="store_true", help="256-color mode")
    parser.add_argument("--seed", type=int, default=2026, help="Override master seed")
    parser.add_argument("--selftest", action="store_true", help="Run safety & determinism tests")
    ns = parser.parse_args(argv)
    return RuntimeConfig(
        fast=ns.fast,
        auto=ns.auto,
        skip_intro=ns.skip_intro,
        sound=ns.sound,
        color_256=ns.color_256,
        seed=ns.seed,
        selftest=ns.selftest,
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    global CFG
    CFG = parse_args(argv)
    if CFG.selftest:
        try:
            return run_selftest(CFG.seed)
        except AssertionError as exc:
            sys.stderr.write(f"[SELFTEST FAILED] {exc}\n")
            return 1

    registry = build_registry(target_count=200, master_seed=CFG.seed)
    check_terminal_size(SCREEN_W, SCREEN_H)
    screen = Screen(SCREEN_W, SCREEN_H)
    try:
        init_terminal()
        run_boot_and_reveal(screen, CFG.seed)
        run_module_deck(screen, registry)
    except KeyboardInterrupt:
        pass
    finally:
        restore_terminal()
    return 0


if __name__ == "__main__":
    sys.exit(main())