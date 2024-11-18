from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login URL
    path("signup/", views.signup_view, name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.list_projects, name='list_projects'),
    path('project/new/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('project/<int:project_id>/export/', views.export_project_markdown, name='export_project_markdown'),
    path('project/<int:todo_id>/update/', views.update_todo, name='update_todo'),
    path('project/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('todo/<int:todo_id>/complete/', views.mark_complete, name='mark_complete'),
    path('todo/<int:todo_id>/pending/', views.mark_pending, name='mark_pending'),
    path('logout/', views.logout_view, name='logout'),
]

