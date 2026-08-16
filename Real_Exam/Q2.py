"""Q2 - Multiprocessing and Asyncio

Students: complete this file directly. Do not create another Python file.
"""

from multiprocessing import Pool, cpu_count
import asyncio


def calculate_sum(numbers, lower, upper):
    """Return the sum of numbers[lower:upper]."""
    # TODO Part 1
    # Code here
    

    pass


def run_multiprocessing():
    numbers = list(range(1, 13))
    lower_and_upper_bounds = [(0, 3), (3, 6), (6, 9), (9, 12)]
    
    # TODO Part 1:
    # Print the list of partial sums and their total.
    # Code here
    prepared_list =[(numbers, lower, upper)]

    # print("Part 1 result:", result)
    # print("Part 1 total:", sum(result))
    pass


async def generate_report(report_name, delay):
    """Wait for delay seconds, then return a completion message."""
    # TODO Part 2
    # Code here

    pass


async def run_async():
    report_specs = [
        ("Report A", 0.3),
        ("Report B", 0.1),
        ("Report C", 0.2),
    ]

    # TODO Part 2:
    # Print the returned list.
    # Code here


    # print("Part 2 result:", result)
    pass


def main():
    run_multiprocessing()
    asyncio.run(run_async())


if __name__ == "__main__":
    main()


