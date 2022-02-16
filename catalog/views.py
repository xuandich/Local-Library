
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from catalog import models
from catalog.models import Book, Author

# Create your views here.


def index(request):
    return render(request, "index.html")


def book(request):
    book_list = Book.objects.all()
    return render(request, "book/book.html", {"book_list": book_list})


def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        publish_date = request.POST.get("pub_date")
        authors_id_list = request.POST.getlist('authors_id_list')
        category_id_list = request.POST.getlist('category_id_list')
        summary = request.POST.get("summary")
        if title == '' or publish_date == '' or authors_id_list == '' or summary == '':
            return HttpResponse('<h3 style="color: #c7254e">Không Được Để Trống</h3>')

        book_obj = Book.objects.create(
            title=title, publish_date=publish_date, summary=summary)
        book_obj.authors.set(authors_id_list)
        book_obj.categorys.set(category_id_list)

        return redirect("/book/")
    author_list = models.Author.objects.all()
    category_list = models.Category.objects.all()
    return render(request, "book/addbook.html", {"author_list": author_list, "category_list": category_list})


def bookdetail(request, id):
    book_obj = models.Book.objects.filter(pk=id).first()
    return render(request, "book/bookdetail.html", {"book_obj": book_obj})


def delbook(request, id):
    book_obj = models.Book.objects.filter(pk=id).first()
    book_obj.delete()
    return redirect("/book/")


def editbook(request, id):

    # ---------------------------------
    book_obj = Book.objects.filter(pk=id).first()
    if request.method == "POST":
        title = request.POST.get("title")
        publish_date = request.POST.get("pub_date")
        authors_id_list = request.POST.getlist('authors_id_list')

        Book.objects.filter(pk=id).update(
            title=title, publish_date=publish_date)
        book_obj.authors.set(authors_id_list)
        return redirect("/book/")
    author_list = Author.objects.all()
    return render(request, "book/editbook.html", {"book_obj": book_obj, "author_list": author_list})


def author(request):
    author_list = models.Author.objects.all()
    return render(request, "author/author.html", {"author_list": author_list})


def addauthor(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        models.Author.objects.create(name=name)
        return redirect("/author/")
    return render(request, "author/addauthor.html")


def delauthor(request, id):
    author_obj = models.Author.objects.filter(id=id).first()
    author_obj.delete()
    return redirect("/author/")


def editauthor(request, id):
    author_obj = models.Author.objects.filter(id=id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        models.Author.objects.filter(id=id).update(name=name)
        return redirect("/author/")
    return render(request, "author/editauthor.html", {"author_obj": author_obj})


def author_book(request, id):
    author_obj = models.Author.objects.filter(pk=id).first()
    book_list = author_obj.book_set.all()
    return render(request, "author/author_book.html", {'book_list': book_list})

# Category

def category(request):
    category_list = models.Category.objects.all()
    return render(request, "category/category.html", {"category_list": category_list})


def addcategory(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        models.Category.objects.create(name=name)
        return redirect("/category/")
    return render(request, "category/addcategory.html")


def delcategory(request, id):
    category_obj = models.Category.objects.filter(id=id).first()
    category_obj.delete()
    return redirect("/category/")


def editcategory(request, id):
    category_obj = models.Category.objects.filter(id=id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        models.Category.objects.filter(id=id).update(name=name)
        return redirect("/category/")
    return render(request, "category/editcategory.html", {"category_obj": category_obj})


def category_book(request, id):
    category_obj = models.Category.objects.filter(pk=id).first()
    book_list = category_obj.book_set.all()
    return render(request, "category/category_book.html", {'book_list': book_list})


from django.db.models import Q 

def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(authors__name__icontains=query))
    return render(request, 'search.html', {'query': query, 'results': results})
