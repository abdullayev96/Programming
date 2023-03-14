from django.db import models
from django.urls import reverse

# class Fakultet(models.Model):
#     name = models.CharField(max_length = 100, blank = False, null= False )
#     age = models.SmallIntegerField(blank = False, null = False)
#
#     def __str__(self):
#         return self.name
#
# class Guruhlar(models.Model):
#     name = models.CharField(max_length = 100, blank = False, null = False)
#
#     def __str__(self):
#         return f"{self.name}"
#
# class Student(models.Model):
#     name = models.CharField(max_length = 100, blank = False,null = False)
#     price = models.IntegerField(blank = False, null = False)
#     fakultet = models.ForeignKey(Fakultet, blank = False, null = True, on_delete = models.SET_NULL)
#     guruhlar = models.ForeignKey(Guruhlar, blank = False, null = True, on_delete = models.SET_NULL)
#
#
#     def __str__(self):
#         return self.name
#
#
#
#
# class Followrs(models.Model):   #### new
#     email =models.CharField(max_length=200, blank=False, null=False)  ### new
#     name = models.CharField(max_length=200, blank=False, null=False)  #### new
#
#
#
#     def __str__(self):
#         return f"{self.email} {self.name}"
#
# class User(models.Model): ##### new
#     name = models.CharField(max_length=200, blank=False, null=False)  #### new
#     comment = models.CharField(max_length=200, blank=False, null=False)
#
#     def __str__(self):
#         return f"{self.name} {self.comment}"

class Women(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat  = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)


    def __str__(self):
        return f"{self.title} || {self.content}"

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_id":self.pk})

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering =['time_create', 'title']



class Category(models.Model):
    name = models.CharField(max_length=300, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_id":self.pk})


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering =['id']

