from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage

from django.shortcuts import render_to_response

# Create your views here.
def search(request):
  query = request.GET['q', '']
  # results = FlatPage.objects.filter(content__icontains=query)
  # template = loader.get_template('search/search.html')
  # context = Context({ 'query': query, 'results': results })
  # response = template.render(context)
  # return HttpResponse(response)
  keyword_results = results = []
  if query:
    keyword_results = FlatPage.objects.filter(
        searchkeyword_keyword_in=query.split()).dsitinct()
    results= FlatPage.objects.filter(content__icontains=query)
  return render_to_response('search/search.html',
      { 'query': query,
        'keyword_results': keyword_results,
        'results': results })
