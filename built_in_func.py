def check_age(age):
    if age < 18:
        print('oooops, you are below voting age.')
    else:
        print('you are eligible to vote')

        # .endswith is a built in function to check if a given parameter ends with the passed argument.
        print('hello'.endswith('X'))
        print('hello'.endswith('o'))


check_age(30)
check_age(77)
check_age(45)
