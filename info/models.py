from django.db import models
from django.core.validators import MinLengthValidator


class Info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, validators=[ MinLengthValidator(10) ])
    email = models.EmailField()
    facebook_link = models.URLField()
    linkedin_link = models.URLField()
    photo = models.ImageField(upload_to='uploaded_images')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



class Job(models.Model):
    CATEGORY_COICES = (
        ("sport", "Sport"),
        ("it", "IT")
    )

    date_start = models.DateField()
    date_end = models.DateField(default=None, blank=True, null=True)
    job_image = models.ImageField(upload_to='uploaded_images')
    company = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    info = models.ForeignKey(Info, related_name='jobs', on_delete=models.CASCADE)
    job_url = models.URLField(default=None, blank=True, null=True)
    category = models.CharField( max_length=10, choices=CATEGORY_COICES, default='it')

    def __str__(self):
        return self.company
