from django.urls import path
from home.views import bmi, bmiuserlist, bmiform, bmi_edit, bmi_delete

app_name = "home"

urlpatterns = [
    path('', bmi, name="bmi"),
    path('bmiuserlist/', bmiuserlist, name="bmiuserlist"),
    path('bmiform/', bmiform, name="bmiform"),
    path('bmi-edit/<int:id>/', bmi_edit, name="bmi_edit"),
    path('bmi-delete/<int:id>/', bmi_delete, name="bmi_delete"),
]