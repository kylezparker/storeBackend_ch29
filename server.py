from flask import Flask
from about import me
from data import mock_data
import json

app= Flask ('server')
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



#get api products, return mock data in json string
@app.get("/api/products")
def aboutProducts():
    # return me["first"] + " " +me["last"]
    # return f
    return json.dumps(mock_data) #parse dicitonary into json string

# @app.post("/api/products")
@app.get("/api/products/<id>")
def get_product_by_id(id):
    # return "id is : " + id
    # for user in mock_data:
    #     if user["id"]== id:
    #         thing= json.dumps(user)
    # return thing
    for prod in mock_data:
        if str(prod["id"])==id:
            return json.dumps(prod)


    return "not found"


@app.get("/api/products_category/<category>")
def prod_categories(category):
    list = []
    for prods in mock_data:
        if prods["category"].lower() == category.lower():
            list.append(prods)


    return json.dumps(list)
    

@app.get("/api/products_cheapest") 
def get_cheapest():
    # prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]
    # solution = prices[0]
    # for num in prices:
    #     if num>solution:
    #         solution=num
    # print (solution)

    solution = mock_data[0]
    for prod in mock_data:
        if prod["price"] < solution["price"]:
            solution=prod
    return json.dumps(solution)


    

@app.get("/api/categories")
def categories():
    list=[]
    listed=[]
    for cat in mock_data:
        list.append(cat["category"])
        if not cat["category"]  in listed:
            listed.append(cat["category"])

    # categories=[]
    # for product in mock_data:
    #     cat= product["category"]
    #     if not cat in categories:
    #         categories.append(cat)

    

    return json.dumps(listed)





app.run(debug=True)