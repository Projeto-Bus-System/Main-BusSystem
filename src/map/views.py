from django.shortcuts import render

# Create your views here.
def render_map(request):
    context = dict()
    context['cor'] = 'Azul'
    return render(request,'map.html',context)