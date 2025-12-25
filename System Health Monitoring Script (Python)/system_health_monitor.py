import psutil
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    alerts = []

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"CPU usage high: {cpu_usage}%")

    if memory.percent > MEM_THRESHOLD:
        alerts.append(f"Memory usage high: {memory.percent}%")

    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"Disk usage high: {disk.percent}%")

    process_count = len(psutil.pids())

    print(f"\nSystem Health Check @ {datetime.now()}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")
    print(f"Running Processes: {process_count}")

    if alerts:
        print("\nALERTS:")
        for alert in alerts:
            print(" -", alert)
    else:
        print("\nSystem is healthy.")

if __name__ == "__main__":
    check_system_health()
