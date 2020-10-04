# from flask import Flask
# app = Flask(__name__)
#

# import sys
# import os
from flask import Flask
# from flask_restful import reqparse, Api, Resource
# import json
# import pyodbc

# To run this app follow the README, but instead of running "flask run"
# just run "python ./app.py"

# Initialize Flask
app = Flask(__name__)

# Setup Flask Restful framework
# api = Api(app)
# parser = reqparse.RequestParser()
# parser.add_argument('customer')

# Create connection to Azure SQL
# server = 'financeapp-sqlserver.database.windows.net'
# database = 'FinanceApp-Database'
# username = 'azureuser'
# password = 'Ent6ehrt2@'
# driver= '{ODBC Driver 17 for SQL Server}'
# conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

@app.route("/")
def hello():
    return "Hello World!"

# # Customer Class
# class Customer(Resource):
#     def get(self, customer_id):
#         customer = {"CustomerID": customer_id}
#         # cursor = conn.cursor()
#         # # cursor.execute("SELECT TOP 2 Name as CategoryName FROM [SalesLT].[ProductCategory]")
#         # # cursor.execute(("SELECT TOP 2 Name as CategoryName FROM [SalesLT].[ProductCategory]""), json.dumps(customer))
#         # cursor.execute("SELECT TOP (1000) * FROM [dbo].[ExpensesTest]")
#         # row = cursor.fetchone()
#         # while row:
#         #     print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
#         #     row = cursor.fetchone()
#         # result = json.loads(cursor.fetchone()[0])
#         # cursor.close()
#         return "result", 200
#
# # Create API route to defined Customer class
# api.add_resource(Customer, '/customer', '/customer/<customer_id>')
#
# # Start App
# if __name__ == '__main__':
#     app.run(port=8000)
