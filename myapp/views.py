from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Person
from .models import Business

# Django will route e.g. http://exampleserver.ed.ac.uk/list to this function
# The "request" object contains extra information about the request.
# The function returns an HttpResponse object, which will be translated
# into HTTP and sent back to the browser.
def list(request):
    response_html = "<h1>This is the list of contacts:</h1><table>"
    for person in Person.objects.all(): # Person.objects.all() returns one object per row in the Person table
        # in Python, f" .... {variable_name} .... " provides a convenient way of
        # substituting variables into a string. Using a triple quote """ rather than ' or " allows
        # the string to be split over multiple lines. 
        response_html += f"""
        <tr>
            <td class="first_name">{person.first_name}</td>
            <td class="last_name">{person.last_name}</td>
            <td class="tel">{person.tel}</td>
            <td class="email">{person.email}</td>
        <tr>
        """
        
    for business in Business.objects.all(): 
        response_html += f"""
        <tr>
            <td class="first_name">{person.first_name}</td>
            <td class="last_name">{person.last_name}</td>
            <td class="tel">{person.tel}</td>
            <td class="email">{person.email}</td>
        <tr>
        """

    # End the table, send the response to the request
    response_html += "</table>"
    return HttpResponse(response_html)

def summary(request):
    # count the number of people and businesses
    person_count, business_count = 0, 0
    for person in Person.objects.all():
        person_count += 1 # increase person_count by 1
    for business in Business.objects.all():
        business_count += 1 # increase business_count by 1
    # in Python, f" .... {variable_name} .... " provides a convenient way of
    # substituting variables into a string. Using a triple quote """ rather than ' or " allows
    # the string to be split over multiple lines. 

    # create a summary
    response_html += f"""
    <p>The number of people in your address book is {person_count}.</p>
    <p>The number of businesses in your address book is {business_count}.</p>
    """
    return HttpResponse(response_html)

# Instead of writing lots of code to handle forms manually, Django allows us to subclass a "generic view"
# (provided as part of the framework) which will do a lot of the work for us.
class PersonCreateView(CreateView):
    model = Person
    fields = ["first_name","last_name","tel","email"]
    success_url = reverse_lazy("list") # redirect to list when successfully created

class BusinessCreateView(CreateView):
    model = Business
    fields = ["business_name","tel","email"]
    success_url = reverse_lazy("list") # redirect to list when successfully created
