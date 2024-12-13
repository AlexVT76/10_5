import time
import multiprocessing
def read_info(name):
    all_data = []
    with open (name,'r') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()



filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = time.time()

for filename in filenames:
    read_info(filename)
runtime = time.time() - start
print(f'Время выполнения {runtime}')
#if __name__ == '__main__':
    #start = time.time()
   # with multiprocessing.Pool() as pool:
       # pool.map(read_info, filenames)
    #runtime = time.time() - start
   # print(f"Время выполнения {runtime}")