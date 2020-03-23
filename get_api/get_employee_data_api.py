# import requests, json
# user = '93857094983055b7'
# password = 'c1b26c7dfdb521cb'
# data_url = 'http://tsdashboard.analyticservice.net/employees-list'
# data = json.dumps({'name':'test', 'description':'some test repo'})
# r = requests.post(data_url,data,auth=('93857094983055b7','c1b26c7dfdb521cb'))
# print(r)
#
# import urllib, httplib2
# github_url =  'http://tsdashboard.analyticservice.net/employees-list'
# h = httplib2.Http('.cache')
# h.add_credentials('93857094983055b7', 'c1b26c7dfdb521cb')
# resp, content = h.request(github_url, 'POST')
# print(resp)
import pycurl, json
github_url = 'http://tsdashboard.analyticservice.net/employees-list'
user_pwd = '93857094983055b7:c1b26c7dfdb521cb'
data = json.dumps({'name': 'test_repo', 'description': 'Some test repo'})
c = pycurl.Curl()
c.setopt(pycurl.URL, github_url)
c.setopt(pycurl.USERPWD, user_pwd)
c.setopt(pycurl.POST, 1)

c.perform()