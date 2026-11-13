# fruits = ["pear","mango","guava"]

# for fruit in fruits:
#     print(fruits)

#Finding the total score
# student_score = [143,135,167,123,134]
# sum = 0   
# for score in student_score:
#     sum += score
#     print(sum)
# sum = 0 
# for num in range(1,101):
#     sum += num

# print(sum)


for num in range(1,101):
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 5 == 0:
        print("Buzz")

    elif num % 3 == 0  :
        print("Fizz")
        
    print(num)

  
    
