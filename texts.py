from typing import Dict

# Локализованные строки интерфейса
T: Dict[str, Dict[str, str]] = {
    # Главный экран
    'main_title': {
        'ru': 'Главное меню', 'en': 'Main Menu', 'hi': 'मुख्य मेनू', 'es': 'Menú principal'
    },
    'main_desc': {
        'ru': 'Выберите действие ниже.', 'en': 'Choose an action below.',
        'hi': 'नीचे से कोई कार्रवाई चुनें।', 'es': 'Elige una acción abajo.'
    },

    # Кнопки главного экрана
    'btn_instruction': {
        'ru': '📘 Инструкция', 'en': '📘 Instructions', 'hi': '📘 निर्देश', 'es': '📘 Instrucciones'
    },
    'btn_support': {
        'ru': '🆘 Поддержка', 'en': '🆘 Support', 'hi': '🆘 सहायता', 'es': '🆘 Soporte'
    },
    'btn_change_lang': {
        'ru': '🌐 Сменить язык', 'en': '🌐 Change language', 'hi': '🌐 भाषा बदलें', 'es': '🌐 Cambiar idioma'
    },
    'btn_get_signal': {
        'ru': '🚀 Получить сигнал', 'en': '🚀 Get signal', 'hi': '🚀 सिग्नल प्राप्त करें', 'es': '🚀 Obtener señal'
    },
    'btn_open_miniapp': {
        'ru': '🔓 Открыть доступ', 'en': '🔓 Open dostup',
        'hi': '🔓 मिनी-ऐप खोलें', 'es': '🔓 Abrir dostup'
    },
    'btn_open_vip_miniapp': {
        'ru': '👑 Открыть PLATINUM', 'en': '👑 OpenPLATINUM',
        'hi': '👑 PLATINUM मिनी-ऐप खोलें', 'es': '👑 Abrir mini-app PLATINUM'
    },

    # Инструкция
    'instruction_title': {
        'ru': 'Как начать', 'en': 'How to start', 'hi': 'कैसे शुरू करें', 'es': 'Cómo empezar'
    },
    'instruction_text': {
    'ru':   "1) Зарегистрируйте аккаунт на брокере, по кнопке ниже \n"
            "2) Ожидайте автоматической проверки регистрации, бот вас оповестит.\n"
            "3) После успешной проверки следуйте оставшимся шагам\n"
            "4) Нажмите «Получить сигнал».\n"
            "5) Выберите инструмент для торговли в первой строчке интерфейса бота.\n"
            "6) Дублируйте этот инструмент на брокере.\n"
            "7) Выберите модель торговли TESSA Plus для обычных пользователей, TESSA Quantum для платинум пользователей.\n"
            "8) Выберите любое время экспирации.\n"
            "9) Дублируйте тоже самое время экспирации на брокере.\n"
            "10) Нажмите кнопку «Сгенерировать сигнал» и торгуйте строго исходя из аналитики бота, "
            "старайтесь подбирать более высокую вероятность.\n"
            "11) Заработайте профит.",
    'en':  "1) Register an account with the broker using the button below.\n"
           "2) Wait for the automatic registration check — the bot will notify you.\n"
           "3) After a successful check, follow the remaining steps.\n"
           "4) Tap \"Get Signal\".\n"
           "5) In the first row of the bot interface, choose the instrument to trade.\n"
           "6) Select the same instrument on the broker.\n"
           "7) Choose the trading model: TESSA Plus for regular users, TESSA Quantum for Platinum users.\n"
           "8) Choose any expiration time.\n"
           "9) Set the same expiration time on the broker.\n"
           "10) Tap \"Generate signal\" and trade strictly according to the bot’s analytics; "
           "try to pick higher probabilities.\n"
           "11) Take your profit.",
    'hi':  "1) नीचे दिए गए बटन से ब्रोक़र पर अकाउंट बनाएँ।\n"
           "2) स्वतः पंजीकरण जाँच का इंतज़ार करें — बॉट आपको सूचित करेगा।\n"
           "3) सफल जाँच के बाद शेष चरणों का पालन करें।\n"
           "4) \"सिग्नल प्राप्त करें\" दबाएँ।\n"
           "5) बॉट इंटरफ़ेस की पहली पंक्ति में ट्रेड करने के लिए इंस्ट्रूमेंट चुनें।\n"
           "6) वही इंस्ट्रूमेंट ब्रोक़र पर भी चुनें।\n"
           "7) ट्रेडिंग मॉडल चुनें: सामान्य उपयोगकर्ताओं के लिए TESSA Plus, और प्लैटिनम उपयोगकर्ताओं के लिए TESSA Quantum।\n"
           "8) कोई भी एक्सपायरी समय चुनें।\n"
           "9) वही एक्सपायरी समय ब्रोक़र पर भी सेट करें।\n"
           "10) \"सिग्नल जनरेट करें\" दबाएँ और बॉट की एनालिटिक्स के अनुसार ही ट्रेड करें; "
           "अधिक संभावना वाले विकल्प चुनने की कोशिश करें।\n"
           "11) मुनाफ़ा कमाएँ।",
    'es':  "1) Registra una cuenta en el bróker con el botón de abajo.\n"
           "2) Espera la verificación automática del registro; el bot te avisará.\n"
           "3) Tras la verificación correcta, sigue los pasos restantes.\n"
           "4) Pulsa «Obtener señal».\n"
           "5) En la primera fila de la interfaz del bot, elige el instrumento para operar.\n"
           "6) Duplica ese instrumento en el bróker.\n"
           "7) Elige el modelo de trading: TESSA Plus para usuarios normales, TESSA Quantum para usuarios Platinum.\n"
           "8) Elige cualquier tiempo de expiración.\n"
           "9) Configura el mismo tiempo de expiración en el bróker.\n"
           "10) Pulsa «Generar señal» y opera estrictamente según el análisis del bot; "
           "intenta elegir probabilidades más altas.\n"
           "11) Obtén el beneficio."
},
    'btn_register': {
        'ru': '📝 Зарегистрироваться', 'en': '📝 Register',
        'hi': '📝 पंजीकरण', 'es': '📝 Registrarse'
    },
    'already_registered': {
        'ru': 'Вы уже зарегистрированы ✅',
        'en': 'You are already registered ✅',
        'hi': 'आप पहले से पंजीकृत हैं ✅',
        'es': 'Ya estás registrado ✅'
    },

    # Экраны шагов
    'lang_title': {
        'ru': 'Выберите язык', 'en': 'Choose language', 'hi': 'भाषा चुनें', 'es': 'Elige idioma'
    },

    'subscribe_title': {
        'ru': 'Шаг 1 — Подписка', 'en': 'Step 1 — Subscribe',
        'hi': 'चरण 1 — सदस्यता', 'es': 'Paso 1 — Suscribirse'
    },
    'subscribe_text': {
        'ru': 'Подпишитесь на наш канал, затем вернитесь в бота.',
        'en': 'Subscribe to our channel, then return to the bot.',
        'hi': 'हमारे चैनल को सब्सक्राइब करें, फिर बॉट पर लौटें।',
        'es': 'Suscríbete a nuestro canal y vuelve al bot.'
    },
    'btn_ive_subscribed': {
        'ru': '🔄 Я подписался', 'en': "🔄 I've subscribed",
        'hi': '🔄 मैंने सदस्यता ले ली', 'es': '🔄 Ya me suscribí'
    },
    'sub_confirmed': {
        'ru': 'Подписка подтверждена ✅',
        'en': 'Subscription confirmed ✅',
        'hi': 'सदस्यता की पुष्टि हो गई ✅',
        'es': 'Suscripción confirmada ✅'
    },
    'sub_not_yet': {
        'ru': 'Пока не вижу подписку. Проверьте, что вы вступили в канал и попробуйте ещё раз.',
        'en': "I don't see the subscription yet. Please join the channel and try again.",
        'hi': 'अभी सदस्यता नहीं दिख रही। कृपया चैनल जॉइन करें और फिर से प्रयास करें।',
        'es': 'Aún no veo la suscripción. Únete al canal e inténtalo de nuevo.'
    },

    'register_title': {
        'ru': 'Шаг 2 — Регистрация', 'en': 'Step 2 — Registration',
        'hi': 'चरण 2 — पंजीकरण', 'es': 'Paso 2 — Registro'
    },
    'register_text': {
        'ru': 'Зарегистрируйтесь у брокера через кнопку ниже.',
        'en': 'Register with the broker via the button below.',
        'hi': 'नीचे दिए बटन से पंजीकरण करें।',
        'es': 'Regístrate con el bróker usando el botón.'
    },

    'deposit_title': {
        'ru': 'Шаг 3 — Депозит', 'en': 'Step 3 — Deposit',
        'hi': 'चरण 3 — जमा', 'es': 'Paso 3 — Depósito'
    },
    'deposit_text': {
        'ru': 'Внесите первый депозит через кнопку ниже.',
        'en': 'Make your first deposit via the button below .',
        'hi': 'पहली जमा राशि नीचे दिए बटन से करें ।',
        'es': 'Realiza tu primer depósito con el botón .'
    },

    'access_title': {
        'ru': 'Доступ открыт', 'en': 'Access granted',
        'hi': 'प्रवेश खुला', 'es': 'Acceso concedido'
    },
    'access_text': {
        'ru': 'Вы выполнили все шаги. Откройте мини-апп.',
        'en': 'All steps are complete. Open the mini-app.',
        'hi': 'सभी चरण पूरे। मिनी-ऐप खोलें।',
        'es': 'Todos los pasos completos. Abre la mini-app.'
    },

    # Депозит/Platinum
    'btn_deposit': {
        'ru': '💳 Внести депозит', 'en': '💳 Deposit',
        'hi': '💳 जमा करें', 'es': '💳 Depositar'
    },

    'platinum_title': {
        'ru': 'Поздравляем! Платинум', 'en': 'Congratulations! Platinum',
        'hi': 'बधाई! प्लेटिनम', 'es': '¡Felicidades! Platino'
    },
    'platinum_text': {
        'ru': 'Ваш общий депозит достиг порога. Доступна VIP мини-апп.',
        'en': 'Your total deposits reached the threshold. VIP mini-app is available.',
        'hi': 'आपकी कुल जमा राशि सीमा तक पहुंच गई है। VIP मिनी-ऐप उपलब्ध है।',
        'es': 'Tus depósitos alcanzaron el umbral. Mini-app VIP disponible.'
    },

    # Навигация
    'btn_menu': {
        'ru': '↩️ В главное меню', 'en': '↩️ Main menu',
        'hi': '↩️ मुख्य मेनू', 'es': '↩️ Menú principal'
    },

    # рядом с остальными ключами
    'deposit_need': {
        'ru': 'Необходимо внести',
        'en': 'Required',
        'hi': 'आवश्यक राशि',
        'es': 'Requerido',
    },
    'deposit_paid': {
        'ru': 'Внесено',
        'en': 'Paid',
        'hi': 'जमा किया',
        'es': 'Aportado',
    },
    'deposit_left': {
        'ru': 'Осталось внести',
        'en': 'Left to pay',
        'hi': 'बाकी राशि',
        'es': 'Falta por aportar',
    },

}


def t(lang: str, key: str) -> str:
    """Безопасное извлечение перевода с фоллбэком на EN/ключ."""
    d = T.get(key) or {}
    return d.get(lang) or d.get('en') or key
