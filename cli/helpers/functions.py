import os

def validate_day(day: int) -> int | ValueError:
    if day < 1 or day > 25:
        raise ValueError("Day value must be between 1 and 25")
    return day

def validate_phase(phase: int) -> int | None:
    if phase not in (1, 2):
        raise ValueError("Phase must be 1 or 2")
    return phase

def validate_year(year: int) -> int | ValueError:
    if year < 2015 or year > 2024:
        raise ValueError("Year value must be between 2015 and 2024")
    return year

def create_day(day: int):
    day_folder = f"day{day}"
    os.mkdir(day_folder)
    os.chdir(day_folder)
    with open("first.py", 'w') as first, open("second.py", 'w') as second, open("__init__.py", "w"):
        first.write("def solve():\n\tpass\n\nif '__name__' == '__main__':\n\tsolve()")
        second.write("def solve():\n\tpass\n\nif '__name__' == '__main__':\n\tsolve()")
    os.makedirs("data")
    os.chdir("data")
    open("input.txt", 'w')