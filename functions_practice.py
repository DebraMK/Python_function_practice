# function with no return
def hello():
    print("Hello, welcome to this file")

# function with 3 arguments returning a list
def pack(petname, age, species):
    return (petname + "," + age + "," + species)

# function that returns series of strings with unlimited list length
def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food)):
            if i == 0:    
                print(f"First I eat {food[0]}")  
            else:    
                print(f"Next I eat {food[i]}") 
    
        
hello() 
print(pack("Rue", "3", "cat"))
eat_lunch([])
eat_lunch(["cookies!"])
eat_lunch(["sandwich", "grapes", "cookies"])

