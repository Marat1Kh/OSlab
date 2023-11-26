import subprocess
import time
import matplotlib.pyplot as plt

# Configuration
threads_num = 25
measure_time = 30
pid = "2158640"  # Replace with the actual PID you want to monitor

# Initialize variables for storing data
values = []
times = []

# Record start time for the measurement
start_time = time.time()

# Define the number of header lines in the 'top' command output
header_lines = 7

while time.time() - start_time < measure_time:
    # Execute 'top' command and get the output
    res = subprocess.check_output(["top", "-p", pid, "-H", "-o", "PID", "-b", "-n", "1"]).decode("utf-8").split("\n")

    # Initialize the CPU usage sum for this iteration
    cpu_usage_sum = 0

    # Only iterate over the number of lines that actually exist
    num_lines = min(threads_num, len(res) - header_lines)

    for k in range(num_lines):
        line_index = header_lines + k
        if line_index < len(res):
            res_tmp = res[line_index].split()
            res_tmp = [x for x in res_tmp if x]
            if res_tmp:
                try:
                    cpu_usage = float(res_tmp[8])  # CPU usage is typically at the 9th position (index 8)
                    cpu_usage_sum += cpu_usage
                except ValueError:
                    continue  # Skip any lines where conversion to float is not possible

    # Record the CPU usage sum and the time since the start
    times.append(time.time() - start_time)
    values.append(cpu_usage_sum)

# Plotting
fig, ax = plt.subplots()
ax.set_xlabel('Seconds')
ax.set_ylabel('% CPU Usage')
ax.step(times, values, where='post')  # Use 'post' to indicate the step occurs after the value
plt.savefig('cpu_usage_per_20.png')
plt.show()

