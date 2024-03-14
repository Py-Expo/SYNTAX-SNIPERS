import tkinter as tk
from tkinter import messagebox

class Bill:
    def __init__(self, vendor_name, date, amount, description, invoice_number):
        self.vendor_name = vendor_name
        self.date = date
        self.amount = amount
        self.description = description
        self.invoice_number = invoice_number

def identify_duplicates(bills):
    seen = set()
    duplicates = []
    for bill in bills:
        bill_info = (bill.vendor_name, bill.date, bill.amount, bill.description, bill.invoice_number)
        if bill_info in seen:
            duplicates.append(bill)
        else:
            seen.add(bill_info)
    return duplicates

def eliminate_duplicates(bills):
    unique_bills = []
    seen = set()
    for bill in bills:
        bill_info = (bill.vendor_name, bill.date, bill.amount, bill.description, bill.invoice_number)
        if bill_info not in seen:
            unique_bills.append(bill)
            seen.add(bill_info)
    return unique_bills

def submit_bill():
    vendor_name = vendor_entry.get()
    date = date_entry.get()
    amount = float(amount_entry.get())
    description = description_entry.get()
    invoice_number = invoice_number_entry.get()
    bill = Bill(vendor_name, date, amount, description, invoice_number)
    bills.append(bill)
    vendor_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    invoice_number_entry.delete(0, tk.END)

def generate_updated_bills():
    duplicates = identify_duplicates(bills)
    updated_bills = eliminate_duplicates(bills)
    
    # Display duplicate bills in a message box
    if duplicates:
        messagebox.showinfo("Duplicate Bills", f"Duplicate Bills:\n{', '.join([f'Vendor: {bill.vendor_name}, Date: {bill.date}, Amount: {bill.amount}, Description: {bill.description}, Invoice Number: {bill.invoice_number}' for bill in duplicates])}")
    
    # Display updated bills in a message box
    if updated_bills:
        messagebox.showinfo("Updated Bills", f"Updated Bills:\n{', '.join([f'Vendor: {bill.vendor_name}, Date: {bill.date}, Amount: {bill.amount}, Description: {bill.description}, Invoice Number: {bill.invoice_number}' for bill in updated_bills])}")

# Create Tkinter GUI
root = tk.Tk()
root.title("Expense Management System")

vendor_label = tk.Label(root, text="Vendor Name:")
vendor_label.grid(row=0, column=0)
vendor_entry = tk.Entry(root)
vendor_entry.grid(row=0, column=1)

date_label = tk.Label(root, text="Date:")
date_label.grid(row=1, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=1, column=1)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

description_label = tk.Label(root, text="Description:")
description_label.grid(row=3, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=3, column=1)

invoice_number_label = tk.Label(root, text="Invoice Number:")
invoice_number_label.grid(row=4, column=0)
invoice_number_entry = tk.Entry(root)
invoice_number_entry.grid(row=4, column=1)

submit_button = tk.Button(root, text="Submit Bill", command=submit_bill)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

generate_button = tk.Button(root, text="Generate Updated Bills", command=generate_updated_bills)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

bills = []

root.mainloop()
