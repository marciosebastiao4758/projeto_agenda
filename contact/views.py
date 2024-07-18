from django.shortcuts import render, redirect
from .models import Contact, Category
from django.db.models import Q


def index(request):
    # filtrando os contatos pelo campo show=True e ordenando pelo id e fatiando
    contacts = Contact.objects\
        .filter(show=True)\
            .order_by("-id")[:10]
            # printando a consulta sql no terminal
    # print(contacts.query)
        
    return render(request, "contact/index.html", {"contacts":contacts})

def contact(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)
    return render(request, "contact/contact.html", {"contact":single_contact})


def search(request):
    # pegando o valor do request com request.GET sendo que get("q", "") está pegando valor do nome
    search_value = request.GET.get("q", "").strip()
    if search_value == "":
        return redirect("contact:index")
        
            # printando a consulta sql no terminal
    # print("search_value", search_value)
    # filtrando os contatos pelo campo show=True e ordenando pelo id e fatiando
    contacts = Contact.objects\
        .filter(show=True)\
            .filter(
                Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(email__icontains=search_value) |
                Q(phone_icontains=search_value) 
                )\
            .order_by("-id")
    # printando a consulta:
    print(contacts.query)
        
    return render(request, "contact/index.html", {"contacts":contacts})