from django.http import HttpResponse


# Create your views here.
def commodityView(request):
    return HttpResponse('Hello World')


def detailView(request, id):
    return HttpResponse('Hello World')
