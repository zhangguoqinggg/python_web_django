
import pandas as pd

from sqlalchemy import create_engine


class mysql_engine():
    user = 'root'
    passwd = 'Crmtalend123!'
    host = '120.132.101.125'
    port = '3306'
    db_name = 'crm'
    engine = create_engine('mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user, passwd, host, port, db_name))


def get_data(sql):
    pg_enine = mysql_engine()

    with pg_enine.engine.connect() as con, con.begin():
        df = pd.read_sql(sql, con)  # 获取数据
    con.close()

    return df

df = get_data('''SELECT * FROM biz_product where id = "cadc8dbb54c44a72a3d34c7d7073decb" ; ''')

print(df)