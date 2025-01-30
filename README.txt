This is a very simple implementation of some features of an application for managing contact information.

You will not need to write any code for this exercise. The questions are designed to allow you to demonstrate your ability to think about code and to communicate your thinking.

As you answer the questions, imagine that you are the maintainer of this software. This means that you are allowed to consider changing any part of the design and implementation to improve the application.

The relevant files for the questions will be

django-example/myapp/models.py
django-example/myapp/views.py

There are four URLs accessible to the user in this application:

/ - the root of the application calls summary() to display counts of 
the number of people and the number of businesses in the address book.

/list - displays a list of contacts in a table

/add_person - adds a person to the address book

/add_business - adds a business to the address book
