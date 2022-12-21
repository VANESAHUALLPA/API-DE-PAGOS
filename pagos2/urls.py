from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pagos', api.Pago2ViewSet, 'pagos')

urlpatterns = router.urls