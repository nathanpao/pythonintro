def myfun(x, *pos_param, **key_param):
    print(x)
    key_param['id'] = 123
    for each_arg in pos_param:
        print(each_arg)
    for key,value in key_param.items():
        print(key, value)
    modified_pos_param = pos_param+(50,)
    my_fun2(*modified_pos_param, **key_param)

def my_fun2(*args, **kwargs):
    print(args)
    print(kwargs)

myfun(10, 20, 30, 40, name="Nathan", sal=10000000)