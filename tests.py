# -*- coding: utf-8 -*-
import numpy as np
import telebot
import telegram
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types

rus_test = "Здесь вы можете проверить свой технический английский\n\n" \
           "Tехнический английский язык – это достаточно широкая и объемная категория языка, " \
           "которая охватывает многие виды деятельности, техническое обслуживание и множество профессий.\n\n" \
           "Важно понять, что технический уровень английского это не обычное владение языком. " \
           "\n Это – совершенно особая терминология, которая нужна вам для вашего вида деятельности.\n\n" \
           "Технический уровень английского языка применяется во многих сферах деятельности, а именно:\n" \
           "- IT сфера или программирование: " \
           "    \n - web-разработка всех специализаций, сборка и ремонт компьютеров" \
           "\n -инженерная сфера: средства коммуникации и сопутствующие механизмы" \
           "\n -автомобильная промышленность: горюче-смазочные материалы, запчасти, автомобили" \
           "\n -проектные организации: создание проектных организаций" \
           "\n -армия и военно-морской флот: оружие, авиатехника и т.д." \
           "\n -оборудование: торговое, строительное и медицинское" \
           "\n -видео- и телетехника, мобильные телефоны и фотоаппараты" \
           "\n -торговля и маркетинг\n\n" \
           "Напоминаем: данный тест не может дать объективную оценку, он может только приблизительно " \
           "оценить ваши знания" \
           "\nНо он способен помочь вам понять, на что стоит обратить внимание и какие у вас есть пробелы\n\n" \
           "Источники: http://www.quizful.net/test/english-for-it\n\n" \
           "https://englex.ru/english-for-it-specialists/"



eng_test = "Here you can check your technical English\n\n" \
    " Technical English is a fairly broad and voluminous language category, " \
    "which covers many activities, maintenance, and many professions.\n\n" \
    "It is important to understand that the technical level of English is not an ordinary language proficiency. "\
    "\n This is a very special terminology that you need for your type of activity.\n\n" \
    "The technical level of English is used in many areas of activity, namely:\n" \
    "- IT sphere or programming: " \
    "\n - web-development of all specializations, Assembly and repair of computers" \
    "\n -engineering field: communication and related mechanisms" \
    "\n automotive industry: fuel and lubricants, spare parts, cars" \
    "\n -project organization: project organizations" \
    "\n -the army and Navy weapons, aircraft etc." \
    "\n -hardware: trade, construction and medical" \
    "\n -video and TV technician mobile phones and cameras" \
    "\n -trade and marketing\n\n" \
    "Reminder: this test can give an objective assessment, it can only approximately" \
    "assess your knowledge" \
    "\nbut he is able to help you understand what you should pay attention to you spaces\n\n" \
           "Sources: http://www.quizful.net/test/english-for-it\n\n" \
           "https://englex.ru/english-for-it-specialists/"

cho_rus = "- Выберите сферу, чтобы проверить свои знания\n\n" \
          "- Choose a field to test your knowledge"


test = [['1. You pass through a(n) ___ to enter another network.', '1. network', '2. gateway', '3. place', 'firewall', 1],
       ['2. You usually need to open an ___ before you can shop online.',
        '1. item', '2. exchange', '3. account', '4. order', 2],
       ['3. Select the best definition of the word “hardware”',
        '1. such term does not exists', '2. а program built into the circuitry of а RОМ',
        '3. all people engaged in production of the computer and maintenance of its work',
        '4. the physical equipment and components in а computer system', 3],
        ['4. Select the best definition of the word "meta tag"',
         '1. an amount of something that you can count',
         '2. the HTML or XHTML used to provide metadata about a website',
         '3. a short description that gives the main details', '4. used to describe movement on the Internet', 1],
        ['5. How ___ do they defrag their computers?’ ‘Every Monday morning.',
         '1. many', '2. often', '3. long', '4. much', 1],
        ['6. Do you want to know what the database is used___?\nfor/to',
         '1. both correct', '2. both incorrect', '3. to', '4. for', 3],
        ['7. I’m a data ___ – I process data.',
         '1. analyst', '2. architect',
         '3. supporter', '4. developer', 0],
        ['8. Which type of software does every computer need?',
         '1. Desktop publishing software', '2. Web browser',
         '3. Operating system', '4. Word processor', 2],
        ["9. Select all the right choices about the driver\n1. The driver controls the computer device like printer, scanner, or hard disk.\n2. All computer devices need drivers.\n3. With the driver we can drive a car in games.\n4. This is a new kind of mouse.",
         '1. 2, 4', '2. 1, 2, 3', '3. 1, 2', '4. 1', 2],
        ['10. Your software isn’t compatible ___ this computer.', '1. for', '2. with','3. to','4. at', 1],
        ['11. I need to ___ the new software on your computer. It’ll take half an hour.',
         '1. insert', '2. install', '3. transfer', '4. connect', 1],
        ["12. Please choose the correct spelling for:\n"
         "The programmer ___ works with me is intelligent",
         '1. who', '2. that', '3. Both are incorrect','4. Both are correct',3],
        ['13. Select the best definition of the word "end user"\n <b>- a person who</b>',
         '1. writes computer programs', '2. uses a product or service on a computer',
         '3. modifies computer programs', '4. writes or modifies computer programs or applications', 1],
        ['14. The computer system ___ this morning and nobody knows why.','1. is crashing', '2. crashes',"3. crashed", "4. will crash", 2],
        ['15. Select a devices used to output information',
         '1. monitor, motherboard, mouse', '2. scanner, printer',
         '3. monitor, scanner', '4. printer, monitor', 3]]

qu = ['1. You pass through a(n) <b>gateway</b> to enter another network.',
      '2. You usually need to open an <b>account</b> before you can shop online.',
      '3. Select the best definition of the word “hardware”',
      '4. Select the best definition of the word "meta tag"',
      '5. How <b>often</b> do they defrag their computers?’ ‘Every Monday morning.',
      '6. Do you want to know what the database is used <b>for</b>?',
      '7. I’m a data <b>analyst</b> – I process data.',
      '8. - Which type of software does every computer need?\n <b>- Operating system</b>',
      '9. Select all the right choices about the driver\n<b>1. The driver controls the computer device like printer, scanner, or hard disk.</b>\n<b>2. All computer devices need drivers.</b>\n3. With the driver we can drive a car in games.\n4. This is a new kind of mouse.',
      '10. Your software isn’t compatible <b>with</b> this computer.',
      '11. I need to <b>install</b> the new software on your computer. It’ll take half an hour.',
      '12. Please choose the correct spelling for:\n The programmer <b>who/that</b> works with me is intelligent',
      '13. Select the best definition of the word “end user”\n '
      '<b>- a person who...uses a product or service on a computer</b>',
      '14. The computer system <b>crashed</b> this morning and nobody knows why.',
      '15. Select a devices used to output information\n<b>- printer, monitor</b>']

rez_33_rus = "Вы владеете английским на уровне пользователя, знаете базовые технические слова, однако есть проблемы с более глубоким пониманием компьютера\n\n" \
             "Советы:\n" \
             "Рекомендуем вам обратить внимание на учебники для начинающих:\n" \
             "https://fktpm.ru/file/63-english-for-information-technology-pearson-longman.pdf\n\n" \
             "http://storage1.expresspublishingapps.co.uk/careerpaths/InformationTechnology.pdf\n\n" \
             "Так же при необходимости вы можете пользоваться айти-словарём:\n" \
             "https://www.dataprise.com/it-glossary\n\n" \
             "Рекомендуем смотреть обучающие видео, обращаться за помощью на специалные тематические форумы и больше практиковаться. Удачи!"

rez_33_eng = "You speak English at the user level, you know the basic technical words, but there are problems with a deeper understanding of the computer\n\n" \
             "Tips:\n" \
             "We recommend that you pay attention to the tutorials for beginners:\n" \
             "https://fktpm.ru/file/63-english-for-information-technology-pearson-longman.pdf\n\n" \
             "http://storage1.expresspublishingapps.co.uk/careerpaths/InformationTechnology.pdf\n\n" \
             "Also, if necessary, you can use the IT dictionary:\n" \
             "https://www.dataprise.com/it-glossary\n\n" \
             "We recommend you to watch training videos, ask for help on special thematic forums and practice more. Good luck!"

rez_66_rus = "Вы достаточно хорошо владеете техническим английским, знаете базовые технические слова и можете поговорить про устройство компьютера, однако есть к чему стремиться\n\n" \
             "Советы:\n" \
             "Рекомендуем вам обратить внимание на учебники для среднего уровня:\n" \
             "https://drive.google.com/file/d/0Bz-oncXpTbqXODk5M2U2OWItZWYyNS00ZjY0LWFhZjAtNTE4MWJmZWZiNTFi/view?amp;hl=en\n\n" \
             "http://englishonlineclub.com/pdf/Oxford%20English%20for%20Industries%20-%20English%20for%20Telecoms%20and%20Information%20Technology%20[EnglishOnlineClub.com].pdf\n\n" \
             "Так же при необходимости вы можете пользоваться айти-словарём:\n" \
             "https://www.dataprise.com/it-glossary\n\n" \
             "Обратите внимание на более глубокое устройство компьютера, больше практикуйтесь и не бойтесь ошибаться. Удачи!"

rez_66_eng = "You are quite good at technical English, you know the basic technical words and can talk about the computer device, but there is something to strive for\n\n" \
" Tips:\n" \
"We recommend that you pay attention to the textbooks for the intermediate level:\n" \
"https://drive.google.com/file/d/0Bz-oncXpTbqXODk5M2U2OWItZWYyNS00ZjY0LWFhZjAtNTE4MWJmZWZiNTFi/view?amp;hl=en\n\n" \
"http://englishonlineclub.com/pdf/Oxford%20English%20for%20Industries%20-%20English%20for%20Telecoms%20and%20Information%20Technology%20[EnglishOnlineClub.com].pdf\n\n" \
"Also, if necessary, you can use the IT dictionary:\n" \
"https://www.dataprise.com/it-glossary\n\n" \
" Pay attention to the deeper structure of the computer, practice more, and don't be afraid to make mistakes. Good luck!"

rez_100_rus = "Вы хороший специалист. При необходимости вы всегда знаете где искать решение проблемы, советуем больше практиковаться, чтобы становиться ещё лучше"

rez_100_eng = "You are a good specialist. If necessary, you always know where to look for a solution to the problem, we advise you to practice more to become even better"
it_test = []