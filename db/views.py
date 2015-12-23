from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import User, Post, Category


def posts_list(request, category, page_no=1):
    page_no = int(page_no)
    if page_no <= 0 :
        page_no = 1

    posts_per_page = 2
    start = (page_no-1)  * posts_per_page
    end = start + posts_per_page

    if category == 'all':
        posts = Post.objects.filter(is_visible=True).order_by('-create_at')[start:end]
        no_of_posts = Post.objects.filter(is_visible=True).count()
        # category = 'all'
    else:
        posts = Post.objects.filter(is_visible=True, category__name = category).order_by('-create_at')[start:end]
        no_of_posts = Post.objects.filter(is_visible=True, category__name = category).count()

    no_of_pages = no_of_posts/posts_per_page
    # if no_of_pages is decimal round it to int
    if round(no_of_pages) != no_of_pages:
        no_of_pages = round(no_of_pages + .5)

    page_title = category.title() + ' Posts'

    return render(request, 'db/posts_list.html', {
        'posts': posts,
        'category': category,
        'page_title': page_title,
        'page_no': page_no,
        'no_of_pages': range(1,int(no_of_pages)+1),
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not post.is_visible:
        post = None;
    return render(request, 'db/post_detail.html', {'post':post,})
