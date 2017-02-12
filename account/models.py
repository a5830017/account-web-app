from django.db import models

# Create your models here.
class Account(models.Model):
    account_text = models.CharField(max_length=200)
    total_money = models.IntegerField(default=0)

    def __str__(self):
        return self.account_text

class List(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    list_text = models.CharField(max_length=200)
    get_money = models.IntegerField(default=0)
    pay_money = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.list_text