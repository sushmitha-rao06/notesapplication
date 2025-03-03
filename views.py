from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .db import NotesDB

database = NotesDB()

def render_signup_page(request):
    return render(request, 'signup.html')

def render_login_page(request):
    return render(request, 'login.html')

@csrf_exempt
def signup_user(request):
    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    password =  request.POST.get('password')

    print( firstName, lastName, email, password)

    response = database.create_user_in_db(firstName, lastName, email, password )
    if not response:
        return JsonResponse({
            "success" : False,
            "message" : f"Signup Got Failled,"
        })

    return JsonResponse({"success": True})

@csrf_exempt
def login_user(request):
    
    email = request.POST.get('email')
    password =  request.POST.get('password')

    print(email, password)

    response = database.validate_user( email, password )
    
    if len(response[1]) == 0:
        return JsonResponse({
            "success" : False,
            "message" : f"Login Got Failled, No Email got registered" 
        })


    #validate password
    password_from_db = response[1][0][4]

    if password != password_from_db :
        return JsonResponse({
            "success" : False,
            "message" : f"Login Got Failled, Wrong Password"
        })

    request.session['user_id'] = response[1][0][0]
    print(response[1][0][1])
    return JsonResponse({
        "success": True,
        "userId" : response[1][0][0]})

@csrf_exempt
def dashboard(request):
    user_id = request.GET.get('userId')
    # import pdb
    # pdb.set_trace()

    if not user_id :
       return HttpResponseRedirect('/login')
        

    data =  database.get_notes_of_user(user_id)
    print(data)
    context_data = {
        "data" : data
    }

    return  render(request, 'dashboard.html',{"data" : data})


@csrf_exempt
def savenotes(request):
    # UserId = request.session['user_id'] 
    notes = request.POST.get('textarea')
    UserId = request.POST.get('userId')


    response  = database.save_notes_of_user(UserId, notes)

    if  not response :
        return JsonResponse({
            "success" : False,
            "message" : f"Dashboard Failed Loading"
        })
    
    return JsonResponse({"success" : True })



@csrf_exempt
def delete_notes(request):
    id = request.POST.get('id')
    response =  database.delete_notes_of_user(id)
    if  not response :
        return JsonResponse({
            "success" : False,
            "message" : f"Failed to delete data"
        })
    
    return JsonResponse({"success" : True })
