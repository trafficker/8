from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import os


def callother(request):
    app = request.GET.get('app')
    if app == 'calc':
        os.system( 'open /applications/calculator.app')  # 这里可以运行你自己的python程序，需要提供一个借口 return render(request,'callotherapp/callother.html',{'text':'ran calc s
        return render(request, 'callotherapp/callother.html', {'text': 'ran  calc successful'})

