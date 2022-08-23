from django.db import models


class Info(models.Model):
    tel_nomer = models.IntegerField()
    facebook = models.CharField(max_length=25)
    instagram = models.CharField(max_length=25)
    telegram = models.CharField(max_length=25)
    location = models.CharField(max_length=255)


class Banner(models.Model):
    img = models.ImageField(upload_to='img/Banner/')


class MainCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/Category/', null=True, blank=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/SubCategory/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name








class Brend(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/Brend/')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


class ProductColorModelImage(models.Model):
    img = models.ImageField(upload_to='img/Products/ProductColorImage/')


class ProductViewImage(models.Model):
    img = models.ImageField(upload_to='img/Products/ProductViewImage/')


class Product(models.Model):
    CHOICES = (
        ('1', '1 yulduz'),
        ('2', '2 yulduz'),
        ('3', '3 yulduz'),
        ('4', '4 yulduz'),
        ('5', '5 yulduz'),
    )
    name = models.CharField(max_length=255)
    text = models.TextField()
    about = models.TextField()
    rate = models.CharField(max_length=15,
                            choices=CHOICES,
                            default=0)
    price = models.IntegerField()
    installment_plan_price = models.IntegerField()
    main_img = models.ImageField(upload_to=f'img/Products/')
    view_img = models.ManyToManyField(ProductViewImage, blank=True)
    color_img = models.ManyToManyField(ProductColorModelImage, blank=True)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()


class Opinion(models.Model):
    CHOICES = (
        ('1', '1 yulduz'),
        ('2', '2 yulduz'),
        ('3', '3 yulduz'),
        ('4', '4 yulduz'),
        ('5', '5 yulduz'),
    )
    name = models.CharField(max_length=100)
    tel_nomer = models.IntegerField()
    fikr = models.TextField()
    at_site_rate = models.CharField(max_length=25,
                                    choices=CHOICES,
                                    default=0)
