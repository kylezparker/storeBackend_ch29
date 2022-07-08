# imports/global/fn def/instructions





def run_test():
    print("test 1-dictionaries")


    me = {
        "first": "kyle",
        "last" : "parker",
        "age" : 29,
        "hobbies" : [],
        "address": {
            "street": "evergreen",
            "number": "22-b",
            "city": "springfield",
            "state":"ca",
            "zip": "92011"
        }
    }


    print(me)
    print(me["first"])
    print(me["first"]+" "+me["last"])


# change keys
    me["age"]= me["age"] + 1
    me["age"]=99


# add keys
    me["preferred_color"]= "purple"

    print(me)


# read if exits

    if "middle" in me: #checks for existence
        print(me["middle"])
    address= me["address"]
    print(type(address))
# print full address

    # print(me["address"])
    print(f'{address["street"]} #{address["number"]}')
    print(me["address"]["street"]+ " " +me["address"]["number"]+ " " +me["address"]["city"]+ " " +me["address"]["state"]+ " " +me["address"]["zip"])
run_test()





# f strings in python
