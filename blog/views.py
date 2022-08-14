
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,  DeleteView
from .models import Post, Comment
from django.urls import reverse_lazy, reverse  # new
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm, CommentForm, EditForm


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"


class BlogCommentView(CreateView):
    model = Comment
    template_name = "add_comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post_detail", kwargs={"pk": pk})


class BlogCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "newpost.html"

    def form_invalid(self, form):
        print("Error", form.errors)
        return super().form_invalid(form)

    def get_success_url(self):

        return reverse("home")


class BlogUpdateView(UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    form_class = EditForm


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
