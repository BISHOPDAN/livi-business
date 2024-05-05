from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User
from django.core.exceptions import ValidationError
# Create your models here.


class CompanyProfile(models.Model):
    cover_picture = models.ImageField(upload_to='company_cover_images')
    company_logo = models.ImageField(upload_to='company_logos')
    company_name = models.CharField(max_length=100, unique=True)
    tagline = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contact_number = PhoneNumberField(blank=True, null=True)
    average_turnover = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    momentum = models.TextField(blank=True)
    recognition = models.TextField(blank=True)
    compliments = models.TextField(blank=True)
    happy_clients = models.PositiveIntegerField(blank=True, null=True)
    awards_won = models.PositiveIntegerField(blank=True, null=True)
    projects = models.PositiveIntegerField(blank=True, null=True)
    twitter_url = models.CharField(max_length=250, blank=True)
    facebook_url = models.CharField(max_length=250, blank=True)
    instagram_url = models.CharField(max_length=250, blank=True)
    linkedin_url = models.CharField(max_length=250, blank=True)
    is_available = models.BooleanField(default=True)
    company_url = models.CharField(max_length=250, blank=True)
    user = models.OneToOneField(
        User, related_name="user_info", on_delete=models.CASCADE, unique=True)
    template_type = models.CharField(max_length=15, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    approved_status = models.CharField(max_length=10, default="Pending")

    def __str__(self):
        return self.company_name


class CompanyWorksDone(models.Model):
    company_id = models.ForeignKey(
        CompanyProfile, related_name='company_info', on_delete=models.CASCADE)
    works_images = models.ImageField(upload_to='work_done_image')
    work_name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.work_name


class CompanyServices(models.Model):
    company_id = models.ForeignKey(
        CompanyProfile, related_name="company_details", on_delete=models.CASCADE)
    available_country = models.CharField(max_length=20, default="")
    available_state = models.CharField(max_length=20, default="")
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.service_name

    class Meta:
        unique_together = ('service_name', 'company_id')


class CompanySubServices(models.Model):
    company_services = models.ForeignKey(
        CompanyServices, on_delete=models.CASCADE)
    sub_service_cover_picture = models.ImageField(
        upload_to='company_sub_service_cover_picture', blank=True)
    sub_service_name = models.CharField(max_length=100)
    sub_service_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.sub_service_name

    class Meta:
        unique_together = ('company_services', 'sub_service_name')


class CompanyEnquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(
        CompanySubServices, on_delete=models.CASCADE)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    enquiry_status = models.CharField(max_length=10, default='Pending')
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user.username} enquired {self.sub_service.company_services.company_id.company_name}"

    class Meta:
        unique_together = ['user', 'sub_service', 'email', 'message']


class HREmployees(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='employee_profile_image', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = PhoneNumberField(blank=True, null=True)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    ZIP_code = models.CharField(max_length=10)
    # Emergency Details
    emergency_contact_name = models.CharField(
        max_length=100, blank=True, null=True)
    emergency_contact_number = PhoneNumberField(blank=True, null=True)
    emergency_address = models.CharField(max_length=255, blank=True, null=True)
    emergency_city = models.CharField(
        max_length=50, blank=True, null=True)
    emergency_state = models.CharField(
        max_length=50, blank=True, null=True)
    emergency_ZIPcode = models.CharField(
        max_length=10, blank=True, null=True)
    business_card_confirmation = models.BooleanField(default=False)
    # Professional information
    employee_id = models.CharField(max_length=6, db_index=True)
    username = models.CharField(max_length=50)
    work_type = models.CharField(max_length=10)
    email = models.EmailField()
    designation = models.CharField(max_length=100)
    work_status = models.CharField(max_length=50)
    joining_date = models.DateField()
    office_location = models.CharField(max_length=50)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    HRA = models.DecimalField(max_digits=10, decimal_places=2)
    transportation_allowance = models.DecimalField(
        max_digits=10, decimal_places=2)
    other_allowance = models.DecimalField(max_digits=10, decimal_places=2)
    # Documents
    document_type = models.CharField(max_length=50, blank=True)
    documents = models.FileField(
        upload_to='employee_documents', blank=True, null=True)
    # uploaded_date = models.DateField()
    expiry_date = models.DateField()
    # bank details
    bank_name = models.CharField(max_length=50)
    bank_country = models.CharField(max_length=50, blank=True)
    iban_number = models.CharField(max_length=30, blank=True, null=True)
    swift_Code = models.CharField(max_length=15, blank=True, null=True)
    routing_number = models.CharField(max_length=15, blank=True, null=True)
    branch_name = models.CharField(max_length=50)
    account_holder_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        unique_together = ('company', 'employee_id')
        verbose_name = 'HR System Employees'


class Payroll(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    employee = models.ForeignKey(HREmployees, on_delete=models.CASCADE)
    payroll_date = models.DateField(auto_now=True)
    leave = models.IntegerField(blank=True, null=True)
    deduction = models.IntegerField(blank=True, null=True)
    salary_per_month = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.employee.first_name} {self.employee.last_name}"

    class Meta:
        unique_together = ('company', 'employee')
        verbose_name = 'Employees Payroll'


class BusinessCards(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    hr_employee = models.ForeignKey(
        HREmployees, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hr_employee.username}"

    class Meta:
        verbose_name_plural = 'Business Cards'


class JobsCategory(models.Model):
    name = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)


class Jobs(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    job_category = models.ForeignKey(JobsCategory, on_delete=models.CASCADE)
    job_position = models.CharField(max_length=50)
    job_type = models.CharField(max_length=20)
    job_nature = models.CharField(max_length=20)
    job_experience = models.IntegerField()
    no_of_vacancy = models.IntegerField()
    gender = models.CharField(max_length=15)
    posted_date = models.DateField()
    last_date_to_apply = models.DateField()
    close_date = models.DateField()
    language = models.CharField(max_length=15)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    education_level = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company.company_name


class LeadGeneration(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    lead_id = models.CharField(max_length=6, blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    email = models.EmailField()
    contact_number = PhoneNumberField(blank=True, null=True)
    name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20)
    lead_source = models.CharField(max_length=15)
    lead_owner = models.CharField(max_length=20)
    lead_status = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.company.company_name

    class Meta:
        unique_together = ('company', 'lead_id')


class CompanyServicePromotion(models.Model):
    company_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    service_id = models.ForeignKey(CompanyServices, on_delete=models.CASCADE)
    sub_service_id = models.ForeignKey(
        CompanySubServices, on_delete=models.CASCADE)
    promotion_name = models.CharField(max_length=100)
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    promotion_valid_from = models.DateField()
    promotion_valid_to = models.DateField()
    promotion_cover_picture = models.ImageField(
        upload_to='company_promotion_picture', blank=True)
    voucher_code = models.CharField(max_length=100)
    one_time_usage = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.promotion_name

    class Meta:
        unique_together = ('company_id', 'service_id',
                           'sub_service_id', 'promotion_name')


class CompanyDocuments(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=30)
    issued_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    document = models.FileField(upload_to='company_documents')
    document_status = models.CharField(max_length=10, default="Active")
    is_available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.document_name

    class Meta:
        unique_together = ('company', 'document_name')


class QrCodeForBusinessCard(models.Model):
    business_card = models.ForeignKey(BusinessCards, on_delete=models.CASCADE)
    qr_image = models.ImageField(upload_to='business_card_qr_image')
    url = models.CharField(max_length=255)


class QrCodeForCompany(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    qr_image = models.ImageField(upload_to='company_qr_image')
    url = models.CharField(max_length=255)
