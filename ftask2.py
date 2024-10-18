# Activity 2
# On the following slide is an example of a function that 
# includes a parameter. 
# Parameters are responsible for functions being able to 
# work on different data inputs. 
# Edit the snippet on the following slide to include two or more parameters and
# a running order count updated when the function is called

# base = {
#     "Thin" : "1",
#     "Deep" : "2",
#     "Stuffed" : "3"
# }


order_count = 0




def take_order(base,topping,topping2):
    global order_count
    # input("Choose Base: ")
    # input("Choose Topping 1: ")
    # input("Choose Topping 2: ")
    print("{} Pizza with {} and {}". format(base,topping,topping2))
    order_count += 1
    

take_order(input("Choose Base: "),input("Choose Topping 1: "),input("Choose Topping 2: "))