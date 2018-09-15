from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Poll, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name='pollsapp/index.html'
    context_object_name='latest_poll_list'

    def get_queryset(self):
        return Poll.objects.all()[:5]

class DetailView(generic.DetailView):
    model=Poll
    template_name='pollsapp/detail.html'

class ResultView(generic.DetailView):
    model=Poll
    template_name='pollsapp/results.html'

def vote(request, poll_id):
    p=get_object_or_404(Poll, pk=poll_id)
    try:
        select_choice= p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'pollsapp/detail.html', {'poll': p, 'error_msg':'You didnt select'})

    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))



