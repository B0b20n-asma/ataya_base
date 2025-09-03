from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MemberContribution, TraderContribution, FinancialReport
from .forms import MemberContributionForm, TraderContributionForm, FinancialReportForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


@login_required
def dashboard(request):
    members = MemberContribution.objects.all()
    traders = TraderContribution.objects.all()
    reports = FinancialReport.objects.all()
    return render(request, 'bmab/dashboard.html', {'members': members, 'traders': traders, 'reports': reports})

@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MemberContributionForm()
    return render(request, 'bmab/form.html', {'form': form, 'title': 'Add Member'})
@login_required
def view_member(request, pk):
    member = MemberContribution.objects.get(pk=pk)
    return render(request, 'bmab/view_member.html', {'member': member})

@login_required
def update_member(request, pk):
    member = get_object_or_404(MemberContribution, pk=pk)
    if request.method == 'POST':
        form = MemberContributionForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MemberContributionForm(instance=member)
    return render(request, 'bmab/form.html', {'form': form, 'title': 'Update Member'})

@login_required
def delete_member(request, pk):
    member = get_object_or_404(MemberContribution, pk=pk)
    member.delete()
    return redirect('dashboard')

# Similarly for Trader
@login_required
def add_trader(request):
    if request.method == 'POST':
        form = TraderContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TraderContributionForm()
    return render(request, 'bmab/form.html', {'form': form, 'title': 'Add Trader'})

@login_required
def view_trader(request, pk):
    trader = TraderContribution.objects.get(pk=pk)
    return render(request, 'bmab/view_trader.html', {'trader': trader})

@login_required
def update_trader(request, pk):
    trader = get_object_or_404(TraderContribution, pk=pk)
    if request.method == 'POST':
        form = TraderContributionForm(request.POST, instance=trader)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TraderContributionForm(instance=trader)
    return render(request, 'bmab/form.html', {'form': form, 'title': 'Update Trader'})

@login_required
def delete_trader(request, pk):
    trader = get_object_or_404(TraderContribution, pk=pk)
    trader.delete()
    return redirect('dashboard')

@login_required
def add_financial_report(request):
    if request.method == 'POST':
        form = FinancialReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FinancialReportForm()
    return render(request, 'bmab/form.html', {'form': form, 'title': 'Add Financial Report'})

# View Financial Report
@login_required
def view_financial_report(request, pk):
    report = get_object_or_404(FinancialReport, pk=pk)
    return render(request, 'bmab/view_financial_report.html', {'report': report})

# Update Financial Report
@login_required
def update_financial_report(request, pk):
    report = get_object_or_404(FinancialReport, pk=pk)
    if request.method == 'POST':
        form = FinancialReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FinancialReportForm(instance=report)
    return render(request, 'bmab/form.html', {'form': form, 'title': 'Update Financial Report'})

# Delete Financial Report
@login_required
def delete_financial_report(request, pk):
    report = get_object_or_404(FinancialReport, pk=pk)
    report.delete()
    return redirect('dashboard')


def logout_view(request):
    """Logs out the user and redirects to login page with a message."""
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # make sure 'login' is your login URL name

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("dashboard")  # 👈 change 'dashboard' to your home page URL name
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "bmab/login.html")