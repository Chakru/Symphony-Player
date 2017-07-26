from django.views import generic
from .models import *
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import *



class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_title', 'artist', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('Music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Display form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            User = form.save(commit=False)

            Username = form.cleaned_data['username']
            Password = form.cleaned_data['password']
            User.set_password(Password)
            User.save()

            # Return user object if credentials are correct
            user = authenticate(username=Username, password=Password)

            if User is not None:

                if User.is_active:
                    login(request, user)
                    return redirect('Music:index')

            # If the password or the username is incorrect
                return render(request, self.template_name, {'form':form})







