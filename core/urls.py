from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home, login_page, logout_page

app_name = 'core'

urlpatterns = [
    # path('file-upload/s3/create-aws-presigned-urls-profile-image/', AWSCreatePreSignedUrlsForProfileImageView.as_view(), name='file_upload_s3_profile_image'),
    path('',home, name='home'),
    path('login/',login_page, name='login'),
    path('logout/',logout_page, name='logout')
]

urlpatterns += staticfiles_urlpatterns()

