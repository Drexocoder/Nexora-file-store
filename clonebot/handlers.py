"""Minimal clone runtime while the Nexora V2 template registry is rebuilt.

All legacy template implementations are intentionally
removed from the runtime. New templates will register their own handlers.
"""

from __future__ import annotations

import logging

from pyrogram import Client, filters
from pyrogram.types import Message

log = logging.getLogger("nexora.clonebot")


def register_clone_handlers(app: Client) -> None:
    """Attach the neutral runtime used when no V2 template is installed."""

    @app.on_message(filters.command("start") & filters.private)
    async def start(client: Client, message: Message) -> None:
        await message.reply_text(
            "**Template unavailable**\n\n"
            "> This clone is retired and no longer supported.\n\n"
            "→ New Nexora V2 templates will be available from the Factory."
        )

    @app.on_message(filters.private & filters.command(["help", "owner"]))
    async def help_or_owner(client: Client, message: Message) -> None:
        await message.reply_text(
            "**Nexora V2**\n\n"
            "> This clone has been retired.\n"
            "> Create or deploy a supported V2 template from the main Factory."
        )
