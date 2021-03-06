"""Medical URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns
from django.contrib import admin
from APP import views
from Medical import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login_page),
    # url(r'^load_home_page/', views.load_home_page)
    url(r'^load_add_item_page/', views.load_add_item_page),
    url(r'^search/', views.search_page),
    url(r'^add_an_item/', views.add_new_item),
    url(r'search_for_item', views.search_for_item),
    url(r'^show_complete_stock/', views.show_complete_stock),
    url(r'^show_home/', views.show_home),
    url(r'^dashboard/', views.dashboard),
]
'''
# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
'''