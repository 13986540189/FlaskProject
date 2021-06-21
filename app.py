from datetime import timedelta

from flask import Flask,request,render_template,redirect,jsonify
import utils
import time
from jieba.analyse import extract_tags

app = Flask(__name__)

@app.route('/time',methods=['GET'])
def get_time():
    #将当前时间返回给客户端
    return utils.get_time()

@app.route('/',methods=['GET'])
def Hello_word():
    return render_template("main.html")

@app.route('/center1',methods=['GET'])
def get_c1_data():
    data=utils.get_c1_data()
    #使用flask中的jsonify将字典转化成json字符串返回给客户端
    return jsonify({"confirm":int(data[0]),"suspect":int(data[1]),"heal":int(data[2]),"dead":int(data[3])})

@app.route('/center2',methods=['GET'])
def get_c2_data():
    res=[]
    for tup in utils.get_c2_data():
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

@app.route('/left1')
def get_l1_data():
    data=utils.get_l1_data()
    day,confirm,suspect,heal,dead=[],[],[],[],[]
    for a,b,c,d,e in data[7::]:
        day.append(a.strftime('%m-%d'))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})

@app.route('/left2')
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add, heal_add, dead_add = [],[],[],[],[]
    for a, b, c, d, e in data[7::]:
        day.append(a.strftime('%m-%d'))
        confirm_add.append(b)
        suspect_add.append(c)
        heal_add.append(d)
        dead_add.append(e)
    print(day)
    return jsonify({"day":day,"confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add})

@app.route('/right1')
def get_r1_data():
    data=utils.get_r1_data()
    province_name=[]
    confirm=[]
    for tup in data:
        province_name.append(tup[0])
        confirm.append(int(tup[1]))
    return jsonify({"province_name":province_name,"confirm":confirm})

@app.route('/right2')
def get_r2_data():
    data=utils.get_r2_data()
    keyword=[]
    for tup in data:
        #使用jieba分词提取关键字
        key=extract_tags(tup[0])
        for i in key:
            keyword.append({"name":i,"value":tup[1]})
    return jsonify({"keyword":keyword})




if __name__ == '__main__':
    #监听用户请求，如果有用户请求到来就执行app__call_方法，call方法为请求的入口
    app.run(debug=True,host="0.0.0.0",port="80")
    app.send_file_max_age_default = timedelta(seconds=1)
