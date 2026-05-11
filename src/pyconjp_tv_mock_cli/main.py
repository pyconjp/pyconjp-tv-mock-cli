import click

from pyconjp_tv_mock_cli import __version__

MOCK_SCHEDULE = [
    {"time": "10:00", "title": "オープニング", "speaker": "運営チーム"},
    {"time": "10:30", "title": "Pythonでつくる CLI ツール入門", "speaker": "山田 太郎"},
    {"time": "11:30", "title": "PyPI へのパッケージ公開ハンズオン", "speaker": "鈴木 花子"},
    {"time": "13:00", "title": "型ヒントと mypy 実践", "speaker": "田中 次郎"},
    {"time": "14:00", "title": "クロージング", "speaker": "運営チーム"},
]

MOCK_SPEAKERS = [
    {"name": "山田 太郎", "bio": "Python 歴 10 年。OSS 活動が趣味。"},
    {"name": "鈴木 花子", "bio": "パッケージング職人。PyPI に 20 本以上公開。"},
    {"name": "田中 次郎", "bio": "型安全な Python を布教中。"},
]


@click.group()
@click.version_option(__version__, prog_name="pyconjp-tv")
def cli() -> None:
    """PyCon JP TV デモ用 CLI ツール"""


@cli.command()
@click.option("--name", "-n", default="World", show_default=True, help="挨拶する相手の名前")
@click.option("--lang", "-l", type=click.Choice(["ja", "en"]), default="ja", show_default=True, help="言語")
def greet(name: str, lang: str) -> None:
    """挨拶を表示します"""
    if lang == "ja":
        click.echo(f"こんにちは、{name}！")
    else:
        click.echo(f"Hello, {name}!")


@cli.command()
def schedule() -> None:
    """モックのイベントスケジュールを表示します"""
    click.echo(click.style("=== PyCon JP TV スケジュール ===", bold=True))
    for session in MOCK_SCHEDULE:
        time = click.style(session["time"], fg="cyan")
        title = session["title"]
        speaker = click.style(session["speaker"], fg="yellow")
        click.echo(f"  {time}  {title}  ({speaker})")


@cli.command()
def speaker() -> None:
    """モックの登壇者一覧を表示します"""
    click.echo(click.style("=== 登壇者一覧 ===", bold=True))
    for i, s in enumerate(MOCK_SPEAKERS, start=1):
        name = click.style(s["name"], fg="green")
        click.echo(f"  {i}. {name}")
        click.echo(f"     {s['bio']}")
