from django.db import models

# Create your models here.

class Penangkaran(models.Model):
     nama_tempat      = models.CharField(max_length=75)
     grs_lintang = models.FloatField(null=True)
     grs_bujur = models.FloatField(null=True)

     def __str__(self):
         return self.nama_tempat

class Data(models.Model):
     jenis  = models.CharField(max_length=75)
     deskripsi  = models.CharField(max_length=750)
     gambar    = models.ImageField(null=True, blank=True, upload_to="image/")
     
     def __str__(self):
         return self.jenis