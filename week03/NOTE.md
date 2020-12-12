学习笔记

数据库

安装
dev.mysql.com
yum install mysql57-community-release-el7-10.noarch.rpm
yum install mysql-community-server
yum remove mysql57-community-release-el7-10.noarch
systemctl start mysqld.service
systemctl enable mysqld
systemctl status mysqld.service
grep 'password' /var/log/mysqld.log
mysql -u root -p *****
修改密码
Mysql>alter user 'root'@'localhost' identified by 'newpassword';
安全复杂度设置
Mysql>show variables like 'validate_password%';
Mysql>set global validate_password_policy=0;

字符集
查看字符集
show variables like '%character%';
查看校对规则
show variables like '%collation_%'
utf8mb4相当于UTF-8
utf8mb4为4字节，可以存emoji表情，utf8为3字节，不能存emoji表情
vi my.cnf
[client]
default_character_set = utf8mb4
[mysql]
default_character_set = utf8mb4
交互连接超时时间
interactive_timeout=28800
非交互连接超时时间
wait_timeout=28800
最大连接数
max_connections=1000
mysql字符集设置
character_set_server = utf8mb4
为每个连接客户端执行的字符串
init_connect = 'set names utf8mb4'

character_set_client_handshake= FALSE
collation_server = utf8mb4_unicode_ci
 





python官方包
MySQLdb是Python2的包，适用与MySQL5.5和Python2.7
Python3的MySQLdb包叫mysqlclient，加载依然是MySQLdb
pip install mysqlclient
import MySQLdb

其他db-api
pip install pymysql         --流行度较高
pip install mysql-connector-python        --mysql官方

使用ORM连接
pip install sqlalchemy