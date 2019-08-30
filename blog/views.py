from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(tgl_terbit__lt=timezone.now()).order_by('-tgl_terbit')
	return render(request, 'blog/post_list.html',{'posts': posts})
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_baru(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
## Hapus komentar untuk dibawah untuk menghilangkan fitur simpan sebgai draft
##			post.tgl_terbit = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
###			hilangkan komentar untuk menghilangkan draft
###			post.tgl_terbit = timezone.now())
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required	
def post_draft_list(request):
	posts = Post.objects.filter(tgl_terbit__isnull=True).order_by('tgl_buat')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required	
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.terbit()
	return redirect('post_detail', pk=pk)

@login_required	
def post_hapus(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list')
