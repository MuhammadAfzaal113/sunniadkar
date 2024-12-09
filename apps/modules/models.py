import uuid

from django.db import models
from apps.utils.abstract_models import CommonFields
from apps.modules.choices import *
from apps.user.models import User


class Salawat(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Salawat'
        verbose_name_plural = 'Salawat'

    def delete(self, *args, **kwargs):
        super(Salawat, self).delete(*args, **kwargs)


class SalawatTranslation(CommonFields):
    salawat = models.ForeignKey(Salawat, on_delete=models.CASCADE)
    
    language = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Salawat Translation'
        verbose_name_plural = 'Salawat Translations'

    def delete(self, *args, **kwargs):
        super(SalawatTranslation, self).delete(*args, **kwargs)


class SalawatAudio(CommonFields):
    salawat = models.ForeignKey(Salawat, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)

    def __str__(self):
        return self.salawat.title

    class Meta:
        verbose_name = 'Salawat Audio'
        verbose_name_plural = 'Salawat Audios'

    def delete(self, *args, **kwargs):
        super(SalawatAudio, self).delete(*args, **kwargs)

#  Dua models


class DuaCategory(CommonFields):
    category_name = models.CharField(max_length=255)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Dua Category'
        verbose_name_plural = 'Dua Categories'

    def delete(self, *args, **kwargs):
        super(DuaCategory, self).delete(*args, **kwargs)


class Dua(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(DuaCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Dua'
        verbose_name_plural = 'Duas'

    def delete(self, *args, **kwargs):
        super(Dua, self).delete(*args, **kwargs)


class Books(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Mewlid(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mewlid'
        verbose_name_plural = 'Mewlids'
        

class Qasida(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Qasida'
        verbose_name_plural = 'Qasidas'
        
class Lecture(CommonFields):
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lecture'
        verbose_name_plural = 'Lectures'
        
class Article(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class QA(CommonFields):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question & Answer'
        verbose_name_plural = 'Questions & Answers'


class Download(CommonFields):
    title = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Download'
        verbose_name_plural = 'Downloads'
        
class MarriageGuide(CommonFields):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Marriage Guide'
        verbose_name_plural = 'Marriage Guides'
        
        
class  LifeLesson(CommonFields):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.author.full_name
    
    class Meta:
        verbose_name = 'Life Lesson'
        verbose_name_plural = 'Life Lessons'
        

class PledgeSalawat(CommonFields):
    amount = models.IntegerField()
    name = models.CharField(max_length=255, default='Guest')
    address = models.TextField()
    salat = models.CharField(max_length=255, choices=SalatChoices.choices)
    
    def __str__(self):
        return self.salat
    
    class Meta:
        verbose_name = 'Pledge Salawat'
        verbose_name_plural = 'Pledge Salawats'
        
class Community(CommonFields):
    name = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    like = models.IntegerField(default=0)
    dua = models.IntegerField(default=0)
    ameen = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name