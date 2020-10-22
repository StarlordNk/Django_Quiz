from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Question,Marks
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.  
    
def getQuestion(id):
    current=Question.objects.get(pk=id)
    id2=current.next
    try:
        next=Question.objects.get(pk=id2)
    except:
        next=None
    return current,next

def connector():
    q=Question.objects.all()
    temp=0
    for i in q:
        i.next=temp
        temp=i.id
        i.save()
    return temp
    
        
def checkAnswer(id,choice):
    score=0
    q,qu=getQuestion(id)
    if choice == q.option1  and q.op1:
        score +=1
    elif choice==q.option2 and q.op2:
        score +=1
    elif choice==q.option3 and q.op3:
        score +=1
    elif choice==q.option4 and q.op4:
        score +=1
    return score,qu

def quiz(request):
    if request.method=='POST':
        id = int(request.POST['id'])
        choice = request.POST['choice']
        score,ques=checkAnswer(id,choice)
        marks=Marks.objects.get(fk=request.user.id)
        marks.score +=score
        marks.save()
        if ques != None:
            return render(request , 'quiz.html' ,{'ques':ques})
        else:
            score='Score is '+str(marks.score)
            messages.info(request, score)
            return render(request , 'result.html', {'score' :score} )
    else:
        if request.user.is_active: 
            id=connector()  
            ques=Question.objects.get(pk=id)
            marks_all=Marks.objects.all()
            if Marks.objects.filter(fk=request.user.id):
                marks=Marks.objects.get(fk=request.user.id)
                marks.score=0
                marks.save()
                
            else:
                m=Marks.objects.create(fk=request.user.id,score=0)
            return render(request , 'quiz.html',{'ques': ques })
        else:
            messages.info(request,'Login First ')
            return render(request, 'login.html')



# Create your views here.
