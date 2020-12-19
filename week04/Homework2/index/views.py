from django.shortcuts import render
from django.http import HttpResponse
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,desc,func,and_,or_,not_
from sqlalchemy.ext.declarative import declarative_base
from .models import CommentStar
from django.forms.models import model_to_dict
# Create your views here.

def index(request):    
    comments=CommentStar.objects.filter(star__gt='allstar30 rating')
    for comment in comments:
        comment.star=comment.star[7:8]+'星'
    # return HttpResponse([comment.star+'    '+comment.comment+'<br/>' for comment in comments])
    return render(request, 'index.html',locals())
