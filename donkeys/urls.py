from django.urls import path
from .views import DonkeyList, DonkeyDetail

urlpatterns = [
  path('', DonkeyList.as_view(), name='donkey_list'),
  path('<int:pk>', DonkeyDetail.as_view, name='donkey_detail')
]