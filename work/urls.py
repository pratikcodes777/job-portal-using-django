from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job , name='create-job'),
    path('update-job/<int:pk>' , views.update_job , name='update-job'),
    path('update-job/<int:pk>' , views.update_job , name='update-job'),
    path('apply-to-jobs/<int:pk>' , views.apply_to_jobs , name='apply-to-jobs'),
    path('manage-jobs/' , views.manage_jobs , name='manage-jobs'),
    path('all-applicants/<int:pk>' , views.all_applicants , name='all-applicants'),
    path('applied_jobs' , views.applied_jobs , name='applied-jobs'),

   
]