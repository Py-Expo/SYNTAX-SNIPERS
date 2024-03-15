from flask import Flask, request, render_template, redirect, url_for
from collections import namedtuple

app = Flask(__name__)

# Dummy user data for demonstration
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

Bill = namedtuple('Bill', ['vendor_name', 'vendor_address', 'vendor_contact', 'amount', 'date', 'invoice_number', 'description'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Redirect to the bill comparison page if login is successful
            return redirect(url_for('check_bills'))
        else:
            # Redirect back to login page with an error message
            return render_template('login.html', error="Invalid username or password.")

    # Render the login page if GET request
    return render_template('login.html')

@app.route('/check_bills', methods=['POST'])
def check_bills():
    num_bills = int(request.form['num_bills'])
    bills = []

    for i in range(num_bills):
        bill = Bill(
            request.form[f'vendorName_{i}'],
            request.form[f'vendorAddress_{i}'],
            request.form[f'vendorContact_{i}'],
            float(request.form[f'amount_{i}']),
            request.form[f'date_{i}'],
            request.form[f'invoiceNumber_{i}'],
            request.form[f'description_{i}']
        )
        bills.append(bill)

    duplicate_bills, updated_bills = identify_duplicates(bills)

    return render_template('result.html', duplicate_bills=duplicate_bills, updated_bills=updated_bills)

def identify_duplicates(bills):
    seen = set()
    duplicates = []
    updated_bills = []

    for bill in bills:
        bill_info = (
            bill.vendor_name, bill.vendor_address, bill.vendor_contact,
            bill.amount, bill.date, bill.invoice_number, bill.description
        )

        if bill_info in seen:
            duplicates.append(bill)
        else:
            seen.add(bill_info)
            updated_bills.append(bill)

    return duplicates, updated_bills

if __name__ == '__main__':
    app.run(debug=True)
