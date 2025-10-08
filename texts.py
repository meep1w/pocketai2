from typing import Dict

# Локализованные строки (только чешский)
T: Dict[str, Dict[str, str]] = {
    # Главный экран
    'main_title': {'cs': 'Hlavní menu'},
    'main_desc': {'cs': 'Vyber akci níže.'},

    # Кнопки главного экрана
    'btn_instruction': {'cs': '📘 Instrukce'},
    'btn_support': {'cs': '🆘 Podpora'},
    'btn_get_signal': {'cs': '🚀 Získat signál'},
    'btn_open_miniapp': {'cs': '🔓 Otevřít přístup'},
    'btn_open_vip_miniapp': {'cs': '👑 Otevřít PLATINUM'},

    # Инструкция
    'instruction_title': {'cs': '🔹 Postupujte podle následujících kroků:'},
    'instruction_text': {'cs':
        "1️⃣ Zaregistrujte si účet u brokera PocketOption – nutně přes našeho bota. Pro registraci zadejte: /start → Získat signál → Zaregistrovat se.\n"
        "2️⃣ Počkejte na automatickou kontrolu registrace – bot vás upozorní.\n"
        "3️⃣ Po úspěšné kontrole vložte svůj vklad: /start → Získat signál → Vložit vklad.\n"
        "4️⃣ Počkejte na automatickou kontrolu vkladu – bot vás upozorní.\n"
        "5️⃣ Klikněte na „Získat signál“.\n"
        "6️⃣ Vyberte nástroj pro obchodování v první řádce rozhraní bota.\n"
        "7️⃣ Zkopírujte tento nástroj u brokera PocketOption.\n"
        "8️⃣ Zvolte obchodní model: \nTESSA Plus – pro běžné uživatele \nTESSA Quantum – pro Platinum uživatele\n"
        "9️⃣ Vyberte libovolný čas expirace.\n"
        "🔟 Zkopírujte stejný čas expirace u brokera PocketOption.\n"
        "1️⃣1️⃣ Klikněte na „Vygenerovat signál“ a obchodujte výhradně podle analýzy bota – vždy volte vyšší pravděpodobnost."
        "1️⃣2️⃣ Získejte profit. 💰🚀"
    },

    'btn_register': {'cs': '🟢 Zaregistrovat se'},
    'already_registered': {'cs': 'Už jsi zaregistrován ✅'},

    # Экраны шагов
    'subscribe_title': {'cs': '🚀 Krok 1 — Odběr kanálu'},
    'subscribe_text': {'cs': 'Přihlaste se k odběru kanálu a vraťte se zpět — Pote klikněte na ✅ Ověřit odběr.'},
    'btn_ive_subscribed': {'cs': '🔄 Jsem přihlášen'},
    'sub_confirmed': {'cs': '✅ Ověřit odběr'},
    'sub_not_yet': {'cs': 'Odběr zatím nevidím. Připoj se ke kanálu a zkus to znovu.'},

    'register_title': {'cs': '✅ Krok 2 — Registrace'},
    'register_text': {'cs': 'Zaregistrujte se na PocketOption pomocí tlačítka níže. Po dokončení registrace se vraťte zpět sem.'},

    'deposit_title': {'cs': 'Krok 3 — Vklad'},
    'deposit_text': {'cs': 'Proveď první vklad pomocí tlačítka níže.'},

    'access_title': {'cs': 'Přístup povolen'},
    'access_text': {'cs': 'Splnil(a) jsi všechny kroky. Otevři mini-app.'},

    # Депозит/Platinum
    'btn_deposit': {'cs': '💳 Vklad'},
    'platinum_title': {'cs': 'Gratulujeme! Platinum'},
    'platinum_text': {'cs': 'Součet tvých vkladů dosáhl prahu. VIP mini-app je dostupná.'},

    # Навигация
    'btn_menu': {'cs': '⬅️ Zpět do menu'},

    # Прогресс/суммы
    'deposit_need': {'cs': 'Nutno vložit'},
    'deposit_paid': {'cs': 'Vloženo'},
    'deposit_left': {'cs': 'Zbývá vložit'},
}

def t(_lang: str, key: str) -> str:
    """
    Возвращает строку только на чешском.
    _lang игнорируем — бот работает на одном языке.
    """
    d = T.get(key) or {}
    return d.get('cs') or key
