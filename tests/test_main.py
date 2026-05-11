import pytest
from click.testing import CliRunner

from pyconjp_tv_mock_cli.main import cli


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_greet_default(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["greet"])
    assert result.exit_code == 0
    assert "こんにちは、World！" in result.output


def test_greet_with_name(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["greet", "--name", "Python"])
    assert result.exit_code == 0
    assert "こんにちは、Python！" in result.output


def test_greet_english(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["greet", "--name", "Python", "--lang", "en"])
    assert result.exit_code == 0
    assert "Hello, Python!" in result.output


def test_schedule(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["schedule"])
    assert result.exit_code == 0
    assert "スケジュール" in result.output
    assert "10:00" in result.output


def test_speaker(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["speaker"])
    assert result.exit_code == 0
    assert "登壇者" in result.output
    assert "山田 太郎" in result.output


def test_version(runner: CliRunner) -> None:
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output
