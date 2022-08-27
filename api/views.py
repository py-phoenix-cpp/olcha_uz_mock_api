from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import *


class InfoView(viewsets.ReadOnlyModelViewSet):
    queryset = Info.objects.order_by('-id')[:1]
    serializer_class = InfoSerializer


class BannerView(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all().order_by('-id')
    serializer_class = BannerSerializer

    def create(self, request):
        img = request.FILES['img']
        Banner.objects.create(img=img)
        return Response({'done'})

class SubCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class MainCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer


class BrandView(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductColorModelImageView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductColorModelImage.objects.all()
    serializer_class = ProductSerializer


class ProductViewImageView(viewsets.ReadOnlyModelViewSet):
    queryset = ProductViewImage.objects.all().order_by('-id')
    serializer_class = ProductViewImageSerializer


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, requests, pk=None):
        query = Product.objects.get(id=pk)
        query.delete()
        return Response({'destroyed'})

    @action(methods=['get'], detail=False)
    def filter_by_category(self, request, pk=None):
        query = Product.objects.filter(id=pk)
        return Response(self.serializer_class(query, many=True).data)


class NewsView(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer

    def create(self, request):
        title = request.POST['title']
        text = request.POST['text']
        date = request.POST['date']
        News.objects.create(title=title, text=text, date=date)
        return Response({'message': 'done'})

    def destroy(self, requests, pk=None):
        query = News.objects.get(id=pk)
        query.delete()
        return Response({'destroyed'})


class OpinionView(viewsets.ReadOnlyModelViewSet):
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