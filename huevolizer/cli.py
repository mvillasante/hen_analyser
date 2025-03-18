import pandas as pd

import typer

cli = typer.Typer()


@cli.command()
def write_control_chart_data(data_path: str = typer.Option("Path of daily egg data")):
    pd.read_csv(data_path).to_csv("salida.csv")


@cli.command()
def version():
    typer.echo("0.0.1")
