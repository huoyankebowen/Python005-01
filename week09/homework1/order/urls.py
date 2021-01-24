"""order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from order.order.models import Order
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=['put'],detail=True)
    def cancel(self, request, *args, **kwargs):
        """ 
        取消订单 
        """ 
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = OrderSerializer(instance, data=request.data, partial=partial,context={'request': request})         
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['Canceld']=1 
        serializer.save()
        return Response(serializer.data)

        # try:
        #     order=self.get_queryset().get(Order_id=pk)
        #     order.Canceld=1
        #     Order.save()
        # except Exception as e:
        #     print(e)
        # return Response(f'order {pk} is canceled')

class OrderCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['Product']


class OrderCreateViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    


  

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'orders/create', OrderCreateViewSet)
router.register(r'orders', OrderViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
