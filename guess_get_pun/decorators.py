import functools
import time
from datetime import datetime


def log_performance_to_file(log_file_path):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                log_file.write(f"Timestamp: {timestamp}\n")
                log_file.write(f"Function: {func.__name__} executed in {duration:.4f} seconds\n")
                log_file.write(f"Result: {result}\n")
                log_file.write("--------------------------------------------------\n")

            return result

        return wrapper

    return decorator
