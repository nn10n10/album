from turtle import title
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from photo.models import Photo
from django.core.paginator import Paginator

def home(request):
    photos       = Photo.objects.all()
    # 新增分页代码
    paginator    = Paginator(photos, 9)
    page_number  = request.GET.get('page')
    paged_photos = paginator.get_page(page_number)
    # 将分页器对象传入上下文
    context = {'photos': paged_photos}


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(request, username=username, password=password)
        # 登入
        if user is not None and user.is_superuser:
            login(request, user)
        # 登出
        isLogout  = request.POST.get('isLogout')
        if isLogout == 'True':
            logout(request)
    return render(request, 'photo/list.html', context)
def upload(request):
    if request.method == 'POST' and request.user.is_superuser:
        images = request.FILES.getlist('images')
        for i in images:
            photo = Photo(image=i)
            photo.save()
    return redirect('home')
# Create your views here.
