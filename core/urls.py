from django.urls import path
from .views import Home, Add_Stud, Delete_Student, Update_Stud

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('Add_Stud/', Add_Stud.as_view(), name='Add_Stud'),
    path('Delete_Stud', Delete_Student.as_view(), name='Delete_Stud'),
    path('Update_Student/<int:id>/', Update_Stud.as_view(), name='Update_Student')
]
