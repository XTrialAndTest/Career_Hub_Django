from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
# image, title, time, location, description, company


# {
# id:1,
# image: logo1,
# title: "Web Developer",
# time:"Now",
# location:"Nairobi",
# description:"Web Developer: Designing and coding websites, ensuring functionality, and collaborating with team members in Nairobi.",
# company:"Linus Tech Co."
# },


class Employer_Model(models.Model):
    name = models.CharField(max_length=200)
    logo = CloudinaryField('image logo', null=True, blank=True)

    @property
    def logo_url(self):
        return (
            f"https://res.cloudinary.com/dlepgnfkx/{self.logo}"
        )

    def __str__(self):
        return self.name


class Job_Model(models.Model):

    TYPE = (('part-time', 'part-time'),
            ('remote', 'remote'), ('contract', 'contract'), ('negotiation', 'negotiation'))

    level = (('Senior', 'Senior'), ('Junior', 'Junior'),
             ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'))
    title = models.CharField(max_length=200)
    contract_type = models.CharField(
        max_length=200, choices=TYPE, default='negotiation')
    location = models.CharField(max_length=200,)
    level = models.CharField(max_length=200, choices=level, default='Senior')
    description = models.TextField()
    auther = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_posted = models.DateTimeField(timezone.now(), null=True, blank=True)
    employer = models.ForeignKey(
        Employer_Model, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
