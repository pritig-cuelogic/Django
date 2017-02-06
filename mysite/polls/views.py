from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext
from django.utils import translation

from .models import Question, Choice

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
	    'latest_question_list': latest_question_list,
	    'first_name': 'Priti',
	    'last_name': 'Gupta'
	}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',
		                            args=(question.id,)))

@login_required(login_url="login/")
def home(request):
	# Translators: This message appears on the home page only
	message2 = ugettext("Today is November 26.")
	lan = request.LANGUAGE_CODE
	return render(request, 
    	          'home.html',{'message2': message2,
    	                       'lan': lan,
    	             })
