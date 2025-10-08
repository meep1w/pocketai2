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
    'instruction_title': {'cs': 'Jak začít'},
    'instruction_text': {'cs':
        "1) Zaregistruj si účet u brokera pomocí tlačítka níže.\n"
        "2) Počkej na automatickou kontrolu registrace — bot tě upozorní.\n"
        "3) Po úspěšné kontrole pokračuj podle kroků.\n"
        "4) Stiskni „Získat signál“.\n"
        "5) V první řádce rozhraní bota zvol nástroj pro obchodování.\n"
        "6) Stejný nástroj zvol u brokera.\n"
        "7) Zvol model: TESSA Plus pro běžné uživatele, TESSA Quantum pro Platinum.\n"
        "8) Zvol libovolný čas expirace.\n"
        "9) Stejný čas nastav u brokera.\n"
        "10) Stiskni „Vygenerovat signál“ a obchoduj striktně dle analytiky bota; vybírej vyšší pravděpodobnost.\n"
        "11) Získej profit."
    },

    'btn_register': {'cs': '📝 Registrovat'},
    'already_registered': {'cs': 'Už jsi zaregistrován ✅'},

    # Экраны шагов
    'subscribe_title': {'cs': 'Krok 1 — Odběr kanálu'},
    'subscribe_text': {'cs': 'Přihlas se k odběru našeho kanálu a vrať se do bota.'},
    'btn_ive_subscribed': {'cs': '🔄 Jsem přihlášen'},
    'sub_confirmed': {'cs': 'Odběr potvrzen ✅'},
    'sub_not_yet': {'cs': 'Odběr zatím nevidím. Připoj se ke kanálu a zkus to znovu.'},

    'register_title': {'cs': 'Krok 2 — Registrace'},
    'register_text': {'cs': 'Zaregistruj se u brokera pomocí tlačítka níže.'},

    'deposit_title': {'cs': 'Krok 3 — Vklad'},
    'deposit_text': {'cs': 'Proveď první vklad pomocí tlačítka níže.'},

    'access_title': {'cs': 'Přístup povolen'},
    'access_text': {'cs': 'Splnil(a) jsi všechny kroky. Otevři mini-app.'},

    # Депозит/Platinum
    'btn_deposit': {'cs': '💳 Vklad'},
    'platinum_title': {'cs': 'Gratulujeme! Platinum'},
    'platinum_text': {'cs': 'Součet tvých vkladů dosáhl prahu. VIP mini-app je dostupná.'},

    # Навигация
    'btn_menu': {'cs': '↩️ Hlavní menu'},

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
