from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '23062217430',
        'name': 'Simforianus Jonathan Flonas Harefa',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)