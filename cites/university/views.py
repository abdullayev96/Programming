from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import Women, Category


menu = [{"title":"Programming", "url_name":"about"},
        {"title":"Add page", "url_name":"add_page"},
        {"title": "python tell our", "url_name":"contact"},
        {"title":"Back go","url_name": "login"},
]

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    ctx = {
        "posts":posts,
        "cats":cats,
        "menu":menu,
        "title":"Menu site",
        "cat_selected":0,

    }
    return render(request, 'home.html', ctx)



def about(request):
    return render(request, 'about.html', {"menu":menu, 'title':"About title"})


def addpage(request):
    return HttpResponse(f"Add page ")

def contact(request):
    return HttpResponse(f"Contact  page ")

def login(request):
    return HttpResponse(f"Login page ")


def pageNotFound(request, exception):   ###### Debug False bolganda ishlaydi
    return HttpResponseNotFound('<h3>Now  Not Found page but a long time : you must try again </h3>')

def show_post(request, post_id):
    return HttpResponse(f"Thera are only new post on site ={post_id}")

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    # if len(posts) == 0:
    #     raise Http404()
    ctx = {
        "posts": posts,
        "cats": cats,
        "menu": menu,
        "title": "Menu site",
        "cat_selected": cat_id,

    }
    return render(request, 'home.html', ctx)




# def home(request, chat_id):
#     if (request.POST):
#         print(request.POST)
#     return HttpResponse(f"Good sites={chat_id}")

#
# def archive(request, year):
#     if (int(year) > 2020):
#         return redirect('/')
#
#     return HttpResponse(f"<h1>History по годам</h1>{year}</p>")

#


#
# def create(request):
#     w= Women.objects.create(title='Yangi house oldik ', content= 'qachon kelasan dostim ')
#     w.save()
#     return w
#
#
# def filter(request, pk):
#     templatetags = Women.objects.filter(title='Django')
#
#
# def  get(request, pk):
#     templatetags = Women.objects.get(pk=pk)
#     templatetags.save()
#     return render(request, {"post":templatetags})
#
# def filter_by(request):
#     w=Women.objects.filter(pk__lte=4).order_by('title')
#
#
# def order_by(request):
#     o=Women.objects.order_by('title')
#     e=Women.objects.order_by('id')   #### - id bersak oxiradan tartiblab beradi


