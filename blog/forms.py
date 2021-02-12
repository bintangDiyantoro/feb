from django import forms
from .models import Artikel

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'penulis', 'foto',)
        widgets = {
            'judul': forms.TextInput(
                attrs={
                    'placeholder': 'Judul jangan kosong!'
                }
            ),
            'penulis': forms.TextInput(
                attrs={
                    'placeholder': 'Plis Otong jangan ikut campur'
                }
            )
        }
        labels = {
            'isi': 'konten'
        }
