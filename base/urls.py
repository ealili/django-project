from django.urls import path
from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate, DeleteView, CustomLoginView, RegisterPage, chat_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', NoteList.as_view(), name='notes'),
    path('note/<int:pk>/', NoteDetail.as_view(), name='note'),
    path('note-create/', NoteCreate.as_view(), name='note-create'),
    path('note-update/<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    path('note-delete/<int:pk>/', DeleteView.as_view(), name='note-delete'),
    path('chat/', chat_view, name='chat_view'),
]
