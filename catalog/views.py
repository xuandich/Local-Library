
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from catalog import models
from catalog.models import Book, Author

# Create your views here.

# Book

def index(request):
    """ Trang Chủ
    Output: Hiển thị trang index.html
    """
    return render(request, "index.html")


def book(request):
    """ Hiển thị tất cả sách
    Input: Lấy dữ liệu từ database
    Output: Hiển thị trang book.html
    """
    book_list = Book.objects.all()
    return render(request, "book/book.html", {"book_list": book_list})


def addbook(request):
    """ Thêm Sách
    Input: Nhâp từ bàn phím (title, date, summary) + chọn trong database(author,category)
    Ouput: Lưu Sách vào database sau đó chuyển đến trang book.html
    """
    if request.method == 'POST':
        title = request.POST.get("title")
        publish_date = request.POST.get("pub_date")
        authors_id_list = request.POST.getlist('authors_id_list')
        category_id_list = request.POST.getlist('category_id_list')
        summary = request.POST.get("summary")
        if title == '' or publish_date == '' or category_id_list=='' or authors_id_list == '' or summary == '':
            # Nếu các ô này để trống -> sẽ hiển thị thông báo như bên dưới: 
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
    """ Hiển thị thông tin chi tiết của sách
    Input: sách với id được chọn
    Output: Hiển thị trang bookdetail.html
    """
    book_obj = models.Book.objects.filter(pk=id).first()
    return render(request, "book/bookdetail.html", {"book_obj": book_obj})


def delbook(request, id):
    """ Xóa sách
    Input: sách với id được chọn
    Output: Xóa sách khỏi database và sau đó chuyển đến trang book.html
    """
    book_obj = models.Book.objects.filter(pk=id).first()
    book_obj.delete()
    return redirect("/book/")


def editbook(request, id):
    """ Sửa thông tin của Sách
    Input: sách với id được chọn
    Output: Lưu sách vào database với thông tin mới (vừa được sửa đổi)
            Sau đó chuyển sang trang book.html
    """
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

# Author

def author(request):
    """ Hiện thị danh sách tác giả
    Input: Lấy tất cả tác giả từ database 
    Output: Đưa dữ liệu lên trang author.html
    """
    author_list = models.Author.objects.all()
    return render(request, "author/author.html", {"author_list": author_list})


def addauthor(request):
    """ Thêm Tác Giả
    Input: Nhâp từ bàn phím (name)
    Ouput: Lưu tác giả vào database sau đó chuyển đến trang author.html
    """
    if request.method == 'POST':
        name = request.POST.get("name")
        models.Author.objects.create(name=name)
        return redirect("/author/")
    return render(request, "author/addauthor.html")


def delauthor(request, id):
    """ Xóa tác giả
    Input: Tác giả với id được chọn
    Output: Xóa tác giả khỏi database và sau đó chuyển đến trang author.html
    """
    author_obj = models.Author.objects.filter(id=id).first()
    author_obj.delete()
    return redirect("/author/")


def editauthor(request, id):
    """ Sửa thông tin của tác giả
    Input: tác giả với id được chọn
    Output: Lưu tác giả vào database với thông tin mới (vừa được sửa đổi)
            Sau đó chuyển sang trang author.html
    """
    author_obj = models.Author.objects.filter(id=id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        models.Author.objects.filter(id=id).update(name=name)
        return redirect("/author/")
    return render(request, "author/editauthor.html", {"author_obj": author_obj})


def author_book(request, id):
    """ Hiện thị danh sách các tác phảm của 1 tác giả được chọn
    Input: Lấy dữ liệu sách từ database với id tác giả
    Output: Đưa dữ liệu lên trang author_book.html
    """
    author_obj = models.Author.objects.filter(pk=id).first()
    book_list = author_obj.book_set.all()
    return render(request, "author/author_book.html", {'book_list': book_list, 'author': author_obj})


# Category

def category(request):
    """ Hiện thị danh sách thể loại
    Input: Lấy tất cả thể loại từ database 
    Output: Đưa dữ liệu lên trang category.html
    """
    category_list = models.Category.objects.all()
    return render(request, "category/category.html", {"category_list": category_list})


def addcategory(request):
    """ Thêm Thể Loại
    Input: Nhâp từ bàn phím (name)
    Ouput: Lưu thể loại vào database sau đó chuyển đến trang category.html
    """
    if request.method == 'POST':
        name = request.POST.get("name")
        models.Category.objects.create(name=name)
        return redirect("/category/")
    return render(request, "category/addcategory.html")


def delcategory(request, id):
    """ Xóa thể loại
    Input: thể loại với id được chọn
    Output: Xóa thể loại khỏi database và sau đó chuyển đến trang category.html
    """
    category_obj = models.Category.objects.filter(id=id).first()
    category_obj.delete()
    return redirect("/category/")


def editcategory(request, id):
    """ Sửa thông tin của thể loại
    Input: thể loại với id được chọn
    Output: Lưu thể loại vào database với thông tin mới (vừa được sửa đổi)
            Sau đó chuyển sang trang category.html
    """
    category_obj = models.Category.objects.filter(id=id).first()
    if request.method == "POST":
        name = request.POST.get("name")
        models.Category.objects.filter(id=id).update(name=name)
        return redirect("/category/")
    return render(request, "category/editcategory.html", {"category_obj": category_obj})


def category_book(request, id):
    """ Hiện thị danh sách các tác phẩm cùng một thể loại được chọn
    Input: Lấy dữ liệu sách từ database với id thể loại
    Output: Đưa dữ liệu lên trang category_book.html
    """
    category_obj = models.Category.objects.filter(pk=id).first()
    book_list = category_obj.book_set.all()
    return render(request, "category/category_book.html", {'book_list': book_list, 'category':category_obj})


from django.db.models import Q 

def search(request):
    """ Hàm tìm kiếm sách, tác giả, thể loại
    Input: Giá trị nhập từ bàn phím
    Outphut: Hiển thị tất cả sách, thể loại, tác giả có chứa từ khóa tìm kiếm 
    """
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        if query == '':
            query = 'None'
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(authors__name__icontains=query) |
            Q(categorys__name__icontains=query))
    return render(request, 'search.html', {'query': query, 'results': results})
