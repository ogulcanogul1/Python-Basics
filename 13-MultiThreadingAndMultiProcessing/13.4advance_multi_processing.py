from concurrent.futures import ProcessPoolExecutor

import time


def square_num(num):
    time.sleep(0.5)
    return num ** 3



numbers = [i for i in range(90)]




if __name__ == "__main__":

    process_start_time =  time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_num,numbers) 

    for result in results:
        print(result)
    
    process_end_time = time.time() - process_start_time 

    print(f"process end time : {process_end_time}")


    start_time =  time.time()
    result_nums = map(square_num,numbers)

    for result in result_nums :
        print(result)

    end_time = time.time() - start_time 
    print(f"process end time : {process_end_time}")
    print(f"end time : {end_time}")



