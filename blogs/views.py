from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import template

from blogs.forms import PageForm
from blogs.models import Page



class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        # pages = self.get_queryset().all()
        user_pages = None
        if self.request.user.is_authenticated:
          user_pages = Page.objects.filter(author=request.user)
        all_pages = Page.objects.filter(is_public=True)

        return render(request, 'list.html', {
          'user_pages': user_pages,
          'all_pages': all_pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific blog page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

class PageNew(CreateView):
    model = Page

    def get(self, request):
      """ Prints the form """
      page_form = PageForm()
      return render(request, 'add_page.html', {
        'page_form': page_form
      })

    def post(self, request):
      """processes the form and adds a blog """
      form = PageForm(request.POST)
      form.instance.author = self.request.user
      print(form)
      if form.is_valid():
        page = form.save()
        return HttpResponseRedirect(reverse('blog-details-page', args=[page.slug] ))
      else:
        return render(request, 'add_page.html', {
        'page_form': form,
      })


class BlogUpdate(UpdateView):
    model= Page
    fields = ['title', 'content', 'is_public']
    template_name_suffix = '_update_form'

    def post(self, request, slug):
      """processes the form and adds a blog """
      obj = get_object_or_404(Page, slug=slug)
      form = PageForm(request.POST, instance=obj)
      if form.is_valid():
        form.save()
        print(form)
        # Page.objects.filter(slug=slug).update(content=form.instance.content)
        return HttpResponseRedirect(reverse('blog-details-page', args=[slug] ))
      else:
        return render(request, 'blogs/page_update_form.html', {
          'form': form,
        })

def delete_object(request, slug):
  Page.objects.filter(slug=slug).delete()
  return HttpResponseRedirect(reverse('blog-list-page'))
