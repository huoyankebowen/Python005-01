from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey,desc,func,and_,or_,not_
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime
import sys

Base = declarative_base()

class Customer(Base):
    __tablename__='customer'
    customerid=Column(Integer(),primary_key=True)
    customername=Column(String(50))

class Capital(Base):
    __tablename__='capital'
    customerid=Column(Integer(),primary_key=True)
    totalcap=Column(Float())

class Transaction(Base):
    __tablename__='transaction'
    transid=Column(Integer(),primary_key=True)
    transtime=Column(DateTime(),default=datetime.now)
    fromid=Column(Integer())
    toid=Column(Integer())
    transamt=Column(Float())

    

dburl="mysql+pymysql://testuser:testpass@localhost:3333/testdb?charset=utf8mb4"
engine=create_engine(dburl,echo=True,encoding="utf-8")

Base.metadata.create_all(engine)


customer1=Customer(customerid=1,customername='张三')
customer2=Customer(customerid=2,customername='李四')

capital1=Capital(customerid=1,totalcap=101)
capital2=Capital(customerid=2,totalcap=1)

SessionClass=sessionmaker(bind=engine)
session=SessionClass()
session.add(customer1)
session.add(customer2)
session.add(capital1)
session.add(capital2)
session.commit()

for result in session.query(Capital.customerid,Capital.totalcap):
    print(result)
fromcustomer=session.query(Customer).filter(Customer.customername=='张三').first().customerid
tocustomer=session.query(Customer).filter(Customer.customername=='李四').first().customerid
fromcapital=session.query(Capital).filter(Capital.customerid==fromcustomer)
try:
    if fromcapital.first().totalcap<100:
        raise Exception('用户余额不足')
except Exception as e:
    print(e)
    sys.exit(1)
fromcapital.update({Capital.totalcap: Capital.totalcap-100})
tocapital=session.query(Capital).filter(Capital.customerid==tocustomer)
tocapital.update({Capital.totalcap: Capital.totalcap+100})
transaction=Transaction(fromid=fromcustomer,toid=tocustomer,transamt=100)
session.add(transaction)
for result in session.query(Capital.customerid,Capital.totalcap):
    print(result)
session.commit()


for result in session.query(Capital.customerid,Capital.totalcap):
    print(result)
fromcustomer=session.query(Customer).filter(Customer.customername=='张三').first().customerid
tocustomer=session.query(Customer).filter(Customer.customername=='李四').first().customerid
fromcapital=session.query(Capital).filter(Capital.customerid==fromcustomer)
try:
    if fromcapital.first().totalcap<100:
        raise Exception('用户余额不足')
except Exception as e:
    print(e)
    sys.exit(1)
fromcapital.update({Capital.totalcap: Capital.totalcap-100})
tocapital=session.query(Capital).filter(Capital.customerid==tocustomer)
tocapital.update({Capital.totalcap: Capital.totalcap+100})
transaction=Transaction(fromid=fromcustomer,toid=tocustomer,transamt=100)
session.add(transaction)
for result in session.query(Capital.customerid,Capital.totalcap):
    print(result)
session.commit()

# query=query.filter(Book_table.book_id==2)
# query.update({Book_table.book_name:'newbook'})
# new_book=query.first()
# print(new_book.book_name)