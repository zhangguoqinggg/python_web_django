import requests
import pandas as pd

from lxml import etree
from .get_company_address_setting import source_file,target_file
df = pd.read_csv(source_file)
df.columns=['id','company_name','company_address']
df['url'] = "https://xin.baidu.com/s?q="+df['company_name']+"&t=0"
credit_code_list = []
industry_type_list = []
company_address_list = []
company_name_list = []
for i in range(0, len(df)):
    # 第一次访问连接入口
    first_page = requests.get(df['url'][i])
    first_tree = etree.HTML(first_page.text)
    try:
        detail_url = "https://xin.baidu.com/" + first_tree.xpath('//div[@class="zx-ent-logo"]/a/@href')[0]
        next_page = requests.get(detail_url)
        next_tree = etree.HTML(next_page.text)
        credit_code_list.append(next_tree.xpath('//table[@class="zx-detail-basic-table"]/tbody/tr[4]/td[2]/text()')[0])
        industry_type_list.append(
            next_tree.xpath('//table[@class="zx-detail-basic-table"]/tbody/tr[3]/td[4]/text()')[0])
        company_address_list.append(
            next_tree.xpath('//table[@class="zx-detail-basic-table"]/tbody/tr[9]/td[2]/text()')[0])
        company_name_list.append(df['company_name'][i])
    except:
        print('以下网页无法访问')
        print('{}'.format(df['url'][i]))
        continue

pre_df = [company_name_list,
          credit_code_list,
        industry_type_list  ,
        company_address_list
 ]

data=pd.DataFrame(pre_df)#这时候是以行为标准写入的
data=data.T#转置之后得到想要的结果
data.rename(columns={0:'company_name_list',1:'credit_code_list',2:'industry_type_list',3:'company_address_list'},inplace=True)#注意这里0和1都不是字符串
data.to_csv(target_file, encoding="utf-8")