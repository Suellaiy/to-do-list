from django.shortcuts import render, redirect

from schedule.models import Schedule


def create_or_show_schedule(request):
    if request.method == 'POST':
        pass

    posts = Schedule.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'to-do-list.html', context)


def do_check(request, pk):
    schedule = Schedule.objects.get(pk=pk)

    if schedule.complete_schedule == True:
        schedule.complete_schedule=False
    else:
        schedule.complete_schedule=True

    schedule.save()
    return redirect('index')


def schedule_create(request):
    if request.method == 'POST':
        context = request.POST['context']
        date_time = request.POST['date_time']
        Schedule.objects.create(context=context, date_time=date_time)

    return redirect('index')
