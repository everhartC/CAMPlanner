from django.shortcuts import render, redirect, HttpResponse
from .models import Trip, Gear, Message
from loginReg.models import User
from .forms import MessageForm, TripForm

# Create your views here.
def dashboard(request):
    this_user = User.objects.get(id=request.session['user_id'])
    all_gear = Gear.objects.all()
    participated_trips = this_user.trips.all()
    created_trips = this_user.created_trips.all()
    my_trips = participated_trips.union(created_trips)
    form = TripForm()
    all_msgs = Message.objects.all().order_by('created_at')[:5:1]
    
    all_users = User.objects.exclude(fname__contains=request.session['name'])
    context = {
        'allgear': all_gear,
        'mytrips': my_trips,
        'allusers': all_users,
        'tripform': form,
        'allmsgs': all_msgs,
        'this_user': this_user,
        'created_trips': created_trips,
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
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
        )
        for participant in participants:
            new_trip.participants.add(User.objects.get(id=int(participant)))
    return redirect('dashboard')

def viewTrip(request, tripid):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=tripid)
    all_users = User.objects.exclude(fname__contains=request.session['name'])
    all_msgs = Message.objects.filter(trip=this_trip)
    if this_trip.creator.id == this_user.id:
        all_gear = Gear.objects.all()
        all_trip_users = this_trip.participants.all()

        context = {
            'this_user':this_user,
            'gear': all_gear,
            'tripusers': all_trip_users,
            'thistrip': this_trip,
            'allusers': all_users,
            'allmsgs': all_msgs,
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
            'all_msgs': all_msgs,

        }
        return render(request, 'view_trip.html', context)
    # return HttpResponse()

def editTrip(request, tripid):
    this_user = User.objects.get(id=request.session['user_id'])
    this_trip = Trip.objects.get(id=tripid)

    this_trip.name = request.POST['name']
    this_trip.creator = this_user
    this_trip.participants = request.POST['participants']
    this_trip.start_date = request.POST['startdate']
    this_trip.end_date = request.POST['enddate']

    this_trip.save()
    return redirect(f'/dashboard/trip/{tripid}')

def addMsg(request, tripid):
    this_trip = Trip.objects.get(id=tripid)
    this_user = User.objects.get(id=request.session['user_id'])
    # form = MessageForm()
    if request.method == "POST":
    #     new_msg = Message.objects.create(
    #         msg = request.POST['msg'],
    #         user_who_posted = this_user,
    #         trip = this_trip,
    #     )
        form = MessageForm(request.POST)
        if form.is_valid():
            new_msg = form.save(commit=False)
            new_msg.user_who_posted = this_user
            new_msg.trip = this_trip
            new_msg.save()
        else:
            print(form.errors)

        return redirect(f'/dashboard/trip/{tripid}')

def deleteMsg(request, uid, msgid):
    this_user = User.objects.get(id=uid)
    if request.session['user_id'] is not this_user.id:
        return redirect('/')
    
    this_msg = Message.objects.get(id=msgid)
    this_msg.delete()
    return redirect('dashboard')
    
