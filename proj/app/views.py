
from django.http import HttpResponse
def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']

    text = f' host: {host},browser {user_agent},ip: {ip}'
    return HttpResponse(text, headers={'SecretCode':'12312123'})
def error(request):
    return HttpResponse('К сожалению произошла ошибка', status=400, reason='Incorrect data')

def user1(request,login='No login',Name='Noname',num=0):
    return HttpResponse(f'User: {login}, папка с именем {Name}, Номер поста {num}')
