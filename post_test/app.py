from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/signup',methods=['POST'])
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    
    adminEmail="qwer@qwer.com"
    adminPassword="12341234"
    
    #만약에 회원가입한 사람이 admin일 경우,
    #관리자님 환영합니다. 라고 출력
    #아닐 경우, 
    # "안녕~"
    
    if email == adminEmail:
        if password == adminPassword:
            msg = "관리자님 환영합니다."
            #return render_template('signup.html',email="관리자",password=password)
        else:
            msg = "관리자님 비번 더 생각해보세요."
            #return render_template('signup.html',email="관리자",password=password)
    else:
        msg = "꺼지셈"
    return render_template('signup.html',msg=msg)