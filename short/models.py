from django.db import models
from .utils import create_shortcode, code_generator

class URL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True, blank=True)
    count       = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
            self.count = 1
        super(URL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
