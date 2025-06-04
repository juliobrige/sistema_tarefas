from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa, Categoria
from datetime import datetime

def lista_tarefas(request):
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        prioridade = request.POST.get("prioridade")
        cat_id = request.POST.get("categoria")
        data = request.POST.get("agendada_para")

        categoria = Categoria.objects.get(id=cat_id) if cat_id else None
        agendada_para = datetime.strptime(data, "%Y-%m-%d") if data else None

        Tarefa.objects.create(
            descricao=descricao,
            prioridade=prioridade,
            categoria=categoria,
            agendada_para=agendada_para
        )
        return redirect('lista_tarefas')
    q = request.GET.get("q")
    tarefas = Tarefa.objects.all()
    if q:
        tarefas = tarefas.filter(descricao__icontains=q)


    tarefas = Tarefa.objects.all().order_by('-id')
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/lista.html', {
        'tarefas': tarefas,
        'categorias': categorias
    })

def concluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')


def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        tarefa.descricao = request.POST.get("descricao")
        tarefa.prioridade = request.POST.get("prioridade")
        cat_id = request.POST.get("categoria")
        data = request.POST.get("agendada_para")

        tarefa.categoria = Categoria.objects.get(id=cat_id) if cat_id else None
        tarefa.agendada_para = datetime.strptime(data, "%Y-%m-%d") if data else None
        tarefa.save()
        return redirect('lista_tarefas')

    return render(request, 'tarefas/editar.html', {
        'tarefa': tarefa,
        'categorias': categorias
    })

def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == "POST":
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'tarefas/confirmar_exclusao.html', {'tarefa': tarefa})

