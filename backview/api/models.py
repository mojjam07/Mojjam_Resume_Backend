from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.degree} at {self.institution_name}"
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    location = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    profile_picture = models.ImageField(upload_to='testimonial_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

class NewTestimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    profile_picture = models.ImageField(upload_to='new_testimonial_pics/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name

class Consult(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service_type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"New consult from {self.name} on {self.date}"
    
class Question(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    question = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"A new question from {self.name}"

class Images(models.Model):
    name = models.CharField(max_length=100)
    image_data = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
