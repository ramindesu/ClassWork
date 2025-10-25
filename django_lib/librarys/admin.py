from django.contrib import admin

# Register your models here.
from .models import Author,Book,Member,Borrow,Catergory,Publisher
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name' , 'bio' , 'nationality')
    search_fields = ('name',)
    #
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin): 
    list_display = ('name' , 'addrers' , 'email' , 'website')
    search_fields = ('name', 'email')

@admin.register(Catergory)
class CatergoryAdmin(admin.ModelAdmin): 
    list_display = ('name' , 'description')
    search_fields = ('name',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):    
    list_display = ('name'  , 'email' , 'number','join_status')
    search_fields = ('name', 'email')

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin): 
    list_display = ('Borrow_date' , 'return_Date' , 'fine' , 'book_id','member_id')
    search_fields = ('book_id', 'member_id')