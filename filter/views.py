from django.shortcuts import render
from .models import *
from django.db.models import Count

def main(request):
    # 전체 스택 
    stacks=Stack.objects.all()

    if request.method=="POST":
        selected_stack_ids=request.POST.getlist('stack')
        # 선택된 스택들 모두 불러옴 
        selected_stacks=Stack.objects.filter(id__in=selected_stack_ids)

        # 선택된 스택들이 정확히 일치하는 CodeQuest 객체 찾기
        # 배열에 있고, 개수가 일치하는지 확인 
        codequests=CodeQuest.objects.filter(stacks__in=selected_stacks).annotate(stack_count=Count('stacks')).filter(stack_count=len(selected_stacks))

        context={
            "selected_stacks": selected_stacks,
            "codequests": codequests,
            'stacks': stacks
        }
    else:
        context={
            'stacks': stacks
        }
    
    return render(request, 'main.html', context)