
from concurrent.futures import ThreadPoolExecutor
import time

def get_number(number):
    return f'num:{number}'


numbers = [i for i in range(51500)]


tp_start_time = time.time()


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(get_number,numbers)


for result in results:
    print(result)

tp_end_time = time.time() - tp_start_time
print(f"multi thread end time (3 thread) : {tp_end_time}")


##---------------------------------------------------------------------------------------------------------------------

start_time = time.time()


results = map(get_number,numbers)

for result in results:
    print(result)

end_time = time.time() - start_time


print(f"multi thread end time (3 thread) : {tp_end_time}")

print(f'1 thread end time : {end_time}')


'''
Normal map nasıl çalışıyor?

Python’un kendi map fonksiyonu:

def get_number(n):
    return f"num:{n}"

numbers = [1, 2, 3]
results = map(get_number, numbers)

for r in results:
    print(r)


Çıktı:

num:1
num:2
num:3


👉 map, listedeki her elemana sırayla fonksiyonu uygular ve sonuçları iterator olarak döner.

'''