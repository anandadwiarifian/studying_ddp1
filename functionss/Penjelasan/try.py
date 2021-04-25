def a_function(fixed_param, *tuple_param):
    print("fixed =", fixed_param)
    print("tuple =", tuple_param)

a_function(1, 2, 3, 4)
a_function(1)
a_function(fixed_param=4)
a_function(tuple_param=(1,2,3), fixed_param=1)