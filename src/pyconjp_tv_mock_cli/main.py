import argparse
from collections.abc import Sequence

from pyconjp_tv_mock_cli import __version__

MOCK_SCHEDULE = [
    {"time": "10:00", "title": "オープニング", "speaker": "運営チーム"},
    {"time": "10:30", "title": "Pythonでつくる CLI ツール入門", "speaker": "山田 太郎"},
    {
        "time": "11:30",
        "title": "PyPI へのパッケージ公開ハンズオン",
        "speaker": "鈴木 花子",
    },
    {"time": "13:00", "title": "型ヒントと mypy 実践", "speaker": "田中 次郎"},
    {"time": "14:00", "title": "クロージング", "speaker": "運営チーム"},
]

MOCK_SPEAKERS = [
    {"name": "山田 太郎", "bio": "Python 歴 10 年。OSS 活動が趣味。"},
    {"name": "鈴木 花子", "bio": "パッケージング職人。PyPI に 20 本以上公開。"},
    {"name": "田中 次郎", "bio": "型安全な Python を布教中。"},
]


def _greet_command(args: argparse.Namespace) -> None:
    if args.lang == "ja":
        print(f"こんにちは、{args.name}！")
    else:
        print(f"Hello, {args.name}!")


def _schedule_command(_: argparse.Namespace) -> None:
    print("=== PyCon JP TV スケジュール ===")
    for session in MOCK_SCHEDULE:
        print(f"  {session['time']}  {session['title']}  ({session['speaker']})")


def _speaker_command(_: argparse.Namespace) -> None:
    print("=== 登壇者一覧 ===")
    for i, speaker in enumerate(MOCK_SPEAKERS, start=1):
        print(f"  {i}. {speaker['name']}")
        print(f"     {speaker['bio']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PyCon JP TV デモ用 CLI ツール")
    parser.add_argument(
        "--version",
        action="version",
        version=f"pyconjp-tv {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    greet_parser = subparsers.add_parser("greet", help="挨拶を表示します")
    greet_parser.add_argument(
        "--name",
        "-n",
        default="World",
        help="挨拶する相手の名前",
    )
    greet_parser.add_argument(
        "--lang",
        "-l",
        choices=["ja", "en"],
        default="ja",
        help="言語",
    )
    greet_parser.set_defaults(func=_greet_command)

    schedule_parser = subparsers.add_parser(
        "schedule",
        help="モックのイベントスケジュールを表示します",
    )
    schedule_parser.set_defaults(func=_schedule_command)

    speaker_parser = subparsers.add_parser(
        "speaker",
        help="モックの登壇者一覧を表示します",
    )
    speaker_parser.set_defaults(func=_speaker_command)

    return parser


def cli(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    args.func(args)
    return 0


def main() -> None:
    raise SystemExit(cli())
