
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('employee',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('students/', views.StudentsView, name='students'),
    path('students/<int:pk>/', views.StudentsDetailView, name='studentsDetail'),
    # path('employee/', views.EmployeeView.as_view(), name='employee'),
    # path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employeeDetail'),

    path('', include(router.urls)),


    path('blogs/', views.BlogView.as_view(), name='blogs'),
    path('comments/', views.CommentView.as_view(), name='comments'),


    path('blogs/<int:pk>', views.BlogDetailView.as_view(), name='blogDetail'),
    path('comments/<int:pk>', views.CommentDetailView.as_view(), name='commentDetail'),

]
