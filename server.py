from bson import ObjectId
from colorama import Cursor
from flask import Flask, request
from about import me
from data import mock_data
from flask_cors import CORS

import random
import json
from config import db

app= Flask ('server')
CORS(app)   #allow request from any origin 
# print("hello from server")




@app.get("/")
def home():
    return "hello from server"

@app.get("/test")
def test():
    return "test"



@app.get("/about")
def about():
    return "this is the bookstore"




###################################################################################
#################### API ENDPOINTS =PRODUCTS ###################################
###################################################################################


@app.get("/api/version")
def version():
    return "1.0"


@app.get("/api/about")
def aboutMe():
    # return me["first"] + " " +me["last"]
    # return f
    return json.dumps(me) #parse dicitonary into json string


def fix_mongo_id(obj):
    obj['id']=str(obj["_id"])
    del obj["_id"]
    return obj



#get api products, return mock data in json string
@app.get("/api/products")
def aboutProducts():

    cursor=db.products.find({})
    results=[]
    for prod in cursor:
        fix_mongo_id(prod)
        results.append(prod)
    # return me["first"] + " " +me["last"]
    # return f
    return json.dumps(results) #parse dicitonary into json string

@app.post("/api/products")
def save_product():
    product= request.get_json()

    # add product to cat, assign an id to product, return as json

    # print(product)

    # mock_data.append(product)
    # product["id"]= random.randint(1, 123123123123)

    db.products.insert_one(product)
    fix_mongo_id(product)

    # product["_id"]=str(product["_id"])

    # del product["_id"]

    # print(product)

    return json.dumps(product)

    # print(product)

    

# @app.post("/api/products")
@app.get("/api/products/<id>")
def get_product_by_id(id):
    prod = db.products.find_one({"_id": ObjectId(id)})
    if not prod:
        return "not found"

    fix_mongo_id(prod)
    return json.dumps(prod)


    # return "id is : " + id
    # for user in mock_data:
    #     if user["id"]== id:
    #         thing= json.dumps(user)
    # return thing
    # for prod in mock_data:
    #     if str(prod["id"])==id:
    #         return json.dumps(prod)


    # return "not found"


@app.get("/api/products_category/<category>")
def prod_categories(category):
    cursor=db.products.find({"category": category})
    results=[]
    for prods in cursor:
        fix_mongo_id(prods)
        results.append(prods)


    # list = []
    # for prods in mock_data:
    #     if prods["category"].lower() == category.lower():
    #         list.append(prods)


    return json.dumps(results)
    

@app.get("/api/products_cheapest") 
def get_cheapest():
    # prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]
    # solution = prices[0]
    # for num in prices:
    #     if num>solution:
    #         solution=num
    # print (solution)

    # cursor=db.products.find({})
    # results=[]
    # for prod in cursor:
    #     fix_mongo_id(prod)
    #     results.append(prod)


    cursor=db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution=prod
    
    fix_mongo_id(solution)

    # solution = mock_data[0]
    # for prod in mock_data:
    #     if prod["price"] < solution["price"]:
    #         solution=prod
    return json.dumps(solution)


    

@app.get("/api/categories")
def get_categories():
    # list=[]
    # listed=[]
    # for cat in mock_data:
    #     list.append(cat["category"])
    #     if not cat["category"]  in listed:venv
    #         listed.append(cat["category"])

    categories=[]
    cursor=db.products.find({})
    for product in cursor:
        cat=product["category"]
        if not cat in categories:
            categories.append(cat)
    
    return json.dumps(categories)


    # categories=[]
    # cursor= db.products.find({})
    #     for product in cursor:
    #     list.append(cat["category"])
    #     if not cat["category"]  in listed:
    #         listed.append(cat["category"])


    # categories=[]
    # for product in mock_data:
    #     cat= product["category"]
    #     if not cat in categories:
    #         categories.append(cat)

    

    # return json.dumps(listed)


# return # of prods in catalog
# api/count_products

@app.get("/api/count_products")
def countPrpducts():
   cursor=db.products.find({})
   index=0
   for prod in cursor:
    index=index+1
   return json.dumps({"count": index})


@app.get("/api/search/<text>")
def returnText(text):
    results = []

    text=text.lower()
    for prod in mock_data:
        # if text in prod.title:
        if text in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)



    ################################################################################
    ############ API ENDPOINTS = coupoons codes ######################################



app.run(debug=True)