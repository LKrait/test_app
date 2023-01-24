from django.db import models
import random


SUBJECT = [
("English", "English"),("Mathematics", "Mathematics"),("Science", "Science"),("Social Science", "Social Science"),
("Arts", "Arts")
]


class AcademicYear(models.Model):
	academicyearid = models.CharField(
		max_length=10,default=random.randrange(10000,99999,1))
	academicyear = models.IntegerField(
		choices=[(2023, 2023), (2024, 2024), (2025, 2025)], verbose_name="Academic Year"
	)

	def __str__(self):
		return f'{self.academicyear}'


class Term(models.Model):
	termid = models.CharField(
		max_length=20, default=random.randrange(100,999,1))
	academicyearid = models.ForeignKey(
		to=AcademicYear, on_delete=models.CASCADE)
	order = models.IntegerField(
		choices=[(1,1), (2,2), (3,3), (4,4)], verbose_name="Term"
	)
	date_start = models.DateField(verbose_name="Term Commence")
	date_end = models.DateField(verbose_name="Term End")
	comment = models.CharField(max_length=255, blank=True)


class Week(models.Model):
	termid = models.ForeignKey(to=Term, on_delete=models.CASCADE)
	order = models.PositiveSmallIntegerField(choices=[
		(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12)], verbose_name="Week"
	)
	comment = models.CharField(max_length=255, blank=True)


class Subject(models.Model):
	subjectid = models.CharField(max_length=7, verbose_name="Subject ID", primary_key=True,
		default=random.randrange(10000,99999,1))
	subjectname = models.CharField(max_length=50, verbose_name="Subject", choices=SUBJECT)
	grade = models.CharField(
		max_length=2, choices=[(3,3), (4,4),(5,5),(6,6),(7,7),(8,8)]
	)
	academicyearid = models.ForeignKey(to=AcademicYear, on_delete=models.CASCADE)
	totalscore = models.PositiveSmallIntegerField()

	def __str__(self):
		return f'Grade {self.grade} {self.subjectname}'


class Assessment(models.Model):
	assessmentid = models.CharField(
		max_length=20, default=random.randrange(10000, 99999,1), primary_key=True)
	