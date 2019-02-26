from django.urls import path
from myblog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/edit/<pk>', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/remove/<pk>', views.PostDeleteView.as_view(), name='post_remove'),
    path('draft/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/comment/<pk>', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/approve/<pk>', views.comment_approve, name='comment_approve'),
    path('comment/remove/<pk>', views.comment_remove, name='comment_remove'),
    path('post/publish/<pk>', views.post_publish, name='post_publish'),
    path('signup/', views.Signup.as_view(), name='signup'),
]
