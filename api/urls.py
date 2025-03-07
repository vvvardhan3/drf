from django.urls import path, include
from . import views
from fileupload.views import FileUploadView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.employeeViewset, basename='employee')

urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),
    # path('employees/',views.employees.as_view()),
    # path('employees/<int:pk>/',views.employeesDetails.as_view()),
    path('', include(router.urls)),
    path('blogs/',views.blogView.as_view()),
    path('comments/',views.commentView.as_view()),
    path('blogs/<int:pk>/',views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view()),
    
]