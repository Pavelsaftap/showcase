from django.http import HttpResponse


def main(request):
    return HttpResponse("main")


def authorization(request):
    return HttpResponse('Authorization')


def search(request):
    return HttpResponse("Search")


