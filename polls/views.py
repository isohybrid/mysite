from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from polls.models import Poll, Choice

# Create your views here.
def index(request):
  latest_poll_list = Poll.objects.order_by('pub_date')[:5]
  template = loader.get_template('polls/index.html')
  content = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
  return HttpResponse(template.render(context))

def detail(request, poll_id):
  return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
  return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, ChoiceNotExist):
    return render(request, 'polls/detail.html', {
      'poll':p,
      'error_message': "You didn't select a choice.",
      })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data being posted twicec if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
