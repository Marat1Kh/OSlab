import subprocess
import time
import matplotlib.pyplot as plt
import re

# Configuration
stress_ng_command = ["stress-ng", "--sched", "4", "--sched-period", "10000000", "--timeout", "60s"]
measure_time = 60  # seconds
pid = None  # We will fill this in after starting stress-ng

# Start stress-ng process
process = subprocess.Popen(stress_ng_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
time.sleep(5)  # Wait a bit for stress-ng to start

# Try to find the PID of stress-ng for monitoring
try:
    pid = subprocess.check_output(["pgrep", "-f", " ".join(stress_ng_command)]).decode().strip()
except subprocess.CalledProcessError:
    print("Failed to find stress-ng process. Exiting.")
    process.terminate()
    exit()

# Initialize data collection
states = {'R': [], 'S': [], 'D': [], 'T': [], 'Z': []}  # Add more states if needed
times = []

start_time = time.time()

while time.time() - start_time < measure_time:
    # Get the top command output for the stress-ng process
    output = subprocess.check_output(["top", "-b", "-n", "1", "-H", "-p", pid]).decode()

    # Count the number of threads in each state
    thread_states = re.findall(r"\s(\w)\s+\d+\s+stress-ng", output)
    for state in states.keys():
        states[state].append(thread_states.count(state))

    # Record the current time
    times.append(time.time() - start_time)

    # Wait for the next measurement
    time.sleep(1)

# Terminate the stress-ng process if it's still running
process.terminate()

# Plotting
fig, ax = plt.subplots()

# Plot a stacked area chart for each thread state
ax.stackplot(times, states.values(), labels=states.keys())

ax.legend(loc='upper left')
ax.set_xlabel('Seconds')
ax.set_ylabel('Threads')
ax.set_title('Running Threads of stress-ng sched-period')
plt.savefig('running_threads.png')
plt.show()

