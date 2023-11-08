from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post, Category, Tag, Comment
from .forms import CommentForm, PostForm, SearchForm
from django.utils.text import slugify
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone

class CategoryContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all().order_by('-name')
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            obj = self.get_object()
            if obj.author == request.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to update this item')
        return super().dispatch(request, *args, **kwargs)
    

class PostList(CategoryContextMixin,ListView):
    model = Post
    ordering = '-created_at'
    context_object = 'posts'
    template_name = 'blog/blog_main.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_keyword = self.request.GET.get('q')

        if search_keyword:
            # queryset = queryset.filter(title__icontains=search_keyword)
            # distinct()는 중복을 제거합니다.
            # Q는 |(or), &(and), ~(not) 연산자를 사용할 수 있습니다.
            # icontains는 대소문자를 구분하지 않는 검색입니다.
            queryset = queryset.filter(
                Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(tags__name__icontains=search_keyword)).distinct()

        return queryset


class PostDetail(CategoryContextMixin, DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all().order_by('-name')
    context = {
        'post_list': Post.objects.filter(category=category).order_by('-pk'),
        'categories': categories,
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'category': category,
        'category_list': Category.objects.all().order_by('-name'),
    }
    return render(request, 'blog/blog_list.html', context)


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    print(tag)
    post_list = tag.post_set.all()
    categories = Category.objects.all().order_by('-name')
    context = {
        'post_list': post_list,
        'categories': categories,
        'no_category_post_count': Post.objects.filter(category=None).count(),
        'tag': tag,
        'category_list': Category.objects.all().order_by('-name'),
    }
    return render(request, 'blog/blog_list.html', context)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_write.html'

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            # 원래 기존에 리턴하던 값을 response에 담아둡니다.
            response = super(PostCreate, self).form_valid(form)

            tags_str = self.request.POST.get('tags_str')
            if tags_str:
                tags_str = tags_str.strip()
                tags_str = tags_str.replace(',', ';')
                tags_list = tags_str.split(';')
                for t in tags_list:
                    t = t.strip()
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    # self.object는 새로만든 Post 객체
                    self.object.tags.add(tag)
            return response
        else:
            return redirect('/blog/')


class PostUpdate(LoginRequiredMixin, UpdateView, AuthorRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/blog_edit.html'



def comment_write(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                # commit=False를 하면, DB에 바로 저장되지 않습니다.
                # 대신, 메모리에 Comment 객체를 하나 생성해 줍니다.
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})


class CommentUpdate(LoginRequiredMixin, UpdateView, AuthorRequiredMixin):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(CommentUpdate, self).form_valid(form)
        else:
            return redirect('/blog/')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            comment = self.get_object()
            if comment.author == request.user:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to update this comment')
        return super().dispatch(request, *args, **kwargs)


def comment_delete(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author == request.user:
            comment.delete()
            return redirect(comment.post.get_absolute_url())
        else:
            return HttpResponse('You are not allowed to delete this comment')
    return redirect('/blog/')


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        posts = Post.objects.filter(title__icontains=query)
        return render(request, 'search_results.html', {'posts': posts})
    

blog_main = PostList.as_view()
blog_write = PostCreate.as_view()
blog_edit = PostUpdate.as_view()
blog_delete = DeleteView.as_view()
comment_edit = CommentUpdate.as_view()
blog_detail = PostDetail.as_view()
