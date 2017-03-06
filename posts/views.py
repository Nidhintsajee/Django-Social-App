from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import CommentForm, PostForm
from django.shortcuts import redirect

# Create your views here.

def post_feed(request):
    posts = Post.objects.filter()
    posts = posts.filter()
    return render(request,'posts/feed.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'posts/detail.html',{'post': post,'comments': comments,'comment_form': comment_form})

@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = form.cleaned_data["image"]
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})