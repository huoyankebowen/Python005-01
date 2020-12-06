学习笔记

requests库
https://requests.readthedocs.io/zh_CN/latest/
get方式
r = requests.get('http://httpbin.org')
Eg:
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
header={'user-agent':user_agent}
myurl='https://movie.douban.com/top250'
r = requests.get(myurl,headers=header,timeout=30)
payload={'key1':'value1','key2':['value2','value3']}
r = requests.get('http://www.httpbin.org',params=payload)

r.status_code,r.headers,r.text
eg：
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
header={'user-agent':user_agent}
myurl='https://movie.douban.com/top250'
response=requests.get(myurl,headers=header)
print(response.text)
post方式
r=requests.post('http://httpbin.org/post',data={'key':'value'})
r.json()
在session中带cookies
with requests.Session() as s:
    s.get()

使用xpath取得网页上的电影列表
selecter=lxml.etree.HTML(response.text)
film_name=select.xpath('//div[@class="hd"]/a/span[1]/text()')

Socket API
socket(),bind(),listen(),accept(),recv(),send(),close(),sendall()

Request headers
Cookies 客户会话信息，登录成功信息
Host 网站主机名
Referer 从哪个页面转来的
User-Agent 当前浏览器版本


异常

try :
    语句
except Exception as e:
    语句

常见异常
LookupError下的IndexError和KeyError
IOError
NameError
TypeError
AttributeError
ZeroDivisionError

也可以通过Exception捕获所有异常

自定义异常
class UserInputError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self,ErrorInfo)
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo

userinput='a'

try:
    if (not userimput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as e:
    print(e)
finally:
    del userinput
自定义异常捕获后程序不会退出，如想退出加sys.exit(1)

异常美化，用第三方库pretty_errors
import pretty_errors

文件异常
with open('文件名',encoding='编码') as f :

自己实现with
class Open:
    def __enter__(self):
        print('open')
    def __exit__(self,type,value,trace):
        print('close')
    def __call__(self):
       pass

with Open() as f:
    pass

