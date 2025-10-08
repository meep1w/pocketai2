from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from texts import t
from settings import settings

# РАНЬШЕ было:
# _ADMIN_IDS = getattr(settings, "ADMIN_IDS", []) or [getattr(settings, "ADMIN_ID", None)]
# _SUPPORT_DEEPLINK = f"tg://user?id={_ADMIN_IDS[0]}" if _ADMIN_IDS and _ADMIN_IDS[0] else None

def kb_main(lang: str, is_platinum: bool, can_open: bool, support_url: str | None) -> InlineKeyboardMarkup:
    """
    Главное меню. Ссылку поддержки даем только https, без tg://user?id=...
    Порядок приоритетов: support_url из БД → SUPPORT_URL из .env → CHANNEL_URL из .env → https://t.me/
    """
    sup = (
        support_url
        or (getattr(settings, "SUPPORT_URL", "") or None)
        or (getattr(settings, "CHANNEL_URL", "") or None)
        or "https://t.me/"
    )
    rows = [
        [InlineKeyboardButton(text=t(lang, "btn_instruction"), callback_data="instructions")],
        [InlineKeyboardButton(text=t(lang, "btn_support"), url=sup)],
    ]
    if can_open:
        url = settings.MINI_APP_PLATINUM if is_platinum else settings.MINI_APP
        label = t(lang, "btn_open_vip_miniapp") if is_platinum else t(lang, "btn_open_miniapp")
        rows.append([InlineKeyboardButton(text=label, web_app=WebAppInfo(url=url))])
    else:
        rows.append([InlineKeyboardButton(text=t(lang, "btn_get_signal"), callback_data="get_signal")])
    return InlineKeyboardMarkup(inline_keyboard=rows)



def kb_instruction(lang: str) -> InlineKeyboardMarkup:
    # Регистрация через callback — чтобы показать алерт, если уже зарегистрирован
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(lang, "btn_register"), callback_data="btn_register")],
        [InlineKeyboardButton(text=t(lang, "btn_menu"), callback_data="menu")],
    ])


# kb_lang удалена: выбор языка пользователю больше не предлагается.


def kb_subscribe(lang: str, channel_url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📣 Telegram', url=channel_url)],
        [InlineKeyboardButton(text=t(lang, 'btn_ive_subscribed'), callback_data='check_sub')],
        [InlineKeyboardButton(text=t(lang, 'btn_menu'), callback_data='menu')],
    ])


def kb_register(lang: str, url: str) -> InlineKeyboardMarkup:
    # Утилита для экранов, где нужна именно URL-кнопка регистрации
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(lang, "btn_register"), url=url)],
        [InlineKeyboardButton(text=t(lang, "btn_menu"), callback_data="menu")],
    ])


def kb_deposit(lang: str, url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(lang, "btn_deposit"), url=url)],
        [InlineKeyboardButton(text=t(lang, "btn_menu"), callback_data="menu")],
    ])


def kb_access(lang: str, vip: bool) -> InlineKeyboardMarkup:
    url = settings.MINI_APP_PLATINUM if vip else settings.MINI_APP
    label = t(lang, "btn_open_vip_miniapp") if vip else t(lang, "btn_open_miniapp")
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=label, web_app=WebAppInfo(url=url))],
        [InlineKeyboardButton(text=t(lang, "btn_menu"), callback_data="menu")],
    ])
