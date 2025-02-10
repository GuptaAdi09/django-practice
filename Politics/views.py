from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Parties,Candidate,Mumbai_Region
from  django.http import JsonResponse
from django.db.models import Q

# Create your views here.

def login_view():
    return HttpResponse("login required")



def parties(request):
    query_set = Parties.objects.all()
    
    return render(request,"parties.html",context={"query_set":query_set})

def list_the_party_candidate(request,id):
    party = Parties.objects.get(id=id)
    
    candidates = party.candidate_set.all()
    context = {
        'candidates': candidates,
        'party':party,
        
    }
    return render(request,'candidate.html',context)

@login_required()
def vote(request, PartyName, candidate_name):
    print("User:", request.user)  # Debugging
    print("Is Authenticated:", request.user.is_authenticated)
    if not request.user.is_authenticated:
        print("login required")


    obj = Candidate.objects.get(candidate_name__exact=candidate_name)

    if request.method == "POST":
        
        obj.total_vote += 1
        obj.save()

        messages.success(request, f"You have voted for {candidate_name}!")  # Show success message
        return redirect('politics:result', PartyName=PartyName, candidate_name=candidate_name)  # Redirect to result page
    
    return render(request, 'voting.html', {
        'PartyName': PartyName,
        'candidate_name': candidate_name,
        'obj': obj
    })

def search(request):
    if request.method == "POST":
        data = request.POST['data']
        try:
            region= get_object_or_404(Mumbai_Region,assembly_constitution_name__iexact=data)
            candidates = region.candidate_set.all()
            return render(request,'search.html',context={'candidates':candidates})
        except:
            messages.error(request, f"No assembly found with this name {data}")
            return redirect('politics:all_parties')
        
        
       
        
    return render(request,'search.html')

def result(request,PartyName,candidate_name):
    return HttpResponse("Successfully voted")
           
def search_candidate(request):
    query = request.GET.get("q","")
    if query:

        candidate = Candidate.objects.filter(candidate_name__icontains=query)[:10]
    results = [{"id":c.id, 
                "name":c.candidate_name,
                "age": c.candidate_age,
                "party_name": c.party_name.party_name,
                "votes": c.total_vote,
                "assembly_name" : c.from_which_assembly.assembly_constitution_name,
                } for c in candidate]
    return JsonResponse(results ,safe=False)

def search_page(request):
    return render(request, "real_search.html")