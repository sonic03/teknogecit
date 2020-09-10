from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponse
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.models import Permission,User,Group
from articles.models import Articles,Comments,Category,Visit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.text import slugify
# Create your views here.

def index(request):

    articles=Articles.objects.all()

    for article in articles:
        comments=article.comments.all()

        cc=comments.count()
        
        print(cc)


    return render(request,"index.html",{"articles":articles})

def hakkimizda(request):
    


    return render(request,"hakkimizda.html")


@permission_required("articles.delete_articles",raise_exception=False)
@login_required(login_url="user:login")
def dashboard(request):

    articles=Articles.objects.filter(author=request.user)
    

    
    

    context={
        "articles":articles,
        
        
    }
    return render(request,"dashboard.html",context)
@login_required
def addArticle(request):

    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author=request.user
        article.slug=slugify(article.title.replace("'"," "))
        article.save()

        messages.success(request,"Makale ekleme başarılı")
        return redirect("index")

   
 
    return render(request,"addarticle.html",{"form":form})



def addCategory(request):

    category=Category.objects.all()

    if request.method=="POST":
        
        catname = request.POST.get("catname")

        newCategory=Category(name=catname)
        

        newCategory.save()
        messages.success(request,"Eklendi")
        return render(request,"dashboard.html")

    
    return render(request,"addcategory.html",{"category":category})

    


def details(request,slug):
    #article=Articles.objects.filter(id=id).first()
    
    
    
    ip_address=request.META.get('REMOTE_ADDR', '')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip_address)
    print(ip)
    print("**********")


    article=get_object_or_404(Articles,slug=slug)
    similar=Articles.objects.filter(category=article.category).order_by("-add_date")
    paginator = Paginator(similar, per_page=4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    comments=article.comments.all()
    like=article.likes.all().count()
    response = render(request, 'detail.html')
    visits =  request.session.get('visits','0') 
    if request.session.get('visits'):

        
        request.session['visits'] = visits + 1
    
    
        

    print(visits)
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    if num_visits > 1:
        num_visits=1
    



    
    
    return render(request,"detail.html",{"article":article,"comments":comments,'similar': page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number),"like":like,'num_visits':num_visits,"visits":visits})










@login_required
def updateArticle(request,id):

    article=get_object_or_404(Articles,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author=request.user
        article.save()

        messages.success(request,"Makale güncelleme başarılı")
     
        return redirect("index")

    return render(request,"update.html",{"form":form})

@permission_required("articles.delete_articles")
@login_required
def deleteArticle(request,id):
    article=get_object_or_404(Articles,id=id)
    article.delete()
     
    messages.success(request,"Makale silme başarılı")
     
    return redirect("articles:dashboard")




def makaleler(request):
    
    cate=Category.objects.all()
    keyword = request.GET.get("keyword")
    category=request.GET.get("category")
    if keyword and category:
        articles = Articles.objects.filter(title__contains=keyword,category__name=category)
        return render(request,"makaleler.html",{"articles":articles,"cate":cate})

    
    articles=Articles.objects.all().order_by("author")
    

   
    return render(request,"makaleler.html",{"articles":articles,"cate":cate})


    



def green(request):


    articles=Articles.objects.filter(category = "green")
    paginator = Paginator(articles, per_page=4)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

   
    return render(request,"green.html",{'articles': page_obj.object_list,
            'paginator': paginator,
            'page_number': int(page_number)})

def addcomment(request,id):
    
    article=get_object_or_404(Articles,id=id)

    if request.method=="POST":
        
        commet_content=request.POST.get("commet_content")

        newComment=Comments(commet_content=commet_content)
        newComment.article=article
        newComment.commet_author=request.user

        newComment.save()

    return redirect(reverse("articles:detail",kwargs={"id":id}))


def visitor(request,slug):
    article=get_object_or_404(Articles,slug=slug)
    if  Visit.objects.filter(
                    article=article,
                    session=request.session.session_key):


                    view = Visit(article=article,
                            ip=request.META['REMOTE_ADDR'],
                            
                            session=request.session.session_key)
                    view.save()
    return HttpResponse(u"%s" % Visit.objects.filter(article=article).count())

@login_required(login_url="user:login")
def likes(request,id):
    article=get_object_or_404(Articles,id=request.POST.get("article_id"))
    article.likes.add(request.user)

    

    return redirect(reverse("articles:detail",kwargs={"id":id}))


def test_session(request):
    request.session.set_test_cookie()
    
    return HttpResponse("Testing session cookie")

def track_user(request):
    response = render(request, 'article/detail.html')
    
    if not request.COOKIES.get('visits'):        
        response.set_cookie('visits', '1', 3600 * 24 * 365 * 2)
    else:
        visits = int(request.COOKIES.get('visits', '1')) + 1
        response.set_cookie('visits', str(visits),  3600 * 24 * 365 * 2)
    return response


def members(request):
    members=User.objects.all()
    return render(request, "members.html",{"members":members})