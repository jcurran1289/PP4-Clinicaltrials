from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('search_ct/', views.search_ct, name='search-ct'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('enroll/<slug:slug>/', views.PostEnroll.as_view(), name='post_enroll'),  # noqa

]
