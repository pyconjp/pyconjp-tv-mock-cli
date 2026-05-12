# pyconjp-tv-mock-cli

PyCon JP TV 202605 デモ用 CLI ツール

## 機能

このツールは PyCon JP TV の配信情報を表示するコマンドラインツールです。以下のコマンドが利用できます：

- **greet**: 挨拶を表示します
  - `--name` / `-n`: 挨拶する相手の名前（デフォルト: World）
  - `--lang` / `-l`: 言語を指定（ja: 日本語、en: 英語、デフォルト: ja）

- **schedule**: PyCon JP TV のイベントスケジュールを表示します

- **speaker**: パーソナリティ一覧を表示します

## セットアップ

### pip を使う場合

```bash
# 基本インストール
pip install -e .

# 開発環境（ruff, mypy, pytest含む）
pip install -e ".[dev]"
```

### uv を使う場合

```bash
# 基本インストール
uv sync

# 開発環境（ruff, mypy, pytest含む）
uv sync --extra dev
```

## 使用例

```bash
# 挨拶コマンド（日本語）
pyconjp-tv greet --name Alice

# 挨拶コマンド（英語）
pyconjp-tv greet --name Bob --lang en

# スケジュール表示
pyconjp-tv schedule

# パーソナリティ表示
pyconjp-tv speaker
```
