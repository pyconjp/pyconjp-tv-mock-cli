import pytest

from pyconjp_tv_mock_cli.main import cli


def test_greet_default(capsys: pytest.CaptureFixture[str]) -> None:
    result = cli(["greet"])
    assert result == 0
    captured = capsys.readouterr()
    assert "こんにちは、World！" in captured.out


def test_greet_with_name(capsys: pytest.CaptureFixture[str]) -> None:
    result = cli(["greet", "--name", "Python"])
    assert result == 0
    captured = capsys.readouterr()
    assert "こんにちは、Python！" in captured.out


def test_greet_english(capsys: pytest.CaptureFixture[str]) -> None:
    result = cli(["greet", "--name", "Python", "--lang", "en"])
    assert result == 0
    captured = capsys.readouterr()
    assert "Hello, Python!" in captured.out


def test_schedule(capsys: pytest.CaptureFixture[str]) -> None:
    result = cli(["schedule"])
    assert result == 0
    captured = capsys.readouterr()
    assert "スケジュール" in captured.out
    assert "19:30" in captured.out


def test_speaker(capsys: pytest.CaptureFixture[str]) -> None:
    result = cli(["speaker"])
    assert result == 0
    captured = capsys.readouterr()
    assert "登壇者" in captured.out
    assert "Manabu TERADA" in captured.out


def test_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        cli(["--version"])
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "0.1.0" in captured.out
