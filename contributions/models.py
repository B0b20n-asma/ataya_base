from django.db import models

MONTHS = [
    ('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'),
    ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'),
    ('Jul', 'July'), ('Aug', 'August'), ('Sep', 'September'),
    ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December'),
]

class MemberContribution(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    # Monthly contributions
    Jan = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Feb = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Mar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Apr = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    May = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Jun = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Jul = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Aug = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Sep = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Oct = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Nov = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Dec = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total_amount(self):
        return sum([self.Jan,self.Feb,self.Mar,self.Apr,self.May,self.Jun,
                    self.Jul,self.Aug,self.Sep,self.Oct,self.Nov,self.Dec])

    def __str__(self):
        return f"{self.name} ({self.number})"


class TraderContribution(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    amount_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    total_months_subscribed = models.IntegerField(default=0)
    # Monthly contributions
    Jan = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Feb = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Mar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Apr = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    May = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Jun = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Jul = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Aug = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Sep = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Oct = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Nov = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Dec = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total(self):
        return self.amount_per_month * self.total_months_subscribed

    def __str__(self):
        return f"{self.name} ({self.number})"


class FinancialReport(models.Model):
    year = models.IntegerField()
    # INCOME
    balance_brought_forward = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_members = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_traders = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    remaining_sick_death = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_donors = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # EXPENDITURE
    withdrawal_from_treasurer = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    other_expenses = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    @property
    def total_income(self):
        return self.balance_brought_forward + self.total_members + self.total_traders + self.remaining_sick_death + self.total_donors

    @property
    def total_expenditure(self):
        return self.withdrawal_from_treasurer + self.other_expenses

    @property
    def yearly_income(self):
        return self.total_income - self.total_expenditure

    def __str__(self):
        return f"Financial Report ({self.year})"