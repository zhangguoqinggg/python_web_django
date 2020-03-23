import requests
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud

url = 'https://api.yimian.xyz/coro'
data = requests.get(url).text

city_dic = {}

json_data = json.loads(data)

for p in json_data:
    if 'cities' in  p :
        for c in p['cities']:
            city_dic[c['cityName']] = c['currentConfirmedCount']
    else :
        city_dic[p['provinceName']] = p['currentConfirmedCount']
print(city_dic)
cloud = WordCloud(font_path="D:\\project\\python_web\\python_web_django\\get_api\\HYQuHeiW.ttf",background_color='white').generate_from_frequencies(frequencies=city_dic)
plt.figure()
plt.axis('off')
plt.imshow(cloud,interpolation='bilinear')

plt.savefig('coro.png')


