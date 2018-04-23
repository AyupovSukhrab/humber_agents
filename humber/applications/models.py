from django.db import models
from django.urls import reverse

class Agent(models.Model):
    agent_name = models.CharField(max_length=200, default=None)
    other_agent_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    middle_name = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, default=None)
    province = models.CharField(max_length=200, verbose_name='Province/State', blank=True)
    city = models.CharField(max_length=200, default=None)
    street = models.CharField(max_length=200, default=None)
    office = models.CharField(max_length=200, verbose_name='Apartment/Office', default=None)
    postal_code = models.CharField(max_length=200, default=None)
    phone_num1 = models.CharField(max_length=20, verbose_name='Phone number', default=None)
    phone_num2 = models.CharField(max_length=20, blank=True, verbose_name='Alternative phone number', default=None)
    email1 = models.EmailField(max_length=100, verbose_name='Email address', default=None)
    email2 = models.EmailField(max_length=100, blank=True, verbose_name='Second email address')
    email3 = models.EmailField(max_length=100, blank=True, verbose_name='Third email address')
    website = models.CharField(max_length=200, default=None, blank=True)

    def __str__(self):
        return self.agent_name

    def get_absolute_url(self):
        return reverse(Agent, kwargs={'id': self.id})

class AgentStatus(models.Model):
    selections = {
        ('new agent', 'new agent'),
        ('approved', 'approved'),
        ('not approved', 'not approved'),
        ('cancelled', 'cancelled'),
    }
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices= selections, default='new agent')

    def __str__(self):
        return self.status
