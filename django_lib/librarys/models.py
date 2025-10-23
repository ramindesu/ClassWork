from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=60)
    bio = models.CharField(max_length=255)
    nationality = models.CharField(max_length=60)

class Publisher(models.Model):
    name = models.CharField(max_length=60)
    addrers = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

class Catergory(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)

class Member(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    number = models.IntegerField()
    join_status = models.BooleanField()

class Book(models.Model):
    title = models.CharField(max_length=32)
    publish_year = models.IntegerField()
    copy_qunatity = models.IntegerField()
    availability = models.BooleanField()
    ISBN = models.IntegerField(unique=True)
    Author_id = models.ForeignKey(Author,on_delete=models.CASCADE)
    Publisher_id = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    Catergory_id = models.ForeignKey(Catergory,on_delete=models.CASCADE)

class Borrow(models.Model):
    Borrow_date = models.DateField()
    return_Date = models.DateField()
    fine = models.IntegerField()
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)

