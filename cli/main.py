import os
import typer

from os.path import join
from rich import print as rprint
from importlib import import_module
from typing import Annotated

from helpers.constants import PUZZLE_MAPPER
from helpers.functions import validate_day, validate_phase, validate_year, create_day
from console import console

app = typer.Typer()

@app.command()
def solve(
    year: Annotated[int, typer.Option()],
    day: Annotated[int, typer.Option()],
    phase: Annotated[int, typer.Option()]
):
    day, phase, year = validate_day(day=day), validate_phase(phase=phase), validate_year(year=year)
    phase = PUZZLE_MAPPER[phase]
    try:
        module = import_module(f"aocli.puzzles.year{year}.day{day}.{phase}")
        module.solve()
    except ModuleNotFoundError:
        rprint(
            f"🚨 Ooops, i can't find any problems to solve.\n🤔 Are you sure you already solve the day {day} phase {phase} ?"
        )

@app.command()
def generate(year: Annotated[int, typer.Option()]):
    year = validate_year(year)
    puzzles_path = join(os.getcwd(), "aocli\puzzles")
    folder_name = f"year{year}"
    folder_path = join(puzzles_path, folder_name)
    with console.status("🤖 Generating puzzle folder ..."):
        try:
            os.makedirs(folder_path)
        except FileExistsError:
            rprint(
                f"🚨 Puzzles folder for the year {year} already exist !"
            )
            return
        os.chdir(folder_path)
        open('__init__.py', "w")
        for i in range(25):
            create_day(i + 1)
            os.chdir(folder_path)
        console.log(f"🔥 Done ! You can now start to solve puzzles !\n⚠️  Don't forget to add your inputs")
        

if __name__ == "__main__":
    app()