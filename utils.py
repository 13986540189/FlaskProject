import time
import pymysql
def get_time():
    #获取当前时间
    time_str=time.strftime("%Y{}%m{}%d %X".format("-","-"))
    return time_str

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

#查询函数
def query(sql,*args):
    con,cur=get_connect()
    cur.execute(sql,args)
    res=cur.fetchall()
    close_connect(con,cur)
    return res

#从数据库中查询疫情总数据
def get_c1_data():
    sql="select sum(confirm)," \
        "(select suspect from history order by ds desc limit 1)," \
        "sum(heal)," \
        "sum(dead) " \
        "from details "\
        "where update_time=(select update_time from details order by update_time desc limit 1)"
    res=query(sql)
    return res[0]

#从数据库中查询疫情详情数据
def get_c2_data():
    sql="select province_name,sum(confirm) from details " \
        "where update_time=(select update_time from details order by update_time desc limit 1)"\
        "group by province_name"
    res=query(sql)
    return res

def get_l1_data():
    sql="select ds,confirm,suspect,heal,dead from history"
    res=query(sql)
    return res

def get_l2_data():
    sql="select ds,confirm_add,suspect_add,heal_add,dead_add from history"
    res=query(sql)
    return res

def get_r1_data():
    sql='select province_name,confirm from '\
        '(select province_name,confirm from details '\
        'where update_time=(select update_time from details order by update_time desc limit 1) ' \
        'and province_name not in ("湖北","北京","天津","上海","重庆") ' \
        'union all ' \
        'select province_name as province_name,sum(confirm) as confirm from details ' \
        'where update_time=(select update_time from details order by update_time desc limit 1) ' \
        'and province_name in ("北京","上海","天津","重庆") group by province_name) as a ' \
        'order by confirm desc limit 5'
    res=query(sql)
    return res

def get_r2_data():
    sql="select context,heat from hotsearch order by id desc limit 50"
    res=query(sql)
    return res



