import  pymssql
import pymysql
import pandas as pd
from sqlalchemy import Column, String, create_engine
mysql_con = pymysql.connect(host='120.132.101.125', user='root', passwd='Crmtalend123!', db='crm', port = 3306)

cur = mysql_con.cursor()


def read_table(sql):  # sql_order is a string
    """
    提取mysql中的数据并返回成dataframe
    参数只需要sql语句

    """
    conn = pymysql.connect(
        host='120.132.101.125',
        user='root',
        password='Crmtalend123!',
        db='crm',
        port=3306
    )
    cur = conn.cursor()  # 获取操作游标，也就是开始操作
    sql_select = sql  # 查询命令
    cur.execute(sql_select)  # 执行查询语句

    result = cur.fetchall()  # 获取查询结果
    col_result = cur.description  # 获取查询结果的字段描述

    columns = []
    for i in range(len(col_result)):
        columns.append(col_result[i][0])  # 获取字段名，咦列表形式保存

    df = pd.DataFrame(columns=columns)
    for i in range(len(result)):
        df.loc[i] = list(result[i])  # 按行插入查询到的数据

    conn.close()  # 关闭数据库连接

    return df
df = read_table('''
select t1.name quote_name,'AAS' company_name,t2.`name` customer_name ,t1.quote_time ,'Scott' GM_name,'Eavan' PE_name,t3.employeeNumber,t2.industry_level1 industy_level  from quote t1
left join biz_account t2 on t1.account_id = t2.id
left join emp t3 on t1.created_by = t3.openUserId
where t1.life_status = 'normal';
''')
# sqlserver_conn = pymssql.connect(server="WIN-24H0LB5CM6D",user="iplan",password="!QAZ2wsx3edc4rfv",database="YZDQUOTE")
sql_server_engine = create_engine('mssql+pymssql://iplan:!QAZ2wsx3edc4rfv@WIN-24H0LB5CM6D/YZDQUOTE')

# print(df.head())
#
# print(df.columns)
df.to_sql('wallet',con=sql_server_engine,if_exists='replace',index=False)#数据库中表名，