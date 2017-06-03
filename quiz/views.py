from django.shortcuts import render
from .models import Questions

# Create your views here.
def home(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,
        'quiz/home.html',
        {'choices':choices})

def questions(request , choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    return render(request,
        'quiz/questions.html',
        {'ques':ques})

def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        eff = (score/total)*100
    return render(request,
        'quiz/result.html',
        {'score':score,
        'eff':eff,
        'total':total})
def about(request):
    return render(request,
        'quiz/about.html')

def contact(request):
    return render(request,
        'quiz/contact.html')




#
#
#
#
#
#
#
