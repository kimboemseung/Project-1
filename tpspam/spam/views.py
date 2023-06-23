from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import QuestionForm
from .models import Question

def answer_create(request, question_id):
    """
    spam 댓글 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('spam:detail', question_id=question.id)

def index(request):
    """
    전화번호 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request, 'spam/question_list.html', context)

def detail(request, question_id):
    """
    발신자 정보 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'spam/question_detail.html', context)

def question_create(request):
    """
    번호 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('spam:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'spam/question_form.html', context)