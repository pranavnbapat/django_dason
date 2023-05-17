from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


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
    contact_no = models.CharField(max_length=15, unique=True, null=False, blank=False, db_index=True, default="",
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
    menu_name = models.CharField(max_length=30, null=False, blank=False, unique=True,
                                 validators=[RegexValidator(regex=r'^[a-zA-Z0-9()\s]+$', message="Invalid characters")])
    menu_icon = models.CharField(max_length=10, null=False, blank=False, default='list',
                                 validators=[RegexValidator(regex=r'^[a-z-]+$', message="Invalid characters")])
    menu_route = models.CharField(max_length=30, unique=True,
                                  validators=[RegexValidator(regex=r'^[a-zA-Z0-9\s-]+$', message="Invalid characters")])
    menu_access = models.CharField(max_length=30, unique=True,
                                   validators=[RegexValidator(regex=r'^[a-zA-Z0-9\s-]+$', message="Invalid characters")])
    menu_order = models.SmallIntegerField(null=True, blank=True,
                                          validators=[RegexValidator(regex=r'^[0-9]+$', message="Invalid characters")])

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu_name} ({self.menu_route})"
        # return self.menu_name


class KnowledgeObjects(models.Model):
    class Meta:
        db_table = "knowledge_objects"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PDF2Text(models.Model):
    class Meta:
        db_table = "pdf2text"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')
    old_filename = models.CharField(max_length=255, null=False, blank=False,
                                    validators=[RegexValidator(regex=r'^[\w\.-\s]+$', message="Invalid characters")])
    new_filename = models.CharField(max_length=255, null=False, blank=False)
    application_type = models.CharField(max_length=20, null=False, blank=False)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    file_text = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FakerModel(models.Model):
    class Meta:
        db_table = "faker_model"

    id = models.BigAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                             blank=False, null=False, verbose_name='ID')
    keywords = models.CharField(max_length=255, null=False, blank=False, db_index=True,
                                validators=[RegexValidator(regex=r'^[\w\.-\s,_]+$', message="Invalid characters")])
    description = models.TextField(blank=True, null=True)
    contact_no = models.CharField(max_length=10, db_index=True, default='',
                                  validators=[RegexValidator(regex=r'^[0-9- ]+$', message="Invalid phone number")])
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ElasticSearchStatistics(models.Model):
    search_term = models.CharField(max_length=255, db_index=True)
    column_name = models.CharField(max_length=255, db_index=True)
    hits = models.IntegerField(default=0)

    class Meta:
        db_table = "es_search_stats"
        unique_together = ('search_term', 'column_name')


class UserActivityLog(models.Model):
    class Meta:
        db_table = 'user_activity'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    method = models.CharField(max_length=10, default=None)
    user_timezone = models.CharField(max_length=63)
    activity = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.method} {self.activity} - {self.timestamp} - {self.user_timezone}"  # Include user_timezone here


class LargeFileUpload(models.Model):
    class Meta:
        db_table = "large_file_upload"

    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')
    old_filename = models.CharField(max_length=255, null=False, blank=False,
                                    validators=[RegexValidator(regex=r'^[\w\.-\s]+$', message="Invalid characters")])
    new_filename = models.CharField(max_length=255, null=False, blank=False)
    application_type = models.CharField(max_length=20, null=False, blank=False)
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ESLangMaster(models.Model):
    class Meta:
        db_table = "es_lang_master"

    id = models.SmallAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                               blank=False, null=False, verbose_name='ID')
    
    language_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    lang_code = models.CharField(max_length=3, blank=False, null=False, unique=True)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language_name


class ESCountriesMaster(models.Model):
    class Meta:
        db_table = "es_countries_master"

    id = models.SmallAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                               blank=False, null=False, verbose_name='ID')

    country_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    country_code = models.CharField(max_length=3, blank=False, null=False, unique=True)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name


class ESCityMaster(models.Model):
    class Meta:
        db_table = "es_city_master"

    id = models.SmallAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                               blank=False, null=False, verbose_name='ID')

    city_name = models.CharField(max_length=100, blank=False, null=False)
    es_countries_master_id = models.ForeignKey(ESCountriesMaster, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city_name


class ESContactNo(models.Model):
    class Meta:
        db_table = "es_contact_no"

    id = models.BigAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                             blank=False, null=False, verbose_name='ID')

    es_users_id = models.ForeignKey('ESUsers', on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=15, unique=True, blank=False, null=False)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_no


class ESUsers(models.Model):
    class Meta:
        db_table = "es_users"

    id = models.BigAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                             blank=False, null=False, verbose_name='ID')

    fname = models.CharField(max_length=50, verbose_name='First Name', blank=False, null=False)
    lname = models.CharField(max_length=50, verbose_name='Last Name', blank=False, null=False)
    dob = models.DateField(verbose_name='Date of Birth', blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', blank=False, null=False)
    address = models.TextField(verbose_name='Address', blank=False, null=False)
    city = models.ForeignKey(ESCityMaster, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class ESHobbies(models.Model):
    class Meta:
        db_table = "es_hobbies"

    id = models.BigAutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                             blank=False, null=False, verbose_name='ID')
    hobby_name = models.CharField(max_length=100, blank=True, null=True)
    es_users_id = models.ForeignKey(ESUsers, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hobby_name


class DefaultAuthUserExtend(AbstractUser):
    contact_no = models.CharField(max_length=10, null=True, db_index=True, default='', blank=True,
                                  validators=[RegexValidator(regex=r'^[0-9- ]+$', message="Invalid phone number")])


class PermissionMaster(models.Model):
    class Meta:
        unique_together = ('menu', 'action')
        db_table = "permission_master"

    ACTION_CHOICES = (
        ('add', 'add'),
        ('edit', 'edit'),
        ('view', 'view'),
        ('delete', 'delete'),
    )
    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    menu = models.ForeignKey(AdminMenuMaster, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.menu.menu_route}_{self.action}"


class CustomPermissions(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                             blank=False, null=False, verbose_name='ID')

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # permission_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    permission_name = models.ForeignKey(PermissionMaster, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "custom_permissions"
        unique_together = ('user', 'permission_name')

    def __str__(self):
        return str(self.permission_name)


class GroupCustomPermissions(models.Model):
    id = models.AutoField(primary_key=True, db_column='id', db_index=True, editable=False, unique=True,
                          blank=False, null=False, verbose_name='ID')

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission_name = models.ForeignKey(CustomPermissions, on_delete=models.CASCADE)

    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "custom_group_permissions"
        unique_together = ('group', 'permission_name')
