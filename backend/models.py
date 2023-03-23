from django.db import models
from django.core.validators import RegexValidator


class MyForm(models.Model):
    class Meta:
        db_table = 'my_form'

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')
    fname = models.CharField(max_length=50, null=False, blank=False,
                             validators=[RegexValidator(r'^[a-zA-Z\s]+', message="Invalid characters")])
    lname = models.CharField(max_length=50, null=False, blank=False,
                             validators=[RegexValidator(r'^[a-zA-Z\s]+', message="Invalid characters")])
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False, db_index=True)
    gender = models.CharField(max_length=1, null=False, blank=False,
                              validators=[RegexValidator(r'^[a-zA-Z]+', message="Invalid characters")])
    dob = models.DateField(null=False, blank=False,
                           validators=[RegexValidator(r'^[0-9-]+', message="Invalid characters")])
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
