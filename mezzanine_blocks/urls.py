from django.conf.urls.defaults import url
from django.contrib.admin.views.decorators import staff_member_required
from views import edit

urlpatterns = [
    url(r'^edit/(?P<pk>\d+)/$', staff_member_required(edit), name='blocks-edit')
]
