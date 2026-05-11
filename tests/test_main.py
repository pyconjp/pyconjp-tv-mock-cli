from click.testing import CliRunner

from pyconjp_tv_mock_cli.main import cli


def test_greet_default() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["greet"])
    assert result.exit_code == 0
    assert "こんにちは、World！" in result.output


def test_greet_with_name() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["greet", "--name", "Python"])
    assert result.exit_code == 0
    assert "こんにちは、Python！" in result.output


def test_greet_english() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["greet", "--name", "Python", "--lang", "en"])
    assert result.exit_code == 0
    assert "Hello, Python!" in result.output


def test_schedule() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["schedule"])
    assert result.exit_code == 0
    assert "スケジュール" in result.output
    assert "10:00" in result.output


def test_speaker() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["speaker"])
    assert result.exit_code == 0
    assert "登壇者" in result.output
    assert "山田 太郎" in result.output


def test_version() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output
