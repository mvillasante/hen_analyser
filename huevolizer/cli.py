import pandas as pd

import typer

cli = typer.Typer()


@cli.command()
def write_control_chart_data(data_a):
    pass


@cli.command()
def version():
    typer.echo("0.0.1")
