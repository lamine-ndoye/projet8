from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
    )
from django.http import HttpResponseRedirect


from django.shortcuts import render, get_object_or_404, redirect
from .models import article, Category
from django.views import generic
from blog.forms import SearchPost
from blog.forms import PostForm


from django.contrib.postgres.search import SearchVector , SearchQuery, SearchRank, TrigramSimilarity


# Create your views here.

def post_list(request,category = None):
   posts = article.published.all()
   categorie = Category.objects.all()
   if category:
      category = get_object_or_404(Category, slug = category)
      posts = posts.filter(category = category).order_by('-publish')
   paginator = Paginator(posts,2)
   page = request.GET.get('page')
   try:
      posts = paginator.page(page)
   except PageNotAnInteger:
      posts = paginator.page(1)
   except EmptyPage:
      posts = paginator.page(paginator.num_pages)
   context = {
      'posts':posts,
      'page':page,
      'categorie':categorie,
      'category':category,
   }
   # print(posts)
   return render(request, 'blog/post/list.html', context)


#class PostListView(generic.ListView):
  # queryset = article.objects.all()
   #paginate_by = 2
   #template_name = 'blog/post/list.html'
   #context_object_name = 'posts'



def post_detail(request, year: int,month: int,day: int, detail: str):
   post = get_object_or_404(article, details=detail,status='published', publish__year=year,publish__month=month,publish__day=day)

   return render(request, 'blog/post/detail.html', {'post':post})


def post_search(request):
   query = None
   results = []
   search_form = SearchPost()
   if 'query' in request.GET:
      search_form = SearchPost(request.GET)
      if search_form.is_valid():
         query = search_form.cleaned_data['query']
         vector_search = SearchVector('titel', weight='A') + SearchVector('description', weight='B')
         query_search = SearchQuery(query)
         # results = article.published.annotate(
         #    search=vector_search, rank=SearchRank(vector_search, query_search)
         #    ).filter(rank__gte=0.3).order_by('-rank')
         
         results = article.published.annotate(
              similarity=TrigramSimilarity('titel', query),
              ).filter(similarity__gt=0.1).order_by('-similarity')
         
   return render(request, 'blog/post/search.html',
            {
               'search_form':search_form,
               'query':query,
               'results':results,
               })
   
   
   
def add_post(request):
      if request.method=="POST":
         form = PostForm(request.POST or None, request.FILES or None)
         if form.is_valid():
            obj = form.save(commit=False)
            obj.autors = request.user
            obj.save()
            return redirect('post_list')
      else:
          form = PostForm()
      return render(request, 'blog/post/form.html',{'form':form})
   
   
def post_update(request, year: int,month: int,day: int, detail: str):
      post = get_object_or_404(article, details=detail,status='published', 
                                publish__year=year,publish__month=month,publish__day=day)
      context={}
      if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
            form.save()
         return HttpResponseRedirect(f'/{year}/{month}/{day}/{detail}')
      else:
         form = PostForm(instance=post)
      context['form'] = form
      context['post'] = post
      
      return render(request, 'blog/post/form.html', context)
              

