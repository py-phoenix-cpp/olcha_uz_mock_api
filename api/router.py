from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(f'info', InfoView)
router.register(f'banner', BannerView)
router.register(f'subcategory', SubCategoryView)
router.register(f'category', CategoryView)
router.register(f'maincategory', MainCategoryView)
router.register(f'brend', BrendView)
router.register(f'productcolormodelimage', ProductViewImageView)
router.register(f'productviewimage', ProductViewImageView)
router.register(f'product', ProductView)
router.register(f'news', NewsView)
router.register(f'opinion', OpinionView)
