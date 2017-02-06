def fizzbuzz(run_to):
    fizz_dict = {i:"Fizz" for i in range(3, run_to+1, 3)}
    for j in range(5, run_to+1, 5):
        fizz_dict[j] = fizz_dict.get(j, '') + "Buzz"
    for k in range(1, run_to+1):
        print(fizz_dict.get(k, k))

fizzbuzz(100)