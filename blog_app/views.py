from django.shortcuts import render


# Create your views here.
def post_list(request):
    return render(request, "board.html")


def post_page(request):
    return render(request, "post.html")
