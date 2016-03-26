#!-*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Question, Choice
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # generic.DetailView는 url에 pk값이 반드시 포함되어 전달되야 한다.
    # <app name>/<model name>_detail.html 형태로 사용 한다.
    # 자동으로 Question 변수들을 가져 한다.

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Question object을 가져오거나 못가져오면 404 error 발생
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # Choice 모델에서 question에 forign key로 연동된 choice 데이타를 iterator object로 넘겨줌, iterator는 리스트, 딕셔너리등을 포함하며 {1,2,3} 데이타를 왼쪽부터 차례대로 넘겨주는 objec
        # request.POST['choice']는 details.html에서 name이 choice인 항목에서 value="{{ choice.id }}" 을 string 형태로 넘겨줌
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

