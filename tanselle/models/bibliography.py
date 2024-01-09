from django.conf import settings
from django.db import models
from django.forms import ModelForm, Textarea
from django import forms

CITATION_TYPES = (
    ('book', 'book' ),
    ('article', 'article'),
    ('chapter', 'chapter'),
    ( 'multivolume', 'multivolume'),
)

class Bib(models.Model):
    citation = models.CharField(max_length=20, choices=CITATION_TYPES, default='book')
    author = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=4, blank=True)
    completion = models.CharField(max_length=4, blank=True)
    volumes = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=2048, blank=True)
    url = models.CharField(max_length=255, blank=True)
    tags = models.CharField(max_length=1024, blank=True)
    anthology = models.CharField(max_length=255, blank=True)
 
    def __str__(self):
        return self.title

    def GetBibResults(searchField, searchTerm):
        results = []

        if searchTerm:
            if searchField == "Author":
                results = Bib.objects.filter(author__icontains=searchTerm).order_by('author')
            else:
                if searchField == "Title":
                        results = Bib.objects.filter(title__icontains=searchTerm).order_by('title')
                else:
                    if searchField == "Tags":
                        results = Bib.objects.filter(tags__icontains=searchTerm).order_by('author')                   
        else:
            return Bib.objects.all().order_by('-pk')[:50]
        
        return results

class BibForm(ModelForm):
    class Meta:
        model = Bib
        fields = '__all__'

        widgets = {
            'citation': forms.Select(attrs={'class': 'form-control w-25'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'completion': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'volumes': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'notes': forms.Textarea(attrs={'cols': 120, 'rows': 5}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'anthology': forms.TextInput(attrs={'class': 'form-control'}),
        }
