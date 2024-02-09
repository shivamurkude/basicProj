from django.urls import path
from .views import SubmitForm, GetUser

urlpatterns = [
    path('submit-form/', SubmitForm.as_view(), name='submit_form'),
    path('user/<int:user_id>/', GetUser.as_view(), name='get_user'),
]
