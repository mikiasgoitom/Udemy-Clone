from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Task
from .forms import EventForm, TaskForm

def calendar_view(request):
    events = Event.objects.all()
    tasks = Task.objects.all()
    return render(request, 'calendar/calendar.html', {'events': events, 'tasks': tasks})

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

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'calendar/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = TaskForm()
    return render(request, 'calendar/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = TaskForm(instance=task)
    return render(request, 'calendar/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('calendar_view')
