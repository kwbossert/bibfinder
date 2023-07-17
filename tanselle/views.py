from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Bib, BibForm

import requests

def home(request):
    # url = "https://data.cerl.org/istc/_search?query=jenson"

    # # A GET request to the API
    # response = requests.get(url)

    # # Print the response
 
    # print(response.content)

    return render(request, "index.html")

def repositories(request):

    # Figure out if this is a search or a reset of the search

    search = True
    if request.GET.get("reset"):
        search = False
        searchTerm = ""
        searchField = ""
        status = "All"
    else:
        searchTerm = request.GET.get('search_term', '')
        searchField = request.GET.get('search_field', '')
        status = request.GET.get('status_filter', '')

    if not searchTerm and search:
        if 'repository_search_field' in request.session:
            searchField = request.session['repository_search_field']

            if not request.session.get('repository_search_term', None):
                request.session['repository_search_term'] = ""
            searchTerm = request.session['repository_search_term']

            if not request.session.get('repository_search_status', None):
                request.session['repository_search_status'] = ""

            status = request.session['repository_search_status']
    else:
        request.session['repository_search_field'] = searchField
        request.session['repository_search_term'] = searchTerm
        request.session['repository_search_status'] = status

    # Get the set of repositories to show the user based on role and assignments

    repositories = Repository.GetRepositories(searchField, searchTerm, status)
    return render(request,'repositories.html',{"repositories":repositories})

def bibnew(request):
    context ={}
 
    form = BibForm(request.POST or None)
 
    # save the data from the form and return to repositories page
    if form.is_valid():

        form.save()

        return HttpResponseRedirect("/home")
 
    # add form dictionary to context
    context["form"] = form

    return render(request, "bibedit.html", context)

def bibedit(request, id):
    context ={}
 
    if id == 0:
        form = BibForm(request.POST or None)
    else:
        obj = get_object_or_404(Bib, id = id)
        form = BibForm(request.POST or None, instance = obj)
 
    # save the data from the form and return to repositories page
    if form.is_valid():

        form.save()

        return HttpResponseRedirect("/home")
 
    # add form dictionary to context
    context["form"] = form

    return render(request, "bibedit.html", context)

def delete_bib(request, id):
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Repository, id = id)

    obj.delete()

    return HttpResponseRedirect("/repositories")