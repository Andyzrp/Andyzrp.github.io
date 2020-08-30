import time

start = time.process_time()
for i in range(10000):
    print(i)
end = time.process_time()
print(f'different is {end - start}')
