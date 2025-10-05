import multiprocessing,time


def square_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"{i} square:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"{i} cube:{i*i*i}")

print("asdasfdasdfasfd")
if __name__ == "__main__":
    process_square =  multiprocessing.Process(target=square_numbers)
    process_cube =multiprocessing.Process(target=cube_numbers)

    start_time =  time.time()

    process_square.start()
    process_cube.start()

    ## Wait for the process to complete

    process_square.join()
    process_cube.join()

    end_time = time.time() - start_time

    print(end_time)


'''
Bu yüzden 3 kere görüyorsun print("asdasfdasdfasfd"):
1️⃣ Main process (senin asıl çalıştırdığın script)
2️⃣ process_square spawn edildiğinde dosya yeniden çalışıyor → print tekrar
3️⃣ process_cube spawn edildiğinde dosya yeniden çalışıyor → print tekrar

Ama if __name__ == "__main__": bloğunun içinde olmadığı için, her yeni process açıldığında o print de tekrar ediyor.
'''