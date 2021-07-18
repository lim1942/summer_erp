from django.conf.urls import include, url,static
import basedata.views

# 由于django版本兼容问题，此条url会被 admin 提前截取，并报错，不能下载。
urlpatterns = [
    url(r"dataimport/(?P<object_id>\d+)/action", basedata.views.action_import),
]
