from huevolizer.cli import cli

from typer.testing import CliRunner


runner = CliRunner()


def tests_write_control_chart_data():
    result = runner.invoke(cli, ["write-control-chart", "--help"])
    assert result.exit_code == 0
