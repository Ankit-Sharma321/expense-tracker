from django.urls import path 
from .views import index, deleteTransaction, registration, login_page, logout_page 


urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('login/',login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('delete-transaction/<uuid>', deleteTransaction, name="deleteTransaction")
    # path('delete-transaction/<uuid:uuid>', deleteTransaction, name="deleteTransaction")

]