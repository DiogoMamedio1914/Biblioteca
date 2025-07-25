from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Livro, Cidade, Autor, Editora, Leitor, Genero


class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'index.html', {'livros': livros})

class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})

class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})

class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})

class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})



class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = get_object_or_404(Livro, id=id)
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('livros')
