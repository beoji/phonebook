from django.urls import path
from .views import PersonListView, PersonCreateView, person_update, PersonDeleteView

urlpatterns = [
    path('', PersonListView.as_view(), name='person-list'),
    path('person-create', PersonCreateView.as_view(), name='person-create'),
    path('person-update/<int:pk>', person_update, name='person-update-function'),
    path('person-delete/<int:pk>', PersonDeleteView.as_view(), name='person-delete-function'),
]
