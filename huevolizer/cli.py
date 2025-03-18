from huevolizer.control_limits import X_R_limits_calculator
import pandas as pd

import typer

cli = typer.Typer()


@cli.command()
def write_control_chart_data(data_path: str = typer.Option("Path of daily egg data")):
    raw_data = pd.read_csv(data_path)
    calculator = X_R_limits_calculator(raw_data)
    pd.DataFrame({"Fecha": raw_data.Fecha.loc[1:], "X": calculator.x_s}).to_csv(
        "salida.csv", index=False
    )


@cli.command()
def version():
    typer.echo("0.0.1")
