from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/baru/', views.post_baru, name='post_baru'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('drafts/', views.post_draft_list, name='post_draft_list'),
	path('post/<pk>/publish/', views.post_publish, name='post_terbit'),
	path('post/<pk>/hapus/', views.post_hapus, name='post_hapus'),
]
