from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Experiment, Question, User

from django.utils import timezone

# Create your views here.
def index(request):
    user_id = request.session.get("user")
    if user_id is None:
        user_id = User.objects.create().id
    request.session["user"] = user_id
    template = loader.get_template('polls/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def test(request):
    if request.method == "POST":
        time = request.POST.get('time')
        request.session["time"] = time
    else:
        button_exit = False
        user__id = User.objects.get(id=request.session["user"])
        exp = Experiment.objects.filter(user_id=user__id)
        count = exp.count()
        if count >= 5:
            button_exit=True
        if count >=10:
            request.session['exit']=True
            return redirect('exit')
        question = Question.random_question(Question, exp)
        request.session["question"]=question.id_q
        request.session['time_start'] = (timezone.now() - timezone.datetime(1900, 1, 1, tzinfo=timezone.utc)).seconds
        return render(request, 'polls/test.html', {'question': question, 'button_exit':button_exit, 'count':count+1})

def answer(request):
    if request.method == "POST":
        time_diff = request.session['time_start']
        ans_text = request.POST.get('answer')
        if (ans_text == ""):
            ans_text = "Null"
        ad_ans = request.POST.get('adeq')
        uid = request.session["user"]
        qid = request.session["question"]
        ans = Experiment.objects.create(
            user_id=User.objects.get(id=uid),
            question_id=Question.objects.get(id_q=qid),
            answer=ans_text,
            adequacy = ad_ans,
            time_start = time_diff
        )
        ans.save()
        return redirect('test')
    else:
        template = loader.get_template('polls/answer.html')
        context = RequestContext(request)
        # (timezone.datetime(1900, 1, 1) - timezone.now()).seconds
        request.session['time_start'] = (timezone.now() - timezone.datetime(1900, 1, 1, tzinfo=timezone.utc)).seconds - request.session[
            'time_start']
        return render(request, 'polls/answer.html')

def exit(request):
    return render(request, 'polls/exit.html')