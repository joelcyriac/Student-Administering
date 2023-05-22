from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    physics_marks = models.PositiveIntegerField()
    chemistry_marks = models.PositiveIntegerField()
    maths_marks = models.PositiveIntegerField()
    computer_science_marks = models.PositiveIntegerField()

    def total_percentage(self):
        total_marks = (
            self.physics_marks +
            self.chemistry_marks +
            self.maths_marks +
            self.computer_science_marks
        )
        return (total_marks / 400) * 100
