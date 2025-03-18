import pandas as pd

import typer

cli = typer.Typer()


@cli.command()
def write_control_chart_data(data_path: str = typer.Option("Path of daily egg data")):
    pass


@cli.command()
def version():
    typer.echo("0.0.1")
