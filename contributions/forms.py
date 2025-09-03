

from django import forms
from .models import MemberContribution, TraderContribution, FinancialReport

class MemberContributionForm(forms.ModelForm):
    class Meta:
        model = MemberContribution
        fields = '__all__'

class TraderContributionForm(forms.ModelForm):
    class Meta:
        model = TraderContribution
        fields = '__all__'

class FinancialReportForm(forms.ModelForm):
    class Meta:
        model = FinancialReport
        fields = '__all__'