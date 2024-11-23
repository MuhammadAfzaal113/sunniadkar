import uuid

from django.db import models


class Salawat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salawat_title = models.CharField(max_length=255)
    salawat_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.salawat_title

    class Meta:
        verbose_name = 'Salawat'
        verbose_name_plural = 'Salawat'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super(Salawat, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Salawat, self).delete(*args, **kwargs)


class SalawatTranslation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salawat = models.ForeignKey(Salawat, on_delete=models.CASCADE)
    language = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Salawat Translation'
        verbose_name_plural = 'Salawat Translations'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super(SalawatTranslation, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(SalawatTranslation, self).delete(*args, **kwargs)


class SalawatAudio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salawat = models.ForeignKey(Salawat, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.salawat.salawat_title

    class Meta:
        verbose_name = 'Salawat Audio'
        verbose_name_plural = 'Salawat Audios'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super(SalawatAudio, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(SalawatAudio, self).delete(*args, **kwargs)

#  Dua models


class DuaCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Dua Category'
        verbose_name_plural = 'Dua Categories'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super(DuaCategory, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(DuaCategory, self).delete(*args, **kwargs)


class Dua(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dua_title = models.CharField(max_length=255)
    dua_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(DuaCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.dua_title

    class Meta:
        verbose_name = 'Dua'
        verbose_name_plural = 'Duas'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super(Dua, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Dua, self).delete(*args, **kwargs)


class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_title = models.CharField(max_length=255)
    book_text = models.TextField()
    book_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
