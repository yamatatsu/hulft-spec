# HULFT WebConnect ドキュメント変換ツール

このリポジトリは、HULFT WebConnect V3の公式ドキュメントをHTMLからMarkdownに変換し、統合されたドキュメントファイルを生成するためのツールです。

URLは手動で収集しているため、公式ドキュメントに更新があった場合は、`./*/urls.txt`を更新するか、これを更新する別のスクリプトを作成する必要があります。

## ディレクトリ構成

- **SiteAPI/** - Site API ガイド（100 URL）
- **Agent/** - Agent ガイド（71 URL）
- **CLI/** - CLI ガイド（48 URL）
- **FirstStep/** - ファーストステップガイド（40 URL）

各ディレクトリには以下のファイルが含まれます：
- `README.md` - ディレクトリの説明
- `urls.txt` - 変換対象のURLリスト
- `spec.md` - 生成された統合Markdownドキュメント

## 使い方

### 必要な環境

- Python 3.7以上
- インターネット接続（URLからドキュメントを取得するため）

### セットアップ

1. 仮想環境を作成してアクティベート:
```bash
python3 -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```

2. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

### ドキュメント生成

#### すべてのフォルダを処理:
```bash
python3 generate_specs.py
```

#### 特定のフォルダのみを処理:
```bash
python3 generate_specs.py SiteAPI
python3 generate_specs.py Agent CLI
```

### 処理結果

各フォルダに`spec.md`ファイルが生成されます：

| フォルダ | URLs | ファイルサイズ | 行数 |
|---------|------|--------------|------|
| SiteAPI | 100 | 247KB | 6,978行 |
| Agent | 71 | 94KB | 2,751行 |
| CLI | 48 | 53KB | 1,580行 |
| FirstStep | 40 | 72KB | 1,195行 |
| **合計** | **259** | **466KB** | **12,504行** |

## スクリプトの機能

`generate_specs.py`は以下の処理を実行します：

1. 各フォルダの`urls.txt`からURLリストを読み込み
2. 各URLからHTMLを取得
3. CSS セレクタ `#mc-main-content` でメインコンテンツを抽出
4. HTMLをMarkdownに変換
5. すべてのページを結合して`spec.md`を生成

### 主な特徴

- **リトライ機能**: ネットワークエラー時に自動的に3回までリトライ
- **レート制限**: サーバーに負荷をかけないよう、各リクエスト間に0.5秒の待機
- **エラーハンドリング**: 取得失敗時もエラー情報をドキュメントに記録
- **進捗表示**: 処理状況をリアルタイムで表示

## ログ

スクリプト実行時のログは`generate_specs.log`に保存されます。

## 依存パッケージ

- `beautifulsoup4` - HTML解析
- `html2text` - HTMLからMarkdownへの変換

## ライセンス

このツールはHULFT WebConnectのドキュメントを変換するために作成されました。
元のドキュメントの著作権はSAITECH Inc.に帰属します。
