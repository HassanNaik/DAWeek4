import random

#print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))

my_num = 13
ran_num = random.randint(1,50)

while my_num != ran_num:
    print(f"The number {ran_num} doesn't match my number {my_num}" )
    ran_num = random. randint(1,50)
    

print(f"The number {ran_num} matches my number {my_num}" )

