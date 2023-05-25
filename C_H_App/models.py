from django.db import models

# Create your models here.
from django.db import models

from django.contrib.auth.models import User, AbstractBaseUser

from cloudinary.models import CloudinaryField

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


class Company_Model(models.Model):
    name = models.CharField(max_length=200)
    logo = CloudinaryField('Cv file', null=True, blank=True)

    @property
    def logo_url(self):
        return (
            f"https://res.cloudinary.com/dlepgnfkx{self.logo}"
        )

    def __str__(self):
        return self.name


class Job_Model(models.Model):
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.ForeignKey(Company_Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
