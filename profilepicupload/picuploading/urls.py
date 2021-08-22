from django.urls import path
from . import views as v
urlpatterns=[
    path('',v.index,name="homepage"),
    path('edit/',v.editform,name="editformpage"),
    path('update/<int:id>',v.updatedata,name="updatepage"),
    path('delete/<int:id>',v.deletedata,name="deletepage"),
    path('regform/',v.registration,name="regformpage"),
    path('loginform/',v.loginfn,name="loginformpage"),
    path('logoutform/',v.logoutfn,name="logoutformpage"),
    path('adminpageform/',v.adminpage,name="adminpageformpage"),
    path('welcomeuserform/',v.welcomeuser,name="welcomeuserformpage"),
    path('uploadformpage/',v.uploadphoto,name="uploadformpage"),
    path('addproductpage/',v.addproduct,name="addproductpage"),
]
