import time
def print_numbers(thread_name):
	for i in range(1, 6):
		print(f"{thread_name} count: {i}")
		time.sleep(1)
import threading
thread1 = threading.Thread(target=print_numbers, args=("Thread 1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have completed execution.")
