from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,func,and_,or_,not_
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

class User_table(Base):
    __tablename__='user'
    # 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
    user_id=Column(Integer(),primary_key=True)
    user_name=Column(String(50))
    age=Column(Integer())
    birthday=Column(String(10))
    sex=Column(String(1))
    education=Column(String(20))
    created_on=Column(DateTime(),default=datetime.now)
    updated_on=Column(DateTime(),default=datetime.now,onupdate=datetime.now)

dburl="mysql+pymysql://testuser:testpass@localhost:3333/testdb?charset=utf8mb4"
engine=create_engine(dburl,echo=True,encoding="utf-8")

Base.metadata.create_all(engine)

SessionClass=sessionmaker(bind=engine)
session=SessionClass()
# insert
user1=User_table(user_name='张三',age=20,birthday='2000-11-11',sex='1',education='Bachelor')
user2=User_table(user_name='李四',age=21,birthday='1999-12-12',sex='0',education='Master')
user3=User_table(user_name='王五',age=22,birthday='1998-10-10',sex='1',education='Doctor')

session.add(user1)
session.add(user2)
session.add(user3)

session.commit()

for result in session.query(User_table.user_name,User_table.age,User_table.birthday,User_table.sex,User_table.education):
    print(result)
session.commit()

db=pymysql.connect(host='localhost', user='testuser', password="testpass",database='testdb', port=3333,charset='utf8mb4')

try:
    with db.cursor() as cursor:
        # 增
        sql='insert into user (user_name,age,birthday,sex,education) values (%s,%s,%s,%s,%s)'
        values = (
            ("李七",23,"1997-01-01",'1','Bachelor'),
            ("张八",24,"1996-02-02",'0','Master'),
            ("赵九",25,"1995-03-03",'1','Doctor'),
        )
        cursor.executemany(sql,values)    
        # 查
        sql='select user_name,age,birthday,sex,education from user'
        cursor.execute(sql)
        users=cursor.fetchall()
        for user in users :
            print(user)
    db.commit()
except Exception as e:
    print(f"insert error {e}")
finally:
    db.close()
