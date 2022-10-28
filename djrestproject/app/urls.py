from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import UserViewset
router = DefaultRouter()
router.register('stuapi',views.StudentView,basename='StudentView')

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)



urlpatterns =[
    # path('userlist/',views.UserList),
    # path('userlist/<int:id>',views.UserDetail),
    path('upd/<int:id>',views.UserBioUpdate.as_view(),name='UserBioUpdate'),
    path('',views.UserBio.as_view(),name='userBio'),
    path('view/',views.UserMixins.as_view(),name='view'),
    path('update/<int:pk>',views.CrudMixins.as_view()),
    path('create/',views.MixinCreate.as_view(),name='create'),
    path('crud/<int:pk>/',views.Details.as_view(),name='crud'),
    path('root',views.API),
]+router.urls


# urlpatterns=format_suffix_patterns(urlpatterns)