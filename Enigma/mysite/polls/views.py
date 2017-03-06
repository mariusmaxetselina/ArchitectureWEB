from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Choice, Question

from django.template import loader

from django.http import Http404

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
   # return render(request, 'polls/detail.html', {'question': question})
    #question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
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

class LoginView(TemplateView):

  template_name = 'front/index.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name)


class LogoutView(TemplateView):

  template_name = 'front/index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)


def connexion(request):
    if request.method == 'POST':
        formLogin = loginForm(request.POST)
        if formLogin.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect(deconnexion)
            else:
                messages.add_message(request, messages.ERROR, "Erreur de mot de passe ou de nom d'utilisateur")
                return redirect(index)
    else:
        formLogin = loginForm()
    formRegister = registerForm()
    return render(request, 'polls/index.html', {'formRegister': formRegister, 'formLogin': formLogin})

def deconnexion(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Vous avez été correctement deconnecté! A bientôt ! ")
        return redirect(index)
    else:
        if not request.user.is_authenticated:
            return redirect(connexion)
        else:
            return render(request, 'polls/index.html')

def mdp_oublie(request):
    if request.method == 'POST':
        formMdp = mdpForm(request.POST)
        if formMdp.is_valid():
            username_u = request.POST['username']
            email_u = request.POST['email']
            try:
                user = User.objects.get(username=username_u, email=email_u)
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, "Erreur de nom d'utilisateur ou de l'adresse email")
                return redirect(index)
            nouveaumotdepasse=''
            for i in range(10):
                nouveaumotdepasse += random.choice("abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            user.set_password(nouveaumotdepasse)
            user.save()
            send_mail(
                'texte',
                'A la suite de votre demande, votre mot de passe a été changé. Utilisez désormais '+ nouveaumotdepasse ,
                settings.EMAIL_HOST_USER,
                [email_u], fail_silently=False
            )
        else:
            messages.add_message(request, messages.ERROR, "Erreur de nom d'utilisateur ou de l'adresse email")
            return redirect(index)
    messages.success(request, "Votre nouveau mot de passe vous a correctement été envoyé. Vérifiez votre adresse mail!")
    return redirect(index)





















































    