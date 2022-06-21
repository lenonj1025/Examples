def do_math(*args, **kwargs):

    if kwargs['operation'] == 'add':
        my_sum = 0
        for element in args:
            my_sum += element

        return my_sum

    elif kwargs['operation'] == 'multiply':
        my_product = 1
        for element in args:
            my_product *= element

        return my_product


print(do_math(10, 20, 2, 5, operation="add"))
print(do_math(10, 20, 2, 5, operation="multiply"))

