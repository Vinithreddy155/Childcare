from django.db import models
# Users Model
class User(models.Model):
    ROLES = (
        ('SYS_ADMIN', 'System Administrator'),
        ('FAC_ADMIN', 'Facility Administrator'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=200)  # store hashed
    role = models.CharField(max_length=10, choices=ROLES)

# Facilities Model
class Facility(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('SYS_ADMIN', 'System Administrator'),
        ('FAC_ADMIN', 'Facility Administrator'),
        ('TEACHER', 'Teacher'),
        ('PARENT', 'Parent'),
    )
    role = models.CharField(choices=ROLES, max_length=10)


# Children Model
class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    allergies = models.TextField(blank=True)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="children")

# Enrollments Model
class Enrollment(models.Model):
    STATUS = (
        ('ENROLLED', 'Enrolled'),
        ('WITHDRAWN', 'Withdrawn'),
        ('WAITING', 'Waiting'),
    )
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    classroom_type = models.CharField(max_length=50)
    date_of_enrollment = models.DateField()
    date_of_withdrawal = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)

# Staff Model
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_hire = models.DateField()
    date_of_termination = models.DateField(null=True, blank=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

# ClassroomAssignments Model
class ClassroomAssignment(models.Model):
    classroom_type = models.CharField(max_length=50)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()

# Attendance Model
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()

# AccountingLedger Model
class AccountingLedger(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    week_start_date = models.DateField()
    week_end_date = models.DateField()
    payment_status = models.BooleanField(default=False)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

# Payments Model
class Payment(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    ledger = models.ForeignKey(AccountingLedger, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
