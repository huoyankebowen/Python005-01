学习笔记

python环境

2020年11月21日
15:55

查看版本
python -V
pip -V

pip修改源
豆瓣：http://pypi.doubanio.com/simple/
清华：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
升级pip
方法一：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
方法二：
pip config set global.index-url http://pypi.doubanio.com/simple/
pip install pip -U

pip安装加速
配置文件
Windows:C:\users\xxx\pip\pip.ini
Linux: ~/.pip/pip.conf
格式
[golbal]
Index-url=https://pypi.tuna.tsinghua.edu.cn/simple


vscode需要安装扩展:python,chinese(Simplified) ,rainbow fart
Alt+shift+f 格式化代码
alt+左右 按照单词移动
ctrl+上下左右 移动到头为
alt+上下 上下移动行
ctrl+/ 注释
F5 启动调试
F11 单步调试

Pycharm
属性-项目-python解释器 设置解释器

Jupyter
pip install jupyter
jupyter notebook


创建虚拟环境
python -m venv venv1(目录)
激活虚拟环境
source venv1/bin/activate
退出虚拟环境
deactivate
查看虚拟环境安装了哪些库
source venv1/bin/activate
pip3 freeze > requirements.txt
安装相同的第三方库
pip install -r ./requirements.txt

利用pip离线安装python包-方案
1、在可以联网的开发机器上安装好需要的包
例如：
pip  install  elasticsearch
2、打包已安装的包
#查看安装的包
pip  list
#生成requirements.txt(记录所有依赖包及其精确的版本号)
pip freeze >requirements.txt
#下载对应的包
pip install --download /root/packages -r requirements.txt
3、离线情况安装打包好的包
将packages文件夹和requirement.txt拷贝至离线机器上目录下
执行命令：
pip install --no-index--find-links=./packages -r requirements.txt

语法

2020年11月24日
21:35

空 None
二进制 0b10
八进制 0o10
十六进制 0x10
判断空 var1 is None

python字符串函数
python列表函数
python字典函数

高级数据类型collections 容器数据类型
nametuple() 命名元组
deque 双端队列
Counter 计数器
OrderedDict 有顺序的字典

if 条件 :
	pass
elif:
	pass
else:
	pass

while 条件 :
	pass

for i in list1:
	pass
	
常见模块
time:time.localtime(), time.strftime("%Y-%m-%d %X",time.localtime), time.strptime('2020-10-20 17:46:49',"%Y-%m-%d %X"),time.ctime()
datetime:datetime.today(), datetime.now(), datetime.today()-timedelta(days=1)
logging:
级别:info,warning,error,critical,debug
	logging.basicConfig(filename='test.log',level=logging.DEBUG,datefmt='%Y-%m-%d %H:%M:%S',format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')
	logging.级别()
random
	random(),randrange(0,101,2),choice(['red','blue','orange']),sample([1,2,3,4,5],k=4)
json
	Json.loads(),json.dumps()
pathlib
	p=Path()
	p.resolve
	path='/usr/local/a.txt.py'
	p=Path(path)
	p.name
	p.stem
	p.suffix,p.suffixes
	p.parent,p.parents
	p.parts
os.path
	os.path.abspath('test.log')
	path='/usr/local/a.txt'
	os.path.basename(path),os.path.dirname(path)
	os.path.exists('/etc/passwd')
	os.path.isfile(/etc/passwd'),os.path.isdir(/etc/passwd')
	os.path.join('a','b')


re函数

2020年11月26日
0:34

prog = re.compile(pattern)
result = prog.match(string)
等价于
result = re.match(pattern, string)

re.match(".{11}","12332112312")
re.match(".{11}","12332112312").group()
re.match(".{11}","12332112312").span()
re.match("(.*)@(.*)","abc@123.com")
re.match("(.*)@(.*)","abc@123.com").group(1)

re.search("@","123@123.com")

re.findall("123","123@123.com")

re.sub("\d+","abcxyz","123@123.com")

re.split("@","123@123.com"),re.split("(@)","123@123.com")
