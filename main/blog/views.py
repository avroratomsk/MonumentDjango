from django.shortcuts import render, get_object_or_404

from blog.models import BlogSettings, Post, BlogCategory

def blog(request):
  posts = Post.objects.all()
  category = BlogCategory.objects.all()

  try:
    setup = BlogSettings.objects.get()
  except:
    setup = BlogSettings()
  
  context = {
    "posts": posts,
    "category": category,
    "blog": setup
  }
  return render(request, "pages/blog/blog.html", context)

def category_post(request, category_slug):
  category = BlogCategory.objects.get(slug=category_slug)
  categories = BlogCategory.objects.all()
  post = Post.objects.filter(category=category)

  context = {
    "category": category,
    "categories": categories,
    "posts": post
  }
  return render(request, "pages/blog/blog_category.html", context)

def post(request, slug, category_slug=None,):
    if category_slug:
      post = get_object_or_404(Post, slug=slug, category__slug=category_slug)
    else:
      post = get_object_or_404(Post, slug=slug, category__isnull=True)

    viewed_articles = request.session.get('viewed_articles', [])

    # Проверяем, просматривал ли пользователь эту статью ранее.
    if slug not in viewed_articles:
      # Увеличиваем счетчик просмотров, если статья просматривается впервые.
      post.view_count += 1
      post.save()

      # Добавляем идентификатор статьи в список просмотренных.
      viewed_articles.append(slug)

      # Обновляем сессию, сохраняя в ней обновленный список.
      request.session['viewed_articles'] = viewed_articles


    context = {
        "post": post,
        "absolute_url": request.build_absolute_uri(post.get_absolute_url())
    }

    return render(request, "pages/blog/blog_detail.html", context)