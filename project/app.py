from flask import Flask, render_template, request
import os
import requests
from pprint import pprint as pp
import random

app = Flask(__name__)
token=os.getenv('TELEGRAM_TOKEN')
naver_id=os.getenv('NAVER_ID')
naver_secret=os.getenv('NAVER_SECRET')
base_url = "https://api.hphk.io/telegram"
my_url="https://webhook-graduatediary.c9users.io"


# 웹훅 설정(set webhook) == 텔레그램에게 알리미를 해달라고 하는 것.

# 텔레그램이 우리에게 알림을 줄 때 사용할 route
# 만약 특정 유저가 우리 봇으로 메세지를 보내게 되면,
# 텔레그램 우리에게 알림을 보내온다.(json)

@app.route('/{}'.format(token), methods=['POST']) # POST로 해야 접근이 어려워.
def telegram():
    doc = request.get_json()# json.loads(request)
    chat_id=doc['message']['chat']['id']
    name=doc['message'].get('text')  # doc.get('message').get('text') -> 없으면 넘어감.
    sets={'강창모': 'https://docs.google.com/presentation/d/e/2PACX-1vRwwbV8R5ZUefmUkTzi-E3wKseJZRMDiPAKLeuUKK-Z1pudc9BgNDO5B4YlB-4Gk89GtmTD3E6cCcOI/pub?start=true&loop=false&delayms=15000',
'고성현': 'https://docs.google.com/presentation/d/e/2PACX-1vSs99vp-24a1X4O2NnlzXjJLGlN6G1oBAkB9E8i0guva_enx_gyjqbsq6_8LaUgV1aEwNpRTr78Z0nf/pub?start=true&loop=false&delayms=15000',
'김나영': 'https://docs.google.com/presentation/d/e/2PACX-1vRhy8aUXT-u_MpIdqzug0gU_Ts193ZeOvemZ7WRf8H0vXO1x7dNDvy11nEOa7Mr8-peLGTXYr4Jpo43/pub?start=false&loop=false&delayms=15000',
'김도우': 'https://docs.google.com/presentation/d/e/2PACX-1vT8hcMcU0xL9ItGjCjiPrs_gE7_0GePnSE65Sn4UpZeknjoHJTaIZv8XOSLplFGH2ZiK7XF69QfSnmF/pub?start=true&loop=false&delayms=15000',
'김민정': 'https://docs.google.com/presentation/d/e/2PACX-1vTyrvZ5XihTQURedW0_xLpyDiawxHuh1e7iKJAE0i1yFrv0A-3xr39GigqeW6CC0EITX829PXGSXIfV/pub?start=true&loop=false&delayms=15000',
'김영준': 'https://docs.google.com/presentation/d/e/2PACX-1vRNS7Hr8QhLtiMNJvqoiEO9GnDQaM5jUIKbSyCqToox1cjro0Kw-noKC8xxXUeWdbj3h2idYJpLUbYV/pub?start=false&loop=false&delayms=15000',
'박해원': 'https://docs.google.com/presentation/d/1x-wo9bbVViO1B3RFUH7c7Hbl9qeEiURMlpPJflMhOwg/edit?usp=sharing',
'서지욱': 'https://docs.google.com/presentation/d/e/2PACX-1vQR20_G0HkQ_id0fCLs23HJe0dj0P0PpmleFvOv1Zw74RJPGJcRpctPqQVuDj6pSmzQuzC0ERIaFyhp/pub?start=true&loop=false&delayms=15000',
'손지명': 'https://docs.google.com/presentation/d/e/2PACX-1vSs99vp-24a1X4O2NnlzXjJLGlN6G1oBAkB9E8i0guva_enx_gyjqbsq6_8LaUgV1aEwNpRTr78Z0nf/pub?start=true&loop=false&delayms=15000',
'신동찬': 'https://docs.google.com/presentation/d/e/2PACX-1vT4Cp3alFcMBAjaoeTKzy9yRgIzU_ZCQJOd-_r_70MG3rh7krnojy_S3HpxsW16Opyd8_MkwlA5NFUb/pub?start=true&loop=false&delayms=15000',
'염희돈': "https://docs.google.com/presentation/d/e/2PACX-1vR5hgB_cDEbtxjCcOmQag8YEUqnVwA1quqgThYeAC-_176vtioLkCE2qm8-kqtngB5U3tSG9Egvc2oU/pub?start=true&loop=false&delayms=15000",
'오진석': "https://docs.google.com/presentation/d/e/2PACX-1vQ4-yv1dKQhbziNnKwqR_HxQ8zICW9sjMLrWIVofNVozmFQwDGkk6YiONUrVXp_jqA3CpG9afrmaW9J/pub?start=false&loop=false&delayms=15000",
'윤지원': 'https://docs.google.com/presentation/d/e/2PACX-1vRXeLB7gpSaaw8k1I4YyHqnfVpaJRvMLPxkSlOA877KB6rBwd36gKEfDVFxNFjgeRQYAcHdzgBmSRvw/pub?start=true&loop=false&delayms=15000',
'이재서': 'https://docs.google.com/presentation/d/e/2PACX-1vRWJTJUb0msSsJ8qdAvIsT9eqk6qrMiKE6ZPkumxU9bo8POgc5b4o3iFpTln5lGx4FTgF8udLhJmPLZ/pub?start=true&loop=false&delayms=15000',
'이주원': 'https://docs.google.com/presentation/d/1FTPbD_-6o4lB95WA6TUisjb3KZjoBJLEd3DwG-q_W1Q/edit?usp=sharing',
'이철민': 'https://docs.google.com/presentation/d/e/2PACX-1vSIa-RFoPjff67JxHAbFhwS_MpzDh1XpaHmnUnpUzXKJw7wewqkBCrmvZKE2CCWJ-sAp4U0VQgRx3AQ/pub?start=true&loop=false&delayms=15000',
'이하동': 'https://docs.google.com/presentation/d/e/2PACX-1vQV5jmJw8ST2e4c48uHgBmqdfsaV-7bCi1_C5CTHgmX5Aagt1cfQFm21LApZE4wk0FfwQaLUgnlT5ND/pub?start=true&loop=false&delayms=15000',
'장호익': 'https://docs.google.com/presentation/d/e/2PACX-1vT4rdM8DqPkYLvz6tVD6MMKFA-wUWRzJ7qrpJRSqsA0O43rKkpusngcG1eI-utaoZGOurGQcnBsAnW9/pub?start=false&loop=false&delayms=15000',
'정수원': 'https://docs.google.com/presentation/d/e/2PACX-1vRWJTJUb0msSsJ8qdAvIsT9eqk6qrMiKE6ZPkumxU9bo8POgc5b4o3iFpTln5lGx4FTgF8udLhJmPLZ/pub?start=true&loop=false&delayms=15000',
'정찬미': 'https://docs.google.com/presentation/d/e/2PACX-1vTyrvZ5XihTQURedW0_xLpyDiawxHuh1e7iKJAE0i1yFrv0A-3xr39GigqeW6CC0EITX829PXGSXIfV/pub?start=true&loop=false&delayms=15000',
'최현호': 'https://docs.google.com/presentation/d/e/2PACX-1vSqI7kalM41bVF_FFApd59fQqQCf5ENisVVgY8iBdkarYE4aqGNOdbzUdOrmhK7AblmkWOiKEMY5IDZ/pub?start=false&loop=false&delayms=15000',
'한승은': 'https://docs.google.com/presentation/d/e/2PACX-1vRU8aTvZXvnvUvfBU4viZ9_E4srhVcspkIb8915FQHiXQlM95pEc5Dinrp0wv3KOzYqAuhZrCgG_v0A/pub?start=true&loop=false&delayms=5000'}
    
    if name in sets:
        msg=sets[name]
        requests.get('{}/bot{}/sendMessage?chat_id={}&text={}님 감사합니다.\n{}'.format(base_url,token,chat_id,name,msg))
    else:
        pass
    
    if name == '로또' or name == "lotto":
        msg=sorted(random.sample(range(1,46),6))
        requests.get('{}/bot{}/sendMessage?chat_id={}&text={}'.format(base_url,token,chat_id,msg))
        
    #     img = False
    
    # if doc.get('message').get('photo') is not None:
    #     img = True
    
    # if img:
    #     file_id = doc.get('message').get('photo')[-1].get('file_id')
    #     file = requests.get("{}/bot{}/getFile?file_id={}".format(base_url, token, file_id))
    #     file_url = "{}/file/bot{}/{}".format(base_url, token, file.json().get('result').get('file_path'))
        
    #     # 네이버로 요청
    #     res = requests.get(file_url, stream=True)
    #     clova_res = requests.post('https://openapi.naver.com/v1/vision/celebrity',
    #         headers={
    #             'X-Naver-Client-Id':naver_id,
    #             'X-Naver-Client-Secret':naver_secret
    #         },
    #         files={
    #             'image':res.raw.read()
    #         })
    #     if clova_res.json().get('info').get('faceCount'):
    #         print(clova_res.json().get('faces'))
    #         text = "{}".format(clova_res.json().get('faces')[0].get('celebrity').get('value'))
    #     else:
    #         text = "인식된 사람이 없습니다."
    # else:
    # 	# text 처리
    # 	text = doc['message'].get('text')
        
    # requests.get('{}/bot{}/sendMessage?chat_id={}&text={}'.format(base_url, token, chat_id, text))
    
    return '', 200

@app.route('/setWebhook')
def setWebhook():
# "base url"+"/bot{token}"+"/{method=setWebhook}"
    url = "{}/bot{}/setWebhook?url={}/{}".format(base_url,token,my_url,token) # 배열 지정 가능함?
    response = requests.get(url)
    return '{}'.format(response), 200 # tuple임. 200은 잘 받았다고 서버에 알려주는 거.
    
# @app.route('/')
# def index():
#     return render_template('index.html')