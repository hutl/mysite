from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import *

class IndexView(ListView):
    model = Question
    template_name = "index.html"
    context_object_name = 'questions'
    

class QuestionView(DetailView):
    model = Question
    template_name = "pergunta.html"
    
    def post(self, request, *args, **kwargs):
        question = self.get_object()
        choice_id = request.POST.get('choice')
        selected_choice = question.choice_set.get(pk=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
                
        return redirect('resultados', question.id)

 
class ResultsView(DetailView):
    model = Question
    template_name = "resultados.html"