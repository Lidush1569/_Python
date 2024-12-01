import random
import time

with open("numbers.txt", "w") as file:
    for _ in range(100):
        line = " ".join(str(random.randint(1, 100)) for _ in range(20))
        file.write(line + "\n")

with open("numbers.txt", "r") as file:
    lines = file.readlines()
lines_as_numbers = [list(map(int, line.split())) for line in lines]

filtered_lines = [[num for num in line if num > 40] for line in lines_as_numbers]

with open("filtered_numbers.txt", "w") as file:
    for line in filtered_lines:
        file.write(" ".join(map(str, line)) + "\n")


def read_file_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            yield list(map(int, line.split()))


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds"
        )
        return result

    return wrapper


@measure_time
def read_and_process(filename):
    generator = read_file_generator(filename)
    for line in generator:
        pass


read_and_process("filtered_numbers.txt")
