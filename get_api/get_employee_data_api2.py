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

# print(json_data['response'][0])
# print(type(json_data['response'][0]))
# print(type(json_data['response']))
# print(len(json_data['response']))

# print(json_data['response'][0]['departments'])
# print(type(json_data['response'][0]['departments']))
#需要的几个字段
key_list = ['id','name','code','mobile','email','departments','job_status']
df_list = []
for i in range(0, len(json_data['response'])):
    try:
        json_data['response'][i]['departments'] = json_data['response'][i]['departments'][0]['wechat_id']
    except KeyError:
        json_data['response'][i]['departments'] = 0
    df = {}
    try:
        df['id'] = json_data['response'][i]['id']
    except KeyError:
        df['id'] = 0
    try:
        df['name'] = json_data['response'][i]['name']
    except KeyError:
        df['name'] = 0
    try:
        df['code'] = json_data['response'][i]['code']
    except KeyError:
        df['code'] = 0
    try:
        df['mobile'] = json_data['response'][i]['mobile']
    except KeyError:
        df['mobile'] = 0
    try:
        df['email'] = json_data['response'][i]['email']
    except KeyError:
        df['email'] = 0
    try:
        df['job_status'] = json_data['response'][i]['job_status']
    except KeyError:
        df['job_status'] = 0
    df_list.append(df)

data = pd.DataFrame()
for i in range(0, len(df_list)):
    data_df = pd.DataFrame(df_list[i], index=[0])
    data = data.append(data_df)
data = data[data['job_status'] ==1]
data_df['']
print(data)
