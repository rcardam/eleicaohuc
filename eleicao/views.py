from django.shortcuts import render
from eleicao.models import Votacao
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from eleicao.forms import LoginForm


def home(request):
  template_name = 'index.html'
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cpf = request.POST.get('cpf')
      eleitor = Votacao.objects.filter(cpf=cpf).first()
      cont = { 'ctcpf': cpf}
      if eleitor:
        votos = {'C1','br','nu'}
        if  (eleitor.voto not in votos):
          request.session['sscpf'] = cpf
          context = {
            'eleitor':eleitor
          }
          return render(request,'confirma.html', context)
        else:
          messages.error(request,'Já existe voto para este CPF !')
          return HttpResponseRedirect(reverse('home'), cont)
      else:
        messages.error(request,'CPF não localizado. Tente novamente')
        return HttpResponseRedirect(reverse('home'), cont)
  elif request.method == 'GET':
    form = LoginForm()
    return render(request, template_name, {'form': form})
    

def confirma(request, cpf):
  if request.session.get('sscpf') is not None:
    template_name = 'confirma.html'
    eleitor = Votacao.objects.get(cpf=cpf)
    context = {'eleitor':eleitor}
    return render(request, template_name, context)
  else:
    messages.success(request,'Eleitor não identificado.')
    return HttpResponseRedirect(reverse('home'), {'eleitor':eleitor})
 
def votacao(request):
  template_name = 'votacao.html'
  if request.session.get('sscpf') is not None:
      cpf = request.session.get('sscpf') 
      if request.method == 'GET':
        eleitor = Votacao.objects.filter(cpf=cpf).first()
        if eleitor:
          context = {
            'eleitor':eleitor
          }
        return render(request, template_name, context)
      elif request.method == 'POST':
        template_name = 'confirmavoto.html'
        eleitor = Votacao.objects.filter(cpf=cpf).first()
        eleitor.voto = request.POST.get('voto')
       # print(f"POST-VOTACAO-Voto: {eleitor.voto}")
        #eleitor.save()
        #eleitor = Votacao.objects.filter(cpf=cpf).first()
        context = {'eleitor': eleitor}
        #print(f"{eleitor.cpf} - {eleitor.nome} - {eleitor.voto}")
        #messages.success(request,'Votação realizada com sucesso')
        #return HttpResponseRedirect(reverse('home'), {'eleitor':eleitor})
        return render(request, 'confirmavoto.html', context)
  else:
    messages.success(request,'Eleitor não identificado.')
    return HttpResponseRedirect(reverse('home'), {'eleitor':eleitor})

def confirmavoto(request, cpf):
  template_name = 'confirmavoto.html'
  if request.session.get('sscpf') is not None:
    voto = request.POST.get('voto')
   # print(f"CONFIRMA-Voto-FORM: {voto}")
    request.session['voto'] = voto
    eleitor = Votacao.objects.get(cpf=cpf)
    eleitor.voto = voto
    context = {'eleitor':eleitor}
    return render(request, template_name, context)
  else:
    messages.success(request,'Eleitor não identificado.')
    return HttpResponseRedirect(reverse('home'), {'eleitor':eleitor})



def final(request):
  template_name = 'final.html'
  if request.session.get('sscpf') is not None:
    cpf = request.session.get('sscpf')
    #print(f"FINAL-CPF-Session: {cpf}")
    eleitor = Votacao.objects.filter(cpf=cpf).first()
    if eleitor:
      eleitor.voto = request.session.get('voto')
     # print(f"FINAL-Voto-Session: {eleitor.voto}")
      eleitor.save()
      request.session['voto'] = ''
      request.session['cpf'] = ''   
      return render(request, template_name) 
  else:
    messages.success(request,'Eleitor não identificado.')
    return HttpResponseRedirect(reverse('home'), {'eleitor':eleitor})
      
  

# Create your views here.
