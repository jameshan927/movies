from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse
from django.views import generic
from .models import Question

from .forms import SubscriberForm
from django.contrib.auth.models import User

from django.views.generic.base import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SignUpView(TemplateView):
	template_name = 'signup.html'
	
def subscriber_new(request, template='signup.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # Create the User record
            user = User(username=name, email=email)
            user.set_password("password")
            user.save()
            # Create Subscriber Record
            # Process payment (via Stripe)
            # Auto login the user
            return HttpResponseRedirect('/success/')
    else:
        form = SubscriberForm()

    return render(request, template, {'form':form})
	
	
	
	

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'
	
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('movieapp:results', args=(question.id,)))
	
