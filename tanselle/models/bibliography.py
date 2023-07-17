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

TOPICS = (
    ('unselected', 'unselected'),
    ('Theory of bibliographical analysis', 'Theory of bibliographical analysis'),
    ('History of bibliographical analysis', 'History of bibliographical analysis'),
)

class Bib(models.Model):
    citation = models.CharField(max_length=20, choices=CITATION_TYPES, default='book')
    author = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=4, blank=True)
    completion = models.CharField(max_length=4, blank=True)
    volumes = models.CharField(max_length=255, blank=True)
    notes = models.CharField(max_length=2048, blank=True)
    url = models.CharField(max_length=255, blank=True)
    topics = models.CharField(max_length=255, choices=TOPICS, default='book')
    tags = models.CharField(max_length=255, blank=True)
   
    def __str__(self):
        return self.title

class BibForm(ModelForm):
    class Meta:
        model = Bib
        fields = '__all__'

        widgets = {
            'citation': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control large_field'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control large_field'}),
            'city': forms.TextInput(attrs={'class': 'form-control large_field'}),
            'year': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'completion': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'volumes': forms.TextInput(attrs={'class': 'form-control w-25'}),
            'notes': forms.Textarea(attrs={'cols': 37, 'rows': 6}),
            'url': forms.TextInput(attrs={'class': 'form-control large_field'}),
            'topics': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control large_field'}),
        }
