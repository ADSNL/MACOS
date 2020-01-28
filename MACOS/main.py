from flask import Flask, make_response, request, render_template

import pypyodbc

# creating an object
macos = Flask(__name__)

connection = pypyodbc.connect('Driver={SQL Server};Server=tcp:THINK_S30_01\ADSN,49172;Database=Customer;uid=ADSN;pwd=ADSN_2018')

# creating route for the application
@macos.route('/')
def index():
    return render_template('index.html')

@macos.route('/products')
def products():
    return render_template('products.html')

@macos.route('/books/<id>')
def books(id):
    cursor = connection.cursor()
    tempStr = "Select * from Books where Book_ID="+id
    # cursor.execute("Select TOP 1 * from Books")
    cursor.execute(tempStr)
    fetchData = cursor.fetchall()
    cursor.close()
    return render_template('books.html', data=fetchData)

@macos.route('/books/next')
def booksNext(data):
    intId=data[0]
    intId = intId+1
    tempStr = "Select * from Books where Book_ID = "+intId
    cursor = connection.cursor()
    #cursor.execute("Select * from Books where Book_ID = 1000001")
    cursor.execute(tempStr)
    fetchData = cursor.fetchall()
    cursor.close()
    return render_template('books.html', data=fetchData)

@macos.route('/clothing')
def clothing():
    return render_template('clothing.html')

@macos.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')

@macos.route('/makeup')
def makeup():
    return render_template('makeup.html')

@macos.route('/movies')
def movies():
    return render_template('movies.html')

@macos.route('/pets')
def pets():
    return render_template('pets.html')

@macos.route('/customers')
def customers():
    return render_template('customers.html')

@macos.route('/customerdetails')
def customerdetails():
    return render_template('customerdetails.html')

@macos.route('/reports')
def reports():
    return render_template('reports.html')

@macos.route('/averagespend20002002')
def averagespend20002002():
    return render_template('averagespend20002002.html')

@macos.route('/averagespend20032006')
def averagespend20032006():
    return render_template('averagespend20032006.html')

@macos.route('/averagespendyearlyquarterly')
def averagespendyearlyquarterly():
    return render_template('averagespendyearlyquarterly.html')

# checking and running the application
if __name__ == "__main__":
    macos.run(debug=True)


