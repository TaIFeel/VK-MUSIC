from vkaudiotoken import get_vk_official_token
import requests

login = '' # your vk login, e-mail or phone number
password = '' # your vk password

sess = requests.session()


try:
    info = get_vk_official_token(login, password)

except Exception as exc:
    if exc.extra["error"] == "need_validation":
        code = input("SMS CODE: >>> ")

    info = get_vk_official_token(login, password, code)

sess.headers.update({'User-Agent': info["user_agent"]})

track_list = sess.get(
    "https://api.vk.com/method/audio.get",
    params=[('access_token', info['token']),
            ("count", 100),
            ("offset", 0),
            ('v', '5.89')]
).json()

tracks = track_list['response']['items']
for track in tracks:
    print(f'{track["artist"]} - {track["title"]}: {track["url"]}')
