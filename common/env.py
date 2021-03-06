# Licensed under the MIT license. Copyright (C) nerdguyahmad 2022-2023

"""Configuration constants from env file.

All configurations used by this bot are prefixed with "OXIDE_" for ease
of maintainence and readibility. Most configuration constants are given
default values internally when they are not supplied in env file while
few are required such as `OXIDE_BOT_TOKEN`.

For enivornment variables that need booleans, Any value except 'false' and '0'
will be considered true. Note that case here is insensitive and is completely
ignored while processing booleans.

Configuration options
---------------------

OXIDE_BOT_TOKEN:
    The bot authorization token. (Required)
OXIDE_EXTS_DIRECTORY:
    The directory to use for extensions. This defaults to "cogs/".
OXIDE_EXTS_EXCLUDE:
    The comma separated list of extension names to exclude. Note that
    the names should be relative to given `OXIDE_EXTS_DIRECTORY`. For
    example `ext` is valid and `cogs.ext` is not valid.
OXIDE_DEBUG_MODE:
    A boolean representing whether the bot is being ran in debug mode.
    In debug mode, the global application commands would be moved to
    given "DEBUG_GUILD_ID" guild in command tree for ease of debugging.

    For the sake of convenience, this value can also be set to True
    by passing "--debug-mode" flag while running the bot.

    Example::

        python bot.py --debug-mode
"""

from __future__ import annotations

import os
import dotenv
import sys


def _process_boolean(val: str) -> bool:
    return val.lower() not in ("false", "0")


# Type checker cries about load_dotenv()'s type being
# partially unknown so here we are
dotenv.load_dotenv()  # type: ignore


# Required
BOT_TOKEN = os.environ.get("OXIDE_BOT_TOKEN")

# Optional/default
EXTS_DIRECTORY = os.environ.get("OXIDE_EXTS_DIRECTORY", "cogs/")
EXTS_EXCLUDE = os.environ.get("OXIDE_EXTS_EXCLUDE", "")
DEBUG_MODE = _process_boolean(os.environ.get("OXIDE_DEBUG_MODE", "0")) or "--debug" in sys.argv
DEBUG_GUILD_ID = os.environ.get("OXIDE_DEBUG_GUILD_ID")
