import psutil

def get_size(bytes, suffix="B"):
    # unit conversion
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    partition_usage = psutil.disk_usage(partition.mountpoint)
    print(f"  Free space: {get_size(partition_usage.free)}")
