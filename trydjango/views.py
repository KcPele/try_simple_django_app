from django.http import HttpResponse
import random 
from articles.models import Article
from django.template.loader import render_to_string





def home_view(request):

    number = random.randint(1,4)
    article_obj = Article.objects.get(id=number)
    article_query = Article.objects.all()
    context = {
        "object_list": article_query,
        "id": article_obj.id,
        "title":article_obj.title,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string('home-view.html', context)
    
    return HttpResponse(HTML_STRING)

