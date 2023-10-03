import openai as openai
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from base.models import Note, Message
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserMessageForm
from django.conf import settings


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('notes')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(RegisterPage, self).get(args, kwargs)


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = "base/note_list.html"
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['color'] = 'red' # pass more data to html view
        context['notes'] = context['notes'].filter(user=self.request.user)
        return context


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note'
    template_name = "base/note.html"


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title']
    success_url = reverse_lazy('notes')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    context_object_name = 'note'
    success_url = reverse_lazy('notes')


def get_chatgpt_response(user_message):
    openai.api_key = settings.OPENAI_API_KEY

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=user_message,
        max_tokens=30,
        temperature=0
    )

    return response.choices[0].text.strip()


@login_required
def chat_view(request):
    user_id = request.user.id

    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['user_message']

            # Save user message
            Message.objects.create(user_id=user_id, content=user_message, is_user_message=True)

            chatgpt_response = get_chatgpt_response(user_message)

            # Save ChatGPT response
            Message.objects.create(user_id=user_id, content=chatgpt_response, is_user_message=False)
            form = UserMessageForm()
    else:
        form = UserMessageForm()

    messages = Message.objects.filter(user_id=user_id).order_by('created_at')

    return render(request, 'base/chat_template.html', {'form': form, 'messages': messages})
