from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import post,comment,user
from django.views import View
from .forms import commentForm, createPostForm, registerUserForm, loginUserForm
from django.urls import reverse
from datetime import date
from django.utils.text import slugify
from random import randint
from django.core.exceptions import ValidationError
from . import errors
from django.db import IntegrityError

import blog_posts

# Create your views here.

class index(View):
    def get(self,request):
        try:
            logged_user = user.objects.get(code = request.session["logged_user"])
        except Exception:
            logged_user = False
        latest_posts = post.objects.all().order_by('-date')[0:3]
        return render(request,'blog_posts/index.html', {
        "posts": latest_posts,
        "logged":logged_user
    })

class all_posts(View):
    def get(self,request):
        try:
            logged_user = user.objects.get(code = request.session["logged_user"])
        except Exception:
            logged_user = False
        all_posts = post.objects.all()
        return render(request,'blog_posts/posts.html',{
        'posts':all_posts,
        "logged":logged_user
    })

class one_post(View):
    def get(self, request,slug):
        try:
            logged_user = user.objects.get(code = request.session["logged_user"])
        except Exception:
            logged_user = False
        form = commentForm()
        posts = post.objects.get(slug = slug)
        comments = comment.objects.filter(post = posts)
        return render(request,"blog_posts/post.html",{
        "post":posts,
        "tags":posts.tags.all(),
        "form":form,
        "comments":comments,
        "logged":logged_user
    })
    def post(self,request,slug):
        add = comment(content = request.POST["content"],name = request.POST["name"],post = post.objects.get(slug=slug))
        add.save()
        return HttpResponseRedirect(reverse('post',args=[slug]))

class addReadLater(View):
    def get(self,request,slug):
        try:
            if slug not in request.session["read_later"]:
                request.session["read_later"].append(slug)
                request.session.modified = True
        except:
            request.session["read_later"] = [slug]
        return HttpResponseRedirect(reverse("post",args = [slug]))

class readLater(View):
    def get(self,request):
        try:
            logged_user = user.objects.get(code = request.session["logged_user"])
        except Exception:
            logged_user = False
        if "read_later" in request.session.keys():
            queryset = post.objects.filter(slug__in = request.session["read_later"])
            return render(request,'blog_posts/read_later.html', {
                    "posts":queryset,
                    "read_later":True,
                    "logged":logged_user
                })
        else:
            return render(request,'blog_posts/read_later.html', {
                    "read_later":False,
                    "logged":logged_user
                })

class createPost(View):
    def get(self,request):
        form = createPostForm()
        return render(request,"blog_posts/createpost.html",{
            "form":form
        })
    
    def post(self,request):
        createdPost = post(date = date.today(),title = request.POST["title"],clickbait = request.POST["clickbait"],content = request.POST["content"],author = user.objects.get(code = request.session['logged_user']),image = request.FILES["image"],slug = slugify(request.POST["title"]))
        createdPost.save()
        return HttpResponseRedirect(reverse("all_posts"))

class registerUser(View):
    def get(self,request):
        form = registerUserForm()
        return render(request,"blog_posts/reg_log.html",{
            "form":form
        })

    def post(self,request):
        form = registerUserForm(request.POST)
        if form.is_valid:
            try:
                if request.POST["password"]==request.POST["password2"]:
                    rcode = ""
                    for i in range(15):
                        rcode+= chr(randint(33,126))
                    user(name = request.POST["name"],password=request.POST["password"],email=request.POST["email"],code = rcode).save()
                    return HttpResponseRedirect(reverse("index"))
                else:
                    raise errors.passMatch
            except errors.passMatch:
                error = "passwords doesn't match"
            except IntegrityError:
                error = "user witch such mail already exists"
        return render(request,"blog_posts/reg_log.html",{
                "form":form,
                "error":error,
                "login":False
            })

class loginUser(View):
    def get(self,request):
        form = loginUserForm()
        return render(request, "blog_posts/reg_log.html", {
            "form":form,
            "login":True
        })
    
    def post(self,request):
        form = loginUserForm(request.POST)
        try:
            logged_user = user.objects.get(email = request.POST['mail'])
            if logged_user.password != request.POST['password']:
                raise Exception
        except Exception:
            error = "Your password and login doesn't match any records in our database"
            return render(request,"blog_posts/reg_log.html",{
                "form":form,
                "error":error,
                "login":True
            })
        else:
            request.session["logged_user"] = logged_user.code
            return HttpResponseRedirect(reverse('index'))

class profile(View):
    def get(self,request,name):
        try:
            logged_user = user.objects.get(code = request.session["logged_user"])
        except Exception:
            logged_user = False
        finally:
            userProfile = user.objects.get(name = name)
            if logged_user.name == name :
                ownProfile = True
            else:
                ownProfile = False
            return render(request,"blog_posts/profile.html",{
                "logged": logged_user,
                "ownProfile":ownProfile
                })

    def post(self,request,name):
        user.objects.get(code = request.session["logged_user"]).delete()
        request.session["logged_user"] = False
        return HttpResponseRedirect(reverse('index'))

class logOut(View):
    def get(self,request):
        request.session["logged_user"] = False
        return HttpResponseRedirect(reverse('index'))

