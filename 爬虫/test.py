import requests
import pandas as pd



page = requests.get("https://xin.baidu.com/s?q=浙江浙能台州第二发电有限责任公司&t=0")
print(page.text)

