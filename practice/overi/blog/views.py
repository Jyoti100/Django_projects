from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponseRedirect, reverse, redirect
from .models import Post, Category,Tag
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .forms import FeedbackForm
from overi import helper
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    posts=Post.objects.order_by("-id").all()
    posts = helper.pg_records(request, posts, 3)
    return render(request, 'blog/post_list.html', {'posts':posts})

@login_required
def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_by_category(request, category_slug):
    category=get_object_or_404(Category, slug=category_slug)
    posts=get_list_or_404(Post.objects.order_by("-id"), category=category)
    posts = helper.pg_records(request, posts, 3)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/post_by_category.html', context)

@login_required
def post_by_tag(request, tag_slug):
    tag=get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by("-id"), tags=tag)
    posts = helper.pg_records(request, posts, 3)
    context={'tag':tag, 'posts':posts}
    return render(request,'blog/post_by_tag.html', context)


def test_redirect(request):
    return HttpResponseRedirect(reverse('post_list'))

@login_required
def feedback(request):
    if request.method == 'POST':
        f =FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted')
            return  redirect('feedback')
    else:
        f=FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': f})

def test_cookie(request):
    if not request.COOKIES.get('color'):
        response = HttpResponse('Cookie set')
        response.set_cookie('color', 'blue')
        return response
    else:
        return HttpResponse('your favorite color is {0}'.format(request.COOKIES['color']))

def track_user(request):
    response=render(request, 'blog/track_user.html')
    if not request.COOKIES.get('visits'):
        response.set_cookie('visits', '1')
    else:
        visits = int(request.COOKIES.get('visits', '1')) + 1
        response.set_cookie('visits', str(visits))
    return response

def stop_tracking(request):
    if request.COOKIES.get('visits'):
        response =HttpResponse('Cookies deleted')
        response.delete_cookie('visits')
    else:
        response = HttpResponse('We r not tracking you ')
    return response

def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("testing session cookie")

def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse('Test cookie passed')
    else:
        response=HttpResponse('Test cookies failed')
    return response

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("post_list")
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'blog/login.html')

def secret(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    return render(request, 'blog/secret_page.html')

def logout(request):
    auth.logout(request)
    return render(request, 'blog/logout.html')


