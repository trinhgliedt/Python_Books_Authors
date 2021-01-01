from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.


def book(request):
    context ={
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, 'book.html', context)

def author(request):
    context ={
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all(),
    }

    return render(request, 'author.html', context)

def add_book(request):
    Book.objects.create(tittle= request.POST["book_tittle"], desc = request.POST["desc"],)

    return redirect("/book")

def add_author(request):
    Author.objects.create(first_name= request.POST["first_name"], last_name = request.POST["last_name"], notes= request.POST["notes"])

    return redirect("/author")

def show_book(request, book_id):
    context = {
        "this_book": Book.objects.get(id=book_id),
        "all_authors": Author.objects.all(),
    }
    return render(request, 'showBook.html', context)

def show_author(request, author_id):
    context = {
        "this_author": Author.objects.get(id=author_id),
        "all_books": Book.objects.all(),
    }
    return render(request, 'showAuthor.html', context)


def add_author_to_book(request, book_id):

    no_of_authors = Author.objects.all().count()
    no_of_this_book_authors = Book.objects.get(id=request.POST["book_id"]).written_by.all().count()
    condition = no_of_authors == no_of_this_book_authors # to check if there's any author left to add
    # print("authors: ",no_of_authors, ", no_of_this_book_authors: ", no_of_this_book_authors, ", condition: ",condition )
    if request.method == "POST" and condition == False:
        this_book = Book.objects.get(id=request.POST["book_id"])
        this_author = Author.objects.get(id=request.POST["author_id"])
        this_book.written_by.add(this_author)
        
    return redirect(f"/book/{book_id}")
   
def add_book_to_author(request, author_id):

    no_of_books = Book.objects.all().count()
    no_of_this_author_books = Author.objects.get(id=request.POST["author_id"]).book_written.all().count()
    condition = no_of_books == no_of_this_author_books # to check if there's any author left to add
    # print("authors: ",no_of_authors, ", no_of_this_book_authors: ", no_of_this_book_authors, ", condition: ",condition )
    if request.method == "POST" and condition == False:
        this_book = Book.objects.get(id=request.POST["book_id"])
        this_author = Author.objects.get(id=request.POST["author_id"])
        this_author.book_written.add(this_book)
        
    return redirect(f"/author/{author_id}")