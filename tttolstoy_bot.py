import telebot
from telebot import types
import random

bot = telebot.TeleBot("1968518707:AAGWQ3fX-hoqyUBaorbcsuqptQN895-gCtQ", parse_mode=None)

@bot.message_handler(commands=['start'])
def welcome(message):
	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Welcome-центр Университета👋🏻")
	item2 = types.KeyboardButton("ЭБС📖")
	item3 = types.KeyboardButton("Точка кипения🔥")
	item4= types.KeyboardButton("Контактная информация📞")
	item5 = types.KeyboardButton("Наставление от Льва Николаевича🧐")

	markup.add(item1)
	markup.add(item3)
	markup.add(item2, item4)
	markup.add(item5)

	bot.send_message(message.chat.id, "День добрый, {0.first_name}! Рад тебя здесь видеть! Расскажу тебе все, что ты хотел узнать о ТГПУ им. Л. Н. Толстого. Спрашивай!😌".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def menu(message):
	if message.chat.type == 'private':
			
			#Точка кипения
		if message.text == 'Точка кипения🔥':
			bot.send_message(message.chat.id, 'Психология, инженерия, менеджмент, цифровизация, космонавтика, история, иностранные языки и даже классическая литература - в этих залах витает много знаний. Присмотри, что по нраву, и забирай без остатка!\n \n«Точка кипения» ТГПУ им. Л.Н. Толстого — это зал для мероприятий с современным оборудованием, где часто выступают приглашенные спикеры на самые разные темы. Посещай бесплатные лекции, мастер-классы и семинары и находи друзей по интересам! 🤝\n \nУзнать подробнее о "ТК" и об актуальных ивентах можно на сайте http://utk-tula.ru/ или в социальных сетях:  https://vk.com/utk.tspu (ВК), https://www.instagram.com/utk.tspu/ (Instagram).\n \nВ свободное от лекций время "Точка кипения" становится коворкинг-центром с письменными столами и розетками для работы, обширной библиотекой для исследования и мягкими креслами-мешками для отдыха в перерыве! 😴\n \n📍Зал "Точки кипения" находится на 2 этаже 4 корпуса и работает до 17:00.')


		elif message.text == 'Наставление от Льва Николаевича🧐':
			advice = ['Лучше знать немного истинно хорошего и нужного, чем очень много посредственного и ненужного.', 'Знание только тогда знание, когда оно приобретено уси­лиями своей мысли, а не памятью.', 'Каждый человек – алмаз, который может очистить и не очистить себя, в той мере, в которой он очищен, через него светит вечный свет, стало быть, дело человека не стараться светить, но стараться очищать себя.', 'Если нет сил гореть и разливать свет, то хоть не засти его.', 'Вся моя мысль в том, что ежели люди порочные связаны между собой и составляют силу, то людям честным надо сделать только то же самое.', 'Поэзия есть огонь, загорающийся в душе человека. Огонь этот жжет, греет и освещает. Настоящий поэт сам невольно и с страданием горит и жжет других. И в этом все дело.', 'Искусство – одно из средств различения доброго от злого, одно из средств узнавания хорошего.', 'Любовь уничтожает смерть и превращает ее в пустой призрак; она же обращает жизнь из бессмыслицы в нечто осмысленное и из несчастия делает счастие.', 'Говори только о том, что для тебя ясно, иначе молчи.',  'Если один раз пожалеешь, что не сказал, то сто раз пожалеешь о том, что не смолчал.', 'Часто молчание лучший из ответов.', 'Больше всех говорит тот, кому нечего сказать.', 'У самого злого человека расцветает лицо, когда ему говорят, что его любят. Стало быть, в этом счастье...', 'Пора перестать ждать неожиданных подарков от жизни, а самому делать жизнь.', 'Счастье не в том, чтобы делать всегда, что хочешь, а в том, чтобы всегда хотеть того, что делаешь.', 'Осуждение другого всегда неверно, потому что никто никогда не может знать того, что происходило и происходит в душе того, кого осуждаешь.', 'Все великие перемены в жизни одного человека, а также и всего человечества, начинаются и совершаются в мысли. Для того, чтобы могла произойти перемена чувств и поступков, должна произойти прежде всего перемена мысли.', 'Мысль — начало всего. И мыслями можно управлять. И поэтому, главное дело совершенствования — работать над мыслями.', 'Единственное условие, от которого зависит успех, есть терпение.', 'Надо верить в возможность счастья, чтобы быть счастливым.',  'Истинная сила человека не в порывах, а в нерушимом спокойствии.', 'Придумывай себе как можно больше занятий.', 'Глаза — зеркало души.', 'Живя с людьми, не забывай того, что ты узнал в уединении. И в уединении обдумывай то, что ты узнал из общения с людьми.', 'Я должен был пить много чая, ибо без него не мог работать. Чай высвобождает те возможности, которые дремлют в глубине моей души.', 'Чем больше человек проявляет любви, тем больше люди любят его. А чем больше его любят, тем легче ему любить других.', 'Чтобы быть счастливым, нужно постоянно стремиться к этому счастью и понимать его. Оно зависит не от обстоятельств, а от себя.', 'Мысль должна рождаться в обществе, обработка и выражение ее происходит в одиночестве.', 'В судьбе нет случайностей; человек скорее создает, нежели встречает свою судьбу.', 'Почти всегда, поискав в себе, мы найдем тот же грех, который мы осуждаем в другом. Если же мы не знаем за собой именно того самого греха, то стоит только поискать, и мы найдем еще худший.', 'Делай, что должно, а там будь что будет.']
			bot.send_message(message.chat.id, str(random.choice(advice)))

			#ЭБС
		elif message.text == 'ЭБС📖':
			bot.send_message(message.chat.id, ' ЭБС - "Электронно-библиотечная система"! Река полезной информации в огромном океане интернета. В них ты сможешь найти нужные учебники, пособия и даже томик "Войны и мира"! 😎\n \nНаш университет сотрудничает с тремя онлайн-библиотеками: \n \n"Университетская библиотека online"  https://biblioclub.ru \n \n"Юрайт"   https://urait.ru/ \n \n"IPR Books"   http://www.iprbookshop.ru/ \n \nЧтобы получить доступ ко всем функциям библиотеки - к скачиванию, добавлению закладок и т.д.) необходимо Зарегистрироваться на сайте и затем Войти в систему с помощью своего Логина и Пароля для сайта ТГПУ им. Л. Н. Толстого, который должен прийти тебе на почту.\n \nБолее подробная информация и инструкция по ссылке 👉🏻 https://tsput.ru/about_us/struktura-i-organy-upravleniya-universiteta/the_structure_of_the_university/other_units/libraries/electronic-resources/')

			#Welcome центр
		elif message.text == 'Welcome-центр Университета👋🏻':

			markup = types.InlineKeyboardMarkup(row_width=3)
			item1 = types.InlineKeyboardButton("Творческие коллективы и мастерские🎨", callback_data='art')
			item2 = types.InlineKeyboardButton("Карта университета🗺", callback_data='map')
			item3 = types.InlineKeyboardButton("Шаблоны для заявлений и стипендии📋", callback_data='form')

			markup.add(item1)
			markup.add(item2)
			markup.add(item3)

			bot.send_message(message.chat.id, 'Добро пожаловать на гостевую страницу университета твоей мечты!\n \nЗдесь ты в удобном формате сможешь найти всю основную информацию о работе ТГПУ им. Л. Н. Толстого💫\n \nПроект Welcome-центра реализован студенческим медиа-центром "Tolstoy Talk!". Подписывайся на наши соц. сети: \n \nВК - https://vk.com/tolstoytalk \nИнстаграм - https://www.instagram.com/tolstoytalk/?hl=ru', reply_markup=markup)
			
		elif message.text == 'Контактная информация📞':
			bot.send_message(message.chat.id, ' Устал бегать по всем этажам университета в поисках кафедры? Не волнуйся, я тебе помогу. 😌 \n \n🎓 Факультеты, их деканаты, кафедры, графики работы, телефоны и почты — все по ссылке : https://docs.google.com/spreadsheets/d/1f2Klf1HxHJ0unaIUNyBnhM-i6FQUMLnB/edit?usp=sharing&ouid=107398534421818322172&rtpof=true&sd=true \n \n📲ТГПУ им. Л.Н. Толстого в социальных сетях: \n \nВК: https://vk.com/tsput \nИнстаграм: https://www.instagram.com/tsput/?hl=ru')
		else:
			bot.send_message(message.chat.id, 'Хоть я и великий писатель, но таких слов не знаю')   

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 'art':
				bot.send_message(call.message.chat.id, 'Творческие коллективы и мастерские🎨')
				bot.send_message(call.message.chat.id, '🔥 Горишь душой к творчеству? Тогда позволь рассказать тебе о наших творческих секциях и мастерских, в которых ты не только удовлетворишь свою жажду искусства, но и найдешь новых друзей, мудрых наставников и может даже соавторов для развития твоих мыслей!\n \nВ прикрепленной записи ты найдешь всю нужную тебе информацию 👉🏻 https://vk.com/tolstoytalk?w=wall-78861882_3166')
			elif call.data == 'map':
				bot.send_message(call.message.chat.id, 'Или по-другому: "Да где этот ваш 3 корпус?!"😤 \n \nНе волнуйся, Я расскажу тебе про главные корпуса Университета! Ты узнаешь о том, что находится внутри каждого из них (кафедры, деканаты, библиотеки и т.п.), где расположены все общежития, бассейн, столовая и даже корты и поля для спортивного веселья!  \n \n Вперед к путешествиям по кампусу! 👉🏻 https://docs.google.com/document/d/17eKtx_KHwfNzOJo2iFielgSFy2kT13UJ/edit \n \n 💡 Чтобы быстро найти то, что нужно, воспользуйся "Поиском по тексту" - Ctrl+F!')
			elif call.data == 'form':
				bot.send_message(call.message.chat.id, '"Проболел" две недели? Потерял студак?😞\n \nЯ расскажу тебе, как оплатить учебу онлайн, получить социальную стипендию и заполнить заявление, если учиться стало в тягость и нужен академ.\n \nСтипендии и иные виды материальной поддержки : https://tsput.ru/sveden/grants/ \n \nПлатные образовательные услуги : https://tsput.ru/sveden/paid_edu/ \n \nОбразцы заявлений : https://tsput.ru/faculties_and_departments/departments/department_of_foreign_languages/blank/ ')

			# remove inline buttons
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Welcome-центр Университета👋🏻",
				reply_markup=None)


		

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)