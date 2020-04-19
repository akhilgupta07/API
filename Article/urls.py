from django.urls import path,include
from .import views

urlpatterns = [
    path('article/', views.Article_List),
    path('detail/<int:id>',views.Article_detail),
    path('Article/',views.ArticleAPIView.as_view()),
    path('Articledetail/<int:id>',views.ArticleDetailApiView.as_view()),
    path('Genericarticle/<int:id>',views.GenericAPIView.as_view()),
    
]
