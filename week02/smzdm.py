import time
import requests
from fake_useragent import UserAgent
from lxml import etree

ua=UserAgent(verify_ssl=False)
headers={
    'User-Agent' : ua.random
}
s=requests.Session()

first_url='https://www.smzdm.com/'
first_resp = s.get(first_url, headers=headers)
# with open('smzdm.html','w+',encoding='utf-8') as f :
#     f.write(first_resp.text)

selector = etree.HTML(first_resp.text)
page = selector.xpath('//div[@class="z-feed-content"]/h5/a/@href')
print(page[0])
response=s.get(page[0], headers=headers)
selector = etree.HTML(response.text)
username=selector.xpath('//div[@class="comment_conBox"]/div[@class="comment_avatar_time "]/a/span/text()')
print(username)
comment=selector.xpath('//div[@class="comment_conBox"]/div[@class="comment_conWrap"]/div[@class="comment_con"]/p[1]/span[1]/text()[1]')
print(comment)

usercomment=dict(zip(username,comment))

for i in usercomment:
    print(f'user : {i} \t\t comment  {usercomment[i]}')

with open('smzdmcomment.txt','w+',encoding='utf-8') as f :
    for i in usercomment :
        f.write(f'user : {i} \t\t comment  {usercomment[i]} \r\n')

