import sys
size_bytes = 1921000
size_megabytes = size_bytes / (1024 * 1024)
big_number = 3 ** 9090001
actual_size_bytes = sys.getsizeof(big_number)
actual_size_megabytes = actual_size_bytes / (1024 * 1024)
print(f"Фактический размер в байтах: {actual_size_bytes:,} байт")
print(f"Фактический размер в мегабайтах: {actual_size_megabytes:.2f} МБ")



