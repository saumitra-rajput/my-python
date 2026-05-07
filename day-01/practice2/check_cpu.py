# get the cpu threshold from user
# check the current CPU usage
# if cpu usage above than threshold sent mail
# using psutil

import psutil

def cpu_usage():
    cpu_threshold = float(input("Enter the CPU threshold: "))
    
    current_cpu = psutil.cpu_percent(interval=1)
    print("Current CPU %: ", current_cpu)

    if current_cpu > cpu_threshold:
        print("CPU Alert mail sent...")
    else:
        print("CPU is in good condition.")


cpu_usage()
