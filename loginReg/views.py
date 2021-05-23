from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from dashboard.models import Gear, Trip
from dashboard.forms import GearForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request): 
    if request.method == "POST": 
        errors = User.objects.validator(request.POST) 
        if len(errors) != 0: 
            for key, value in errors.items(): 
                messages.error(request, value) 
            return redirect('/') 
        else: 
            new_user = User.objects.register(request.POST)
            new_user.fname = new_user.fname.title()
            request.session['user_id'] = new_user.id
            request.session['name'] = new_user.fname
            # form = RegisterForm(request.POST)
            # print(form.is_valid())
            # print(form.errors)
            # UNCOMMENT BELOW and CHANGE FOR EXAM
        return redirect('/dashboard')


def login(request): 
    if request.method == "GET":
        return render(request, "index.html")
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')

    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id 
    request.session['name'] = user.fname
    # UNCOMMENT BELOW and CHANGE FOR EXAM
    # return redirect('/quotes') 
    return redirect('/dashboard')

def logout(request): 
    request.session.flush() 
    return redirect('/')

def profile(request, id):
    this_user = User.objects.get(id=request.session['user_id'])
    created_trips = Trip.objects.filter(creator=this_user)
    my_gear = Gear.objects.filter(owner=this_user)
    form = GearForm()
    context = {
        'user': this_user,
        'mytrips': this_user.trips.all(),
        'created_trips': created_trips,
        'mygear': my_gear,
        'gform': form,
    }
    return render(request, "profile.html", context)

def myGear(request, id):
    this_user = User.objects.get(id=request.session['user_id'])
    form = GearForm()
    my_gear = Gear.objects.filter(owner=this_user)

    if request.method == "POST":
        form = GearForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = this_user
            obj.save()


        # new_gear = Gear.objects.create(
        #     name = request.POST['name'],
        #     category = request.POST['category'],
        #     link = request.POST['link'],
        #     photo = uploaded_file_url,
        #     owner = this_user,
        # )
        return redirect(f'/myAccount/{this_user.id}/myGear')


    if request.method == "GET":
        context = {
            'this_user': this_user,
            'gearform': form,
            'mygear': my_gear,
        }

        return render(request, "gear.html", context)
    
