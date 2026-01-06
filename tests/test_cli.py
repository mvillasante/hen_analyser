from huevolizer.cli import cli

import geci_test_tools as gtt
import pandas as pd
from typer.testing import CliRunner

import pytest


runner = CliRunner()


def tests_plot_control_chart():
    result = runner.invoke(cli, ["plot-control-chart", "--help"])
    assert result.exit_code == 0

    data_path = "tests/data/X_R_control_data.csv"
    output_path = "X_R_plot.png"
    gtt.if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "plot-control-chart",
            "--data-path",
            data_path,
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)


def tests_write_control_chart_data():
    result = runner.invoke(cli, ["write-control-chart-data", "--help"])
    assert result.exit_code == 0
    assert " Path of daily egg data]" in result.stdout

    data_path = "tests/data/producción_diaria.csv"
    output_path = "salida.csv"
    gtt.if_exist_remove(output_path)
    result = runner.invoke(
        cli,
        [
            "write-control-chart-data",
            "--data-path",
            data_path,
            "--individuals-count-path",
            "tests/data/conteo_individuos.csv",
            "--output-path",
            output_path,
        ],
    )
    assert result.exit_code == 0
    gtt.assert_exist(output_path)
    obtained = pd.read_csv(output_path)
    expected_columns = ["Fecha", "X", "R"]
    assert obtained.columns.tolist() == expected_columns


def test_version():
    result = runner.invoke(
        cli,
        ["version"],
    )
    expected_version = "0.0.1"
    assert expected_version in result.stdout
