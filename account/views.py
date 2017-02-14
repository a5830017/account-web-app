from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Account, List


class IndexView(generic.ListView):
    template_name = 'account/index.html'
    context_object_name = 'account_list'

    def get_queryset(self):
        return Account.objects.order_by('account_text')


class DetailView(generic.DetailView):
    model = Account
    template_name = 'account/detail.html'


def AccSetting(request): #add account
    return render(request, "account/accsetting.html", '')

def addlist(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, "account/addlist.html", {'account': account },)

def listdb(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    try:
        addlist = request.POST['addlist']
        moneyget = request.POST['moneyget']
        moneypay = request.POST['moneypay']
    except (KeyError, List.DoesNotExist):
        pass
    else:
        if len(addlist)==0:
            return render(request, 'account/addlist.html', {
            'account': account,
            'error_message': "Please fill data in input box.",
        })
        else:
            account.list_set.create(list_text=addlist, get_money=moneyget, pay_money=moneypay, pub_date=timezone.now())
            return HttpResponseRedirect(reverse('account:detail', args=(account.id,)))


'''
    def add_list(self):
        try:
            addlist = request.POST['addlist']
            moneyget = request.POST['moneyget']
            moneypay = request.POST['moneypay']
        except:
            addlist = ""
            moneyget = ""
            moneypay = ""
        else:
            q = Account(list_text=addlist, get_money=moneyget, pay_money=moneypay, pub_date=timezone.now())
            q.save()'''
