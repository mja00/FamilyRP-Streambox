﻿import os

from streamlink import __version__ as LIVESTREAMER_VERSION

from .compat import is_win32

DEFAULT_PLAYER_ARGUMENTS = "{filename}"

if is_win32:
    APPDATA = os.path.normpath("E:/Downloads - Data Drive/Streamlink_for_Windows_Portable_v0.7.0")
    CONFIG_FILES = [os.path.join(APPDATA, "streamlinkrc")]
    PLUGINS_DIR = os.path.join(APPDATA, "plugins")
else:
    XDG_CONFIG_HOME = os.environ.get("XDG_CONFIG_HOME", "~/.config")
    CONFIG_FILES = [
        os.path.expanduser(XDG_CONFIG_HOME + "/streamlink/config"),
        os.path.expanduser("~/.streamlinkrc")
    ]
    PLUGINS_DIR = os.path.expanduser(XDG_CONFIG_HOME + "/streamlink/plugins")

STREAM_SYNONYMS = ["best", "worst"]
STREAM_PASSTHROUGH = ["hls", "http", "rtmp"]

__all__ = [
    "CONFIG_FILES", "DEFAULT_PLAYER_ARGUMENTS", "LIVESTREAMER_VERSION",
    "PLUGINS_DIR", "STREAM_SYNONYMS", "STREAM_PASSTHROUGH"
]



