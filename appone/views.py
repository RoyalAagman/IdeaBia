from django.views.generic import TemplateView, FormView
from .models import Post
from .Forms import AddForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class PostView(LoginRequiredMixin, FormView):
    template_name = "new_post.html"
    form_class = AddForm
    success_url = '/home/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image'],
            author=self.request.user,
        )
        return super().form_valid(form)


class MainPageView(TemplateView):
    template_name = "mainpage.html"
