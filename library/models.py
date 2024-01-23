from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.genre_name

class Author(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank = True)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    preferred_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    registration_code = models.CharField(max_length=20, unique=True, blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.registration_code:
        
            self.registration_code = self.generate_registration_code()
        super(Author, self).save(*args, **kwargs)

    def generate_registration_code(self):
        city_code = self.city[:3].upper()
        latest_registration_number = Author.objects.filter(city=self.city).count() + 1
        new_registration_number = latest_registration_number
        return f"AR{city_code}{new_registration_number:04d}"



class Book(models.Model):
    book_name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    num_pages = models.IntegerField()
    
    def __str__(self):
        return self.book_name
