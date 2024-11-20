import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

# start_time = time.time()
# for name in filenames:
#     read_info(name)
#
# linear_time = time.time() - start_time
# formatted_time = time.strftime('%H:%M:%S', time.gmtime(linear_time))
# print(f'{formatted_time} (линейный)')

# Многопроцессный

if __name__ == '__main__':
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, filenames)

    multiprocessing_time = time.time() - start_time
    formatted_time = time.strftime('%H:%M:%S', time.gmtime(multiprocessing_time))
    print(f'{formatted_time} (многопроцессный)')