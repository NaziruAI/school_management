from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SchoolClass(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name = models.CharField(max_length=150)
    roll_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.roll_number}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.school_class.name}"


# models.py
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)
    form_master_for = models.ForeignKey(SchoolClass, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
        

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    continuous_assessment = models.FloatField()
    exam_score = models.FloatField()

    @property
    def total_score(self):
        return self.continuous_assessment + self.exam_score
