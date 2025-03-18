from huevolizer.control_limits import X_R_limits_calculator
import pandas as pd

import typer

cli = typer.Typer()


@cli.command()
def write_control_chart_data(data_path: str = typer.Option("Path of daily egg data")):
    raw_data = pd.read_csv(data_path)
    calculator = X_R_limits_calculator(raw_data)
    calculator.save_x_r("salida.csv")


@cli.command()
def version():
    typer.echo("0.0.1")
