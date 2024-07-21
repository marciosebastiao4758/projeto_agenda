from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Category
from django.db.models import Q
# from django.core.paginator import Paginator (fazer paginação depois)
from .forms import ContactForm
from django.urls import reverse


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

def create(request):
    form_action = reverse("contact:create")
    if request.method == "POST":
        # print(request.method)
        # print(request.POST.get("first_name")) 
        # print(request.POST.get("last_name")) 
        # print(request.POST.get("phone"))      
        
        form =  ContactForm(request.POST)
        
        context = {
                "form":form,
                "form_action":form_action,
            }
        if form.is_valid():
            # contact = form.save(commit=False)
            # contact.save()
            # print("O formulário é válido")        
            
            contact = form.save()
             
            return redirect("contact:update", contact_id = contact.pk)
        
        return render(request, "contact/contact_create.html",context)
    
    context = {
                "form":ContactForm(),
                "form_action":form_action,
            }
            
             
    return render(request, "contact/contact_create.html", context)
        
    


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        context = {
            "form": form,
            "form_action":form_action,
            }
        if form.is_valid():
            contact = form.save()
            return redirect("contact:update", contact_id = contact.pk)
        
        return render(request, "contact/contact_create.html", context)
        
    context = {
            "form": ContactForm(instance=contact),
            "form_action":form_action,
            }
    return render(request, "contact/contact_create.html", context)


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk = contact_id, show=True)
    confirmation = request.POST.get("confirmation", "no")
    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index")
    
    return render(request, "contact/contact.html", 
                  {"contact":contact, "confirmation":confirmation,})
    
        
    
    