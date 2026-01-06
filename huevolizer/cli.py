from huevolizer.control_limits import X_R_limits_calculator

import matplotlib.pyplot as plt
import pandas as pd
import pyshewhart

import typer

cli = typer.Typer()


@cli.command()
def plot_control_chart(
    data_path: str = typer.Option("Path of X R data"),
    output_path: str = typer.Option("Path of output plot"),
):
    data = pd.read_csv(data_path)
    pyshewhart.XbarR(data["Fecha"], data["X"], sample_size=2)
    plt.savefig(output_path, dpi=900)
    plt.close()


@cli.command()
def write_control_chart_data(
    data_path: str = typer.Option("Path of daily egg data"),
    individuals_count_path: str = typer.Option("Path of daily individuals counts"),
    output_path: str = typer.Option("Path of result"),
):
    raw_data = pd.read_csv(data_path)
    individual_data = pd.read_csv(individuals_count_path)
    calculator = X_R_limits_calculator(raw_data, individual_data)
    calculator.save_x_r(output_path)


@cli.command()
def version():
    typer.echo("0.0.1")
