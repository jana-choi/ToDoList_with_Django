from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse("my_to_do_app first page")
    todos = Todo.objects.all()
    contents = {"todos": todos}
    return render(request, "my_to_do_app/index.html", contents)

def createTodo(request):
    # return HttpResponse("create Todo를 할거야!")
    user_input_str = request.POST["todoContent"]
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse("index"))
    # return HttpResponse("create Todo를 할거야! => " + user_input_str)

def deleteTodo(request):
    done_todo_id = request.GET["todoNum"]
    # print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse("index"))