from django.db import models
from django.urls import reverse

class Character(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True, default='')
  image = image = models.ImageField(upload_to='uploaded_images',blank=True)
  co_occurences = models.ManyToManyField("self",through='CoOccur',blank=True,symmetrical=False)
  def __str__(self):
    return self.name

class Book(models.Model):
  name = models.CharField(max_length=50, unique=True)
  description = models.TextField(blank=True, default='')

  def __str__(self):
    return self.name

class CoOccur(models.Model):
  source = models.ForeignKey(Character, related_name="targeted",on_delete=models.CASCADE)
  target = models.ForeignKey(Character, related_name="sourced",on_delete=models.CASCADE)
  book = models.ForeignKey(Book, related_name="from_book",on_delete=models.CASCADE)
  weight = models.PositiveIntegerField()

  def __str__(self):
    return '{} and {} appeared {} time(s) together in {}'.format(self.source, self.target, self.weight, self.book)

