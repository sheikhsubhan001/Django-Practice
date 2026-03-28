from django.db import models

# Create your models here.
class Student(models.Model):
    Scholorship= [
        ('100', '100%'),
        ('75', '75%'),
        ('50', '50%'),
        ('25', '25%'),
        ('10', '10%'),
        ('0', 'No Scholarship'),
    ]


    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='student_pictures/')
    age = models.IntegerField()
    email = models.EmailField()
    scholorship = models.CharField(max_length=3, choices=Scholorship, default='0')

    def __str__(self):
        return self.name


# ONE to Many relationship between Student and Course

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='courses')

    credit_hours = [
        ("1", "1 cr"),
        ("2", "2 cr"),
        ("3", "3 cr"),
        ("4", "4 cr"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    credit_hours = models.CharField(max_length=1, choices= credit_hours, default="3")

    def __str__(self):
        return f'Student {self.student.name} Have course {self.name}'
    

# Many to Many relationship between Student and Club

class Club(models.Model):
    students = models.ManyToManyField(Student, related_name='clubs')

    club_types = [
        ('Sports', 'Sports'),
        ('Music', 'Music'),
        ('Art', 'Art'),
        ('Science', 'Science'),
        ('Literature', 'Literature'),
    ]
    type = models.CharField(max_length=20, choices=club_types, default='Sports')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'Club {self.name} of type {self.type}'
    
# One to One relationship between Student and Profile

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    portfolio_link = models.URLField()
    age = models.IntegerField()

    def __str__(self):
        return f'Profile of {self.student.name}'
