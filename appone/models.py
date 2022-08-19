from distutils.command.build import build
from django.db import models

# Create your models here.

class breastCancer(models.Model):
    radius_mean = models.FloatField(null=True, blank=True, default=None)
    texture_mean = models.FloatField(null=True, blank=True, default=None)
    perimeter_mean = models.FloatField(null=True, blank=True, default=None)
    area_mean = models.FloatField(null=True, blank=True, default=None)
    smoothness_mean = models.FloatField(null=True, blank=True, default=None)
    compactness_mean = models.FloatField(null=True, blank=True, default=None)
    concavity_mean = models.FloatField(null=True, blank=True, default=None)
    concave_points_mean = models.FloatField(null=True, blank=True, default=None)
    symmetry_mean = models.FloatField(null=True, blank=True, default=None)
    radius_se = models.FloatField(null=True, blank=True, default=None)
    perimeter_se = models.FloatField(null=True, blank=True, default=None)
    compactness_se = models.FloatField(null=True, blank=True, default=None)
    area_se = models.FloatField(null=True, blank=True, default=None)
    concavity_se = models.FloatField(null=True, blank=True, default=None)
    concave_points_se = models.FloatField(null=True, blank=True, default=None)
    fractal_dimension_se = models.FloatField(null=True, blank=True, default=None)
    radius_worst = models.FloatField(null=True, blank=True, default=None)
    texture_worst = models.FloatField(null=True, blank=True, default=None)
    perimeter_worst = models.FloatField(null=True, blank=True, default=None)
    area_worst = models.FloatField(null=True, blank=True, default=None)
    smoothness_worst = models.FloatField(null=True, blank=True, default=None)
    compactness_worst = models.FloatField(null=True, blank=True, default=None)
    concavity_worst = models.FloatField(null=True, blank=True, default=None)
    concave_points_worst = models.FloatField(null=True, blank=True, default=None)
    symmetry_worst = models.FloatField(null=True, blank=True, default=None)
    fractal_dimension_worst = models.FloatField(null=True, blank=True, default=None)


class diabetes(models.Model):
    pregnancies=models.FloatField(null=True, blank=True, default=None)
    glucose=models.FloatField(null=True, blank=True, default=None)
    bloodpressure=models.FloatField(null=True, blank=True, default=None)
    skinthickness=models.FloatField(null=True, blank=True, default=None)
    insulin=models.FloatField(null=True, blank=True, default=None)
    bmi=models.FloatField(null=True, blank=True, default=None)
    dpf=models.FloatField(null=True, blank=True, default=None)
    age=models.FloatField(null=True, blank=True, default=None)

class heart(models.Model):
    age=models.FloatField(null=True, blank=True, default=None)
    sex=models.FloatField(null=True, blank=True, default=None)
    cp=models.FloatField(null=True, blank=True, default=None)
    trestbps=models.FloatField(null=True, blank=True, default=None)
    chol=models.FloatField(null=True, blank=True, default=None)
    fbs=models.FloatField(null=True, blank=True, default=None)
    restecg=models.FloatField(null=True, blank=True, default=None)
    thalach=models.FloatField(null=True, blank=True, default=None)
    exang=models.FloatField(null=True, blank=True, default=None)
    oldpeak=models.FloatField(null=True, blank=True, default=None)
    slope=models.FloatField(null=True, blank=True, default=None)
    ca=models.FloatField(null=True, blank=True, default=None)
    thal=models.FloatField(null=True, blank=True, default=None)

class kidney(models.Model):
    age=models.FloatField(null=True, blank=True, default=None)
    bp=models.FloatField(null=True, blank=True, default=None)
    al=models.FloatField(null=True, blank=True, default=None)
    su=models.FloatField(null=True, blank=True, default=None)
    rbc=models.FloatField(null=True, blank=True, default=None)
    pc=models.FloatField(null=True, blank=True, default=None)
    pcc=models.FloatField(null=True, blank=True, default=None)
    ba=models.FloatField(null=True, blank=True, default=None)
    bgr=models.FloatField(null=True, blank=True, default=None)
    bu=models.FloatField(null=True, blank=True, default=None)
    sc=models.FloatField(null=True, blank=True, default=None)
    pot=models.FloatField(null=True, blank=True, default=None)
    wc=models.FloatField(null=True, blank=True, default=None)
    htn=models.FloatField(null=True, blank=True, default=None)
    dm=models.FloatField(null=True, blank=True, default=None)
    cad=models.FloatField(null=True, blank=True, default=None)
    pe=models.FloatField(null=True, blank=True, default=None)
    ane=models.FloatField(null=True, blank=True, default=None)


class liver(models.Model):
    age=models.FloatField(null=True, blank=True, default=None)
    Total_Bilirubin=models.FloatField(null=True, blank=True, default=None)
    Direct_Bilirubin=models.FloatField(null=True, blank=True, default=None)
    Alkaline_Phosphotase=models.FloatField(null=True, blank=True, default=None)
    Alamine_Aminotransferase=models.FloatField(null=True, blank=True, default=None)
    Aspartate_Aminotransferase=models.FloatField(null=True, blank=True, default=None)
    Total_Protiens=models.FloatField(null=True, blank=True, default=None)
    Albumin=models.FloatField(null=True, blank=True, default=None)
    Albumin_and_Globulin_Ratio=models.FloatField(null=True, blank=True, default=None)
    Gender_Male=models.FloatField(null=True, blank=True, default=None)

class malaria(models.Model):
    image=models.ImageField()

class pneumonia(models.Model):
    image=models.ImageField()