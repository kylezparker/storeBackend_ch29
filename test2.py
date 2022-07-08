

def start_tests():
    print("---------list tests-----------")


    nums = [1,2,2,2,2,2,2,4,2,3,3,3,3,3,3,3,4,4,4,4,5,5,5,7]

    # read from the list
    print(nums[0])
    print(nums[1])

    #add elements to a list
    nums.append(9)
    print(nums)




    # for loop
    for n in nums:
        print (n)




    # for loop from 0 and 20
    for number in range(0,21):
        print(number)







def test1():
    print("test1")
    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]

    # for n in prices:
    #     if n<50:
    #         print(n)




    # number of zeros
    count=0
    for n in prices:
        if n==0:
            # print(n)
            count+=1
    print (count)

    # sum of numbers over 0
    sum=0
    for n in prices:
        if n>0:
            # print(n)
            sum+=n
    print (sum)


    # sum of numbers 
    sums=0
    for n in prices:
        sums+=n
    print (sums)


def test2():
    print("test2")  

    users =  [
    {
        "gender": "F",
        "name": "Louis",
        "color": "Green"
    },
    {
        "gender": "M",
        "name": "Manuel",
        "color": "Gray"
    },
    {
        "gender": "F",
        "name": "Rossy",
        "color": "Pink"
    },
    {
        "gender": "F",
        "name": "Renny",
        "color": "pink"
    },
    {
        "gender": "M",
        "name": "Roman",
        "color": "Purple"
    },
    {
        "gender": "m",
        "name": "John",
        "color": "Pink"
    },
    {
        "gender": "F",
        "name": "Susan",
        "color": "Black"
    }
]

    # for i in users: 
    #     print(users['name'])

    # print(len(users))
    # print(len("asdasdasdasda"))

    # count=0
    # for user in users:
    #     # get name of user dictionary
    #     # print (user["name"])

    #     count+=1
    # print(count)

    for user in users:
        color= user["color"].lower()
        if color=="pink":
            print(user["name"])



def test3():
    print ("-----------------test3------------")
    prices = [123,3,23,6475,58,89,45,34,87,34,-12,23, 123,-23,-123, 0, 123, 0, -29, 10]
    solution = prices[0]
    for num in prices:
        if num>solution:
            solution=num
    print (solution)








# start_tests()
# test1()
# test2()
test3()