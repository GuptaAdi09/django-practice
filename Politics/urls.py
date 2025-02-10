from django.urls import path
from .views import parties,list_the_party_candidate,vote,search,result,login_view,search_candidate,search_page

app_name = "politics"
urlpatterns = [
    path('login/',login_view,name='login'),
    path('search/',search,name='searched'),
    
    path('',parties,name="all_parties"),
    path('<int:id>/',list_the_party_candidate,name="parties_candidate"),
    path('<str:PartyName>/<str:candidate_name>/vote/',vote,name='vote'),
    path('<str:PartyName>/<str:candidate_name>/result/',result,name='result'),
    
    path("search_page/", search_page, name='search_page'),
    path('search_candidate/',search_candidate, name='search_candidate'),
    
    

    
]