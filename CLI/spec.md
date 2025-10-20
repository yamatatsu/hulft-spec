# HULFT WebConnect - CLI

このドキュメントは 48 ページから生成されました。

---


## ページ 1

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/AboutWebCTCLI/AboutWebCTCLI.htm

# HULFT-WebConnectコマンドラインインタフェースについて

HULFT-WebConnectでは、HULFT-WebConnect Data Transfer APIを利用したファイル転送を行うためのコマンドラインインタフェース（以下、CLI）を提供しています。

HULFT未導入環境でもCLIをインストールすることで、HULFTと簡易的なファイル転送を行うことができます。

![](../../Resources/Images/HWC-CLI/AboutWebCTCLI/0010_cli-overview_fig.jpg)


---


## ページ 2

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/Changes/Changes_CLI.htm

# 変更内容一覧

Ver. 3.1.0での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.8 |  Ver 3.1.0 |  変更箇所  
---|---|---|---|---  
1 |  HULFT for IBMiと接続する場合の制限事項の記載変更 |  注意の記載あり |  注意の記載変更 |  [「各項目の説明」](../CLISetting/ExplanEachFieldConf.htm) [「管理情報の設定」](../HULFTSetting/SettingsManageInfoPUT.htm) [「管理情報の設定」](../HULFTSetting/SettingsManageInfoGET.htm)  
記載あり |  記載変更 |  [「制限事項」](../PointsNote/Restrictions.htm)  
2 |  「file.id」に「_」（アンダーバー）が設定可能な記載に変更 |  「_」（アンダーバー）に関する記載なし |  「設定値」に「記号」を追記 「file.id」で使用可能な記号の記載を注意に追記 |  [「各項目の説明」](../CLISetting/ExplanEachFieldTrans.htm)  
  
Ver. 3.0.8での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.7 |  Ver 3.0.8 |  変更箇所  
---|---|---|---|---  
1 |  cli.agent.idの説明文を変更 |  任意の値の記載あり |  任意の値の記載を削除 |  [「各項目の説明」](../CLISetting/ExplanEachFieldConf.htm)  
2 |  HULFT8 for IBMi 接続時の制限事項を追記 |  記載なし |  追記 |  [「各項目の説明」](../CLISetting/ExplanEachFieldConf.htm) [「管理情報の設定」](../HULFTSetting/SettingsManageInfoPUT.htm) [「管理情報の設定」](../HULFTSetting/SettingsManageInfoGET.htm) [「制限事項」](../PointsNote/Restrictions.htm)  
  
Ver. 3.0.7での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.6 |  Ver 3.0.7 |  変更箇所  
---|---|---|---|---  
1 |  各項目の説明の記載変更 |  CLIアップデート設定の記載あり |  CLIアップデート設定の記載変更 |  [「各項目の説明」](../CLISetting/ExplanEachFieldConf.htm)  
2 |  CLIアップデート確認コマンドの記載変更 |  CLIアップデート確認コマンドの記載あり |  CLIアップデート確認コマンドの記載変更 |  [「CLIアップデート確認コマンド」](../CmdRef/CLIUpdateCom.htm)  
3 |  制限事項の追記 |  CLIアップデートの記載なし |  CLIアップデートを追記 |  [「制限事項」](../PointsNote/Restrictions.htm)  
  
Ver. 3.0.6での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.5 |  Ver 3.0.6 |  変更箇所  
---|---|---|---|---  
1 |  集信管理情報の記載変更 |  データ検証の記載なし |  データ検証を追記 |  [「管理情報の設定」](../HULFTSetting/SettingsManageInfoPUT.htm)  
2 |  制限事項の追記 |  データ検証と多重転送の記載なし |  データ検証と多重転送を追記 |  [「制限事項」](../PointsNote/Restrictions.htm)  
3 | 既知の問題の記載変更 | 多重転送を行った場合の記載あり | 多重転送を行った場合の記載を削除 | [「既知の問題点」](../KnownIssues/KnownIssues.htm)  
  
Ver. 3.0.5での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.4 |  Ver 3.0.5 |  変更箇所  
---|---|---|---|---  
1 |  動作環境の記載変更 |  動作環境の記載あり |  弊社ホームページ参照の記載に変更 |  [「CLI 動作環境」](../CLIEnv/OpeEnvCLI.htm)  
2 |  制限事項の記載変更 |  リクエスト禁止期間と電文転送タイプの記載なし |  リクエスト禁止期間と電文転送タイプの追記 |  [「制限事項」](../PointsNote/Restrictions.htm)  
  
Ver. 3.0.2での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.0 |  Ver 3.0.2 |  変更箇所  
---|---|---|---|---  
1 |  運用時の留意点における制限事項の記載変更 |  記載あり |  記載削除 |  [「制限事項」](../PointsNote/Restrictions.htm)


---


## ページ 3

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLIEnv/OpeEnvCLI.htm

# CLI動作環境  
  
動作環境については、以下のURLの弊社ホームページから、HULFT-WebConnectの製品情報を参照してください。

[URL: https://www.hulft.com/](https://www.hulft.com/)


---


## ページ 4

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLIInstll/InstallCLI.htm

# CLIのインストール

CLIの新規インストール方法およびアップデートインストール方法について説明します。


---


## ページ 5

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLIInstll/NewInstall.htm

# 新規インストール方法 

CLIを新規に導入する場合は、以下の手順でインストールします。

(1) 導入先ディレクトリの決定

CLIをインストールするディレクトリ（以下、導入ディレクトリ）を決定します。

**注意**

導入ディレクトリ名に、以下の記号は使用することができません。

Windowsの場合
    
    
    
    ! # % & ' ; [ ] ^ ` { } ? \ / : * " < > |

Linuxの場合
    
    
    
    ! # % & ' ( ) ; ` \ / : " < > | 半角スペース

(2) 圧縮ファイルのダウンロード

Windowsの場合
    

HULFT-WebConnect Management Console（以下、Management Console）の[ダウンロード] 画面から圧縮ファイル（webconnect- transfer-cli-x.x.x-windows.zip）をダウンロードします。

Linuxの場合
    

Management Consoleの[ダウンロード] 画面から圧縮ファイル（webconnect-transfer-cli-x.x.x-linux.tar.gz）をダウンロードします。

(3) 圧縮ファイルの展開

Windowsの場合
    

解凍ソフトを使用して導入ディレクトリに圧縮ファイルを展開します。

Linuxの場合
    

導入ディレクトリに圧縮ファイルを移動し、以下のコマンドを実行します。
    
    
    # tar -xzvf webconnect-transfer-cli-x.x.x-linux.tar.gz


---


## ページ 6

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLIInstll/UpdateInstall.htm

# アップデートインストール方法

CLIを更新する場合は、以下の手順で行います。

また、CLIアップデートコマンドからでも更新できます。コマンドの詳細については、[「コマンドリファレンス」](../CmdRef/CommandRef.htm)を参照してください。

**注意**

ファイル転送中にCLIのアップデートインストールを行うと、正常にインストールできない場合があります。CLIでファイル転送を実行中の場合は、ファイル転送が完了するまで待機してください。

(1) CLIのバックアップ

現在の導入ディレクトリ以下を任意のディレクトリ（以下、バックアップディレクトリ）に退避させます。退避後、現在の導入ディレクトリ以下を削除します。

(2) 圧縮ファイルのダウンロード

Windowsの場合
    

Management Console の[ダウンロード] 画面から圧縮ファイル（webconnect-transfer-cli-x.x.x-windows.zip）をダウンロードします。

Linuxの場合
    

Management Console の[ダウンロード] 画面から圧縮ファイル（webconnect-transfer-cli-x.x.x-linux.tar.gz）をダウンロードします。

(3) 圧縮ファイルの展開

Windowsの場合
    

解凍ソフトを使用して導入ディレクトリに圧縮ファイルを展開します。

Linuxの場合
    

導入ディレクトリに圧縮ファイルを移動し、以下のコマンドを実行します。
    
    
    # tar -xzvf webconnect-transfer-cli-x.x.x-linux.tar.gz

(4) 設定内容の反映

バックアップディレクトリのCLI設定ファイルおよびログの設定ファイルの内容を、導入ディレクトリのCLI設定ファイルに反映します。

バックアップしたファイルを導入ディレクトリにファイルコピーすると、正しく動作しなくなる場合があります。
    
    
    {導入ディレクトリ}/config/transfer-cli.conf
    {導入ディレクトリ}/config/logback.xml

設定内容の詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)と[「CLIのログ」](../CLILog/LogCLI.htm)を参照してください。

(5) バージョン確認

CLIが正しく更新されたかどうかをバージョン表示コマンドで確認します。

コマンドの実行結果で表示される「Version」が更新したCLIのバージョンと一致しているかご確認ください。バージョン表示コマンドの詳細は、[「コマンドリファレンス」](../CmdRef/CommandRef.htm)を参照してください。

(6) バックアップディレクトリの削除

必要に応じて、バックアップディレクトリを削除してください。


---


## ページ 7

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLILog/DefaultLogOutputDest.htm

# 初期設定のログ出力場所

ログファイルの出力場所はCLIを実行したディレクトリによって異なりますが、当ガイドに沿って実行した場合は以下に出力されます。

コンソールログ
    
    
    {導入ディレクトリ}/bin/logs/console.log

転送ログ
    
    
    {導入ディレクトリ}/bin/logs/transfer.log


---


## ページ 8

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLILog/DefaultOutputLogExam.htm

# 初期設定のログ出力例

「ログ出力日付」、「ログ出力時間」、「Agent ID」、「ログレベル」、「ログ出力クラス」、「ログメッセージ番号」、「ログメッセージ」を半角スペース区切りで出力します。

コンソールログ
    
    
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(1)] XxxHandler - I500021 - エンドポイントに接続しました。セッションI D:[XX] (Xxx.java:84)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(1)] XxxHandler - I500022 - Serviceに認証情報を送信します。セッションID:[XX] (Xxx.java:94)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(2)] XxxHandler - I500024 - 認証に成功しました。セッションID:[XX] (Xxx.java:73)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(2)] XxxHandler - I500025 - Serviceに中継情報を送信します。セッションID:[XX] (Xxx.java:76)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(1)] XxxHandler - I500027 - 送信準備が完了しました。セッションID:[XX](Xxx.java:100)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(1)] XxxHandler - I500028 - ファイル送信を開始します。セッションID:[XX], ファイル:[XX], ファイルID:[XX], 処理識別子:[XX] (Xxx.java:102)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(1)] XxxHandler - I500030 - Serviceに完了通知を送信します。セッションID:[XX], ファイル:[XX], ファイルID:[XX], 処理識別子:[XX] (Xxx.java:129)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(2)] XxxHandler - I500031 - ファイル送信が完了しました。セッションID:[XX], ファイル:[XX], ファイルID:[XX], 処理識別子:[XX] (Xxx.java:156)
    20XX-MM-DD XX:XX:XX,XXX INFO [thread(2)] XxxHandler - I500055 - セッションが切断されました。セッションID:[XX], ファイル:[XX], ファイルID:[XX], 処理識別子:[XX], 切断コード:[XX] (Xxx.java:138)

転送ログ
    
    
    20XX-MM-DD XX:XX:XX,XXX [START] Method=put, FileID=SAMPLE, RemoteHost=webconnect_demo_host, Identifier= undefined
    20XX-MM-DD XX:XX:XX,XXX [END ] Method=put, FileID=SAMPLE, RemoteHost=webconnect_demo_host, Identifier= F7EBF875E2420795596ED6EBE69B9F2EB1, status=0, message="Transfer finished successfully."
    20XX-MM-DD XX:XX:XX,XXX [START] Method=get, FileID=SAMPLE, RemoteHost=webconnect_demo_host, Identifier= 0A61DF1FC49115C415535C8626BDAF2DB1
    20XX-MM-DD XX:XX:XX,XXX [END ] Method=get, FileID=SAMPLE, RemoteHost=webconnect_demo_host, Identifier= 0A61DF1FC49115C415535C8626BDAF2DB1, status=0, message="Transfer finished successfully."


---


## ページ 9

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLILog/LogCLI.htm

# CLIのログ

CLIの動作やファイル転送に関する記録をログに残すことができます。


---


## ページ 10

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLILog/LogConfFile.htm

# 設定ファイルの説明

ログの設定ファイルは以下に格納されています。
    
    
    {導入ディレクトリ}/config/logback.xml

CLIは内部でLogbackというログ出力用ライブラリを使用しています。

上記の設定ファイルの内容を変更することにより、出力するログの内容を変更することができます。設定を変更するには、XMLエディタ等で設定ファイルを編集してください。

Logbackについての詳細は、以下のWebサイトを参照してください。

URL: <http://logback.qos.ch/>


---


## ページ 11

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLILog/LogTypes.htm

# ログの種類

ログには、以下の2種類があります。

コンソールログ

CLI の動作に関するログです。

転送ログ

ファイル転送の開始・終了のログです。


---


## ページ 12

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/CLIConfFile.htm

# CLI設定ファイル

CLIの動作について設定します。

CLI導入時に初期設定されている内容を、ご利用のシステム環境にあわせて変更してください。


---


## ページ 13

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/CLISettings.htm

# CLIの設定

CLI設定ファイルおよび転送定義ファイルについて説明します。


---


## ページ 14

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/ExplanEachFieldConf.htm

# 各項目の説明

CLI情報設定

cli.apiKey
    

CLIで使用するAPIキーです。

Management Consoleの[APIキー管理]画面で発行したAPIキーを設定してください。

この項目の設定は必須です。

cli.agent.id
    

CLIを識別するIDです。

この項目の設定は必須です。また、大文字小文字を区別します。

**注意**

以下の理由から、HULFT for IBMiと接続する場合は cli.agent.id に英小文字を使用しないでください。

  * 該当の設定値はHULFTの詳細ホスト情報のホスト名として使用されます。

  * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。




cli.hostname
    

CLIを実行するホスト名です。

この項目の設定は必須です。

**注意**

以下の理由から、HULFT for IBMiと接続する場合は cli.hostname に英小文字を使用しないでください。

  * 該当の設定値はHULFTの詳細ホスト情報のホスト名として使用されます。

  * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。




接続情報設定

connection.id
    

HULFT-WebConnectへの接続を識別するIDです。

サービス内で一意にする必要があります。

この項目の設定は必須です。

**注意**

  * コネクションIDは事前にManagement Consoleで登録する必要があります。

  * 注意バージョン2.2.0より前のCLIを使用している場合、CLI設定ファイルに定義しているコネクションIDにIPフィルタが設定されていないか確認してください。設定されていると、該当するコネクションIDを使用したファイル転送はできなくなります。

  * 以下の理由から、HULFT for IBMiと接続する場合は connection.id に英小文字を使用しないでください。

    * 該当の設定値はHULFTの詳細ホスト情報のホスト名として使用されます。

    * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。




connection.password
    

CLIがHULFT-WebConnectに接続する際の認証パスワードです。

この項目の設定は必須です。

**注意**

コネクションパスワードは事前に Management Console で登録する必要があります。

service.accesspoint
    

CLIが接続するサービスのアクセスポイントです。

この項目の設定値は変更しないでください。

プロキシ情報設定

proxy.host
    

プロキシサーバを経由する場合のホスト名またはドメイン名（IPアドレス）を設定します。

インストール直後は、行の先頭に「#」があるため（コメント行）、無効になっています。

有効にする場合は、先頭の「#」を削除して（コメント解除）、値を設定してください。

この項目は大文字小文字を区別しません。

proxy.port
    

プロキシサーバを経由する場合のポート番号を設定します。

インストール直後は、行の先頭に「#」があるため（コメント行）、無効になっています。

有効にする場合は、先頭の「#」を削除して（コメント解除）、値を設定してください。

proxy.username
    

ユーザ認証が必要なプロキシサーバを経由する場合のユーザ名を設定します。

インストール直後は、行の先頭に「#」があるため（コメント行）、無効になっています。

有効にする場合は、先頭の「#」を削除して（コメント解除）、値を設定してください。

この項目は大文字小文字を区別します。

proxy.password
    

ユーザ認証が必要なプロキシサーバを経由する場合のパスワードを設定します。

インストール直後は、行の先頭に「#」があるため（コメント行）、無効になっています。

有効にする場合は、先頭の「#」を削除して（コメント解除）、値を設定してください。

この項目は大文字小文字を区別します。

CLIアップデート設定

update.action
    

CLI実行時のアップデート通知について設定します。

"update"、"alert"または"none"を設定できます。この項目は大文字小文字を区別します。

"update"または"alert"を設定すると、更新の有無を通知します。手動でアップデートを行ってください。

**= 備考 =**

"update"は非推奨です。今後のバージョンで廃止される予定です。

例 : 更新対象がある場合
    
    
    I600029 - アップデートの確認に成功しました。メッセージ:[You can update to latest version X.X.X from Y.Y.Y.]

例 : 更新対象がない場合
    
    
    I600029 - アップデートの確認に成功しました。メッセージ:[You do not have to update: latest version X.X.X.]

update.action.onError
    

アップデート失敗時にCLIの実行を継続するかどうかを設定します。

「update.action」に"update"または"alert"を指定した場合のみ、設定値が有効になります。

"continue"または"abort"を設定できます。この項目は大文字小文字を区別します。

"continue"を設定すると、アップデートが失敗した場合でもCLIの実行を継続します。

"abort"を設定すると、アップデートが失敗した場合にCLIの実行は中断されます。

システム動作設定

directory.work
    

CLIの作業ディレクトリです。

ファイル転送時の一時ファイルの作成等で使用します。

io.file.overwrite
    

GETによるファイル転送時に使用される集信ファイルを上書きするかどうかを指定します。

集信ファイルを上書きする場合は、"true"を指定してください。

"false"を指定すると、集信ファイルの上書きを行いません。

この項目の設定を省略した場合は、初期値の"false"が設定されます。

io.session.timeout
    

無通信時のセッションタイムアウトを設定します。

単位は秒で、"0"から"60"まで指定できます。

"0"を設定すると、無通信時にセッションタイムアウトを行いません。

この項目の設定を省略した場合は、初期値の"60"が設定されます。

jvm.options
    

CLIを実行するJavaの起動オプションを指定します。

複数のオプションを指定する場合は、半角スペースで区切ります。

この項目は大文字小文字を区別します。

例 : メモリ割り当て
    
    
    jvm.options=-Xms32M -Xmx32M

例 : 言語設定
    
    
    # Set to English.
    jvm.options=-Duser.language=en
    # Set to Japanese.
    jvm.options=-Duser.language=ja

**注意**

指定できる値や形式はJavaの仕様に準じます。

設定ファイルのバージョン情報

configuration.version
    

CLI設定ファイルのバージョン情報です。

この項目の設定値は変更しないでください。

表4.1 設定項目一覧

No |  キー名 |  説明 |  初期値 |  省略時値 |  必須 |  設定値 |  備考  
---|---|---|---|---|---|---|---  
1 |  cli.apiKey |  CLIで使用するAPIキー |  |  |  必須 |  半角英数字 |  大文字小文字を区別します  
2 |  cli.agent.id |  CLIを識別するID |  |  |  必須 |  半角英数字 記号(*1) |  25バイト以内大文字小文字を区別します  
3 |  cli.hostname |  CLIを実行するホスト名 |  |  |  必須 |  半角英数字 記号(*1) |  25バイト以内大文字小文字を区別します  
4 |  connection.id |  コネクションID |  |  |  必須 |  半角英数字 記号(*1) |  16バイト以内大文字小文字を区別します  
5 |  connection.password |  コネクションパスワード |  |  |  必須 |  半角英数字 記号 |  8バイト以上256バイト以内 大文字小文字を区別します  
6 |  service.accesspoint |  サービスアクセスポイント |  service- ap.tokyo.webconnect.hulft.com |  |  必須 |  |  この項目の設定値は変更不可  
7 |  proxy.host |  プロキシホスト |  |  |  |  半角英数字 記号 |  255バイト以内大文字小文字を区別しません  
8 |  proxy.port |  プロキシポート |  |  |  |  1-65535 |   
9 |  proxy.username |  プロキシユーザ名 |  |  |  |  半角文字 |  256バイト以内大文字小文字を区別します  
10 |  proxy.password |  プロキシパスワード |  |  |  |  半角文字 |  256バイト以内大文字小文字を区別します  
11 |  update.action |  CLIアップデート設定 |  alert |  alert |  |  update|alert|none |  大文字小文字を区別します  
12 |  update.action.onError |  アップデート失敗時のCLI実行設定 |  continue |  continue |  |  continue|abort |  大文字小文字を区別します  
13 |  directory.work |  CLIの作業ディレクトリ |  . |  . |  |  |   
14 |  io.file.overwrite |  集信ファイルの上書き指定 |  false |  false |  |  true|false |  大文字小文字を区別します  
15 |  io.session.timeout |  セッションタイムアウト |  60 |  60 |  |  0-60 |   
16 |  jvm.options |  Javaの起動オプション |  -Xms32M -Xmx32M |  |  |  半角文字 |  大文字小文字を区別します  
17 |  configuration.version |  設定ファイルのバージョン情報 |  |  |  必須 |  |  この項目の設定値は変更不可  
*1 |  : |  HULFT8 for IBMiと接続する場合は英小文字を使用しないでください。  
---|---|---  
  
**注意**

「cli.agent.id」、「cli.hostname」、「proxy.host」に設定できる記号は「-（ハイフン）」「.（ピリオド）」です。


---


## ページ 15

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/ExplanEachFieldTrans.htm

# 各項目の説明

destination.hostname
    

接続先のホスト情報です。

「接続先のAgentで使用しているコネクションID（16文字以内）」、「接続先のAgentのAgent ID（25文字以内）」、「接続先のHULFTのホスト名（25文字以内）」をアンダースコア区切りで指定します。

この項目の設定は必須です。

destination.port
    

接続先のHULFTのポート番号です。

この項目の設定は必須です。

PUT時：接続先のHULFTの集信ポート番号

GET時：接続先のHULFTの要求受付ポート番号

file.id
    

接続先のHULFTのファイルIDです。

この項目の設定は必須です。

PUT時：接続先のHULFTの集信管理情報のファイルID

GET時：接続先のHULFTの配信管理情報のファイルID

file.path
    

集配信するファイルのフルパスです。

この項目の設定は必須です。

PUT時：接続先のHULFTに転送する配信ファイルのフルパス

GET時：接続先のHULFTから受信したデータを格納する集信ファイルのフルパス

params.msg0～params.msg5
    

接続先のHULFTへ送信するメッセージです。

params.msgl0～params.msgl1
    

接続先のHULFTへ送信する拡張メッセージです。

表4.2 設定項目一覧

No |  キー名 |  説明 |  初期値 |  省略時値 |  必須 |  設定値 |  備考  
---|---|---|---|---|---|---|---  
1 |  destination.hostname |  接続先のホスト情報 |  |  |  必須 |  半角英数字 記号 |  記号68バイト以内 大文字小文字を区別します  
2 |  destination.port |  接続先HULFTのポート番号 |  |  |  必須 |  1-65535 |  PUT時：集信ポート番号 GET時：要求受付ポート番号  
3 |  file.id |  接続先HULFTのファイルID |  |  |  必須 |  半角大文字英数字 記号 |  50バイト以内 PUT時：集信管理情報のファイルID GET時：配信管理情報のファイルID  
4 |  file.path |  集配信するファイルのフルパス |  |  |  必須 |  |  200バイト以内 PUT時：配信ファイルのフルパス GET時：集信ファイルのフルパス  
5 |  params.msg0～params.msg5 |  接続先HULFTへ送信するメッセージ |  |  |  |  |  50バイト以内  
6 |  params.msgl0～params.msgl1 |  接続先HULFTへ送信する拡張メッセージ |  |  |  |  |  200バイト以内  
  
**注意**

  * 「destination.hostname」に設定できる記号は「-（ハイフン）」「.（ピリオド）」です。

  * 「file.id」に設定できる記号は「_（アンダーバー）」です。





---


## ページ 16

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/SettingsCLIConfFile.htm

# ファイルの設定

設定方法

以下のCLI設定ファイルをテキストエディタ等で編集します。

CLI設定ファイルの文字コードは、UTF-8を使用します。
    
    
    {導入ディレクトリ}/config/transfer-cli.conf

記述フォーマット

行の先頭に半角の「#」があるときは、コメント行とみなされます。

空行は存在していても構いません。また、空行やコメント行は連続しても構いません。項目を設定する行は、以下のフォーマットで記述します。
    
    
    キー名 = 設定値

キー名は設定する項目を表す名前で、項目ごとに異なる名前を使用します。名前はあらかじめ決まっているため、変更することはできません。

キー名と設定値の間は、半角の「=」で区切ります。

設定値の反映

設定ファイルを編集した場合、CLIの次回実行時に変更内容が反映されます。


---


## ページ 17

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/SettingsTransDefFile.htm

# ファイルの設定

設定方法

テンプレートを参考にして、転送定義ファイルをテキストエディタ等で作成・編集します。転送定義ファイルの文字コードは、UTF-8を使用します。

転送定義ファイルのテンプレートは以下に格納されています。
    
    
    {導入ディレクトリ}/config/parameter-template.txt

記述フォーマット

行の先頭に半角の「#」があるときは、コメント行とみなされます。

空行は存在していても構いません。また、空行やコメント行は連続しても構いません。項目を設定する行は、以下のフォーマットで記述します。
    
    
    キー名 = 設定値

キー名は設定する項目を表す名前で、項目ごとに異なる名前を使用します。名前はあらかじめ決まっているため、変更することはできません。

キー名と設定値の間は、半角の「=」で区切ります。

設定値の反映

転送定義ファイルを編集した場合、CLIの次回実行時（該当ファイルを指定して実行時）に変更内容が反映されます。


---


## ページ 18

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLISetting/TransDefFile.htm

# 転送定義ファイル

定義ファイル指定でCLIによるファイル転送を行う場合は、転送定義ファイルを作成する必要があります。定義ファイル指定によるCLIの実行方法は、[「コマンドリファレンス」](../CmdRef/CommandRef.htm)を参照してください。


---


## ページ 19

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CLIUninstll/UninstallCLI.htm

# CLIのアンインストール

導入ディレクトリを削除してください。

CLI設定ファイルの「directory.work」を設定していた場合は、該当ディレクトリも削除してください。


---


## ページ 20

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/CLIUpdateCom.htm

# CLIアップデート確認コマンド

CLIに更新対象があるかどうか確認します。

設定ファイル（transfer-cli.conf）が認識できない場合は、コマンドを実行することができません。

CLI設定ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。

コマンド

update-cli


---


## ページ 21

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/CommandRef.htm

# コマンドリファレンス

コマンドインタフェースについて説明します。
    
    
    **コマンドの説明に使用する表記**
    
    [ ] : 大かっこ。このかっこで囲まれた項目は、省略できることを示します。
    
    { } : 中かっこ。かっこ内の項目の中から 1 つを選択する必要があることを示します。


---


## ページ 22

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/GETSpecifyParam.htm

# GET（パラメータ指定）

転送に必要な情報をコマンドのパラメータに指定して、接続先のHULFTからファイルを GET（送信要求）します。

コマンド
    
    
    webconnect-transfer-cli get -file filePath -f fileId -h connectionId_agentId_host:port [-msg0 message] [-msg1 message] [-msg2 message] [-msg3 message] [-msg4 message] [-msg5 message] [-msgl0 message] [-msgl1 message] [-c filePath]

パラメータ説明

get
    

GETコマンドを表す（省略不可）

-file filePath
    

接続先のHULFTから受信したデータを格納する集信ファイルのフルパス（省略不可）

-f fileId
    

接続先のHULFTの配信管理情報のファイルID（省略不可）

-h connectionId_agentId_host:port
    

接続先のホスト情報（省略不可）

「接続先のAgentで使用しているコネクションID」、「接続先のAgentのAgent ID」、「接続先のHULFTのホスト名：要求受付ポート番号」をアンダースコア区切りで指定します。

-msg0 message ～ -msg5 message
    

接続先のHULFTへ送信するメッセージ（省略可）

50バイト以内で指定します。

-msgl0 message ～ -msgl1 message
    

接続先のHULFTへ送信する拡張メッセージ（省略可）

200バイト以内で指定します。

-c filePath
    

CLI設定ファイルのフルパス（省略可）

省略した場合、「{導入ディレクトリ}/config/transfer-cli.conf」を参照します。

CLI設定ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。


---


## ページ 23

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/GETSpecifyTransDef.htm

# GET（定義ファイル指定）

転送定義ファイルを指定して、接続先のHULFTからファイルをGET（送信要求）します。

コマンド
    
    
    webconnect-transfer-cli get -p filePath [-c filePath]

パラメータ説明

get
    

GETコマンドを表す（省略不可）

-p filePath
    

転送定義ファイルのフルパス（省略不可）

転送定義ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。

-c filePath
    

CLI設定ファイルのフルパス（省略可）

省略した場合、「{導入ディレクトリ}/config/transfer-cli.conf」を参照します。

CLI設定ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。


---


## ページ 24

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/PUTSpecifyParam.htm

# PUT（パラメータ指定）

転送に必要な情報をコマンドのパラメータに指定して、接続先のHULFTにファイルをPUT（配信）します。

コマンド
    
    
    webconnect-transfer-cli put -file filePath -f fileId -h connectionId_agentId_host:port [-msg0 message] [-msg1 message] [-msg2 message] [-msg3 message] [-msg4 message] [-msg5 message] [-msgl0 message] [-msgl1 message] [-c filePath]

パラメータ説明

put
    

PUTコマンドを表す（省略不可）

-file filePath
    

接続先のHULFTに転送するファイルのフルパス（省略不可）

-f fileId
    

接続先のHULFTの集信管理情報のファイルID（省略不可）

-h connectionId_agentId_host:port
    

接続先のホスト情報（省略不可）

「接続先のAgentで使用しているコネクションID」、「接続先のAgentのAgent ID」、「接続先のHULFTのホスト名：集信ポート番号」をアンダースコア区切りで指定します。

-msg0 message ～ -msg5 message
    

接続先のHULFTへ送信するメッセージ（省略可）

50バイト以内で指定します。

-msgl0 message ～ -msgl1 message
    

接続先のHULFTへ送信する拡張メッセージ（省略可）

200バイト以内で指定します。

-c filePath
    

CLI設定ファイルのフルパス（省略可）

省略した場合、「{導入ディレクトリ}/config/transfer-cli.conf」を参照します。

CLI設定ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。


---


## ページ 25

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/PUTSpecifyTransDef.htm

# PUT（定義ファイル指定）

転送定義ファイルを指定して、接続先のHULFTにファイルをPUT（配信）します。

コマンド
    
    
    webconnect-transfer-cli put -p filePath [-c filePath]

パラメータ説明

put
    

PUTコマンドを表す（省略不可）

-p filePath
    

転送定義ファイルのフルパス（省略不可）

転送定義ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。

-c filePath
    

CLI設定ファイルのフルパス（省略可）

省略した場合、「{導入ディレクトリ}/config/transfer-cli.conf」を参照します。

CLI設定ファイルの詳細は、[「CLIの設定」](../CLISetting/CLISettings.htm)を参照してください。


---


## ページ 26

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/CmdRef/VersionDispCom.htm

# バージョン表示コマンド

CLIのバージョンを表示します。

コマンド
    
    
    webconnect-transfer-cli -version

パラメータ説明

-version
    

バージョン表示コマンドを表す（省略不可）


---


## ページ 27

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/FileTransfer.htm

# ファイル転送

CLIによるファイル転送方法について説明します。


---


## ページ 28

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/GETMethodSend.htm

# GET（送信要求）

接続先のAgent（集信Agentおよび配信Agent）を経由してHULFTからファイルをGET（送信要求）します。コマンドの詳細については、[「コマンドリファレンス」](../CmdRef/CommandRef.htm)を参照してください。


---


## ページ 29

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/GETMforLx.htm

# Linuxの場合 

(1) ターミナル等のクライアントを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

(2) 以下の例を参考にして、コマンドを実行します。

パラメータ指定の実行例
    
    
    # ./webconnect-transfer-cli get -file /tmp/receivefile -f DEMO -h webconnect_demo_sender:31000

定義ファイル指定の実行例
    
    
    # ./webconnect-transfer-cli get -p /tmp/parameter


---


## ページ 30

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/GETMforWin.htm

# Windowsの場合

(1) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}\bin

(2) 以下の例を参考にして、コマンド（バッチファイル）を実行します。

パラメータ指定の実行例
    
    
    webconnect-transfer-cli get -file C:\tmp\receive.txt -f DEMO -h webconnect_demo_sender:31000

定義ファイル指定の実行例
    
    
    webconnect-transfer-cli get -p C:\tmp\parameter.txt


---


## ページ 31

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/PUTMethodSend.htm

# PUT（配信）

接続先のAgent（集信Agent）を経由してHULFTにファイルをPUT（配信）します。コマンドの詳細については、[「コマンドリファレンス」](../CmdRef/CommandRef.htm)を参照してください。


---


## ページ 32

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/PUTMforLx.htm

# Linuxの場合

(1) ターミナル等のクライアントを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

(2) 以下の例を参考にして、コマンドを実行します。

パラメータ指定の実行例
    
    
    # ./webconnect-transfer-cli put -file /tmp/example -f DEMO -h webconnect_demo_receiver:30000

定義ファイル指定の実行例
    
    
    # ./webconnect-transfer-cli put -p /tmp/parameter


---


## ページ 33

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/FileTransfer/PUTMforWin.htm

# Windowsの場合

(1) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}\bin

(2) 以下の例を参考にして、コマンド（バッチファイル）を実行します。

パラメータ指定の実行例
    
    
    webconnect-transfer-cli put -file C:\tmp\example.txt -f DEMO -h webconnect_demo_receiver:30000

定義ファイル指定の実行例
    
    
    webconnect-transfer-cli put -p C:\tmp\parameter.txt


---


## ページ 34

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/HULFTSetting/ForGETMethod.htm

# GETの場合

CLIを使用して接続先のHULFTにGET（送信要求）する場合の、管理情報の設定について説明します。


---


## ページ 35

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/HULFTSetting/ForPUTMethod.htm

# PUTの場合

CLIを使用して接続先のHULFTにPUT（配信）する場合の、管理情報の設定について説明します。


---


## ページ 36

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/HULFTSetting/HULFTSettings.htm

# HULFTの設定

CLIを使用して接続先のHULFTにPUT（配信）およびGET（送信要求）する場合の、HULFTの設定方法について説明します。


---


## ページ 37

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/HULFTSetting/SettingsManageInfoGET.htm

# 管理情報の設定

接続先のHULFTからファイルをGET（送信要求）する場合は、接続先のHULFTの管理情報の設定が必要となります。

HULFTの管理情報の設定については、HULFTの「オペレーション マニュアル」を参照してください。

(1) 詳細ホスト情報

以下の項目の設定が必要です。

表5.1 詳細ホスト情報の設定項目

項目 |  設定内容  
---|---  
ホスト名 |  CLIのconnection.idの設定値_CLIのcli.agent.idの設定値_CLIのcli.hostname の設定値 **注意**

  * 各項目を「_（アンダースコア）」で区切ります。 各項目の設定値は、CLI 設定ファイル（transfer-cli.conf）で指定した値です。 CLI設定ファイルの内容を事前に確認してください。
  * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。 HULFT for IBMiと接続する場合、以下の設定値に英小文字を使用しないでください。
    * CLIのconnection.id
    * CLIのcli.agent.id
    * CLIのcli.hostname

例) CLI設定ファイルの設定が、connection.id=webconnect、cli.agent.id=demo、cli.hostname=senderの場合 設定値 : webconnect_demo_sender  
集信ポートNo. |  CLIとの通信には使用しないため、初期値から変更する必要はありません。  
要求受付ポートNo. |  CLIとの通信には使用しないため、初期値から変更する必要はありません。  
HULFT7通信モード |  無効  
PROXYサーバ名 |  Agentを起動している接続先マシンのホスト名（HULFTが名前解決できること）  
PROXYポートNo. |  接続先マシンのAgentの待受ポート番号  
  
(2) 転送グループ情報

「詳細ホスト情報」で登録したホストを含む転送グループ情報を登録します。

(3) 配信管理情報

「転送グループ情報」で登録した転送グループIDを設定した配信管理情報を登録します。


---


## ページ 38

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/HULFTSetting/SettingsManageInfoPUT.htm

# 管理情報の設定

接続先のHULFTにファイルをPUT（配信）する場合は、接続先のHULFTの管理情報の設定が必要となります。主に以下の管理情報の設定が必要です。

HULFTの管理情報の設定については、HULFTの「オペレーション マニュアル」を参照してください。

(1) 詳細ホスト情報

CLIのホスト名を登録します。

CLIのホスト名は、CLI設定ファイルの「cli.hostname」に設定した値です。

**注意**

HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。

HULFT for IBMiと接続する場合は cli.hostname に英小文字を使用しないでください。

(2) 集信管理情報

集信管理情報を登録します。

以下の３つは、下記のとおりに設定してください。

集信形態:"単一集信"

世代管理:"しない"

データ検証:"しない"


---


## ページ 39

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/KnownIssues/KnownIssues.htm

# 既知の問題点

Windowsの場合、CLIのコンソールログにJavaのエラーが出力される場合がある

Windowsでファイル転送を行った場合、転送が正常終了していてもCLIのコンソールログにJavaのエラーが出力される場合があります。

例 : Java のエラーが「Can not set SO_KEEPALIVE to true」の場合
    
    
    6 19, 2016 7:45:21 午後 org.glassfish.grizzly.nio.transport.TCPNIOTransport configureChannel
    警告: GRIZZLY0005: Can not set SO_KEEPALIVE to true
    java.net.SocketException: Invalid argument: no further information
        at sun.nio.ch.Net.setIntOption0(Native Method)
        at sun.nio.ch.Net.setSocketOption(Net.java:334)
        at sun.nio.ch.SocketChannelImpl.setOption(SocketChannelImpl.java:190)
        at sun.nio.ch.SocketAdaptor.setBooleanOption(SocketAdaptor.java:271)
        at sun.nio.ch.SocketAdaptor.setKeepAlive(SocketAdaptor.java:370)
        at org.glassfish.grizzly.nio.transport.TCPNIOTransport.configureChannel(TCPNIOTransport.java:439)
        at org.glassfish.grizzly.nio.transport.TCPNIOConnectorHandler.onConnectedAsync(TCPNIOConnectorHandler.java:214)
        at org.glassfish.grizzly.nio.transport.TCPNIOConnectorHandler$1.connected(TCPNIOConnectorHandler.java:154)
        at org.glassfish.grizzly.nio.transport.TCPNIOConnection.onConnect(TCPNIOConnection.java:258)
        at org.glassfish.grizzly.nio.transport.TCPNIOTransport.fireIOEvent(TCPNIOTransport.java:552)
        at org.glassfish.grizzly.strategies.AbstractIOStrategy.fireIOEvent(AbstractIOStrategy.java:112)
        at org.glassfish.grizzly.strategies.WorkerThreadIOStrategy.run0(WorkerThreadIOStrategy.java:117)
        at org.glassfish.grizzly.strategies.WorkerThreadIOStrategy.executeIoEvent(WorkerThreadIOStrategy.java:103)
        at org.glassfish.grizzly.strategies.AbstractIOStrategy.executeIoEvent(AbstractIOStrategy.java:89)
        at org.glassfish.grizzly.nio.SelectorRunner.iterateKeyEvents(SelectorRunner.java:414)
        at org.glassfish.grizzly.nio.SelectorRunner.iterateKeys(SelectorRunner.java:383)
        at org.glassfish.grizzly.nio.SelectorRunner.doSelect(SelectorRunner.java:347)
        at org.glassfish.grizzly.nio.SelectorRunner.run(SelectorRunner.java:278)
        at org.glassfish.grizzly.threadpool.AbstractThreadPool$Worker.doWork(AbstractThreadPool.java:565)
        at org.glassfish.grizzly.threadpool.AbstractThreadPool$Worker.run(AbstractThreadPool.java:545)
        at java.lang.Thread.run(Thread.java:745)
     
    Transfer finished successfully.

CLIアップデートの確認を行った場合、誤った判定結果が出力される場合がある

バージョン2.0.0のCLIでは、アップデートの確認を行うと使用中のCLIが最新であると誤って判定され、その判定結果がコンソール画面およびログファイルに出力されます。


---


## ページ 40

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/ForcedTerminatCLI.htm

# CLIの強制終了

［Ctrl］＋［C］キーなどでCLIのプロセスを強制終了した場合、転送処理時に作成する一時ファイル（.tmp）が作業ディレクトリに残る場合があります。

不要なファイルなので、削除してください。


---


## ページ 41

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/FrequentAskedQuestions.htm

# よくあるご質問

よくあるご質問とその回答を以下のサイトで公開しています。

URL: [HULFT Technical Support & FAQ ](https://www.hulft.com/tech-support/)

ご利用の際は、SP コードおよび製品版の基本サブスクリプションのシリアル番号を使用してログインしてください。


---


## ページ 42

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/PermissionsReceive.htm

# 集信ファイルパーミッション

CLIをLinuxで使用する場合、GET時の集信ファイルのパーミッションは「644」です。

集信ファイルのパーミッションを変更する場合は、CLIの実行後、別途パーミッションの変更作業を行ってください。


---


## ページ 43

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/PointsNotedOperate.htm

# 運用時の留意点

運用時の留意点について説明します。


---


## ページ 44

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/Restrictions.htm

# 制限事項

CLIでは、以下の制限があります。

  * 1転送あたりのファイルサイズの上限は2GBです。

  * 1契約アカウント当たり1分間に最大20転送（「Data Transfer API」「ブラウザ転送」「CLI」の合計の転送リクエスト数）まで行うことができます。

リミット超過時は、超過以降のリクエストを10分間受け付けません（リクエスト禁止期間）。

  * 配信ファイルと集信ファイルが同一かのチェックはファイルサイズのみで行います（集信側の「データ検証」は行えません）。

  * データ暗号化機能は提供しておりません。

  * データ圧縮・解凍機能は提供しておりません。

  * チェックポイント再配信・チェックポイント再送の機能は提供しておりません。

  * ジョブ実行機能は提供しておりません。

  * ネットワーク瞬断時や接続時等の自動再接続・自動再実行機能は提供しておりません。

  * クラスタ対応機能（フェールオーバー対応等）は提供しておりません。

  * バイナリ転送以外のHULFTの転送タイプには対応しておりません。

  * CLI同士のファイル転送には対応しておりません。

  * ファイルサーバ等のネットワーク上のファイル転送には対応しておりません。

  * 接続先のHULFTから要求されたファイル転送には対応しておりません。ファイル転送を行う場合は、CLIからPUTまたはGETを実行してください。

  * Ver.8.1未満のHULFTとのファイル転送には対応しておりません。

  * 高強度暗号強制モードに対応しておりません。

  * 電文転送タイプは「転送速度優先モード」で動作します。対向のHULFTのシステム動作環境設定を「転送速度優先モード」に設定してください。

  * 同一ファイルを配信対象とした多重転送はできません。

  * CLIは自動でアップデートできません。手動でアップデートしてください。

  * 以下の理由から、HULFT for IBMiと接続する場合はCLIのコネクションID（connection.id）、CLIの識別ID（cli.agent.id）、およびCLIのホスト名（cli.hostname）に英小文字を使用しないでください。

    * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。

    * CLIがHULFTと接続する場合、HULFTの詳細ホスト情報のホスト名に「<_cli.hostnameの設定値_ >」または「<_connection.idの設定値_ >_<_cli.agent.idの設定値_ >_<_cli.hostnameの設定値_ >」を設定する必要があります。





---


## ページ 45

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/SessionManage.htm

# セッション管理

CLIはファイル転送を実行している間のみ、HULFT-WebConnectとのセッション接続を行います。ファイル転送が完了すると、CLIはHULFT-WebConnectとのセッションを切断します。


---


## ページ 46

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/PointsNote/TransMultiple.htm

# CLIによる多重転送

多重転送が正常終了した場合でも、console.logに次のようなエラーメッセージが出力される場合があります。
    
    
    E600028 - アップデートは他のプロセスですでに実行されています。
    
    
    j.c.s.s.h.t.w.e.s.BaseApplicationService - Failed to delete the update control file.

この現象を回避するためには、CLI設定ファイル（transfer-cli.conf）のupdate.actionの値を"alert"または"none"に設定してください。


---


## ページ 47

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/Preface/preface.htm

# CLI 操作ガイド \- はじめに

このたびは、本製品をご利用いただき、誠にありがとうございます。

本ガイドは、コマンドラインインタフェース（CLI）を使ってHULFT-WebConnectを操作する方を対象にしています。


---


## ページ 48

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-CLI/Content/CLIGuide/Preface/Transcription.htm

# 表記について

製品名等の固有名詞は、各メーカーの商標または登録商標です。


---

