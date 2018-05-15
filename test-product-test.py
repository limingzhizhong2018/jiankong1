product_list = [('iphone', 5000), ('MacBook', 12000)]
print(product_list)
salary = input("In put your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("what is your shopping:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
        else:
            input("what is your shopping:")
            if user_choice.isdigit():
                user_choice = int(user_choice)





