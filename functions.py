import json
import os
from pywebio.input import input
from pywebio.output import put_text
import re
rule = r"^[A-Z0-9\._+ '\"-]+\@[A-Z0-9]+\.[A-Z0-9]+"       

# Load customer data from file
def load_customers(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    else:
        return []

# Save customer data to file
def save_customers(customers, file_name):
    with open(file_name, 'w') as file:
        json.dump(customers, file)


# Add a new customer
def add_customer(customers, file_name):
    id = input("Enter customer id number: ")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    while True:
        x = re.match(r"^\S+@\S+\.\S+$", email)
        if x is None:
            email = input("Re-Enter customer email: ")
            put_text("Invalid!")
        else:
            put_text("Valid!")
            break
    phone = input("Enter customer phone number: ")
    while True:
        pattern = re.match(r"^[+]{1}(?:[0-9\\-\\(\\)\\/" \
              "\\.]\\s?){6,15}[0-9]{1}$",phone)
        if pattern is None:
            phone = input("Re-Enter customer phone number: ")
            put_text("Invalid!")
        else:
            put_text("Valid")
            break
    address = input("Enter customer address: ")
    customer = {"id": id, "name": name, "email": email, "phone": phone, "address": address}
    customers.append(customer)
    save_customers(customers, file_name)
    

# Update customer information
def update_customer(customers, file_name):
    email = input("Enter customer email: ")
    for customer in customers:
        if customer["email"] == email:
            customer["id"] = input("Enter new customer id number: ")
            customer["name"] = input("Enter new customer name: ")
            customer["phone"] = input("Enter new customer phone number: ")
            customer["address"] = input("Enter new customer address: ")
            save_customers(customers, file_name)
            put_text("Customer information updated.")
            return
    put_text("Customer not found.")

# Delete a customer
def delete_customer(customers, file_name):
    email = input("Enter customer email: ")
    for customer in customers:
        if customer["email"] == email:
            customers.remove(customer)
            save_customers(customers, file_name)
            put_text("Customer deleted.")
            return
    put_text("Customer not found.")

# Search for a customer
def search_customer(customers):
    email = input("Enter customer email: ")
    for customer in customers:
        if customer["email"] == email:
            put_text(f"Customer found! Customer id {customer['id']}")
            put_text(f"Name: {customer['name']}")
            put_text(f"Email: {customer['email']}")
            put_text(f"Phone: {customer['phone']}")
            put_text(f"Address: {customer['address']}")
            return
    put_text("Customer not found.")

# Display all customers
def display_customers(customers):
    for customer in customers:
        put_text("_________Here's customer information!_________")
        put_text("Customers:")
        put_text(f"Customer id number: {customer['id']}")
        put_text(f"Name: {customer['name']}")
        put_text(f"Email: {customer['email']}")
        put_text(f"Phone: {customer['phone']}")
        put_text(f"Address: {customer['address']}")
        put_text("_______________________________")
    put_text("Customer not found.")
