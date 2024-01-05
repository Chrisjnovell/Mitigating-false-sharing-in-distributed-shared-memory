import time
import threading
import matplotlib.pyplot as plt

# Define the number of iterations and array size
NUM_ITER = 100000000
ARR_SIZE = 8

# Define a function to simulate false sharing
def simulate_false_sharing(padding):
    arr = [0] * ARR_SIZE
    def increment(index):
        for i in range(NUM_ITER):
            arr[index] += 1

    # Create two threads to access adjacent array elements
    t1 = threading.Thread(target=increment, args=(0,))
    t2 = threading.Thread(target=increment, args=(1,))

    # Start the threads and wait for them to finish
    start_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.time()
    print("Time taken with padding of size", padding, ":", end_time - start_time, "seconds")
    return end_time - start_time

# Define lists to store padding sizes and times
padding_sizes = []
times = []

# Simulate false sharing without padding and record the time
padding_sizes.append(0)
start_time = time.time()
simulate_false_sharing(0)
end_time = time.time()
times.append(end_time - start_time)

# Simulate false sharing with padding of different sizes and record the times
for padding in range(1, 9):
    padding_sizes.append(padding)
    times.append(simulate_false_sharing(padding))

# Plot the results as a line graph
plt.plot(padding_sizes, times)
plt.xlabel("Padding size")
plt.ylabel("Time taken (seconds)")
plt.title("False sharing simulation with different padding sizes")
plt.show()
