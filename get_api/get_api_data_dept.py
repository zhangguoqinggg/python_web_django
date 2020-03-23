import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
a = HTTPBasicAuth('93857094983055b7', 'c1b26c7dfdb521cb')
r = requests.get(url='http://tsdashboard.analyticservice.net/employees-list', auth=a)

#或者直接(只加载requests模块就行)
# r = requests.get(url=('http://xxx.xxx.xxx'), auth=('user', 'password'))
json_data = json.loads(r.text)
for i in range(0,len(json_data['response'])):
    try :
        json_data['response'][i]['departments_id']=json_data['response'][i]['departments'][0]['wechat_id']
    except KeyError:
        json_data['response'][i]['departments_id'] = 0
    try :
        json_data['response'][i]['departments_name']=json_data['response'][i]['departments'][0]['name']
    except KeyError:
        json_data['response'][i]['departments_name'] = 0
    try :
        json_data['response'][i]['departments_parent_id']=json_data['response'][i]['departments'][0]['parent']['id']
    except KeyError:
        json_data['response'][i]['departments_parent_id'] = 0
dic = {}

df_list = []

for i in range(0, len(json_data['response'])):
    df = {}
    try:
        df['departments_id'] = json_data['response'][i]['departments_id']
    except KeyError:
        df['departments_id'] = 0
    try:
        df['departments_name'] = json_data['response'][i]['departments_name']
    except KeyError:
        df['departments_id'] = 0
    try:
        df['departments_parent_id'] = json_data['response'][i]['departments_parent_id']
    except KeyError:
        df['departments_id'] = 0
    df_list.append(df)
data = pd.DataFrame()
for i in range(0, len(df_list)):
    data_df = pd.DataFrame(df_list[i], index=[0])
    data = data.append(data_df)
data = data.drop_duplicates()
data = data[data['departments_id']!=0]

updata_str_sql = "insert into [m_dept_bk] values   "

for i in range(0,len(data)):
        updata_str_sql = updata_str_sql + "("
        updata_str_sql  =  updata_str_sql + str(data.iloc[i,0]) +",'dep' +REPLICATE('0',4-len(cast( "+ str(data.iloc[i,0])+" as varchar(4))))+cast("+ str(data.iloc[i,0])+" as varchar(4)),'"+ str(data.iloc[i,1]) +"','"+ str(data.iloc[i,2])   +"', getdate())"
        if i == len(data)-2:
            updata_str_sql = updata_str_sql +';'
            break
        else:
            updata_str_sql = updata_str_sql +','

print(updata_str_sql)