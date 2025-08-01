from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils import timezone
from .models import NGO, Event
from .forms import NGOForm, EventForm, EventFilterForm

# Create your views here.
def event_list(request):
    events = Event.objects.all().select_related('ngo')
    form = EventFilterForm(request.GET)
    
   
    if form.is_valid():
        city = form.cleaned_data.get('city')
        state = form.cleaned_data.get('state')
        
        if city:
            events = events.filter(city__icontains=city)
        if state:
            events = events.filter(state__icontains=state)

# Page.
    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cities = Event.objects.values_list('city', flat=True).distinct()
    states = Event.objects.values_list('state', flat=True).distinct()
    
    context = {
        'page_obj': page_obj,
        'form': form,
        'cities': cities,
        'states': states,
        'total_events': events.count(),
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

# Admin Views
@staff_member_required
def admin_dashboard(request):
    total_ngos = NGO.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date_time__gte=timezone.now()).count()
    recent_events = Event.objects.select_related('ngo')[:5]
    
    context = {
        'total_ngos': total_ngos,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'recent_events': recent_events,
    }
    return render(request, 'admin/dashboard.html', context)

@staff_member_required
def ngo_create(request):
    if request.method == 'POST':
        form = NGOForm(request.POST)
        if form.is_valid():
            ngo = form.save()
            messages.success(request, f'NGO "{ngo.name}" created successfully!')
            return redirect('admin_dashboard')
    else:
        form = NGOForm()
    
    return render(request, 'events/ngo_form.html', {
        'form': form,
        'title': 'Register New NGO'
    })

@staff_member_required
def ngo_edit(request, pk):
    ngo = get_object_or_404(NGO, pk=pk)
    if request.method == 'POST':
        form = NGOForm(request.POST, instance=ngo)
        if form.is_valid():
            form.save()
            messages.success(request, f'NGO "{ngo.name}" updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = NGOForm(instance=ngo)
    
    return render(request, 'events/ngo_form.html', {
        'form': form,
        'title': f'Edit {ngo.name}',
        'ngo': ngo
    })

@staff_member_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, f'Event "{event.title}" created successfully!')
            return redirect('admin_dashboard')
    else:
        form = EventForm()
    
    return render(request, 'events/event_form.html', {
        'form': form,
        'title': 'Create New Event'
    })

@staff_member_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, f'Event "{event.title}" updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'events/event_form.html', {
        'form': form,
        'title': f'Edit {event.title}',
        'event': event
    })

@staff_member_required
def ngo_list(request):
    ngos = NGO.objects.all()
    return render(request, 'events/ngo_list.html', {'ngos': ngos})

@staff_member_required
def event_list_admin(request):
    events = Event.objects.select_related('ngo').all()
    return render(request, 'events/event_list_admin.html', {'events': events})
