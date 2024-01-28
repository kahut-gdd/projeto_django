from django.contrib import admin
from django.urls import path

from kahut.views import (
    KahutListView, 
    KahutCreateView, 
    KahutUpdateView, 
    KahutDeleteView,
    KahutCompleteView, 
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", KahutListView.as_view(), name="kahut_list"),
    path("create", KahutCreateView.as_view(), name="kahut_create"),
    path("update/<int:pk>", KahutUpdateView.as_view(), name="kahut_update"),
    path("delete/<int:pk>", KahutDeleteView.as_view(), name="kahut_delete"),
    path("complete/<int:pk>", KahutCompleteView.as_view(), name="kahut_complete"),
]
