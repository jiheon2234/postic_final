from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Announce(models.Model):
    ann_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    career = models.CharField(max_length=45, blank=True, null=True)
    education = models.CharField(max_length=45, blank=True, null=True)
    emp_p = models.CharField(max_length=45, blank=True, null=True)
    emp_t = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=200)
    company_no = models.ForeignKey("Company", models.DO_NOTHING, db_column="company_no")
    worktype_no = models.ForeignKey("Worktype", models.DO_NOTHING, db_column="worktype_no")
    paytype_no = models.ForeignKey(
        "Paytype", models.DO_NOTHING, db_column="payType_no"
    )  # Field name made lowercase.
    paymoney = models.IntegerField(blank=True, null=True)
    sido_no = models.ForeignKey("Sido", models.DO_NOTHING, db_column="sido_no")
    detail_add = models.CharField(max_length=100, blank=True, null=True)
    x = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)
    y = models.DecimalField(max_digits=20, decimal_places=15, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def intreturn(self) -> int:
        return self.paytype_no + 1

    class Meta:
        managed = False
        db_table = "Announce"


class Company(models.Model):
    com_no = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    sector = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    established = models.CharField(max_length=45, blank=True, null=True)
    annual_sales = models.CharField(max_length=45, blank=True, null=True)
    homepage = models.CharField(max_length=100, blank=True, null=True)
    workercnt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "company"


class Paytype(models.Model):
    ptype_no = models.IntegerField(primary_key=True)
    type = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = "payType"


class Sido(models.Model):
    sido_no = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    momid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sido"


class Worktype(models.Model):
    wtype_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "worktype"
