from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'calendar/calendar.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'calendar/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = EventForm()
    return render(request, 'calendar/event_form.html', {'form': form})

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = EventForm(instance=event)
    return render(request, 'calendar/event_form.html', {'form': form})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('calendar_view')
