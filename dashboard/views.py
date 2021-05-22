from django.shortcuts import render, redirect, HttpResponse
from .models import Trip, Gear, Message
from loginReg.models import User
from .forms import TripForm

# Create your views here.
def dashboard(request):
    all_gear = Gear.objects.all()
    all_trips = Trip.objects.all()
    form = TripForm()

    all_users = User.objects.exclude(fname__contains=request.session['name'])
    context = {
        'allgear': all_gear,
        'alltrips': all_trips,
        'allusers': all_users,
        'tripform': form,
    }
    return render(request, 'dashboard.html', context)

def addTrip(request):
    
    this_user = User.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        form = TripForm(request.POST)
        form.is_valid()
        
        userforms = request.POST.getlist('participants')
        participants = []

        for user in userforms:
            participants.append(user)

        new_trip = Trip.objects.create(
            name=request.POST['name'],
            creator=this_user,
            start_date=request.POST['startdate'],
            end_date=request.POST['enddate'],
        )
        for participant in participants:
            new_trip.participants.add(User.objects.get(id=int(participant)))
    return redirect('dashboard')

def viewTrip(request, tripid):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=tripid)
    all_users = User.objects.exclude(fname__contains=request.session['name'])
    if this_trip.creator.id == this_user.id:
        all_gear = Gear.objects.all()
        all_trip_users = this_trip.participants.all()

        context = {
            'this_user':this_user,
            'gear': all_gear,
            'tripusers': all_trip_users,
            'thistrip': this_trip,
            'allusers': all_users,
        }
        return render(request, 'edit_trip.html', context)
    else:
        all_gear = Gear.objects.all()
        all_trip_users = this_trip.participants.all()

        context = {
            'this_user':this_user,
            'gear': all_gear,
            'tripusers': all_trip_users,
            'thistrip': this_trip,
        }
        return render(request, 'view_trip.html', context)
    # return HttpResponse()

def editTrip(request, tripid):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=tripid)

    this_trip.name = request.POST['name']
    this_trip.participants = request.POST['participants']
    this_trip.start_date = request.POST['startdate']
    this_trip.end_date = request.POST['enddate']

    this_trip.save()
    return redirect('viewTrip')

def addGear(request):
    this_user = User.objects.get(id=request.session['user_id'])
