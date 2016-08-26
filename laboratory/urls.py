'''
Created on 11/8/2016

@author: natalia
'''
from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from laboratory.generic import ObjectDeleteFromShelf, ObjectList, \
    LaboratoryRoomsList
from laboratory.ajax_view import list_furniture, list_shelf, list_shelfobject, ShelfObjectCreate, ShelfObjectDelete
from laboratory.views import index


urlpatterns = [
    url(r"^delete/(?P<pk>\d+)$",
        ObjectDeleteFromShelf.as_view(), name="object_Delete"),
    # url(r"^list$", ObjectList.as_view(), name='object-list')
    url(r"^listLaboratoryRooms$", LaboratoryRoomsList.as_view(),
        name='laboratoryRooms_list')
]

urlpatterns += [
    url(r"^furniture/list/$", list_furniture, name="list_furniture"),
    url(r"^shelf/list$", list_shelf, name="list_shelf"),
    url(r"^shelfObject/list$", list_shelfobject, name="list_shelfobject"),
    url(r"^shelfObject/create$", ShelfObjectCreate.as_view(),
        name="shelfobject_create"),
    url(r"^shelfObject/delete/(?P<pk>\d+)$",
        ShelfObjectDelete.as_view(), name="shelfobject_delete"),
    url(r'^$', index, name='index'),
    url(r'^login$', auth_views.login, {
        'template_name': 'laboratory/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {
        'next_page': reverse_lazy('laboratory:index')}, name='logout')
]
