from rest_framework import serializers
from main.models import *


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = "__all__"


class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = "__all__"


class ProductColorModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColorModelImage
        fields = "__all__"


class ProductViewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewImage
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        fields = "__all__"