import argparse
from collections.abc import Sequence

from pyconjp_tv_mock_cli import __version__

SCHEDULE = [
    {"time": "19:30", "title": "オープニング: チャンネル紹介、自己紹介(3分)"},
    {"time": "19:33", "title": "Pythonニュース(10分)"},
    {"time": "19:43", "title": "メイントーク(35分)"},
    {"time": "20:23", "title": "お便りコーナー(5分)"},
    {"time": "20:23", "title": "次回告知、感想(5分)"},
    {"time": "20:30", "title": "🍺タイム"},
]

SPEAKERS = [
    {"name": "Manabu TERADA", "nickname": "terada"},
    {"name": "Takanori Suzuki", "nickname": "takanory"},
]


def _greet_command(args: argparse.Namespace) -> None:
    if args.lang == "ja":
        print(f"こんにちは、{args.name}！")
    else:
        print(f"Hello, {args.name}!")


def _schedule_command(_: argparse.Namespace) -> None:
    print("=== PyCon JP TV スケジュール ===")
    for session in SCHEDULE:
        print(f"  {session['time']}  {session['title']}")


def _speaker_command(_: argparse.Namespace) -> None:
    print("=== 登壇者一覧 ===")
    for i, speaker in enumerate(SPEAKERS, start=1):
        print(f"  {i}. {speaker['name']}")
        print(f"     {speaker['nickname']}")


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
