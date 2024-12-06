from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import BlogPost

def search_view(request):
    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    posts = BlogPost.objects.all()
    if query:
        posts = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)
    if category_filter:
        posts = posts.filter(category__icontains=category_filter)

    categories = BlogPost.objects.values_list('category', flat=True).distinct()

    return render(request, 'search.html', {
        'posts': posts,
        'query': query,
        'categories': categories,
        'selected_category': category_filter,
    })


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogPost


def add_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        category = request.POST.get("category")
        content = request.POST.get("content")

        if title and author and category and content:
            BlogPost.objects.create(title=title, author=author, category=category, content=content)
            messages.success(request, "Blog added successfully!")
            return redirect('search_view')
        else:
            messages.error(request, "All fields are required.")

    return render(request, 'add_blog.html')
