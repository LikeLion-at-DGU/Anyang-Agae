from django.urls import path
import diary.views

app_name = "diary"

urlpatterns = [
    path('', diary.views.calendar_view, name="calendar"),
    path('<int:event_id>/', diary.views.detail, name="detail"),
    path('delete/<int:event_id>/', diary.views.delete, name="delete"),
    path('new/', diary.views.event_create, name="new"),
    path('edit/<int:event_id>/', diary.views.event_edit, name="edit"),
]
