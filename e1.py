def get_name():
    while True:
        full_name = input('Your fullname, Please:')
        if full_name =="exit":
            print('Goodbye ...')
            break
        first_name = full_name.split(' ')[0]
        last_name = full_name.split(' ')[1]
        print('Your Fistname is {0}'.format(first_name))
        print('Your Lastname is {0}'.format(last_name))
        print()


