import os
import random
import time
from collections import Counter
from threading import Thread, Lock
from multiprocessing import Pool


def process_chunk(chunk):
    return Counter(chunk.split())


def create_large_text_file(filename, size_in_mb):
    words = [
        "python",
        "programming",
        "data",
        "science",
        "multithreading",
        "multiprocessing",
        "parallel",
        "performance",
    ]
    with open(filename, "w") as f:
        for _ in range(size_in_mb * 1024 * 1024 // 50):
            line = " ".join(random.choices(words, k=random.randint(5, 15)))
            f.write(line + "\n")


def count_words_sequential(filename):
    with open(filename, "r") as f:
        text = f.read()
    return Counter(text.split())


def count_words_multithreading(filename):
    chunk_size = 1024 * 1024
    word_counts = Counter()
    lock = Lock()

    def process_chunk_in_thread(chunk):
        local_counter = Counter(chunk.split())
        with lock:
            word_counts.update(local_counter)

    threads = []
    with open(filename, "r") as f:
        while chunk := f.read(chunk_size):
            thread = Thread(target=process_chunk_in_thread, args=(chunk,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return word_counts


def count_words_multiprocessing(filename):
    chunk_size = 1024 * 1024

    with open(filename, "r") as f:
        chunks = []
        while chunk := f.read(chunk_size):
            chunks.append(chunk)

    with Pool() as pool:
        results = pool.map(process_chunk, chunks)

    word_counts = Counter()
    for result in results:
        word_counts.update(result)

    return word_counts


def main():
    filename = "large_text.txt"
    size_in_mb = 10
    create_large_text_file(filename, size_in_mb)

    print("File created. Starting performance tests...")

    start_time = time.time()
    seq_counts = count_words_sequential(filename)
    seq_time = time.time() - start_time
    print(f"Sequential word count took {seq_time:.2f} seconds")

    start_time = time.time()
    mt_counts = count_words_multithreading(filename)
    mt_time = time.time() - start_time
    print(f"Multithreading word count took {mt_time:.2f} seconds")

    start_time = time.time()
    mp_counts = count_words_multiprocessing(filename)
    mp_time = time.time() - start_time
    print(f"Multiprocessing word count took {mp_time:.2f} seconds")

    print("\nPerformance Comparison:")
    print(f"Sequential: {seq_time:.2f} seconds")
    print(f"Multithreading: {mt_time:.2f} seconds (Speedup: {seq_time / mt_time:.2f}x)")
    print(
        f"Multiprocessing: {mp_time:.2f} seconds (Speedup: {seq_time / mp_time:.2f}x)"
    )

    os.remove(filename)


if __name__ == "__main__":
    main()
