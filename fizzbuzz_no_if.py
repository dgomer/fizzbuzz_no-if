def fizzbuzz(run_to):
    ''' FizzBuzz, in constant memory space, with no if statements.

    Arguments:
        run_to: The integer value (>0) to generate FizzBuzzes up to. 
    '''
    fizz_num = 3
    buzz_num = 5
    period = fizz_num * buzz_num
    fizz_dict = {i:"Fizz" for i in range(0, period+1, 3)}
    for j in range(0, period+1, 5):
        fizz_dict[j] = fizz_dict.get(j, '') + "Buzz"
    for k in range(1, run_to+1):
        print(fizz_dict.get(k%period, k))

fizzbuzz(100)