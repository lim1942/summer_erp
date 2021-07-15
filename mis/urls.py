from django.conf.urls import include, re_path, static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from mis import settings
import workflow.views
import invent.urls
import basedata.urls
import selfhelp.urls
import mis.views
from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Django-ERP'
admin.site.site_title = 'ERP'

urlpatterns = [
    # 此接口用于用户post自定义设置语言
    path('i18n/', include('django.conf.urls.i18n')),
    # re_path(r'^$', mis.views.home),
    # re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start", workflow.views.start),
    # re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)", workflow.views.approve),
    # re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)", workflow.views.restart),
    # re_path(r'^admin/', admin.site.urls),
    # re_path(r'^admin/invent/', include(invent.urls)),
    # re_path(r'^admin/basedata/', include(basedata.urls)),
    # re_path(r'^admin/selfhelp/', include(selfhelp.urls)),
]
urlpatterns += i18n_patterns(
    re_path(r'^$', mis.views.home),
    re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/start", workflow.views.start),
    re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/approve/(?P<operation>\d+)",
            workflow.views.approve),
    re_path(r"^admin/(?P<app>\w+)/(?P<model>\w+)/(?P<object_id>\d+)/restart/(?P<instance>\d+)", workflow.views.restart),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^admin/invent/', include(invent.urls)),
    re_path(r'^admin/basedata/', include(basedata.urls)),
    re_path(r'^admin/selfhelp/', include(selfhelp.urls)),
    prefix_default_language=True,

)
urlpatterns += static.static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static.static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


