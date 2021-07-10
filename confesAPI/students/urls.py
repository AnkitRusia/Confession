from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from students import views


urlpatterns = [
    url(r'^student/$', views.studentAPI),
    url(r'^student/([0-9]+)$', views.studentAPI),
    url(r'^post/$', views.postAPI),
    url(r'^post/([0-9]+)$', views.postAPI),
    url(r'^StudentImage/([0-9]+)$', views.SaveStudentImage),
    url(r'^PostImage/([0-9]+)$', views.SavePostImage),
    url(r'^postByName/$', views.viewPostByName),
    url(r'^likePost/([0-9]+)$', views.likePost),
    url(r'^addcomment/$', views.addComment),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)