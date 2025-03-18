from huevolizer.cli import cli

from typer.testing import CliRunner


runner = CliRunner()


def tests_write_control_chart_data():
    result = runner.invoke(cli, ["write-control-chart-data", "--help"])
    assert result.exit_code == 0
    assert " Path of daily egg data]" in result.stdout


def test_version():
    result = runner.invoke(
        cli,
        ["version"],
    )
    expected_version = "0.0.1"
    assert expected_version in result.stdout
