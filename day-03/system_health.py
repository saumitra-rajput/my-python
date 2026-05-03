# psutil is install via pip install psutil in root env
import psutil

def check_metrics(name, current, threshold):

    if current > threshold:
        print(f"{name} is in good health {current}")
    else:
        print(f"{name} alert mail is sent to the Admin current status is : {current}")

def system_health():
    cpu_threshold = float(input("Enter the CPU threshold: "))
    disk_threshold = float(input("Enter the disk threshold: "))
    memory_threshold = float(input("Enter the memory threshold: "))

    print("\nRunning system check...\n")

    current_cpu = psutil.cpu_percent(interval=1)
    check_metrics("CPU", current_cpu, cpu_threshold)

    # disk_usage returns sdiskusage(total=1081101176832, used=6713917440, free=1019394904064, percent=0.7)
    # we are using percent to compare 
    current_disk = psutil.disk_usage("/").percent
    check_metrics("DISK", current_disk, disk_threshold)
    
    current_memory = psutil.virtual_memory().percent
    check_metrics("MEMORY", current_memory, memory_threshold)

system_health()
