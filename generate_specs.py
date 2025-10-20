#!/usr/bin/env python3
"""
HULFT WebConnect ドキュメントをURLから取得してMarkdownに変換するスクリプト

各フォルダのurls.txtに記載されたURLからHTMLを取得し、
#mc-main-content セレクタの内容をMarkdownに変換して
spec.mdファイルとして出力します。
"""

import os
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import html2text

# html2textの設定
h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = False
h.ignore_emphasis = False
h.body_width = 0  # 行の折り返しを無効化

def fetch_html(url, retry=3, delay=1):
    """URLからHTMLを取得する（リトライ機能付き）"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    for attempt in range(retry):
        try:
            print(f"  Fetching: {url} (attempt {attempt + 1}/{retry})")
            req = Request(url, headers=headers)
            with urlopen(req, timeout=30) as response:
                html = response.read().decode('utf-8')
                return html
        except (HTTPError, URLError) as e:
            print(f"  Error fetching {url}: {e}")
            if attempt < retry - 1:
                print(f"  Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"  Failed to fetch {url} after {retry} attempts")
                return None
        except Exception as e:
            print(f"  Unexpected error: {e}")
            return None

    return None

def extract_main_content(html):
    """HTMLから#mc-main-contentの内容を抽出する"""
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    main_content = soup.select_one('#mc-main-content')

    if main_content:
        return str(main_content)
    else:
        print("  Warning: #mc-main-content not found")
        return None

def html_to_markdown(html_content):
    """HTMLをMarkdownに変換する"""
    if not html_content:
        return ""

    markdown = h.handle(html_content)
    return markdown

def process_folder(folder_path):
    """フォルダ内のurls.txtを処理してspec.mdを生成する"""
    folder = Path(folder_path)
    urls_file = folder / 'urls.txt'
    output_file = folder / 'spec.md'

    if not urls_file.exists():
        print(f"urls.txt not found in {folder}")
        return False

    print(f"\nProcessing folder: {folder.name}")
    print(f"Reading URLs from: {urls_file}")

    # URLを読み込む
    with open(urls_file, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Found {len(urls)} URLs to process")

    # 各URLを処理してMarkdownを収集
    markdown_parts = []
    markdown_parts.append(f"# HULFT WebConnect - {folder.name}\n\n")
    markdown_parts.append(f"このドキュメントは {len(urls)} ページから生成されました。\n\n")
    markdown_parts.append("---\n\n")

    successful = 0
    failed = 0

    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")

        # HTMLを取得
        html = fetch_html(url)
        if not html:
            failed += 1
            markdown_parts.append(f"\n## ページ {i}: エラー\n\n")
            markdown_parts.append(f"URL: {url}\n\n")
            markdown_parts.append("このページの取得に失敗しました。\n\n")
            markdown_parts.append("---\n\n")
            continue

        # メインコンテンツを抽出
        main_content = extract_main_content(html)
        if not main_content:
            failed += 1
            markdown_parts.append(f"\n## ページ {i}: コンテンツなし\n\n")
            markdown_parts.append(f"URL: {url}\n\n")
            markdown_parts.append("#mc-main-content が見つかりませんでした。\n\n")
            markdown_parts.append("---\n\n")
            continue

        # Markdownに変換
        markdown = html_to_markdown(main_content)

        # ページ情報を追加
        markdown_parts.append(f"\n## ページ {i}\n\n")
        markdown_parts.append(f"**URL:** {url}\n\n")
        markdown_parts.append(markdown)
        markdown_parts.append("\n\n---\n\n")

        successful += 1

        # サーバーに負荷をかけないように待機
        time.sleep(0.5)

    # spec.mdに書き込む
    print(f"\nWriting to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(markdown_parts))

    print(f"\nCompleted: {successful} successful, {failed} failed")
    print(f"Output: {output_file}")

    return True

def main():
    """メイン処理"""
    # スクリプトのディレクトリを基準にする
    base_dir = Path(__file__).parent

    # コマンドライン引数でフォルダを指定できるようにする
    if len(sys.argv) > 1:
        folders = sys.argv[1:]
    else:
        # デフォルトは全フォルダ
        folders = ['SiteAPI', 'Agent', 'CLI', 'FirstStep']

    print("=" * 60)
    print("HULFT WebConnect Documentation to Markdown Converter")
    print("=" * 60)

    for folder_name in folders:
        folder_path = base_dir / folder_name
        if folder_path.exists() and folder_path.is_dir():
            try:
                process_folder(folder_path)
            except Exception as e:
                print(f"\nError processing {folder_name}: {e}")
                import traceback
                traceback.print_exc()
        else:
            print(f"\nFolder not found: {folder_path}")

    print("\n" + "=" * 60)
    print("All folders processed!")
    print("=" * 60)

if __name__ == '__main__':
    main()
