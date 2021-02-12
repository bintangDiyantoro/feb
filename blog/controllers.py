from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from .models import Artikel
from .forms import ArtikelForm
# Create your views here.


class Index(ListView):
    model = Artikel
    extra_context = {
        'title': 'Blog',
        'message': 'Selamat datang di blog saya'
    }
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get("keyword"):
            self.queryset = self.model.objects.filter(
                judul__icontains=self.request.GET["keyword"])
        return super().get_queryset()


class Detail(DetailView):
    model = Artikel

    def get_context_data(self, *args, **kwargs):

        self.extra_context = {
            'title': self.model.objects.get(slug=self.kwargs['slug']).judul,
            'message': 'Selamat menikmati detail data kami'
        }
        return super().get_context_data()


class Create(CreateView):
    # model = Artikel
    # fields = ('judul', 'isi', 'penulis', 'foto')
    form_class = ArtikelForm
    template_name = 'blog/artikel_form.html'
    extra_context = {
        'title': 'Tambah data',
        'message': 'Silahkan menambah data'
    }


class Update(UpdateView):
    model = Artikel
    fields = ('judul', 'isi', 'penulis', 'foto')


class Delete(DeleteView):
    model = Artikel
    
    def get_success_url(self):
        return reverse('blog:index')

    def get_context_data(self,*args,**kwargs):
        self.extra_context = {
            'title':'Hapus data',
            'message':'Apakah anda yakin akan menghapus {}?'.format(self.model.objects.get(slug=self.kwargs['slug']).judul)
        }
        return super().get_context_data()
