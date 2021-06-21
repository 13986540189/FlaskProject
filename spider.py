import requests
import json
import pymysql
import time
import traceback
from selenium import webdriver
import sys

def get_cov_data():
    #详情数据url
    details_url=' https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    #历史数据url
    history_url='https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'
    details_response=requests.get(details_url)
    #将获取的详情数据json字符串转化成字典
    details_json=json.loads(details_response.text)
    #key为data的json字符串转化成字典
    details_dic=json.loads(details_json['data'])
    history_response=requests.get(history_url)
    #将历史数据json字符串转化成字典
    history_dic=json.loads(history_response.text)['data']
    history={}
    details = []
    #将历史数据保存
    for i in history_dic['chinaDayList']:
        date=i['y']+'.'+i['date']
        tup=time.strptime(date,'%Y.%m.%d')
        #改变时间格式不然插入数据时数据库会报错
        date=time.strftime('%Y-%m-%d',tup)
        confirm=i['confirm']
        suspect=i['suspect']
        dead=i['dead']
        heal=i['heal']
        history[date]={"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead}
    #将历史当天新增数据保存
    for i in history_dic['chinaDayAddList']:
        date=i['y']+'.'+i['date']
        tup=time.strptime(date,'%Y.%m.%d')
        date=time.strftime('%Y-%m-%d',tup)
        confirm=i['confirm']
        suspect=i['suspect']
        dead=i['dead']
        heal=i['heal']
        history[date].update({"confirm_add":confirm,"suspect_add":suspect,"heal_add":heal,"dead_add":dead})

    update_time=details_dic['lastUpdateTime']
    data_countries=details_dic['areaTree']
    #获取省级数据列表
    data_provinces=data_countries[0]['children']
    #将详情数据保存
    for pro_info in data_provinces:
        provinces_name=pro_info['name']
        for city_info in pro_info['children']:
            city_name=city_info['name']
            confirm=city_info['total']['confirm']
            confirm_add=city_info['today']['confirm']
            heal=city_info['total']['heal']
            dead=city_info['total']['dead']
            details.append([update_time,provinces_name,city_name,confirm,confirm_add,heal,dead])
    return history,details

def get_search_data():
    #设置无头浏览器
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #实例谷歌浏览器对象
    browser = webdriver.Chrome(executable_path=r'chromedriver.exe',options=chrome_options)
    url="http://top.baidu.com/buzz/shijian.html"
    #get请求百度热搜榜url
    browser.get(url)
    tr=browser.find_elements_by_tag_name("tr")
    context=[]
    #获取每个热搜的标题以及对应的热度,并封装在字典中
    for i in range(2,len(tr)+1):
        title=browser.find_element_by_xpath('//table[@class="list-table"]/tbody/tr['+str(i)+']//td[@class="keyword"]').text
        heat=browser.find_element_by_xpath('//table[@class="list-table"]/tbody/tr['+str(i)+']//td[@class="last"]').text
        context.append({"title":title,"heat":heat})
    return context
    browser.close()


#获取连接
def get_connect():
    con = pymysql.connect(host="39.103.232.195", port=3306, user="root", passwd="root", db="newsqa", charset="utf8")
    cur = con.cursor()
    return con,cur

#关闭连接
def close_connect(con,cur):
    if con:
        con.close()
    if cur:
        cur.close()

#保存详情数据到数据库中
def up_details():
    con=None
    cur=None
    try:
        li=get_cov_data()[1]
        con,cur=get_connect()
        sql="update details set update_time=%s,confirm=%s,confirm_add=%s,heal=%s,dead=%s  where province_name=%s and city_name=%s"
        sql_query="select %s=(select update_time from details order by id desc limit 1)"
        cur.execute(sql_query,li[0][0])
        if not cur.fetchone()[0]:
            print(f"{time.asctime()}开始更新详情最新数据")
            for item in li:
                cur.execute(sql,(item[0],item[3],item[4],item[5],item[6],item[1],item[2]))
            con.commit()
            print(f"{time.asctime()}更新详情最新数据完毕")
        else:
            print(f"{time.asctime()}详情表已是最新数据")
    except:
        traceback.print_exc()
    finally:
        close_connect(con,cur)

#保存历史数据到数据库中
def up_history():
    con=None
    cur=None
    try:
        li=get_cov_data()[0].items()
        con,cur=get_connect()
        sql="insert into history(ds,confirm,confirm_add,suspect,suspect_add,heal,heal_add,dead,dead_add) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query="select confirm from history where ds=%s"
        for k,v in li:
            if not cur.execute(sql_query,k):
                print(f"{time.asctime()}开始更新历史最新数据")
                cur.execute(sql,[k,v.get('confirm'),v.get('confirm_add'),v.get('suspect'),v.get('suspect_add'),v.get('heal'),v.get('heal_add'),v.get('dead'),v.get('dead_add')])
        print(f"{time.asctime()}历史数据更新完毕")
        con.commit()
    except:
        traceback.print_exc()
    finally:
        close_connect(con,cur)

def up_search():
    con,cur=None,None
    try:
        context=get_search_data()
        con,cur=get_connect()
        sql="insert into hotsearch(ds,context,heat) values(%s,%s,%s)"
        for i in context:
            cur.execute(sql,(time.strftime("%Y-%m-%d %X"),i.get('title'),i.get('heat')))
            con.commit()
        print(f"{time.asctime()}热搜数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_connect(con,cur)


if __name__ == '__main__':
    up_history()
    up_details()
    up_search()
    #以下为在Linux环境下的代码
    # if len(sys.argv) == 1:
    #     message= '''请输入参数
    # 参数说明:up_history 更新历史记录表
    #         up_details 更新详情记录表
    #         up_search 更新热搜记录表
    #         '''
    #     print(message)
    # else:
    #     order = sys.argv[1]
    #     if order == "up_history":
    #         up_history()
    #     elif order == "up_details":
    #         up_details()
    #     elif order == "up_search":
    #         up_search()



