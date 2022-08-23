from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import *


class InfoView(viewsets.ReadOnlyModelViewSet):
    queryset = Info.objects.order_by('-id')[:1]
    serializer_class = InfoSerializer


class BannerView(viewsets.ModelViewSet):
    queryset = Banner.objects.all().order_by('-id')
    serializer_class = BannerSerializer
    http_method_names = ['get', 'post']


class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class MainCategoryView(viewsets.ModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    http_method_names = ['get', 'post', 'delete']

class BrendView(viewsets.ModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
    http_method_names = ['get', 'post']

class ProductColorModelImageView(viewsets.ModelViewSet):
    queryset = ProductColorModelImage.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post']

class ProductViewImageView(viewsets.ModelViewSet):
    queryset = ProductViewImage.objects.all().order_by('-id')
    serializer_class = ProductViewImageSerializer
    http_method_names = ['get', 'post']

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer
    http_method_names = ['get', 'post', 'delete']

    # def create(self, request, *args, **kwargs):
    #     title = request.POST.get('title')
    #     text = request.POST.get('text')
    #     date = request.POST.get('date')
    #     News.objects.create(title=title, text=text, date=date)
    #     return Response({'message': 'done'})

class OpinionView(viewsets.ModelViewSet):
    queryset = Opinion.objects.all()
    serializer_class = OpinionSerializer
    http_method_names = ['get', 'post']

    # def create(self, request, *args, **kwargs):
    #     name = request.POST.get('name')
    #     tel_nomer = request.POST.get('tel_nomer')
    #     fikr = request.POST.get('fikr')
    #     at_site_rate = request.POST.get('at_site_rate')
    #     News.objects.create(name=name, tel_nomer=tel_nomer, fikr=fikr, at_site_rate=at_site_rate)
    #     return Response({'message': 'done'})