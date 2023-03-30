from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def default_list():
    return "list"


def default_undefined():
    return "undefined"


class EUCountries(models.Model):
    class Meta:
        db_table = "countries_master"

    id = models.SmallAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                               blank=False, null=False, verbose_name='ID')
    country = models.CharField(max_length=50, null=False, blank=False,
                               validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Invalid characters")])
    country_code = models.CharField(max_length=2, null=False, blank=False,
                                    validators=[RegexValidator(regex=r'^[a-zA-Z]+$', message="Invalid characters")])
    calling_code = models.CharField(max_length=4, null=False, blank=False,
                                    validators=[RegexValidator(regex=r'^[0-9+]+$', message="Invalid characters")])
    status = models.BooleanField(default=1)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MyForm(models.Model):
    class Meta:
        db_table = 'my_form'

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')
    fname = models.CharField(max_length=50, null=False, blank=False,
                             validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Invalid characters")],
                             error_messages={'blank': 'This field is required', 'null': 'This field is required'})
    lname = models.CharField(max_length=50, null=False, blank=False,
                             validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Invalid characters")],
                             error_messages={'blank': 'This field is required', 'null': 'This field is required'})
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False, db_index=True,
                              error_messages={'unique': 'This email already exists', 'blank': 'This field is required',
                                              'null': 'This field is required'})
    contact_no = models.CharField(max_length=15, null=True, db_index=True, default='',
                                  validators=[RegexValidator(regex=r'^[0-9- ]+$', message="Invalid phone number")])
    countries_master_id = models.ForeignKey(EUCountries, on_delete=models.PROTECT, null=True, to_field="id")
    gender = models.CharField(max_length=1, null=False, blank=False,
                              validators=[RegexValidator(regex=r'^[a-zA-Z]+$', message="Invalid characters")])
    dob = models.DateField(null=False, blank=False,
                           validators=[RegexValidator(regex=r'^[0-9-]+$', message="Invalid characters")],
                           error_messages={'blank': 'This field is required', 'null': 'This field is required'})
    avatar = models.CharField(max_length=50, null=True, blank=True,
                              validators=[RegexValidator(regex=r'^[a-zA-Z0-9.-_]+$', message="Invalid characters")])
    descr = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Clean the data before saving
        self.fname = self.fname.strip()
        self.fname = ' '.join(elem.capitalize() for elem in self.fname.split())
        self.lname = self.lname.strip()
        self.lname = ' '.join(elem.capitalize() for elem in self.lname.split())
        self.email = self.email.strip().lower()

        # Call the superclass's save() method to save the instance to the database
        super().save(*args, **kwargs)


class AdminMenuMaster(models.Model):
    class Meta:
        db_table = "admin_menu_master"
        verbose_name = "admin_menu_master"

    id = models.SmallAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                               blank=False, null=False, verbose_name='ID')
    menu_name = models.CharField(max_length=20, null=False, blank=False, unique=True,
                                 validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Invalid characters")])
    menu_icon = models.CharField(max_length=10, null=False, blank=False, default='list',
                                 validators=[RegexValidator(regex=r'^[a-z-]+$', message="Invalid characters")])
    menu_route = models.CharField(max_length=20, unique=True,
                                  validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Invalid characters")])
    menu_order = models.SmallIntegerField(null=True, blank=True,
                                          validators=[RegexValidator(regex=r'^[0-9]+$', message="Invalid characters")])
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
