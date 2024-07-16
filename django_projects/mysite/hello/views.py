# Create your views here.
from django.http import HttpResponse

# Create your views here.

# https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)

# https://www.youtube.com/watch?v=Ye8mB6VsUHw

def myview(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits)+" <!-- 488fbc61 -->")
    resp.set_cookie('dj4e_cookie', '488fbc61', max_age=1000)
    return resp