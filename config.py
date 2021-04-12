# -*- coding: utf-8 -*-
token = "1769712553:AAFxk2jnn_yVHEMoNaNHyKMqFAF6X5eoY28"
db_file = "database.vdb"

test = [['1. ___your name?', '1. Who’s', '2. What’s', '3. How’s', '4. Why’s', 1],
       ['2. How many brothers ___ ?', '1. do you have', '2. you have', '3. are you have', '4. do you has', 0],
       ['3. Look at ___ men over there. Do you recognise them?', '1. that', '2. those', '3. these', '4. this', 1],
        ['4. I forgot ___ Jenny. I need ___ her now.', '1. to call / to call', '2. calling / to call',
         '3. to call / calling', '4. calling / calling', 0],
        ['5. There weren''t ___ people in the streets.', '1. a', '2. some', '3. the', '4. any', 3],
        ['6. ___ anything?', '1. Was he said', '2. Did he said', '3. Did he say', '4. Does he said', 2],
        ['7. She gets up at seven in the morning. Куда вы поставите слово always?',
         '1. Между she и gets.', '2. В начало предложения.',
         '3. После gets up.', '4. Между gets и up.', 0],
        ['8. Ответом на какой вопрос является следующее предложение? - I’m an engineer.',
         '1. What do you do for a living?', '2. Where are you staying?',
         '3. What are you doing here?', '4. Where are you from?', 0],
        ['9. He works very ___.', '1. harder', '2. hardest', '3. hardly', '4. hard', 3],
        ['10. Выберите подходящий ответ на вопрос: \n- What was the food like there?',
         '1. - Amazing! Especially the fish.', '2. - Very sad. I couldn’t stop crying.',
         '3. - It started well, but the ending was terrible.',
         '4. - They sang all of my favourite songs.', 0],
        ['11. Выберите подходящий фразовый глагол: We arranged to meet at 7.30, but she never ___',
         '1. turned up', '2. made up', '3. gave up', '4. ended up', 0],
        ["12. Thank you so much for inviting me. But I'm afraid I can't make it tonight "
         "because I'll be busy helping my parents. If I ___ so busy, I ___.",
         '1. is not, had come', '2. wouldn’t have been, had come', '3. am not, would come','4. were not, would come',3],
        ['13. There were lots of people crossing the road. Чем можно заменить слово lots, чтобы сохранить значение?',
         '1. a handful', '2. a whale', '3. loads', '4. kilos', 2],
        ['14. Переведите предложение с помощью глагола wish: Жаль, что я не видел этого (it).',
         '1. I wish that I had seen it.', '2. I wish I had seen it.',
         "3. I wish I'd seen it.", "4. I wish that I'd seen it.", 1],
        ['15.  Выберите слово для продолжения ряда синонимов: hitch, setback, glitch, snag',
         '1. problem', '2. flashback', '3. joy', '4. rest', 0],
        ['16.  We ___ have pocket money when we were younger.', '1. didn’t get used to', '2. weren’t used to',
         '3. didn’t use to', '4. don’t get used to', 2],
        ['17. Подберите правильное продолжение: Apparently, it’s going to pour down tomorrow all day, so…',
         '1. ...it’ll be very hot, which I hate.', '2. ...it will clear out in the morning.',
         '3. ...I might get a bit of a suntan.', '4. ...we’d better stay at home \nand keep out of the rain.', 3],
        ["18. Chris phoned to say they'd arrived safely, so that really put my mind ___.",
         '1. to sleep', '2. at rest', '3. down', '4. away', 1],
        ['19.  Подберите глагол, сочетающийся со словом ambitions.',
         '1. to achieve all your ambitions', '2. to get all your ambitions',
         '3. to reach all your ambitions', '4. to take all your ambitions', 0],
        ['20.  I could listen to it all day. The music is so inspiring, so ___.',
         '1. weird', '2. uplifting',
         '3. creepy', '4. heart-sinking', 1],
        ['21. I didn’t like the song at first, but now it is really ___ me.',
         '1. getting to', '2. breaking through',
         '3. growing on', '4. catching up', 2],
        ['22. Hurry up! The film ___ by the time we get to the cinema.',
         '1. will probably have started', '2. is probably starting',
         '3. will probably be starting', '4. has probably started', 0],
        ['23.  I’m writing to ___ about the Chinese courses offered by your center.',
         '1. request', '2. demand', '3. inquire', '4. interrogate', 2],
        ['24. The area was full of black smoke from factories, ___ the name "the Black Country.',
         '1. though', '2. hence', '3. consequently', '4. nevertheless', 1],
        ['25. Что означает “to open a can of worms”?',
         '1. Спустить всех собак на кого-либо.',
         '2. Разговорить болтливого человека.',
         '3. Приготовить что-то несъедобное.',
         '4. Создать ряд проблем, требующих решения.', 3],
        ['26.  After my son broke his friend’s new toy, I had to ___ 50 dollars so that they could buy him a new one.',
         '1. give out', '2. cough up', '3. take on', '4. break out', 1],
        ['27. ___ the people I spoke to knew him.', '1. No of', '2. No one of', '3. None of', '4. Not a single of', 2],
        ["28. Найдите подходящее завершение реплики: I didn't even eat lunch today.\n - Really? ___",
         '1. Should you?', '2. How come?', '3. I might as well.', '4. Get it over with.',1 ],
        ['29. If you are flicking through your Facebook feed, you are...?',
        '1. reading each post very carefully.','2. looking for some specific information.',
         '3. using the search box.', '4. quickly reading some of the posts.', 3],
        ['30.  - I wish we ___ about it earlier. \n- Oh, well, we didn’t.',
         '1. had thought', '2. have thought',
         '3. thought', '4. could think', 0]]


questions = ["1. <b>What's</b> your name?",
             '2. How many brothers <b>do you have</b> ?',
             '3. Look at <b>those</b> men over there. Do you recognise them?' ,
             '4. I forgot <b>to call</b> Jenny. I need <b>to call</b> her now.',
             "5. There weren't <b> any</b> people in the streets.",
             '6. <b>Did he say</b> anything? ',
             '7. She <b>always</b> gets up at seven in the morning.',
             '8. <b>- What do you do for a living</b>? \n- I’m an engineer. ',
             '9. He works very <b>hard</b>.',
             '10. What was the food like there?\n<b>- Amazing! Especially the fish.</b>.',
             '11. We arranged to meet at 7.30, but she never <b>turned up</b>.',
             "12. Thank you so much for inviting me. "
             "But I'm afraid I can't make it tonight because I'll be busy helping my parents. "
             "If I <b>were not</b> so busy, I <b>would come</b>.",
             '13. There were <b>loads</b> of people crossing the road. Чем можно заменить слово lots, '
             'чтобы сохранить значение?',
             '14. Переведите предложение с помощью глагола wish: - Жаль, что я не видел этого (it). '
             '\n(<b>- I wish I had seen it.</b>)',
             '15. Выберите слово для продолжения ряда синонимов: hitch, setback, glitch, snag'
             '\n(<b> problem</b>)',
             '16. We <b>didn’t use to</b> have pocket money when we were younger.',
             '17. Apparently, it’s going to pour down tomorrow all day, so <b>we’d better stay at home and '
             'keep out of the rain.</b>',
             "18. Chris phoned to say they'd arrived safely, so that really put my mind <b>at rest</b>.",
             '19. Подберите глагол, сочетающийся со словом ambitions.\n<b>- to achieve all your ambitions</b>',
             '20. I could listen to it all day. The music is so inspiring, so <b>uplifting</b>.',
             '21. I didn’t like the song at first, but now it is really <b>growing on</b> me.',
             '22. Hurry up! The film <b>will probably have started</b> by the time we get to the cinema.',
             '23.  I’m writing to <b>inquire</b> about the Chinese courses offered by your center.',
             '24. The area was full of black smoke from factories, <b>hence</b> the name "the Black Country."',
             '25. Что означает “ to open a can of worms”? \n <b>- Создать ряд проблем, которые требуют решения.</b>',
             '26. After my son broke his friend’s new toy, I had to <b>cough up</b> 50 dollars so that they '
             'could buy him a new one.',
             '27. <b>None of</b> the people I spoke to knew him.',
             "28. - I didn't even eat lunch today. \n- Really? <b>How come?</b>",
             '29. If you are flicking through your Facebook feed, you are <b>...'
             'quickly reading some of the posts?</b>?',
             '30. - I wish we <b>had thought</b> about it earlier. \n- Oh, well, we didn’t.']

A1 = "<b>A1. Уровень Beginner (Начальный) </b>\n\n" \
                "На уровне Beginner ты можешь использовать английский в повседневных ситуациях:" \
                "чтобы представиться и рассказать о себе или поддержать простой разговор с носителями языка, " \
                "когда те говорят медленно и разборчиво. \n\n" \
                "<b>Словарный запас:</b> до 1 500 слов, в основном существительные, " \
                "прилагательные, местоимения и самые употребляемые глаголы. Здесь тебе пригодится список 100 " \
                "самых используемых слов в английском.\n\n" \
                "<b>Listening:</b> Поймёшь на слух несложные фразы с базовой лексикой.\n\n" \
                "<b>Reading:</b> Прочитаешь короткие надписи на плакатах, дорожных знаках и в записках.\n\n" \
                "<b>Writing:</b> Напишешь простой емейл и сообщение, заполнишь форму с персональными данными: " \
                "имя, фамилия, национальность и т. д. \n\n" \
                "<b>Speaking:</b> Сможешь поболтать с носителями, если они говорят медленно и формулируют предложения,"\
                "используя простую лексику. " \
                "Обсудишь погоду, любимую еду и фильмы, расскажешь о семье и своих интересах, а также сможешь " \
                "попросить воды или спросить, где находится туалет. \n\n" \
                "<b>Grammar:</b> глаголы to be (быть) и to have (иметь), единственное и множественное число, " \
                "личные и притяжательные местоимения, предлоги времени и места, отрицание, вопросы " \
                "со вспомогательными глаголами to be и to do, Present Simple (Простое настоящее время), " \
                "Present continuous (Настоящее длительное время), модальный глагол can, Past Simple " \
                "(Простое прошедшее)," \
                "неправильные глаголы, Future Simple (Простое будущее время), " \
                "конструкция to be going to (собираться что-либо сделать), указательные местоимения, " \
                "исчисляемые и неисчисляемые существительные, количественные местоимения few/a few, little/ a little.\n\n" \
     "На базовом уровне твоя основная задача — сделать английский частью повседневной жизни. \n" \
     "Вот несколько советов для практики каждый день.\n" \
     "- Пиши списки покупок и планы на день на английском. " \
     "\n - Заведи дневник, где в нескольких предложениях описывай свой день." \
     "\n - Смотри простые сериалы, содержащие простую лексику и много повторений." \
     "\n - Читай адаптированные книги на уровней A1–A2." \
     "\n\n Изучение английского на начальном этапе — это метод проб и ошибок. " \
     "Не бойся ошибаться и будь терпелив, ведь изучение языка требует времени. "

A2 = "<b>A2. Уровень Elementary (Базовый)</b>\n\n" \
                "На уровне Elementary тебе комфортно в большинстве повседневных ситуаций за границей, " \
                "например, в магазине или транспорте, а также ты можешь поддержать разговор " \
                "с носителем языка на личные темы.\n\n" \
                "<b>Словарный запас:</b> 1500–2000 слов.\n\n" \
                "<b>Listening:</b> Понимаешь диалоги на личные темы: о семье и работе.\n\n" \
                "<b>Reading:</b> Читаешь короткие тексты и понимаешь простые письма. " \
                "Сможешь сориентироваться в расписаниях автобусов или поездов.\n\n" \
                "<b>Writing:</b>  Пишешь короткие сообщения, подписываешь открытки и можешь сделать конспект.  \n\n" \
                "<b>Speaking:</b> Общаешься на повседневные темы и ведёшь small talks, " \
                "используя простые грамматические конструкции. Можешь рассказать о своих друзьях " \
                "или сделать комплимент. \n\n" \
                "<b>Grammar:</b> сравнительная и превосходная степень прилагательных, " \
                "Past continuous (Прошедшее длительное время), фразовые глаголы, " \
                "модальные глаголы must/can/could/should/have to, Present perfect (Настоящее совершенное время), " \
                "наречия частотности, обстоятельства времени и места, " \
                "артикли с исчисляемыми и неисчисляемыми существительными, герундий, " \
                "фразы с want и would like, Wh-вопросы в прошедшем времени, " \
                "условные предложения нулевого и первого типа.\n\n"\
"На базовом уровне твоя основная задача — сделать английский частью повседневной жизни. \n" \
     "Вот несколько советов для практики каждый день.\n" \
     "- Пиши списки покупок и планы на день на английском. " \
     "\n - Заведи дневник, где в нескольких предложениях описывай свой день." \
     "\n - Смотри простые сериалы, содержащие простую лексику и много повторений." \
     "\n - Читай адаптированные книги на уровней A1–A2." \
     "\n\n Изучение английского на начальном этапе — это метод проб и ошибок. " \
     "Не бойся ошибаться и будь терпелив, ведь изучение языка требует времени. "


B1 = "<b>B1. Уровень Intermediate (Средний)</b>\n\n" \
                "На уровне Intermediate ты уже можешь использовать английский на рабочем месте в знакомых ситуациях, " \
                "чтобы прочитать отчёт, написать письмо или поучаствовать в обсуждении, выразив своё мнение. Т" \
                "ы уверенно чувствуешь себя в путешествии, ведёшь спонтанные беседы с носителями и " \
                "можешь уточнить непонятную информацию.\n\n" \
                "<b>Словарный запас:</b> 2000–3000 слов.\n\n" \
                "<b>Listening:</b> Понимаешь, о чём говорят люди и какую точку зрения они выражают. " \
                "Можешь слушать новости и аудиосериалы, связанные с повседневной жизнью, а также смотреть фильмы " \
                "в оригинале с английским субтитрами без специфической лексики и акцентов.\n\n" \
                "<b>Reading:</b> Читаешь тексты непрофильной тематики. Понимаешь их смысл, " \
                "а о значении незнакомых слов догадываешься из контекста. \n\n" \
                "<b>Writing:</b>  Напишешь небольшой связный текст и рабочее письмо, составишь резюме. \n\n" \
                "<b>Speaking:</b> Сможешь вести беседы без подготовки и справишься с большинством ситуаций, " \
                "путешествуя по англоязычной стране. Чётко и уверенно опишешь личный и профессиональный опыт, " \
                "а также расскажешь о мечтах, надеждах и планах. Можешь проходить собеседования на английском. \n\n" \
                "<b>Grammar:</b>  Future continuous (Будущее длительное время), " \
                "Past perfect (Прошедшее совершенное время), продолжаешь изучать фразовые глаголы, " \
                "Present perfect continuous (Настоящее совершенное длительное время), разница между " \
                "Present perfect и Past simple, Reported speech (Косвенная речь), пассивный залог, " \
                "условные предложения второго и третьего типа, предположения о будущем с will и going to, " \
                "модальные глаголы might/may и should have/might have." \
     "\n\nОкружи себя английским и продолжай практиковаться в языке, уделяя особое внимание темам, которые " \
     "тебя интересуют, или тем областям, в которых ты планируешь работать. " \
     "\nВот несколько советов, как прокачать английский на среднем уровне: " \
     "\n - Измени язык на телефоне, компьютере и в соцсетях на английский." \
     "\n - Читай как можно больше на английском, особенно о том, что тебе интересно. " \
     "\n - Переводи небольшие новости и статьи из Financial Times или The Guardian." \
     " Выписывай незнакомые слова, делай заметки и пересказывай содержание. " \
     "\n - Продолжай вести дневник о том, как провёл день." \
     "\n - Найди подкаст на интересную тебе тему и слушай его по дороге на работу или учёбу. " \
     "Старайся уловить общую суть и выпиши в заметки пять – шесть новых слов." \
     "\n - Найди собеседника. Это могут быть твои друзья, тоже жаждущие выучить английский, " \
     "или носители языка, например, классный мэтч в Tinder! "

B2 = "<b>B2. Уровень Upper-Intermediate (Выше среднего)</b>\n\n" \
                "На уровне Upper-Intermediateты уверенно используешь английский в своей области, " \
                "можешь провести презентацию и выразить своё мнение как во время разговора, так и письменно. " \
                "Ты можешь комфортно путешествовать и понимаешь большую часть информации в медиа." \
                "\n\n<b>Словарный запас:</b> 3000–4000 слов.\n\n" \
                "<b>Listening:</b>  Отлично понимаешь разговоры на личные и профессиональные темы. " \
                "Можешь смотреть фильмы без субтитров, если сюжет касается простых жизненных ситуаций." \
                "\n\n<b>Reading:</b> Ты можешь читать газеты и понимаешь повестку дня, " \
                "начинаешь разбираться в технических терминах.\n\n" \
                "<b>Writing:</b>  Пишешь тексты на широкий круг тем, можешь вести простую бизнес-переписку." \
                "\n\n<b>Speaking:</b> Общаешься спонтанно с носителями языка, можешь участвовать в дискуссиях " \
                "и рассказывать о событиях по всем типичным ситуациям. " \
                "\n\n<b>Grammar:</b> Future perfect (Будущее совершенное время), " \
                "Future perfect continuous (Будущее совершенное длительное время), " \
                "смешанный тип условных предложений, Relative clauses (Придаточные предложения), " \
                "Wish/If only, Would для выражение привычек в прошлом." \
"\n\nОкружи себя английским и продолжай практиковаться в языке, уделяя особое внимание темам, которые " \
     "тебя интересуют, или тем областям, в которых ты планируешь работать. " \
     "\nВот несколько советов, как прокачать английский на среднем уровне: " \
     "\n - Измени язык на телефоне, компьютере и в соцсетях на английский." \
     "\n - Читай как можно больше на английском, особенно о том, что тебе интересно. " \
     "\n - Переводи небольшие новости и статьи из Financial Times или The Guardian." \
     " Выписывай незнакомые слова, делай заметки и пересказывай содержание. " \
     "\n - Продолжай вести дневник о том, как провёл день." \
     "\n - Найди подкаст на интересную тебе тему и слушай его по дороге на работу или учёбу. " \
     "Старайся уловить общую суть и выпиши в заметки пять – шесть новых слов." \
     "\n - Найди собеседника. Это могут быть твои друзья, тоже жаждущие выучить английский, " \
     "или носители языка, например, классный мэтч в Tinder! "


C1 = "<b>C1. Уровень Advanced (Продвинутый)</b>\n\n" \
                "Английский на уровне Advanced можно использовать в любых ситуациях на работе и учёбе. " \
                "Ты понимаешь сложные темы, даже если у тебя мало базовых знаний, и можешь без проблем выразить " \
                "свои чувства и объяснять точку зрения. Ты даже понимаешь юмор и можешь пошутить в разговоре. " \
                "\n\n<b>Словарный запас:</b> 4000–5000 слов.\n\n" \
                "<b>Listening:</b> Понимаешь длинные речи и выступления на незнакомые темы. Можешь смотреть фильмы " \
                "без субтитров, слушать любые подкасты и смотреть стендапы." \
                "\n\n<b>Reading:</b> Читаешь большие и сложные тексты, любые книги и руководства без словаря. " \
                "Понимаешь разные стили и не спотыкаешься на технической терминологии. " \
                "\n\n<b>Writing:</b>  Пишешь хорошо структурированные тексты, в которых можешь " \
                "чётко изложить свою точку зрения, и сочинения с использованием сложных стилистических конструкций. " \
                "\n\n<b>Speaking:</b> Ведёшь спонтанные беседы и общаешься на английском без затруднений, " \
                "меняя стиль общения по ситуации. Можешь отстоять свою точку зрения в споре, " \
                "привести аргументы и сделать конкретные выводы. " \
                "\n\n<b>Grammar:</b> Inversion with negative adverbials (Отрицательная инверсия), " \
                "смешанный тип условных предложений, модальные глаголы в прошедшем времени, пассивный залог." \
     "\n\n Изучение английского — непрерывный процесс, и даже на продвинутом уровне всегда есть чему поучиться. " \
     "\n Ежедневная практика поможет поддерживать высокий уровень. " \
     "Погрузись в английский с головой. " \
     "\n На продвинутом уровне ты можешь читать книги в оригинале и смотреть фильмы без словаря и субтитров. " \
     "\n Пытайся разобраться в разных акцентах: американском, британском, австралийском и т. д. " \
     "\n Делай звонки на английском по работе или чтобы уточнить вопрос в службе поддержки. " \
     "\n Проводи время с англоговорящими друзьями и коллегами, общайся на англоязычных форумах и в соцсетях. " \
     "\n А ещё лучше — проведи время в англоязычной стране."
C2 = "<b>C2. Уровень Proficiency (Владение в совершенстве)</b>\n\n" \
                "Уровень Proficiency соотносится с уровнем владения языка как у носителя. Ты понимаешь всё, " \
                "что слышишь и читаешь, говоришь по-английски бегло, не задумываясь. " \
                "Можешь обобщать информацию из разных источников и аргументировать любую точку зрения. " \
                "\n\n<b>Словарный запас:</b> более 5 000 слов.\n\n" \
                "<b>Listening:</b> Понимаешь любую речь, даже если говорят очень быстро с акцентом. " \
                "\n\n<b>Reading:</b> Читаешь сложные тексты и узкопрофильные статьи. " \
                "\n\n<b>Writing:</b>  Свободно излагаешь свои мысли, можешь написать текст в любом стиле: " \
                "от рабочего отчёта до научной статьи." \
                "\n\n<b>Speaking:</b> Проводишь презентации и публичные выступления. Общаешься на любые темы, " \
                "можешь вести разговоры о политике, медицине и юриспруденции. Уверенно используешь " \
                "в разговоре идиомы и учтойчивые выражения." \
                "\n\n<b>Grammar:</b> Оттачиваешь уже выученные конструкции и учишь новые идиомы." \
     "\n\n Изучение английского — непрерывный процесс, и даже на продвинутом уровне всегда есть чему поучиться. " \
     "\n Ежедневная практика поможет поддерживать высокий уровень. " \
     "Погрузись в английский с головой. " \
     "\n На продвинутом уровне ты можешь читать книги в оригинале и смотреть фильмы без словаря и субтитров. " \
     "\n Пытайся разобраться в разных акцентах: американском, британском, австралийском и т. д. " \
     "\n Делай звонки на английском по работе или чтобы уточнить вопрос в службе поддержки. " \
     "\n Проводи время с англоговорящими друзьями и коллегами, общайся на англоязычных форумах и в соцсетях. " \
     "\n А ещё лучше — проведи время в англоязычной стране."

rus_help = "Если ты хочешь узнать общий  уровень своего английского, напиши /start\n\n" \
           "Если ты хочешь узнать подробнее о боте, напиши /info\n\n"\
           "Если ты хочешь проверить уровень своего технического английского, напиши /tests"

eng_help = "If you want to know the level of English according to the international standard write /start\n\n" \
           "If you want to know information about bot or tests write /info \n\n"\
           "If you want to test your technical English level, write /tests"

rus_start = "Этот тест состоит из 30 вопросов и направлен на проверку ваших знаний, " \
            "тест включает в себя вопросы на знание времён, грамматики, модальных и фразовых глаголов, " \
            "артиклей и общих правил\n\n Желаете начать?"

eng_start = "Hi, this test consists of 30 questions and is aimed at testing your knowledge, " \
            "the test includes questions on the knowledge of tenses, grammar, modal and phrasal verbs, " \
            "articles and general rules \n\n Would you like to start the test?"

rus_info = "Этот бот был создан с целью проверки общего уровня английского языка, а так же направлен на проверку " \
           "техничского английского\n\n" \
           "Тест был составлен, основываясь на стандарте Common European Framework of Reference for Languages (CEFR)\n"\
           "Согласно общеевропейской шкале уровней владения иностранным языком, выделяют 6 ступеней в освоении " \
           "английского языка. Это:\n\n" \
           "- Beginner (A1, начинающий)\n" \
           "- Elementary (A2, элементарный)\n" \
           "- Intermediate (B1, средний)\n" \
           "- Upper-Intermediate (B2, выше среднего)\n" \
           "- Advanced (C1, продвинутый)\n" \
           "- Proficient (C2, опытный)\n\n" \
           "Не забывайте о том, что данный тест не может дать точную оценку, он может лишь приблизительно " \
           "оценить ваш уровень.\n\n" \
           "источники:  https://ru.wikipedia.org/wiki/Общеевропейские_компетенции_владения_иностранным_языком\n\n" \
           "https://rm.coe.int/CoERMPublicCommonSearchServices/DisplayDCTMContent?documentId=090000168045bb65\n\n" \
           "https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989\n\n" \
           "http://www.englishprofile.org/images/pdf/GuideToCEFR.pdf"

eng_info = "This bot was created to test the general level of English, as well as to check the" \
"technical English\n\n" \
" The test was compiled based on the standard Common European Framework of Reference for Languages (CEFR)\n" \
"According to the pan-European scale of levels of foreign language proficiency, there are 6 stages " \
           "in the development of English. This is:\n\n" \
"- Beginner (A1, начинающий)\n" \
           "- Elementary (A2, элементарный)\n" \
           "- Intermediate (B1, средний)\n" \
           "- Upper-Intermediate (B2, выше среднего)\n" \
           "- Advanced (C1, продвинутый)\n" \
           "- Proficient (C2, опытный)\n\n" \
"Do not forget that this test can not give an accurate assessment, it can only approximate your level.\n\n" \
"sources:  https://ru.wikipedia.org/wiki/Общеевропейские_компетенции_владения_иностранным_языком\n\n" \
"https://rm.coe.int/CoERMPublicCommonSearchServices/DisplayDCTMContent?documentId=090000168045bb65\n\n" \
"https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2018/1680787989\n\n" \
"http://www.englishprofile.org/images/pdf/GuideToCEFR.pdf"

A1_E = "<b>A1. Beginner level </b>\n\n" \
    "At Beginner level, you can use English in everyday situations:" \
    "to introduce yourself and talk about yourself, or to have a simple conversation with native speakers, " \
    "when they speak slowly and clearly. \n\n" \
    "<b>Vocabulary:</b> up to 1,500 words, mostly nouns, " \
    "adjectives, pronouns, and the most commonly used verbs. Here you will find a list of the 100 " \
    "most used words in English.\n\n" \
    "<b>Listening:</b> You will understand simple phrases with basic vocabulary by ear.\n\n" \
    "<b>Reading:</b> You will read short inscriptions on posters, road signs and in notes.\n\n" \
    "<b>Writing:</b> Write a simple email and message, fill out a form with personal data: " \
    "first name, last name, nationality, etc. \n\n" \
    " <b>Speaking:</b> You can chat with native speakers if they speak slowly and formulate sentences,"\
    " using simple vocabulary. " \
    "You will discuss the weather, your favorite food and movies, tell about your family and your interests, " \
           "and you can also" \
    "ask for water or ask where the toilet is located. \n\n" \
    "<b>Grammar:</b> verbs to be and to have, singular and plural, " \
    "personal and possessive pronouns, prepositions of time and place, negation, questions" \
    "with auxiliary verbs to be and to do, Present Simple (Simple present tense), " \
    "Present continuous (Present long tense), modal verb can, Past Simple" \
    "(Simple past), " \
    " irregular verbs, Future Simple (Simple future tense), " \
    "construction to be going to (going to do something), demonstrative pronouns, " \
    "calculable and uncountable nouns, quantitative pronouns few/a few, little/ a little.\n\n" \
       "At a basic level, your main task is to make English a part of everyday life. \n" \
    "Here are some tips for practicing every day.\n" \
    " - Write shopping lists and plans for the day in English. "\
    "\n - Start a diary, where you can describe your day in a few sentences. " \
    " \n - Watch simple TV shows that contain simple vocabulary and a lot of repetition." \
       "\n - Read adapted books at levels A1–A2." \
    "\n \n Learning English at the initial stage is a trial and error method. "\
    "Don't be afraid to make mistakes and be patient, because learning a language takes time."

A2_E = "<b>A2. Elementary Level (Basic)</b>\n\n" \
        "At the Elementary level, you are comfortable in most everyday situations abroad, " \
        "for example, in a store or transport, and you can also have a conversation" \
        " with a native speaker on personal topics.\n\n" \
        "<b>Vocabulary:</b> 1500-2000 words.\n\n" \
        "<b>Listening:</b> You understand dialogues on personal topics: about family and work.\n\n" \
        "<b>Reading:</b> You read short texts and understand simple letters. " \
        "You will be able to navigate in the schedules of buses or trains.\n\n" \
        "<b>Writing: </b> You write short messages, sign postcards, and you can take notes. \n\n" \
        "<b>Speaking:</b> You communicate on everyday topics and conduct small talks, " \
        "using simple grammatical constructions. You can tell about your friends " \
        " or make a compliment. \n\n" \
        "<b>Grammar:</b> comparative and superlative adjectives, " \
        "Past continuous (Past long tense), phrasal verbs, " \
        "modal verbs must/can/could/should/have to, Present perfect (Present perfect tense), " \
        "adverbs of frequency, circumstances of time and place, " \
        "articles with calculable and uncountable nouns, gerund, " \
        "phrases with want and would like, Wh - questions in the past tense, " \
        "conditional sentences of type zero and type one.\n\n" \
"At a basic level, your main task is to make English a part of everyday life. \n" \
    "Here are some tips for practicing every day.\n" \
    " - Write shopping lists and plans for the day in English. "\
    "\n - Start a diary, where you can describe your day in a few sentences. " \
    " \n - Watch simple TV shows that contain simple vocabulary and a lot of repetition." \
    "\n - Read adapted books at levels A1–A2." \
    "\n\n Learning English at the initial stage is a trial and error method. "\
    "Don't be afraid to make mistakes and be patient, because learning a language takes time."

B1_E = "<b>B1. Intermediate level (Intermediate)</b>\n\n" \
        "At the Intermediate level, you can already use English in the workplace in familiar situations, " \
        "to read the report, write a letter, or participate in the discussion by expressing your opinion. T" \
        "s feel confident in the journey, conduct spontaneous conversations with native speakers and" \
        " can clarify incomprehensible information.\n\n" \
        "<b>Vocabulary:</b> 2000-3000 words.\n\n" \
        "<b>Listening:</b> You understand what people are talking about and what point of view they are expressing. "\
        "You can listen to news and audio series related to everyday life, as well as watch movies" \
        " in the original with English subtitles without specific vocabulary and accents.\n\n" \
        "<b>Reading:</b> You read non-core texts. Do you understand their meaning, " \
        "and you can guess the meaning of unfamiliar words from the context. \n\n" \
        "<b>Writing: </b> Write a small coherent text and a working letter, make a resume. \n\n" \
        "<b>Speaking:</b> You will be able to conduct conversations without preparation and will cope with most situations, " \
        "traveling in an English-speaking country. Clearly and confidently describe your personal and professional experience,"\
        "you will also tell us about your dreams, hopes and plans. You can pass the interviews in English. \n\n" \
        "<b>Grammar:</b> Future continuous (Future long time), " \
        "Past perfect (Past perfect tense), continue to learn phrasal verbs, " \
        "Present perfect continuous (Present perfect long time), the difference between" \
        " Present perfect and Past simple, Reported speech( Indirect speech), passive voice, " \
        "conditional sentences of the second and third types, assumptions about the future with will and going to, " \
        "the modal verbs might/may and should have/might have." \
"\n\nCover yourself in English and continue to practice the language, paying special attention to the topics that " \
" interest you, or the areas in which you plan to work."\
"\nHere are some tips on how to improve your English at an intermediate level: " \
"\n\n - Change the language on your phone, computer and social networks to English. " \
"\n - Read as much as possible in English, especially about what you are interested in. "\
"\n - Translate small news and articles from the Financial Times or The Guardian. " \
       "Write out unfamiliar words, make notes, and retell the content. "\
"\n - Keep a diary about how you spent the day." \
"\n - Find a podcast on a topic that interests you and listen to it on the way to work or school. Try to grasp the general essence and write down five or six new words in your notes." \
"\n - Find the interlocutor. It can be your friends who are also eager to learn English, or native speakers, for example, a cool match on Tinder! "

B2_E = "<b>B2. Upper-Intermediate level (Above average)</b>\n\n" \
        "At the Upper-Intermediate level, you can confidently use English in your field, " \
        "you can make a presentation and express your opinion both during the conversation and in writing. "\
        "You can travel comfortably and understand most of the information in the media." \
        "\n\n<b>Vocabulary:</b> 3000-4000 words.\n\n" \
        "<b>Listening:</b> Perfectly understand conversations on personal and professional topics. " \
        "You can watch movies without subtitles if the plot concerns simple life situations." \
        "\n\n<b>Reading:</b> You can read the papers and understand the agenda, " \
        "you start to understand the technical terms.\n\n" \
        "<b>Writing: </b> You write texts on a wide range of topics, you can conduct simple business correspondence." \
        "\n\n<b>Speaking:</b> You communicate spontaneously with native speakers, you can participate in " \
        " discussions and talk about events in all typical situations. " \
        "\n\n<b>Grammar:</b> Future perfect), " \
        "Future perfect continuous (Future perfect long time), " \
        "mixed type of conditional sentences, Relative clauses (Subordinate clauses), " \
        "Wish/If only, Would for expressing habits in the past." \
"\n\nCover yourself in English and continue to practice the language, paying special attention to the topics that " \
" interest you, or the areas in which you plan to work."\
"\nHere are some tips on how to improve your English at an intermediate level: " \
"\n\n-Change the language on your phone, computer and social networks to English. " \
"\n - Read as much as possible in English, especially about what you are interested in. "\
"\n - Translate small news and articles from the Financial Times or The Guardian. " \
       " Write out unfamiliar words, make notes, and retell the content. "\
"\n - Keep a diary about how you spent the day." \
"\n - Find a podcast on a topic that interests you and listen to it on the way to work or school. Try to grasp the general essence and write down five or six new words in your notes." \
"\n - Find the interlocutor. It can be your friends who are also eager to learn English, or native speakers, for example, a cool match on Tinder! "


C1_E = "<b>C1. Advanced Level (Advanced)</b>\n\n" \
        "English at the Advanced level can be used in any situation at work and at school. "\
        "You understand complex topics, even if you have little basic knowledge, and you can easily express" \
            "your feelings and explain your point of view. You even understand humor and can make jokes in conversation. " \
        "\n\n<b>Vocabulary:</b> 4000-5000 words.\n\n" \
        "<b>Listening:</b> You understand long speeches and speeches on unfamiliar topics. You can watch movies " \
        "without subtitles, listen to any podcasts and watch stand-ups." \
        "\n\n<b>Reading:</b> You read large and complex texts, any books and manuals without a dictionary. "\
        "You understand different styles and do not stumble on technical terminology. "\
        "\n\n<b>Writing: </b> You write well-structured texts in which you can " \
        " clearly state your point of view, and essays using complex stylistic constructions. " \
        "\n\n<b>Speaking:</b> You have spontaneous conversations and communicate in English without difficulty, " \
        "changing the style of communication according to the situation. You can defend your point of view in an argument, " \
        "to present arguments and draw concrete conclusions. " \
        "\n\n<b>Grammar:</b> Inversion with negative adverbials (Negative inversion), " \
        "mixed type of conditional sentences, modal verbs in the past tense, passive voice." \
"\n\nLearning English is a continuous process, and even at an advanced level there is always something to learn. "\
"\nDaily practice will help to maintain a high level. "\
"Immerse yourself in English with your head. "\
"\n At an advanced level, you can read books in the original and watch movies without a dictionary or subtitles. "\
"\n Try to understand different accents: American, British, Australian, etc. " \
"\n Make calls in English for work or to clarify a question in the support service. " \
"\n Spend time with English-speaking friends and colleagues, communicate on English-language forums and social networks. "\
"\nA even better-spend time in an English-speaking country."

C2_E = "<b>C2. Proficiency level (Perfect proficiency)</b>\n\n" \
        "Proficiency level corresponds to the level of language proficiency as a native speaker. You understand everything, " \
        "what you hear and read, speak English fluently, without thinking. "\
        "You can summarize information from different sources and argue any point of view. " \
        "\n\n<b>Vocabulary:</b> more than 5,000 words.\n\n" \
        "<b>Listening:</b> You can understand any speech, even if they speak very quickly with an accent. " \
        "\n\n<b>Reading:</b> You read complex texts and narrow-profile articles. " \
        "\n\n<b>Writing:</b> You are free to express your thoughts, you can write a text in any style: " \
        "from a working report to a scientific article." \
        "\n\n<b>Speaking:</b> You make presentations and public appearances. You communicate on any topic, " \
        "you can talk about politics, medicine, and law. Confidently use " \
        " in conversation idioms and considerate expressions." \
        "\n\n<b>Grammar:</b> You hone already learned constructions and learn new idioms." \
"\n\nLearning English is a continuous process, and even at an advanced level there is always something to learn. "\
"\nDaily practice will help to maintain a high level. "\
"Immerse yourself in English with your head. "\
"\n At an advanced level, you can read books in the original and watch movies without a dictionary or subtitles. "\
"\n Try to understand different accents: American, British, Australian, etc. " \
"\n Make calls in English for work or to clarify a question in the support service. " \
"\n Spend time with English-speaking friends and colleagues, communicate on English-language forums and social networks. "\
"\nA even better-spend time in an English-speaking country."

A1_a = "lox"