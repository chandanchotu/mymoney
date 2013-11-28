
from django.shortcuts import render_to_response
from django.template import RequestContext
# create your views here


from django.shortcuts import redirect


def home(request):
    
    if request.user.is_authenticated():



        user_obj = request.user
        username = user_obj.username
        
        return render_to_response('user/home.html', {'username':'username'}, context_instance=RequestContext(request))
    else:
        return redirect('/accounts/login/')



