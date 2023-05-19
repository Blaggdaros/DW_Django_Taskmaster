# from django.db.models import Q
from django.shortcuts import redirect, render

from tasks import forms
from tasks.models import Subject, Task


def homepage(request):
    tasks = Task.objects.all().order_by("-created")[0:4]
    return render(
        request,
        "tasks/homepage.html",
        {
            "title": "TaskMaster homepage",
            "tasks": tasks,
        },
    )


LISTA_TAREAS = [
    {"id": 1, "title": "Aprender Python", "urgent": True},
    {"id": 2, "title": "Aprender Django", "urgent": True},
    {"id": 3, "title": "Comprar melocotones", "urgent": False},
]


def list_tasks(request):
    tasks = Task.objects.all()
    return render(
        request,
        "tasks/list_tasks.html",
        {
            "title": "Tareas activas",
            "tasks": tasks,
        },
    )


def list_subjects(request):
    subjects = Subject.objects.all()
    return render(
        request,
        "tasks/list_subjects.html",
        {
            "title": "Temas",
            "subjects": subjects,
        },
    )


def subject_detail(request, pk):
    subject = Subject.objects.get(pk=pk)
    # tasks = [t for t in Task.objects.all() if t.subject_id == pk]
    return render(
        request,
        "tasks/subject_detail.html",
        {
            "title": f"Tema {subject.name}",
            "subject": subject,
            # "tasks": tasks,
        },
    )


def search(request):
    tasks = []
    query = ""
    if request.method == "POST":
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            tasks = Task.objects.filter(title__icontains=query)
            priority = form.cleaned_data.get("priority") or []
            if priority:
                tasks = tasks.filter(priority__in=priority)
            urgent = form.cleaned_data.get("urgent", False)
            if urgent:
                tasks = tasks.filter(urgent=True)
    else:
        form = forms.SearchForm()

    return render(
        request,
        "tasks/search.html",
        {
            "title": "Buscar tareas",
            "form": form,
            "tasks": tasks,
            "query": query,
        },
    )


def list_tasks_per_year(request, year):
    tasks = Task.objects.filter(created__year=year)
    return render(
        request,
        "tasks/list_tasks.html",
        {
            "title": f"Tareas creadas en el año {year}",
            "tasks": tasks,
        },
    )


def lab_view(request):
    return render(request, "tasks/lab.html", {"title": "Labs page,"})


def list_by_priority(request, priority):
    priority = priority[0].upper()
    tasks = Task.objects.filter(priority=priority)
    return render(
        request,
        "tasks/list_tasks.html",
        {
            "title": f"Tareas de prioridad {priority}",
            "tasks": tasks,
        },
    )


def create_task(request):
    if request.method == "POST":
        form = forms.CreateTaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect("/")
    else:
        form = forms.CreateTaskForm()
    return render(
        request,
        "tasks/create_task.html",
        {
            "title": "Nueva Tarea",
            "form": form,
        },
    )


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect("/")
    else:
        form = forms.EditTaskForm(instance=task)
    return render(
        request,
        "tasks/edit_task.html",
        {
            "title": f"Editar tarea #{task.pk}",
            "form": form,
        },
    )

    # ModelA.objects.filter(num__gt=23)  # num > 23
    # ModelA.objects.filter(num__gt=23)  # num >= 23
    # ModelA.objects.filter(num__gt=23)  # num <= 23
    # ModelA.objects.filter(num__gt=23)  # num <= 23
    # ModelA.objects.exclude(num=23)  # num != 23

    # hoy = datetime...
    # ModelA.objects.exclude(fecha=hoy)
    # ModelA.objects.exclude(fecha__gt=hoy)
    # ModelA.objects.exclude(fecha__year=2023)
    # ModelA.objects.exclude(fecha__year__gte=2023)
    # ModelA.objects.exclude(fecha__month=2)
    # ModelA.objects.exclude(fecha__month__gte=10)
    # ModelA.objects.exclude(fecha__year=2023).filter(fecha__month=2)

    # txt = str()
    # ModelA.objects.filter(texto=txt)
    # ModelA.objects.filter(texto__gt=txt)
    # ModelA.objects.filter(texto__contains=txt)
    # ModelA.objects.filter(texto__icontains=txt)
    # ModelA.objects.filter(texto__startwith=txt)
    # ModelA.objects.filter(texto__istartwith=txt)

    # task = Task.objects.filter(priority="L").filter(priority="n")
    # task = Task.objects.exclude(priority="h")
    # task = Task.objects.filter(priority__in=['l', 'n'])

    # task = Task.objects.filter(subject__name="core")
