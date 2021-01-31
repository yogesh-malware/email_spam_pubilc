from django.shortcuts import render
from .spammer import GMAIL


def index(request):
    return render(request,'index.html')


def result(request):
    email = str(request.POST.get('email'))
    body = str(request.POST.get('body'))
    count = int(request.POST.get('count')[0])
    print(
        f'''
            {email}
            {body}
            {count}
        '''
    )
    GMAIL(
    receiver=str(email),
    body=str(body),
    count=count).send()
    return render(request,'success.html')