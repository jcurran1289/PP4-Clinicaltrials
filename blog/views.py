from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import QuestionForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        questions = post.questions.filter(approved=True).order_by("-created_on")
        enrolled = False
        if post.no_participants.filter(id=self.request.user.id).exists():
            enrolled = True

        return render(
            request, 
            "post_detail.html",
            {
                "post": post,
                "questions": questions,
                "asked": False,
                "enrolled": enrolled,
                "question_form": QuestionForm()
            }
        
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        questions = post.questions.filter(approved=True).order_by("-created_on")
        enrolled = False
        if post.no_participants.filter(id=self.request.user.id).exists():
            enrolled = True

        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            question_form.instance.email = request.user.email
            question_form.instance.name = request.user.username
            question = question_form.save(commit=False)
            question.post = post
            question.save()
        else:
            question_form = QuestionForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "questions": questions,
                "asked": True,
                "question_form": question_form,
                "enrolled": enrolled,
            },
        )

class PostEnroll(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.no_participants.filter(id=request.user.id).exists():
            post.no_participants.remove(request.user)
        else:
            post.no_participants.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def search_ct(request):
    if request.method =="POST":
        searched =  request.POST['searched']
        search_post = Post.objects.filter(primary_disease__contains =  searched)

        return render(
            request,
            "search_ct.html",
            {
                'searched':searched,
                'search_post':search_post
            },
        )
    else:
            return render(
            request,
            "search_ct.html",
            {
    
            },
        )