"""Nexora premium Telegram custom emoji registry.

Keep all platform-wide custom emoji markup in one place so Factory text,
buttons, logs, wallet screens, referrals, and templates share one visual
language.

Each value is Telegram HTML custom-emoji markup and can be embedded directly
in bot messages.
"""


class EMOJI:
    USER = '<tg-emoji emoji-id="5408846628763217930">👤</tg-emoji>'
    STADIUM = '<tg-emoji emoji-id="5195426924981154277">🏟</tg-emoji>'
    QUESTION = '<tg-emoji emoji-id="5452061640507803327">❔</tg-emoji>'
    FOOTBALL = '<tg-emoji emoji-id="5875210601717830561">⚽️</tg-emoji>'
    STAR = '<tg-emoji emoji-id="5895511022340411227">⭐️</tg-emoji>'
    BOLT = '<tg-emoji emoji-id="6023761060786346622">⚡️</tg-emoji>'
    TARGET = '<tg-emoji emoji-id="6125218994455582617">🎯</tg-emoji>'
    BRAIN = '<tg-emoji emoji-id="5237799019329105246">🧠</tg-emoji>'
    SPARKLES = '<tg-emoji emoji-id="5451636889717062286">✨</tg-emoji>'
    SHIELD = '<tg-emoji emoji-id="5251203410396458957">🛡</tg-emoji>'
    MUSCLE = '<tg-emoji emoji-id="5427342093674630148">💪</tg-emoji>'
    DIAMOND = '<tg-emoji emoji-id="5971895400792067820">🔹</tg-emoji>'
    MONEY = '<tg-emoji emoji-id="6278294652541996868">💰</tg-emoji>'
    GEM = '<tg-emoji emoji-id="5471952986970267163">💎</tg-emoji>'
    ROBOT = '<tg-emoji emoji-id="6030400221232501136">🤖</tg-emoji>'
    EXTRA_LIKE_1 = '<tg-emoji emoji-id="5251343946021362924">👍</tg-emoji>'
    CONSOLE = '<tg-emoji emoji-id="6023852878597200124">🎮</tg-emoji>'
    CROWN = '<tg-emoji emoji-id="5895709153476742796">👑</tg-emoji>'
    BALL = '<tg-emoji emoji-id="6021757930989164684">⚾️</tg-emoji>'
    GREEN_BUTTON = '<tg-emoji emoji-id="5852777287451151788">🟢</tg-emoji>'
    NEXT = '<tg-emoji emoji-id="5807440329934118281">➡️</tg-emoji>'
    CONGRATS = '<tg-emoji emoji-id="6041731551845159060">🎉</tg-emoji>'
    VOTE = '<tg-emoji emoji-id="6032745346390560408">🗳</tg-emoji>'
    CRICKET = '<tg-emoji emoji-id="6030703634902161922">🏏</tg-emoji>'
    BID = '<tg-emoji emoji-id="6039729023343400390">🔨</tg-emoji>'
    TIMER = '<tg-emoji emoji-id="6194961953308283021">⏳</tg-emoji>'
    WARN = '<tg-emoji emoji-id="5408943604829794451">⚠️</tg-emoji>'
    CLOCK = '<tg-emoji emoji-id="6035276353438227060">⏰</tg-emoji>'
    TICK = '<tg-emoji emoji-id="5406690851533370477">✅</tg-emoji>'
    WRONG = '<tg-emoji emoji-id="5807692706507399432">✖️</tg-emoji>'
    BACK = '<tg-emoji emoji-id="5807862477974674485">⬅️</tg-emoji>'
    TROPHY = '<tg-emoji emoji-id="6021644067111180663">🏆</tg-emoji>'
    SAVE = '<tg-emoji emoji-id="6021741567163767583">💾</tg-emoji>'
    RESTORE = '<tg-emoji emoji-id="6021772508108167860">♻️</tg-emoji>'
    END = '<tg-emoji emoji-id="6271674836628541366">🛑</tg-emoji>'
    STOP = '<tg-emoji emoji-id="5938215362473496448">🚫</tg-emoji>'
    FIRE = '<tg-emoji emoji-id="6021384767050618542">🔥</tg-emoji>'
    AIR = '<tg-emoji emoji-id="6023619893801261729">💨</tg-emoji>'
    OUT = '<tg-emoji emoji-id="5402569791758150517">💀</tg-emoji>'
    ROCKET = '<tg-emoji emoji-id="5929393980683848892">🚀</tg-emoji>'
    WINNER = '<tg-emoji emoji-id="6269400956387987689">🥇</tg-emoji>'
    LETTER = '<tg-emoji emoji-id="6023985764885338464">📜</tg-emoji>'
    SEARCH = '<tg-emoji emoji-id="5929240366883541760">🔍</tg-emoji>'
    GRAPH = '<tg-emoji emoji-id="5936143551854285132">📊</tg-emoji>'
    LOCK = '<tg-emoji emoji-id="6037249452824072506">🔒</tg-emoji>'
    HELP = '<tg-emoji emoji-id="6021620268697393273">ℹ️</tg-emoji>'
    ADD = '<tg-emoji emoji-id="6033108709213736873">➕</tg-emoji>'
    CLEAN = '<tg-emoji emoji-id="5278491193053822590">🧹</tg-emoji>'
    CLAP = '<tg-emoji emoji-id="6021561470595112226">👏</tg-emoji>'
    SIREN = '<tg-emoji emoji-id="6023782836270536399">🚨</tg-emoji>'
    MSG = '<tg-emoji emoji-id="6030863729808120196">💬</tg-emoji>'
    USTAR = '<tg-emoji emoji-id="5895583431194054511">🌟</tg-emoji>'
    SWAP = '<tg-emoji emoji-id="5807492110059838726">🔄</tg-emoji>'
    LIKE = '<tg-emoji emoji-id="6037400098801979304">👍</tg-emoji>'

    # Keep acknowledgements limited to the two approved custom likes.
    BOT_LIKES = (LIKE, EXTRA_LIKE_1)

    @staticmethod
    def random_like():
        import random
        return random.choice(EMOJI.BOT_LIKES)

    # Backwards-compatible aliases used by older modules.
    SHEILD = SHIELD
    RIGHT_ARROW = NEXT


__all__ = ["EMOJI"]
