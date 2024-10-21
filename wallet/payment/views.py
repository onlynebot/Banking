from django.shortcuts import render
from .models import TransactionType, Transaction, PaymentAccount
from .forms import TransactionTypeForm
from django.views.generic import (
    ListView, DetailView, CreateView, 
    UpdateView, DeleteView
)
from django.urls import reverse_lazy
# Create your views here.

class TransactionTypeListView(ListView):
    model = TransactionType
    template_name = 'payment/transaction_type_list.html'
    context_object_name = 'transactiontypes'

class TransactionTypeCreateView(CreateView):
    model = TransactionType
    template_name = 'payment/transaction_type_create.html'
    form_class = TransactionTypeForm
    success_url = reverse_lazy('transaction_type_list')

class TransactionTypeDetailView(DetailView):
    model = TransactionType
    template_name = 'payment/transaction_type_detail.html'
    context_object_name = 'transactiontype'