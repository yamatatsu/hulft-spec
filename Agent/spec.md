# HULFT WebConnect - Agent

このドキュメントは 71 ページから生成されました。

---


## ページ 1

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentLog/AgentLog.htm

# Agent のログ

Agent の起動・停止やファイル転送に関する記録をログに残すことができます。


---


## ページ 2

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentLog/DefLogOutDestination.htm

# 初期設定のログ出力場所

バージョン 2.3.1以前の Agent では、デフォルトのログファイルは以下に出力されます。
    
    
    {導入ディレクトリ}/bin/logs/agent.log

バージョン 2.4.0 以降の Agent で出力されるログの種類については以下の通りです。

表8.1 ログ種類一覧

No |  ログファイル （{導入ディレクトリ}/bin/logs/配下） |  設定ファイル （{導入ディレクトリ}/config/配下） |  説明  
---|---|---|---  
1 |  agent-exec.log |  logback.xml |  Agent 起動処理（Windows サービスによる起動を除く）に関するログと、アップデート確認に関するログが出力されます。  
2 |  agent-rmi.log(*) |  logback-rmi.xml |  CommandRegistryServer に関するログが出力されます。 また、Windows サービスによる起動の場合は、Agent 起動処理に関するログも合わせて出力されます。  
3 |  agent-send.log(*) |  logback-send.xml |  配信Agent に関するログが出力されます。 ファイル転送関連のログもこちらに出力されます。  
4 |  agent-recv.log(*) |  logback-recv.xml |  集信Agent に関するログが出力されます。 ファイル転送関連のログもこちらに出力されます。  
5 |  agent-command.log |  logback-command.xml |  「Agent 状態確認コマンド」、または「Agent 停止コマンド」を実行した際に読み込んだ設定ファイル（agent.conf）に関する情報ログが出力されます。 ※出力レベルをDEBUG もしくはTRACE に指定した場合のみ出力されます。  
6 |  agent-win_serv.log |  logback-win_serv.xml |  サービス起動時のアップデート確認に関するログと、サービス停止関連のログが出力されます。 ※Windows サービスを利用した場合のみ出力されます。  
  
**= 備考 =**

Agent 起動完了後、常駐するプロセスのログが出力されるのは*がついた3種類のログとなります。(起動方法に関わらず、Windows、Linux とも同様)


---


## ページ 3

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentLog/DefLogOutEx.htm

# 初期設定のログ出力例

「ログ出力日付」、「ログ出力時間」、「Agent ID」、「ログレベル」、「ログ出力クラス」、「ログメッセージ番号」、「ログメッセージ」を半角スペース区切りで出力します。
    
    
    20XX-MM-DD XX:XX:XX,XXX AGENTID[agentID] INFO jp.co.saison.xxx - I110001 - 配信Agentを起動します。 (Xxxxx.java:142)
    20XX-MM-DD XX:XX:XX,XXX AGENTID[agentID] INFO jp.co.saison.xxx - I110015 - Serviceに接続します。アクセスポイント:[XX](Xxxxx.java:157)
    20XX-MM-DD XX:XX:XX,XXX AGENTID[agentID] INFO jp.co.saison.xxx - I110004 - 配信Agentの情報をServiceに送信します。 (Xxxxx.java:31)
    20XX-MM-DD XX:XX:XX,XXX AGENTID[agentID] INFO jp.co.saison.xxx - I110002 - 配信Agentを起動しました。 (Xxxxx.java:189)
    20XX-MM-DD XX:XX:XX,XXX AGENTID[agentID] WARN jp.co.saison.xxx - W100007 - 警告を検知しました。(Xxxxx.java:169)
    20XX-MM-DD XX:XX:XX,XXX AGENTID[agentID] ERROR jp.co.saison.xxx - E100000 - エラーを検知しました。(Xxxxx.java:169)


---


## ページ 4

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentLog/LogConfigFile.htm

# 設定ファイルの説明

バージョン 2.3.1以前の Agentでは、ログの設定ファイルは以下に格納されています。
    
    
    {導入ディレクトリ}/config/logback.xml 

Agent は内部で Logback というログ出力用ライブラリを使用しています。 

上記の設定ファイルの内容を変更することにより、出力するログの内容を変更することができます。

設定を変更するには、XML エディタ等で設定ファイルを編集してください。

Logback についての詳細は、以下の Web サイトを参照してください。

URL: <http://logback.qos.ch/>

また、バージョン 2.4.0 以降の Agent では、出力されるログファイルごとに設定ファイルが存在します。

必要に応じて対象となる設定ファイルを編集してください。

設定ファイルを編集する場合、出力先のログファイル名が重複しないようご注意ください。

各設定ファイルと対応するログファイル名・出力内容についての詳細は、[「初期設定のログ出力場所」](DefLogOutDestination.htm)を参照してください。


---


## ページ 5

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/AgentSet.htm

# Agent の設定

Agent 設定ファイルおよびコネクション ID 認証ファイルについて説明します。

**注意**

一部の項目は事前にManagement Consoleで登録する必要があります。

詳細は、[「ファーストステップガイド」](../../../../HWC-FSG/Content/FirstStep/ServiceSet/ServiceSettings.htm)を参照してください。


---


## ページ 6

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/AgentSetFile.htm

# Agent設定ファイル

Agent の動作について設定します。

Agent 導入時に初期設定されている内容を、ご利用のシステム環境にあわせて変更してください。


---


## ページ 7

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/AgentSetFileItem.htm

# 各項目の説明

Agent 情報設定

agent.id

Agent を識別する ID です。

任意の値を設定できます。複数の Agent で同じコネクション ID を使用する場合は、各 Agent に異なる Agent ID を指定する必要があります。

この項目の設定は必須です。また、大文字小文字を区別します。

**注意**

以下の理由から、HULFT for IBMiと接続する場合は agent.id に英小文字を使用しないでください。

  * 該当の設定値はHULFTの詳細ホスト情報のホスト名として使用されます。

  * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。




agent.sender.port

配信 Agent の待受ポートです。 

HULFT 配信からの通信を受け付けます。実行環境に応じて任意の値を設定してください。

この項目の設定値は、オペレーティングシステムが予約しているポート番号や他のアプリケーションが使用するポート番号と重複しないように注意してください。

この項目の設定は必須です。

agent.command.port

Agent のコマンド実行時に使用する内部通信ポートです。

実行環境に応じて任意の値を設定してください。

この項目の設定値は、オペレーティングシステムが予約しているポート番号や他のアプリケーションが使用するポート番号と重複しないように注意してください。

この項目の設定を省略した場合は、初期値の "1099" が設定されます。

接続情報設定

connection.keystore.filepath

[「コネクション ID 認証ファイル」](ConIDAuthoSetFile.htm) へのファイルパスを設定します。

Agent 設定ファイルからの相対パスまたは絶対パスで設定してください。

この項目の設定は必須です。 

service.accesspoint

Agent が接続するサービスのアクセスポイントです。

この項目の設定値は変更しないでください。

プロキシ情報設定

proxy.host

プロキシサーバを経由する場合のホスト名またはドメイン名（IP アドレス）を設定します。

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

Windows サービス起動設定

windows.service.startup.sender

配信用の Agent を Windows サービスとして使用する場合の起動設定をします。

"on" または "off" を設定できます。この項目は大文字小文字を区別します。

"on" を設定すると、Windows サービス開始時に配信用の Agent が起動されます。

windows.service.startup.receiver

集信用の Agent を Windows サービスとして使用する場合の起動設定をします。

"on" または "off" を設定できます。この項目は大文字小文字を区別します。

"on" を設定すると、Windows サービス開始時に集信用の Agent が起動されます。

**= 補足 =**

Linux の場合、「Windows サービス起動設定」の内容は使用されません。

Agent アップデート設定

update.action

Agent 起動時のアップデート通知について設定します。

"alert" または "none" を設定できます。この項目は大文字小文字を区別します。

"alert" を設定すると、更新の有無を通知します。手動でアップデートを行ってください。

例 : 更新対象がある場合
    
    
    I600029 - アップデートの確認に成功しました。メッセージ:[You can update to latest version X.X.X from Y.Y.Y.]

例 : 更新対象がない場合
    
    
    I600029 - アップデートの確認に成功しました。メッセージ:[You do not have to update: latest version X.X.X.]

update.action.onError

アップデート通知が失敗した場合の Agent の起動について設定します。「update.action」に "alert" を指定した場合のみ、設定値が有効になります。

この項目には "continue" が設定され、アップデート通知が失敗した場合でも Agent の起動は続行されます。

この項目の設定値は変更しないでください。

システム動作設定

session.keepalive.interval

サービスとのセッション維持のために Agent が送信するキープアライブパケットの送信間隔を設定します。

プロキシサーバ等を経由して Agent とサービスが通信する場合、プロキシサーバ等の無通信時のタイムアウト設定によってはセッションが切断される場合があります。

予期しないセッションの切断を防止するために、Agent をインストールする環境に合わせて設定値を調整してください。

単位はミリ秒で、"0" から "3600000" まで指定できます。

"0" を設定すると、Agent はキープアライブパケットの送信を行いません。

session.management.reconnect.times

Agent 起動中にネットワークエラーが発生し、Agent とサービスが切断された場合、サービスに管理セッションの再接続を試みる回数を設定します。

"0" から "360" まで指定できます。

"0" を設定すると、セッションの再接続を行いません。

指定した回数を超えて再接続に失敗した場合、Agent が停止します。

session.management.reconnect.interval

セッションの再接続の試行間隔を設定します。

単位は秒で、"0" から "60" まで指定できます。

"0" を設定すると、待ち時間なしでセッションの再接続を試みます。

jvm.options

Agent を実行する Java の起動オプションを指定します。

複数のオプションを指定する場合は、半角スペースで区切ります。

この項目は大文字小文字を区別します。

例 : メモリ割り当て
    
    
    jvm.options=-Xms64M -Xmx256M

例 : 言語設定
    
    
    # Set to English.
    jvm.options=-Duser.language=en
    # Set to Japanese.
    jvm.options=-Duser.language=ja

例 : タイムゾーン設定
    
    
    # Set to Tokyo.
    jvm.options=-Duser.timezone=Asia/Tokyo
    # Set to Los Angeles.
    jvm.options=-Duser.timezone=America/Los_Angeles
    # Set to UTC +9.
    jvm.options=-Duser.timezone=UTC+9

**= 補足 =**

指定できる値や形式は Java の仕様に準じます。 

詳細は、<https://www.oracle.com/technetwork/jp/java/index.html>を参照してください。

設定ファイルのバージョン情報

configuration.version

Agent 設定ファイルのバージョン情報です。

この項目の設定値は変更しないでください。

表3.1 設定項目一覧

No |  キー名 |  説明 |  初期値 |  省略時値 |  必須 |  設定値 |  備考  
---|---|---|---|---|---|---|---  
1 |  agent.id |  Agent ID |  |  |  ✔ |  半角英数字記号 |  25バイト以内 大文字小文字を区別します  
2 |  agent.sender.port |  配信 Agent の待受ポート  |  46000 |  |  ✔ |  1-65535 |   
3 |  agent.command.port |  コマンド用内部通信ポート  |  1099 |  1099 |  |  1-65535 |   
4 |  connection.keystore.filepath |  コネクション ID 認証ファイルへのファイルパス |  ./connection.keystore |  |  ✔ |  |   
5 |  service.accesspoint |  サービスアクセスポイント |  service-ap.tokyo.webconnect.hulft.com |  |  ✔ |  |  この項目の設定値は変更不可   
6 |  proxy.host |  プロキシホスト |  |  |  |  半角英数字記号 |  255バイト以内 大文字小文字を区別しません  
7 |  proxy.port |  プロキシポート |  |  |  |  1-65535 |   
8 |  proxy.username |  プロキシユーザ名 |  |  |  |  半角文字 |  256バイト以内 大文字小文字を区別します  
9 |  proxy.password |  プロキシパスワード |  |  |  |  半角文字 |  256バイト以内 大文字小文字を区別します  
10 |  windows.service.startup.sender |  Windows サービス起動設定（配信 Agent） |  on |  on |  |  on | off |  大文字小文字を区別します  
11 |  windows.service.startup.receiver |  Windows サービス起動設定（集信 Agent） |  on |  on |  |  on | off |  大文字小文字を区別します  
12 |  update.action |  Agent アップデート通知設定 |  alert |  alert |  |  alert |  
none |  大文字小文字を区別します  
13 |  update.action.onError |  アップデート失敗時の Agent 起動設定 |  continue |  continue |  |  continue |  この項目の設定値は変更不可  
14 |  session.keepalive.interval |  キープアライブパケットの送信間隔  
（ミリ秒）  |  60000 |  60000 |  |  0-  
3600000 |   
15 |  session.management.reconnect.times |  管理セッション再接続回数 |  360 |  360 |  |  0-360 |   
16 |  session.management.reconnect.interval |  管理セッション再接続間隔（秒） |  30 |  30 |  |  0-60 |   
17 |  jvm.options |  Java の起動オプション |  -Xms64M -Xmx256M |  |  |  半角文字 |  大文字小文字を区別します  
18 |  configuration.version |  設定ファイルのバージョン情報 |  |  |  ✔ |  |  この項目の設定値は変更不可  
  
**= 備考 =**

「agent.id」、「proxy.host」に設定できる記号は「-（ハイフン）」「.（ピリオド）」です。


---


## ページ 8

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/AgentSetFileSettings.htm

# ファイルの設定

設定方法

以下の Agent 設定ファイルをテキストエディタ等で編集します。
    
    
    {導入ディレクトリ}/config/agent.conf

記述フォーマット

行の先頭に半角の「#」があるときは、コメント行とみなされます。

空行は存在していても構いません。また、空行やコメント行は連続しても構いません。

項目を設定する行は、以下のフォーマットで記述します。
    
    
    キー名 = 設定値

キー名は設定する項目を表す名前で、項目ごとに異なる名前を使用します。

名前はあらかじめ決まっているため、変更することはできません。

キー名と設定値の間は、半角の「=」で区切ります。

設定値の反映

設定ファイルを編集した場合、変更内容を反映させるためには Agent を再起動する必要があります。


---


## ページ 9

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/ConIDAuthoSetFile.htm

# コネクション ID 認証ファイル

HULFT-WebConnect との接続で使用するコネクション ID とそのパスワードを設定します。

複数のコネクション ID とパスワードを設定することができます。

ただし、異なるアカウントで登録したコネクション ID を混在させることはできません。


---


## ページ 10

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/ConIDAuthoSetFileItem.htm

# 各項目の説明

コネクション ID

HULFT-WebConnect への接続を識別する ID です。

サービス内で一意にする必要があります。

この項目には半角英数字および「-（ハイフン）」「.（ピリオド）」を、16バイト以内で指定できます。

この項目は大文字小文字を区別します。

**= 備考 =**

コネクション ID は事前に Management Console で登録する必要があります。

また、Agent が使用するコネクション ID は、「クライアント種別」に「HULFT」を含める必要があります。

**注意**

  * バージョン 2.2.0 より前の Agent を使用している場合、コネクション ID 認証ファイルに定義しているコネクション ID に IP フィルタが設定されていないか確認してください。

一つでも設定されていると、Agent を起動できなくなります。



  * 以下の理由から、HULFT for IBMiと接続する場合はコネクション ID に英小文字を使用しないでください。

    * 該当の設定値はHULFTの詳細ホスト情報のホスト名として使用されます。

    * HULFT for IBMiは、管理情報の設定値に英小文字を使用できません。




コネクションパスワード 

Agent が HULFT-WebConnect に接続する際の認証パスワードです。

この項目には半角英数字および記号を、8 - 256バイト以内で指定できます。

この項目は大文字小文字を区別します。

**= 備考 =**

コネクションパスワードは事前に Management Console で登録する必要があります。


---


## ページ 11

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentSet/ConIDAuthoSetFileSettings.htm

# ファイルの設定

設定方法

Agent 設定ファイル 内の「connection.keystore.filepath」に指定されたファイルをテキストエディタ等で編集します。

デフォルトでは以下のようになっています。
    
    
    {導入ディレクトリ}/config/connection.keystore

記述フォーマット

空行、コメント行の扱いは、Agent 設定ファイルと同様です。

項目を設定する行は、以下のフォーマットで記述します。
    
    
    コネクション ID:コネクションパスワード

コネクション ID とコネクションパスワードは、半角の「:」で区切ります。

複数のコネクション ID を指定する場合は、改行して同様の設定をしてください。

設定値の反映

設定ファイルを編集した場合、変更内容を反映させるためには Agent を再起動する必要があります。


---


## ページ 12

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/AgentUninstall.htm

# Agent のアンインストール

各 OS ごとの Agent のアンインストール方法について説明します。


---


## ページ 13

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/DeletionInstallDirectory.htm

# 導入ディレクトリの削除

導入ディレクトリを削除してください。


---


## ページ 14

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/DeletionService.htm

# サービスの削除

Agent をサービスとして起動した場合は、サービスを削除します。


---


## ページ 15

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/DeletionServiceInit.htm

# init.d スクリプトの場合

(1) サービスの停止

サービスを停止します。 

サービスの停止方法については、[「Agent の停止（Linux）」](../TerminateAgent/ForLinuxTerminateAgent.htm)を参照してください。

(2) サービスの登録解除

以下のコマンドを実行します。
    
    
    # chkconfig --del sender_agent
    # chkconfig --del receiver_agent

(3) init.d スクリプトの削除

「/etc/init.d」に配置したスクリプト（sender_agent, receiver_agent）を削除します。


---


## ページ 16

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/DeletionServiceLinux.htm

# サービスの削除（Linux）


---


## ページ 17

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/DeletionServiceSystemd.htm

# systemd の場合

(1) サービスの停止

サービスを停止します。

サービスの停止方法については、[「Agent の停止（Linux）」](../TerminateAgent/ForLinuxTerminateAgent.htm)を参照してください。

(2) Unit ファイルの削除

「/etc/systemd/system」に配置した Unit ファイル（senderAgent.service、receiverAgent.service）を削除します。

(3) 変更の適用

「systemctl daemon-reload」を実行します。


---


## ページ 18

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/DeletionServiceWin.htm

# サービスの削除（Windows）

(1) サービスを停止します。

サービスの停止方法については、[「Agent の停止（Windows）」](../TerminateAgent/ForWinTerminateAgent.htm)を参照してください。

(2) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

(3) 以下のコマンド（バッチファイル）を実行し、サービスを削除します。
    
    
    > service uninstall [任意のサービス名]
    Uninstalling the service '[任意のサービス名]' ...
    The service '[任意のサービス名]' has been uninstalled.

上記のように出力されれば成功です。

サービス名を省略した場合、「webconnect-agent」というサービス名のサービスを削除します。

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。


---


## ページ 19

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/AgentUninstall/TerminateAgentUninstall.htm

# Agent の停止

Agent を停止します。 

Agent の停止方法については、[「Agent の停止」](../TerminateAgent/TerminateAgent.htm)を参照してください。


---


## ページ 20

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/Changes/Changes_AGG.htm

# 変更内容一覧

Ver. 3.1.0での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.9 |  Ver 3.1.0 |  変更箇所  
---|---|---|---|---  
1 |  HULFT for IBMiと接続する場合の制限事項の記載変更 |  注意の記載あり |  注意の記載変更 |  [「各項目の説明」](../AgentSet/AgentSetFileItem.htm) [「各項目の説明」](../AgentSet/ConIDAuthoSetFileItem.htm)  
脚注の記載あり |  脚注の記載変更 |  [「管理情報の設定」](../HULFTSettings/SendFileResendFile.htm)  
記載あり |  記載変更 |  [「制限事項」](../PointsNote/Restrictions.htm)  
2 |  対応機能に関する制限事項を修正 |  Zstandardの記載あり |  Zstandardの記載削除 簡易転送の記載追記 |  [「制限事項」](../PointsNote/Restrictions.htm)  
  
Ver. 3.0.9での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.8 |  Ver 3.0.9 |  変更箇所  
---|---|---|---|---  
1 |  管理セッション再接続回数の初期値と省略時値を変更 |  120と記載 |  360に変更 |  [「各項目の説明」](../AgentSet/AgentSetFileItem.htm)  
2 |  Zstandardに関する制限事項を追記 |  記載なし |  追記 |  [「制限事項」](../PointsNote/Restrictions.htm)  
  
Ver. 3.0.8での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.7 |  Ver 3.0.8 |  変更箇所  
---|---|---|---|---  
1 |  ログ設定ファイルの記載を追記 |  記載なし |  追記 |  [「設定ファイルの説明」](../AgentLog/LogConfigFile.htm)  
2 |  ログの種類の記載を追記 |  記載なし |  追記 |  [「初期設定のログ出力場所」](../AgentLog/DefLogOutDestination.htm)  
3 |  エラー内容の詳細の記載を削除 |  記載あり |  記載削除 |  [「HULFT の完了コード」](../PointsNote/StatusCodeHULFT.htm)  
4 |  多重実行に関する記載を追記 |  記載なし |  追記 |  [「Agent の起動およびアップデート確認時の多重実行制限」](../PointsNote/MultipleExecutionRestrictions.htm)  
5 |  バージョン2.3.1までの記載を追記 |  記載なし |  追記 |  [「既知の問題点」](../KnownIssues/KnownIssues.htm)  
6 |  HULFT8 for IBMi 接続時の制限事項を追記 |  記載なし |  追記 |  [「各項目の説明」](../AgentSet/AgentSetFileItem.htm) [「各項目の説明」](../AgentSet/ConIDAuthoSetFileItem.htm) [「管理情報の設定」](../HULFTSettings/SendFileResendFile.htm) [「制限事項」](../PointsNote/Restrictions.htm)  
  
Ver. 3.0.7での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.6 |  Ver 3.0.7 |  変更箇所  
---|---|---|---|---  
1 |  session.management.reconnect.timesの説明文を追記 |  セッションの再接続に失敗した場合の記載なし |  セッションの再接続に失敗した場合を追記 |  [「各項目の説明」](../AgentSet/AgentSetFileItem.htm)  
  
Ver. 3.0.6での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.5 |  Ver 3.0.6 |  変更箇所  
---|---|---|---|---  
1 | update.action.onErrorの説明文を修正 |  アップデートが失敗 |  アップデート通知が失敗 |  [「各項目の説明」](../AgentSet/AgentSetFileItem.htm)  
2 | 配信要求を受ける場合の記載を修正 |  データ検証の記載なし |  データ検証を追記 |  [「管理情報の設定」](../HULFTSettings/SendFileResendFile.htm)  
3 | Agent バージョン1 の記載を削除 | Agent バージョン1 の記載あり | Agent バージョン1 の記載を削除 |  [「ファイル転送（送信要求・再送要求）」](../HULFTSettings/SendReqResendReq.htm) [「Agent 管理」](../PointsNote/ManageAgent.htm) [「Agent の再起動」](../PointsNote/RestartAgent.htm)  
  
Ver. 3.0.5での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.4 |  Ver 3.0.5 |  変更箇所  
---|---|---|---|---  
1 | 動作環境の記載変更 |  動作環境の記載あり |  弊社ホームページ参照の記載に変更 |  [「Agent 動作環境」](../OpeEnv/OpeEnv.htm)  
2 | タイトルの変更と説明文の修正 |  大容量ファイルの転送 |  Agent のメモリが枯渇する場合 |  [「Agent のメモリが枯渇する場合」](../PointsNote/TransLargeFile.htm)  
  
Ver. 3.0.2での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.0 |  Ver 3.0.2 |  変更箇所  
---|---|---|---|---  
1 |  運用時の留意点における制限事項の記載変更 |  記載あり |  記載削除 |  [「制限事項」](../PointsNote/Restrictions.htm)


---


## ページ 21

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/AgentStartCommand.htm

# Agent 起動コマンド  
  
配信 Agent または集信 Agent を起動します。

設定ファイル（agent.conf）が認識できない場合は、コマンドを実行することができません。

設定ファイルについては、[「Agent の設定」](../AgentSet/AgentSet.htm)を参照してください。

コマンド
    
    
    agentctl {-s|-r} start

パラメータ説明

-s|-r
    

起動対象の Agent の種類（省略不可）

-s : 配信 Agent

-r : 集信 Agent

start
    

起動コマンドを表す（省略不可）


---


## ページ 22

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/AgentStatusConfirmCommand.htm

# Agent 状態確認コマンド

配信 Agent または集信 Agent の状態を確認します。

設定ファイル（agent.conf）が認識できない場合は、コマンドを実行することができません。

設定ファイルについては、[「Agent の設定」](../AgentSet/AgentSet.htm)を参照してください。

コマンド
    
    
    agentctl {-s|-r} status

パラメータ説明

-s|-r
    

確認対象の Agent の種類（省略不可）

-s : 配信 Agent

-r : 集信 Agent

status
    

状態確認コマンドを表す（省略不可）


---


## ページ 23

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/AgentTerminateCommand.htm

# Agent 停止コマンド

配信 Agent または集信 Agent を停止します。

設定ファイル（agent.conf）が認識できない場合は、コマンドを実行することができません。

設定ファイルについては、[「Agent の設定」](../AgentSet/AgentSet.htm)を参照してください。

正常に Agent の起動が完了した後、または再接続中に停止コマンドを受け付けます。

コマンド
    
    
    agentctl {-s|-r} [-f] stop

パラメータ説明

-s|-r
    

起動対象の Agent の種類（省略不可）

-s : 配信 Agent

-r : 集信 Agent

-f
    

強制終了オプション（省略可）

強制終了する場合に指定します。

このオプションを指定しない場合、配信処理が行われている間は停止できません。

stop
    

停止コマンドを表す（省略不可）


---


## ページ 24

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/AgentUpdateConfirmCommand.htm

# Agent アップデート確認コマンド

Agent に更新対象があるかどうか確認します。

設定ファイル（agent.conf）が認識できない場合は、コマンドを実行することができません。

設定ファイルについては、[「Agent の設定」](../AgentSet/AgentSet.htm)を参照してください。

コマンド
    
    
    update-agent


---


## ページ 25

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/CommandRef.htm

# コマンドリファレンス

コマンドインタフェースについて説明します。
    
    
    コマンドやコントロールカードの説明に使用する表記
    [ ] : 大かっこ。このかっこで囲まれた項目は、省略できることを示します。
    { } : 中かっこ。かっこ内の項目の中から 1 つを選択する必要があることを示します。


---


## ページ 26

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/ProductVerDispCommand.htm

# 製品バージョン表示コマンド

製品バージョンを表示します。

設定ファイル（agent.conf）が認識できない場合は、コマンドを実行することができません。

設定ファイルについては、[「Agent の設定」](../AgentSet/AgentSet.htm)を参照してください。

コマンド
    
    
    agentctl -version

パラメータ説明

-version
    

製品バージョン表示コマンドを表す（省略不可）


---


## ページ 27

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/WinServDeleteCommand.htm

# Windows サービス削除コマンド

Agent のアプリケーションを Windows サービスから削除します。

コマンド
    
    
    service uninstall [servicename]

パラメータ説明

uninstall
    

サービス削除のコマンドであることを表す（省略不可）

servicename
    

削除するサービス名（省略可）

省略した場合、「webconnect-agent」というサービス名のサービスを削除します。


---


## ページ 28

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/CommandRef/WinServRegistCommand.htm

# Windows サービス登録コマンド

Agent のアプリケーションを Windows サービスに登録します。

コマンド
    
    
    service install [servicename]

パラメータ説明

install
    

サービス登録のコマンドであることを表す（省略不可）

servicename
    

登録するサービス名（省略可）

省略した場合、「webconnect-agent」というサービス名で登録されます。


---


## ページ 29

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/HULFTSettings/HULFTSettings.htm

# HULFT の設定

HULFT の設定方法およびファイル転送方法について説明します。


---


## ページ 30

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/HULFTSettings/ResendReqTrans.htm

# 再送要求の場合

HULFT-WebConnect を経由した再送要求では、HULFT の再送要求コマンドで以下のパラメータの指定が必須です。

その他のパラメータや HULFT の操作については、HULFT の「オペレーション マニュアル」を参照してください。

-h
    

再送要求を依頼するホスト名を指定します。

配信側の Agent が複数のコネクション ID で起動している場合、このパラメータで指定したホスト名のコネクション ID と Management Console の [中継履歴] 画面の「配信元コネクション ID」が一致しないことがあります。

-r
    

再送要求の依頼を表します。

再送要求を依頼するときは、このパラメータを指定する必要があります。

-f
    

再送要求を依頼するファイル ID を指定します。

コマンド例 : 再送要求を依頼するホスト名が「xxx_yyy_zzz」、ファイル ID が「FILEID」の場合
    
    
    utlrecv -h xxx_yyy_zzz -r -f FILEID


---


## ページ 31

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/HULFTSettings/SendFileResendFile.htm

# 管理情報の設定

HULFT-WebConnectを使用するには、HULFT の管理情報の設定が必要となります。

主に以下の管理情報の設定が必要です。

HULFTの管理情報の設定については、HULFTの「オペレーション マニュアル」を参照してください。

自HULFTの動作 |  設定項目 |  通信相手のクライアントタイプ  
---|---|---  
Agent |  CLI |  ブラウザ転送 |  D-Client  
配信要求を行う場合 |  詳細ホスト情報 |  ホスト名 |  集信側 Agent のコネクション ID_集信側 Agent の Agent ID_集信側 HULFT のホスト名（*1）（*2） |  CLI に対する配信要求はサポートしていません。 |  ブラウザ転送に対する配信要求はサポートしていません。 |  D-Client 設定のコネクション ID_D-Client ID_D-Client ID（*1）（*2）  
集信ポート番号 |  集信側 HULFT の集信ポート番号 |  初期値から変更する必要はありません（当設定の値は使用しません）。  
HULFT7 通信モード |  無効（*3） |  無効（*4）  
PROXY サーバ名 |  配信側の Agent を起動しているホスト名（HULFT が名前解決できること） |  配信側の Agent を起動しているホスト名（HULFT が名前解決できること）  
PROXY ポートNo. |  配信側の Agent の待受ポート番号（*5） |  配信側の Agent の待受ポート番号（*5）  
転送グループ情報 |  「詳細ホスト情報」で登録したホストを含む転送グループ情報を登録します。 |  「詳細ホスト情報」で登録したホストを含む転送グループ情報を登録します。  
配信管理情報 |  「転送グループ情報」で登録した転送グループ ID を設定した配信管理情報を登録します。 |  「転送グループ情報」で登録した転送グループ ID を設定した配信管理情報を登録します。  
配信要求を受ける場合 |  詳細ホスト情報 |  ホスト名 |  配信側HULFTのホスト名を登録します。 |  通信相手のCLI 設定ファイル「cli.hostname」に設定した値を入れてください。（*2） |  “HWC-BROWSER”を設定してください。 |  D-Client ID の設定値を入れてください。（*2）  
集信管理情報 |  集信管理情報を登録します。 |  集信管理情報を登録します。 以下の３つは、下記のとおりに 設定してください。 集信形態:“単一集信” 世代管理:“しない” データ検証:"しない" |  集信管理情報を登録します。 以下の３つは、下記のとおりに 設定してください。 集信形態:“単一集信” 世代管理:“しない” データ検証:"しない" |  集信管理情報を登録します。  
送信要求を行う場合（*6） |  詳細ホスト情報（1） |  ホスト名 |  要求受付側 Agent のコネクション ID_要求受付側 Agent の Agent ID_要求受付側 HULFT のホスト名（*1）（*2） |  CLI に対する送信要求はサポートしていません。 |  ブラウザ転送に対する送信要求はサポートしていません。 |  D-Clientに対する送信要求はサポートしていません。  
要求受付ポートNo. |  要求受付側 HULFT の要求受付ポート番号  
HULFT7 通信モード |  無効（*3）  
PROXY サーバ名 |  要求発行側の Agent を起動しているホスト名（HULFT が名前解決できること）  
PROXY ポートNo. |  要求発行側の Agent の待受ポート番号（*5）  
詳細ホスト情報（2） |  ホスト名 |  配信側HULFTのホスト名を登録します。  
集信管理情報 |  集信管理情報を登録します。  
送信要求を受ける場合 |  詳細ホスト情報 |  ホスト名 |  集信側 Agent のコネクション ID_集信側 Agent の Agent ID_集信側 HULFT のホスト名（*1）（*2） |  CLI の connection.id の設定値_CLI の cli.agent.id の設定値_CLI の cli.hostname の設定値（*1）（*2） |  ブラウザ転送側のコネクション ID_ブラウザ転送側の Agent ID_ブラウザ転送側のホスト名（*1）（*2） |  D-Client 設定のコネクション ID_D-Client ID_D-Client ID（*1）（*2）  
集信ポート番号 |  集信側 HULFT の集信ポート番号 |  初期値から変更する必要はありません（当設定の値は使用しません）。  
HULFT7 通信モード |  無効（*3） |  無効（*4）  
PROXY サーバ名 |  配信側の Agent を起動しているホスト名（HULFT が名前解決できること）  
PROXY ポートNo. |  配信側の Agent の待受ポート番号（*5）  
転送グループ情報 |  「詳細ホスト情報」で登録したホストを含む転送グループ情報を登録します。  
配信管理情報 |  「転送グループ情報」で登録した転送グループ ID を設定した配信管理情報を登録します。  
*1 |  : |  各項目を「_」（アンダースコア）で区切ります。 コネクション ID および Agent ID は以下のとおりです。

  * Agentと通信を行う場合 対向 Agentの設定ファイル（agent.conf）で指定した値
  * CLIと通信を行う場合 通信相手のCLI設定ファイル（transfer-cli.conf）で指定した値
  * ブラウザ転送を行う場合 Management Console の [ブラウザ転送設定] 画面の「ブラウザ配信要求」タブおよび「ブラウザ送信要求」タブの「ブラウザ定義」で設定したコネクションIDおよびAgent ID、ホスト名は固定値の“HWC-BROWSER”
  * D-Client と通信を行う場合 Management Console の [D-Client設定] 画面で設定したコネクション ID および D-Client ID

例）Agentと通信を行う場合

  * 集信側Agentの設定 コネクションID=webconnect Agent ID=demo HULFTのホスト名=receiver
  * 設定値 webconnect_demo_receiver

  
---|---|---  
*2 |  : |  HULFT for IBMiと接続する場合、以下の設定値に英小文字を使用しないでください。

  * Agentのコネクション IDおよびAgent ID（agent.id）
  * CLIのコネクションID（connection.id）、CLIの識別ID（cli.agent.id）、およびCLIのホスト名（cli.hostname）
  * ブラウザ転送側のコネクションIDおよびAgent ID
  * D-ClientのコネクションIDおよびD-Client ID

  
*3 |  : |  HULFT8からHULFT7にファイル転送する場合は“有効”を指定してください。  
*4 |  : |  HULFT7 通信モードはサポートしていません。  
*5 |  : |  設定ファイル（agent.conf）のAgentの待受ポート（agent.sender.port）に指定した値です。 詳細は、[「Agent の設定」](../AgentSet/AgentSet.htm)を参照してください。  
*6 |  : |  詳細ホスト情報（1）と詳細ホスト情報（2）の両方を登録してください。


---


## ページ 32

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/HULFTSettings/SendFileResendFileTrans.htm

# ファイル転送（配信要求・再配信要求）  
  
HULFT-WebConnect を経由する場合でも、HULFT のファイル転送方法は同じです。

HULFT の管理情報の設定に従って、HULFT-WebConnect を中継してファイル転送されます。

通常の HULFT 転送と同様に、HULFT の状況照会から配信および集信の履歴を確認することができます。

HULFT の操作については、HULFT の「オペレーション マニュアル」を参照してください。


---


## ページ 33

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/HULFTSettings/SendReqResendReq.htm

# ファイル転送（送信要求・再送要求）

Agentを使用して、HULFT-WebConnect を経由した送信要求・再送要求によるファイル転送を行うことができます。

**注意**

HULFT-WebConnect を経由した送信要求・再送要求は、HULFT の管理画面から実行することができません。

HULFT-WebConnect を経由した送信要求・再送要求を行う場合は、HULFT の送信要求コマンド・再送要求コマンドを使用してください。


---


## ページ 34

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/HULFTSettings/SendReqTrans.htm

# 送信要求の場合

HULFT-WebConnect を経由した送信要求では、HULFT の送信要求コマンドで以下のパラメータの指定が必須です。

その他のパラメータや HULFT の操作については、HULFT の「オペレーション マニュアル」を参照してください。

-f
    

集信を行うファイル ID を指定します。

-h
    

送信を依頼する相手ホスト名を指定します。 

配信側の Agent が複数のコネクション ID で起動している場合、このパラメータで指定したホスト名のコネクション ID と Management Console の [中継履歴] 画面の「配信元コネクション ID」が一致しないことがあります。

-msg0|-msg1|-msg2|-msg3|-msg4|-msg5|-msgl0|-msgl1
    

要求発行側 Agent のコネクション ID を以下の形式でメッセージの先頭から指定します。
    
    
    {{RCVCID:コネクション ID}}

「RCVCID:」は大文字固定です。

「コネクション ID」は大文字小文字を区別します。

**= 備考 =**

「-msgl0」、「-msgl1」は HULFT8 以上で指定することができます。

コマンド例 : 詳細ホスト情報に登録した要求受付側（配信側）のホスト名が「xxx_yyy_zzz」、要求発行側（集信側）のコネクション ID が「connectionID」の場合
    
    
    utlrecv -f FILEID -h xxx_yyy_zzz -msg0 {{RCVCID:connectionID}}
    utlrecv -f FILEID -h xxx_yyy_zzz -msgl1 {{RCVCID:connectionID}}userdata


---


## ページ 35

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/InstallationAgent/InstallationAgent.htm

# Agent のインストール

Agent の新規インストール方法およびアップデートインストール方法について説明します。

Agent は HULFT と同一環境に導入することも、HULFT と異なる環境に導入することもできます。


---


## ページ 36

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/InstallationAgent/NewInstallation.htm

# 新規インストール方法

Agent を新規に導入する場合は、以下の手順でインストールします。 

(1) 導入先ディレクトリの決定

Agent をインストールするディレクトリ（以下、導入ディレクトリ）を決定します。

**= 補足 =**

導入ディレクトリ名に、以下の記号は使用することができません。

Windows の場合
    
    
    ! # % & ' ; [ ] ^ ` { } ? \ / : * " < > |

Linux の場合
    
    
    ! # % & ' ( ) ; ` \ / : " < > | 半角スペース

(2) 圧縮ファイルのダウンロード

Windows の場合

HULFT-WebConnect Management Console（以下、Management Console）の[ダウンロード] 画面から圧縮ファイル（webconnect-agent-x.x.x-windows-xxx.zip）をダウンロードします。

Linux の場合

Management Console の[ダウンロード] 画面から圧縮ファイル（webconnect-agent-x.x.x-linux.tar.gz）をダウンロードします。

(3) 圧縮ファイルの展開

Windows の場合

解凍ソフトを使用して導入ディレクトリに圧縮ファイルを展開します。

Linux の場合

導入ディレクトリに圧縮ファイルを移動し、以下のコマンドを実行します。
    
    
    # tar -xzvf webconnect-agent-x.x.x-linux.tar.gz


---


## ページ 37

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/InstallationAgent/UpdateInstallation.htm

# アップデートインストール方法

Agent を更新する場合は、以下の手順で行います。

(1) Agent の停止

Agent が起動している場合は、Agent を停止します。 

停止方法の詳細は、[「Agent の停止」](../TerminateAgent/TerminateAgent.htm)を参照してください。

**= 補足 =**

Agent をサービスとして起動していた場合は、[「サービスの削除」](../AgentUninstall/DeletionService.htm)も行います。

(2) Agent のバックアップ 

現在の導入ディレクトリ以下を任意のディレクトリ（以下、バックアップディレクトリ）に退避させます。

退避後、現在の導入ディレクトリ以下を削除します。

(3) 圧縮ファイルのダウンロード

Windows の場合

Management Console の[ダウンロード] 画面から圧縮ファイル（webconnect-agent-x.x.x-windows-xxx.zip）をダウンロードします。

Linux の場合

Management Console の[ダウンロード] 画面から圧縮ファイル（webconnect-agent-x.x.x-linux.tar.gz）をダウンロードします。

(4) 圧縮ファイルの展開

Windows の場合

解凍ソフトを使用して導入ディレクトリに圧縮ファイルを展開します。

Linux の場合

導入ディレクトリに圧縮ファイルを移動し、以下のコマンドを実行します。
    
    
    # tar -xzvf webconnect-agent-x.x.x-linux.tar.gz

(5) 設定内容の反映

バックアップディレクトリのAgent 設定ファイル、コネクションID 認証ファイル、およびログの設定ファイルの内容を、導入ディレクトリのAgent 設定ファイルに反映します。

バックアップしたファイルを導⼊ディレクトリにファイルコピーすると、正しく動作しなくなる場合があります。

設定内容の詳細は、[「Agent の設定」](../AgentSet/AgentSet.htm)と[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。

**= 補足 =**

コネクション ID 認証ファイルの格納先を確認し、Agent 設定ファイル内の「connection.keystore.filepath」の設定値と一致しているかご確認ください。

(6) バージョン確認

Agent が正しく更新されたかどうかを製品バージョン表示コマンドで確認します。 

コマンドの実行結果で表示される「Version」が更新した Agent のバージョンと一致しているかご確認ください。 

製品バージョン表示コマンドの詳細は、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

(7) Agent の起動

Agent を起動してアップデートインストールの最終確認を行います。

起動方法の詳細は、[「Agent の起動」](../StartupAgent/StartupAgent.htm)を参照してください。


---


## ページ 38

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/KnownIssues/KnownIssues.htm

# 既知の問題点

  * **バージョン 1.1.0 までの Agent では、HULFT-WebConnect と Agent のセッション切断時に、Agent のログに切断コード [CLOSED_ABNORMALLY] のログが出力されてしまう場合がある**

HULFT のファイル転送が正常終了した場合でも、HULFT-WebConnect と Agent のセッション切断時に以下のような切断コード [CLOSED_ABNORMALLY] が Agent のログに出力されてしまう場合があります。
    
    2015-07-03 10:00:00,123 AGENTID[example] INFO jp.co.saison.sis.hulft.tsubomi.agent.receiver.ReceiverEndpoint - I120021 - 転送セッションが切断されました。セッションID：[6ec851da-917f-48ea-b367-7e92abdb57aa], 切断コード：[CLOSED_ABNORMALLY], メッセージ：[Closed abnormally.] (ReceiverEndpoint.java:106)
    

  * **Windows の場合、Agent のログに Java のエラーが出力される場合がある**

Windows で Agent を起動した場合、またはファイル転送を行った場合、転送が正常終了していても Agent のログに Java のエラーが出力される場合があります。

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
    

  * **バージョン 2.3.1 までの Agent では、ログの設定ファイルでローテーションの設定をしていても、ローテーションが行われなかったり、失敗したりする場合がある**

ログの設定ファイル（logback.xml）でローテーションの設定をしていても以下のような動作となり、ローテーションが行われなかったり、失敗したりする場合があります。

ログファイルのローテーションが行われるときに「.tmp」という拡張子が付いたファイルが生成される場合があります。 

生成されたファイルには、ローテーションが行われた他のファイルとの差分が記録されています。

必要に応じて、生成されたファイルの保存や削除を行ってください。

**= 備考 =**

Windowsの場合、Agent が起動している間はログファイルのローテーションは行われません。

Agent の再起動時に正しくローテーションが行われるため、ログファイルのローテーションが必要な場合は、Agent を定期的に再起動してください。

また、ローテーションの初期設定は日毎です。

  * **バージョン 2.0.0 の Agent では、Agent アップデートの確認を行った場合、誤った判定結果が出力される場合がある**

アップデートの確認を行うと使用中のAgentが最新であると誤って判定され、その判定結果がコンソール画面およびログファイルに出力されます。

  * **通信速度が遅い場合、Agentを再起動すると改善する場合がある**





---


## ページ 39

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/OpeEnv/OpeEnv.htm

# Agent 動作環境

動作環境については、以下のURLの弊社ホームページから、HULFT-WebConnectの製品情報を参照してください。 

[URL: https://www.hulft.com/](https://www.hulft.com/)


---


## ページ 40

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/ActMonitorAgent.htm

# Agent の起動監視および自動起動

Agent が予期せず停止した際に自動的に起動する仕組みを、以下のサンプルスクリプトを用いて作成できます。

サンプルスクリプトをスケジューラに登録して一定間隔で実行することで、Agent の起動監視および自動起動を行うことが可能です。

サンプルスクリプトは、Agent の起動方法に応じたものを選択してください。

**注意**

サンプルスクリプトの内容については、改善のため予告なしに変更される事があります。

また、サンプルスクリプトはサポートサービス対象外となりますのでご注意ください。

Windows サービス起動用 Windows コマンド起動用 Linux 用
    
    
    @echo off
    setlocal enabledelayedexpansion
    
    REM --------------------------------------- 
    REM  設定 
    REM --------------------------------------- 
    REM Agentの導入ディレクトリ 
    set "AGENT_PATH=C:\webconnect-agent\bin"
    REM サービス名 
    set SERVICE_NAME=webconnect-agent
    REM ステータスチェックのリトライ最大回数 
    set /a MAX_RETRY=10 
    
    REM --------------------------------------- 
    REM  初期処理 
    REM --------------------------------------- 
    set "CURRENT_DIR=%~dp0"
    cd /d "%AGENT_PATH%"
    
    REM check directory 
    if %ERRORLEVEL% neq 0 (
      echo Cannot cd to !AGENT_PATH! 
      goto :ERROR_END
    )
    
    set DO_NET_STOP=0 
    
    REM リトライのカウンター 
    set /a COUNTER=1 
    
    REM --------------------------------------- 
    REM  配信Agentのステータス確認 
    REM --------------------------------------- 
    :CHECK_SENDING-AGENT_STATUS
    echo CHECK_SENDING-AGENT_STATUS
    FOR /f "DELIMS=" %%i IN ('agentctl.bat -s status') DO SET SENDING-AGENT_STATUS=%%i
    echo RESULT: %SENDING-AGENT_STATUS% 
    
    echo %SENDING-AGENT_STATUS% | findstr "001" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Waiting for starting the sending-side Agent.
      call :SLEEP
      goto :CHECK_SENDING-AGENT_STATUS
    )
    
    echo %SENDING-AGENT_STATUS% | findstr "000" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the sending-side Agent.
      set DO_NET_STOP=1 
      goto :START_SERVICE
    )
    
    echo %SENDING-AGENT_STATUS% | findstr "100" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the sending-side Agent.
      set DO_NET_STOP=1 
      goto :START_SERVICE
    )
    
    echo %SENDING-AGENT_STATUS% | findstr "255" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the sending-side Agent.
      set DO_NET_STOP=1 
      goto :START_SERVICE
    )
    
    REM --------------------------------------- 
    REM  集信Agentのステータス確認 
    REM --------------------------------------- 
    :CHECK_RECEIVING-AGENT_STATUS
    echo CHECK_RECEIVING-AGENT_STATUS
    FOR /f "DELIMS=" %%i IN ('agentctl.bat -r status') DO SET RECEIVING-AGENT_STATUS=%%i 
    echo RESULT: %RECEIVING-AGENT_STATUS% 
    
    echo %RECEIVING-AGENT_STATUS% | findstr "001" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Waiting for starting the receiving-side Agent.
      call :SLEEP
      goto :CHECK_RECEIVING-AGENT_STATUS
    )
    
    echo %RECEIVING-AGENT_STATUS% | findstr "000" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the receiving-side Agent.
      set DO_NET_STOP=1 
      goto :START_SERVICE
    )
    
    echo %RECEIVING-AGENT_STATUS% | findstr "100" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the receiving-side Agent.
      set DO_NET_STOP=1 
      goto :START_SERVICE
    )
    
    echo %RECEIVING-AGENT_STATUS% | findstr "255" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the receiving-side Agent.
      set DO_NET_STOP=1 
      goto :START_SERVICE
    )
    
    goto :END
    
    :START_SERVICE
    
    if !COUNTER! GTR !MAX_RETRY! (
      goto :ERROR_END
    )
    
    set /a COUNTER+=1 
    sc query %SERVICE_NAME% | findstr STATE | findstr STOPPED > nul 
    if !ERRORLEVEL! neq 0 (
      if %DO_NET_STOP%==1 (
        call net stop "!SERVICE_NAME!"
        call :SLEEP
        call :WAIT_TO_STOP_BOTH_AGENTS
        goto :START_SERVICE
      )
    )
    
    call net start "%SERVICE_NAME%"
    call :SLEEP
    goto :CHECK_SENDING-AGENT_STATUS
    
    
    :SLEEP
    ping -n 10 localhost > nul 
    exit /B 0 
    
    :WAIT_TO_STOP_BOTH_AGENTS
    FOR /f "DELIMS=" %%i IN ('agentctl.bat -r status') DO SET RECEIVING-AGENT_STATUS=%%i 
    echo %RECEIVING-AGENT_STATUS% | findstr "100" 1>nul 
    if %ERRORLEVEL% neq 0 (
      call :SLEEP
      goto :WAIT_TO_STOP_BOTH_AGENTS
    )
    exit /B 0 
    
    :END
    cd /d %CURRENT_DIR% 
    exit /B
    
    :ERROR_END
    echo Failed to start Agent.
    exit /b -1 
    
    
    @echo off
    setlocal enabledelayedexpansion
    
    REM --------------------------------------- 
    REM  設定 
    REM --------------------------------------- 
    REM Agentの導入ディレクトリ 
    set "AGENT_PATH=C:\webconnect-agent\bin"
    REM ステータスチェックのリトライ最大回数 
    set /a MAX_RETRY=10 
    
    REM --------------------------------------- 
    REM  初期処理 
    REM --------------------------------------- 
    set "CURRENT_DIR=%~dp0"
    cd /d "%AGENT_PATH%"
    
    REM check directory 
    if %ERRORLEVEL% neq 0 (
      echo Cannot cd to !AGENT_PATH! 
      goto :ERROR_END
    )
    
    REM --------------------------------------- 
    REM  配信Agentのステータス確認 
    REM --------------------------------------- 
    set /a COUNTER=1
    :CHECK_SENDING-AGENT_STATUS
    echo CHECK_SENDING-AGENT_STATUS
    
    FOR /f "DELIMS=" %%i IN ('agentctl.bat -s status') DO SET SENDING-AGENT_STATUS=%%i 
    echo RESULT: %SENDING-AGENT_STATUS% 
    
    echo %SENDING-AGENT_STATUS% | findstr "000" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the sending-side Agent.
      goto :START_SENDING-AGENT
    )
    
    echo %SENDING-AGENT_STATUS% | findstr "100" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the sending-side Agent.
      goto :START_SENDING-AGENT
    )
    
    echo %SENDING-AGENT_STATUS% | findstr "255" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the sending-side Agent.
      goto :START_SENDING-AGENT
    )
    
    goto :CHECK_RECEIVING-AGENT_STATUS
    
    
    :START_SENDING-AGENT
    call agentctl.bat -s start 
    call :SLEEP
    if !COUNTER! LSS !MAX_RETRY! (
      set /a COUNTER+=1 
      goto :CHECK_SENDING-AGENT_STATUS
    ) else (
      goto :ERROR_END
    )
    
    
    REM --------------------------------------- 
    REM  集信Agentのステータス確認 
    REM --------------------------------------- 
    set /a COUNTER=1
    :CHECK_RECEIVING-AGENT_STATUS
    echo CHECK_RECEIVING-AGENT_STATUS
    
    FOR /f "DELIMS=" %%i IN ('agentctl.bat -r status') DO SET RECEIVING-AGENT_STATUS=%%i 
    echo RESULT: %RECEIVING-AGENT_STATUS% 
    
    echo %RECEIVING-AGENT_STATUS% | findstr "000" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the receiving-side Agent.
      goto :START_RECEIVING-AGENT
    )
    
    echo %RECEIVING-AGENT_STATUS% | findstr "100" 1>nul 
    if %ERRORLEVEL%==0  (
      echo Starting the receiving-side Agent.
      goto :START_RECEIVING-AGENT
    )
    
    echo %RECEIVING-AGENT_STATUS% | findstr "255" 1>nul 
    if %ERRORLEVEL%==0 (
      echo Starting the receiving-side Agent.
      goto :START_RECEIVING-AGENT
    )
    
    goto :NORMAL_END
    
    :START_RECEIVING-AGENT
    call agentctl.bat -r start 
    call :SLEEP
    if !COUNTER! LSS !MAX_RETRY! (
      set /a COUNTER+=1
      goto CHECK_RECEIVING-AGENT_STATUS
    ) else (
      goto :ERROR_END
    )
    
    :NORMAL_END
    cd /d %CURRENT_DIR% 
    exit /B
    
    :ERROR_END
    echo Failed to start Agent.
    exit /b -1
    
    :SLEEP
    ping -n 10 localhost > nul 
    exit /B 0
    
    
    #!/bin/bash 
    
    # --------------------------------------- 
    #  設定 
    # --------------------------------------- 
    # Agentの導入ディレクトリ 
    AGENT_PATH=~/webconnect-agent/bin
    # ステータスチェックのリトライ最大回数
    MAX_RETRY=10
    # 待機時間
    SLEEP_SEC=10
    
    CURRENT_DIR=`pwd`
    # --------------------------------------- 
    #  functions 
    # --------------------------------------- 
    function error_end () {
      cd $CURRENT_DIR 
      echo Failed to start Agent.
    }
    
    # --------------------------------------- 
    #  初期処理 
    # --------------------------------------- 
    # check directory 
    if [ ! -e $AGENT_PATH ]; then 
      echo Cannot cd to $AGENT_PATH 
      error_end
      exit 1
    fi 
    
    cd $AGENT_PATH 
    # --------------------------------------- 
    #  配信Agentのステータス確認 
    # --------------------------------------- 
    COUNTER=1
    
    function checkSendingAgentStatus () {
      echo checkSendingAgentStatus
    
      sendingAgentStatus=`./agentctl -s status`
      echo RESULT: $sendingAgentStatus 
    
      echo $sendingAgentStatus | grep -e 000 -e 100 -e 255 > /dev/null
      if [ $? -eq 0 ]; then 
        echo Starting the sending-side Agent.
        return 1
      fi 
      return 0
    }
    
    checkSendingAgentStatus
    if [ $? -ne 0 ]; then 
      while [ $COUNTER -lt $MAX_RETRY ]
      do
        ./agentctl -s start
        sleep $SLEEP_SEC
        checkSendingAgentStatus
        if [ $? -eq 0 ]; then 
          break 
        fi 
        COUNTER=$((COUNTER + 1))
      done 
    
      if [ $COUNTER -ge $MAX_RETRY ]; then
        error_end
        exit 1
      fi 
    fi 
    
    # --------------------------------------- 
    #  集信Agentのステータス確認 
    # --------------------------------------- 
    COUNTER=1
    
    function checkReceivingAgentStatus () {
      echo checkReceivingAgentStatus
    
      receivingAgentStatus=`./agentctl -r status`
      echo RESULT: $receivingAgentStatus 
    
      echo $receivingAgentStatus | grep -e 000 -e 100 -e 255 > /dev/null
      if [ $? -eq 0 ]; then 
        echo Starting the receiving-side Agent.
        return 1
      fi 
      return 0
    }
    
    checkReceivingAgentStatus
    if [ $? -ne 0 ]; then 
      while [ $COUNTER -lt $MAX_RETRY ]
      do 
        ./agentctl -r start
        sleep $SLEEP_SEC
        checkReceivingAgentStatus
        if [ $? -eq 0 ]; then 
          break 
        fi 
        COUNTER=$((COUNTER + 1))
      done 
      
      if [ $COUNTER -ge $MAX_RETRY ]; then
        error_end
        exit 1
      fi 
    fi 
    
    cd $CURRENT_DIR


---


## ページ 41

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/FreqAskedQ.htm

# よくあるご質問

よくあるご質問とその回答を以下のサイトで公開しています。

URL: [HULFT Technical Support & FAQ ](https://www.hulft.com/tech-support/)

ご利用の際は、SP コードおよび製品版の基本サブスクリプションのシリアル番号を使用してログインしてください。


---


## ページ 42

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/ManageAgent.htm

# Agent 管理

Agent は起動に成功すると HULFT-WebConnect に常時セッションを張り続けます。

ファイル転送を行うときのみ Agent を起動するなど、適用業務に応じて Agent の定期的な起動・停止を行ってください。

また、HULFT-WebConnect に Agent の接続情報が不正に残っていて Agent の起動に失敗する場合や、予期しない Agent が接続されている場合は、Management Console の [Agent 接続状況] 画面から、該当する Agent を切断してください。


---


## ページ 43

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/ModifJavaEnvVari.htm

# Java の環境変数の変更

JRE のアップデートを行った場合は、必要に応じて環境変数の設定を変更してください。

また、Agent を Windows サービスとして登録していた場合は、JRE のアップデート後に再登録してください。

Agent を Windows サービスとして 1 度登録すると、次回から登録時の Java の情報をもとにサービスを起動します。

登録時の情報が変更されると、サービスの起動ができなくなりますのでご注意ください。 


---


## ページ 44

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/MultipleExecutionRestrictions.htm

# Agent の起動およびアップデート確認時の多重実行制限

バージョン 2.4.0 以降の Agent では、同一ディレクトリ上で以下の処理を同時に実行することはできません（Windows サービスとして起動する場合を除く）。

  * 配信 Agent の起動

  * 集信 Agent の起動

  * Agent アップデート確認




また、該当の処理を実行している間、以下のディレクトリに起動制御ファイル（agent-activate.lock）が作成され、ファイルロックを行います。
    
    
    {導入ディレクトリ}/bin

起動またはアップデート確認の完了後、起動制御ファイル（agent-activate.lock）は自動的にファイルロックが解除された後、削除されます。

多重実行関連のエラーメッセージは以下の通りです。

a) | 
    
    
    Failed to lock the activation control file.[{導入ディレクトリ}/bin/agent-activate.lock]
    Agent may already be running. Check the status of Agent or wait for a while and try again.  
  
---|---  
| 起動制御ファイル（agent-activate.lock）のロックに失敗した場合に出力されます。  
| Agent 起動、またはAgent アップデート確認が、同一ディレクトリ上のAgent で既に進行中である可能性があります。  
| Agent 状態確認コマンドにて起動状況をご確認いただくか、時間をあけて再度実行してください。  
b) | 
    
    
    Failed to open or lock the activation control file.[{導入ディレクトリ}/bin/agent-activate.lock]  
  
---|---  
| 起動制御ファイル（agent-activate.lock）のオープン、またはロックに失敗した場合に出力されます。  
| 導入ディレクトリ、または起動制御ファイル（agent-activate.lock）に対して、実行ユーザーが権限を持っていない可能性があります。パーミッションをご確認の上、再度実行してください。  
|  また、Agent 起動、またはAgent アップデート確認が、同一ディレクトリ上のAgent で既に進行中である場合もあります。 Agent の起動状態も併せてご確認ください。  
c) | 
    
    
    Failed to delete the activation control file.[{導入ディレクトリ}/bin/agent-activate.lock]  
  
---|---  
| 起動制御ファイル（agent-activate.lock）の自動削除に失敗した場合に出力されます。  
| Agent 起動、またはAgent アップデート確認が重複して行われていないことを確認の上、手動で起動制御ファイルを削除してください。  
|  また、ファイルロックにより手動で削除できない場合は、以下の方法で対象の起動プロセスが終了しているか確認の上、再度削除してください。  
  
**対象プロセス**
    
    
    jp.co.saison.sis.hulft.tsubomi.webconnect.exec.Main

Windows の場合

OSに付属しているタスクマネージャーで、対象の Java プロセスが終了しているか確認します。

Linux の場合

プロセス状態表示コマンド（ps コマンド）を使用して、対象の Java プロセスが終了しているか確認します。


---


## ページ 45

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/NameResoluAgent.htm

# Agent の名前解決

Agent 導入マシンの hosts ファイルに設定された「localhost」の IP アドレスに間違いがあると、Agent は正しく動作しません。

Agent の起動や接続に失敗する場合は、hosts ファイルの設定を見直してください。


---


## ページ 46

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/NonComuTimeOut.htm

# 転送セッションの無通信タイムアウト

ファイルの送信をする際に Agent と HULFT-WebConnect 間でファイル転送用のセッションを張りますが、一定時間、このセッションが無通信となった場合はセッションの切断を行います。

無通信タイムアウトの時間は 72 時間です。無通信タイムアウトで転送が終了した場合、HULFT の履歴にはソケット切断が発生したエラーとして記録されます。


---


## ページ 47

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/PointsNote.htm

# 運用時の留意点


---


## ページ 48

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/RestartAgent.htm

# Agent の再起動

Agent の起動やファイルの転送が連続で失敗する場合は、以下の手順に従って Agent を再起動してください。

(1) Agent の停止

Agent の停止方法については、[「Agent の停止」](../TerminateAgent/TerminateAgent.htm)を参照してください。

(2) Agent プロセスの確認

Agent プロセスが終了していることを確認します。

プロセスが終了していない場合は、手動で終了してください。

Windows の場合

OSに付属しているタスクマネージャーで、Agent の Java プロセスが終了しているか確認します。

**= 備考 =**

Agent をサービスとして起動していた場合は、「webconnect-agent.exe」のプロセスが終了しているかも確認してください。

Linux の場合

プロセス状態表示コマンド（ps コマンド）を使用して、Agent の Java プロセスが終了しているか確認します。

(3) Agent 接続状況の確認

Management Console で Agent の接続状況を確認します。

停止した Agent の接続情報が残っている場合は、該当する Agent を切断してください。

(4) Agent の起動

起動方法の詳細は、[「Agent の起動」](../StartupAgent/StartupAgent.htm)を参照してください。


---


## ページ 49

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/Restrictions.htm

# 制限事項

HULFT-WebConnect では、以下の制限があります。

  * 1 転送あたりのファイルサイズの上限は 20GB です。上限を超えるサイズのファイルは転送エラーになります。

  * 転送多重度の上限は、20 多重 / Agent です。

  * HULFT-HUB を使用した中継・転送との併用はできません。

  * Agent はクラスタ対応機能（フェールオーバー対応等）を提供しておりません。

  * 集信側がHULFT for Linux Ver.7.0.xの場合、送信要求はご利用いただけません。HULFT for Linux Ver.7.1以降をご利用ください。

  * 高強度暗号強制モード、簡易転送に対応しておりません。

  * 以下の理由から、HULFT for IBMi と接続する場合はAgent のコネクションID およびAgentのAgent ID に英小文字を使用しないでください。

    * HULFT for IBMi は、管理情報の設定値に英小文字を使用できません。

    * Agent がHULFT と接続する場合、HULFT の詳細ホスト情報のホスト名に「<_Agent のコネクションID の設定値_ >_<_AgentのAgent ID の設定値_ >_<_HULFT のホスト名_ >」を設定する必要があります。





---


## ページ 50

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/StatusCodeHULFT.htm

# HULFT の完了コード

HULFT の履歴情報のエラーコードが、相手側のエラーを表す完了コードで、かつ詳細コードが「550」の場合は、HULFT-WebConnect の処理でエラーが発生したことを表します。


---


## ページ 51

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/PointsNote/TransLargeFile.htm

# Agent のメモリが枯渇する場合

以下のような場合に、Agent に割り当てられたメモリがより多く消費され枯渇することがあります。

  * 大容量ファイルを転送する場合

  * 集信側のAgentとHULFTの間の通信速度が遅い場合




「OutOfMemoryError」で Agent が異常終了する場合は、設定ファイル（agent.conf）の「jvm.options」で以下のように Agent が利用できるメモリサイズを調整してください。

例:

jvm.options=-Xms64M -Xmx256M -XX:MaxDirectMemorySize=2048m

「OutOfMemoryError」で Agent が異常終了した際、該当の転送は無通信となり、HULFTで設定された値で無通信タイムアウトとなります。また、Agentの再起動が必要となる場合があります。

大容量ファイルを転送する場合には、Agent をデュアルコア以上の環境に導入することを推奨します。


---


## ページ 52

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/Preface/preface.htm

# Agent ガイド \- はじめに

このたびは、本製品をご利用いただき、誠にありがとうございます。

本ガイドは、Agent を使って HULFT-WebConnect を操作する方を対象にしています。


---


## ページ 53

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/Preface/preface.htm#mc-main-content

# Agent ガイド \- はじめに

このたびは、本製品をご利用いただき、誠にありがとうございます。

本ガイドは、Agent を使って HULFT-WebConnect を操作する方を対象にしています。


---


## ページ 54

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/Preface/Preparation.htm

# 事前準備

HULFT-WebConnect Agent （以下、Agent）と HULFT は TCP/IP プロトコル（OS に付属しています）を使用して通信を行います。

通信相手をホスト名で認識するため、ホスト名での接続の検査（ping コマンド）が通る必要があります。

配信側の Agent をインストールするマシンと配信側の HULFT をインストールしているマシンの接続の検査が完了していることをご確認ください。

集信側の Agent をインストールするマシンと集信側の HULFT をインストールしているマシンの接続の検査が完了していることをご確認ください。


---


## ページ 55

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/Preface/Transcription.htm

# 表記について

製品名等の固有名詞は、各メーカーの商標または登録商標です。


---


## ページ 56

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForLinux.htm

# Agent の起動（Linux）

Linux では、Agent をサービス（デーモン）として起動する方法があります。

コマンドによる起動、または systemd、init.d スクリプトによる起動が可能です。


---


## ページ 57

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForLinuxCommando.htm

# コマンドの場合

(1) 起動

a) ターミナル等のクライアントを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

b) 以下のコマンドを実行します。

集信 Agent 起動
    
    
    # ./agentctl -r start
    I120002 - 集信Agentを起動しました。

配信 Agent 起動
    
    
    # ./agentctl -s start
    I110002 - 配信Agentを起動しました。

上記のように出力されれば成功です。 

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

出力されるログについては、[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。

(2) 起動確認

a) ターミナル等のクライアントを起動し、以下のディレクトリに移動してください。
    
    
    {導入ディレクトリ}/bin

b) 以下のコマンドを実行します。

集信 Agent 起動確認
    
    
    # ./agentctl -r status
    status_receiver is called.
    receiver agent is ready to transfer. [002]

配信 Agent 起動確認
    
    
    # ./agentctl -s status
    status_sender is called.
    sender agent is ready to transfer. [002]

上記のように出力されれば成功です。 

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

出力されるログについては、[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。


---


## ページ 58

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForLinuxInit.htm

# init.d スクリプトの場合

(1) 起動スクリプトの生成

Agent に同梱している「generate_init.d_script.sh」を実行します。
    
    
    # sh {導入ディレクトリ}/bin/generate_init.d_script.sh

「sender_agent」と「receiver_agent」というスクリプトが生成されます。

(2) 起動スクリプトの配置

生成されたスクリプトを「/etc/init.d」に配置します。

(3) サービス登録

以下のコマンドでサービス登録を行います。
    
    
    # chkconfig --add sender_agent
    # chkconfig --add receiver_agent

(4) 起動

以下のコマンドで Agent を起動します。
    
    
    # /etc/init.d/sender_agent start
    # /etc/init.d/receiver_agent start

(5) 起動確認

以下のコマンドで Agent の起動を確認します。
    
    
    # /etc/init.d/sender_agent status
    status_sender is called.
    sender agent is ready to transfer. [002]
    # /etc/init.d/receiver_agent status
    status_receiver is called.
    receiver agent is ready to transfer. [002]

また、前述した以下のコマンドでも起動確認が可能です（以下は集信 Agent の例）。
    
    
    # ./agentctl -r status
    status_receiver is called.
    receiver agent is ready to transfer. [002]


---


## ページ 59

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForLinuxSystemd.htm

# systemd の場合

(1) Unit ファイル（.service）の生成

Agent に同梱している「generate_system.d_config.sh」を実行します。
    
    
    # sh {導入ディレクトリ}/bin/generate_system.d_config.sh

「senderAgent.service」と「receiverAgent.service」という Unit ファイルが生成されます。

(2) Unit ファイルの配置

生成された Unit ファイルを「/etc/systemd/system」に配置します。

(3) 変更の適用

「systemctl daemon-reload」を実行します。

(4) 起動

以下のコマンドで Agent を起動します。
    
    
    # systemctl start senderAgent
    # systemctl start receiverAgent

(5) 自動起動の設定

以下のコマンドで Agent の自動起動の設定をします。
    
    
    # systemctl enable senderAgent
    # systemctl enable receiverAgent

以下のコマンドで Agent の自動起動の解除設定をします。
    
    
    # systemctl disable senderAgent
    # systemctl disable receiverAgent

(6) 起動確認

以下のコマンドで Agent の起動を確認します。
    
    
    # systemctl status senderAgent
    # systemctl status receiverAgent

また、前述した以下のコマンドでも Agent の起動確認が可能です（以下は集信 Agent の例）。
    
    
    # ./agentctl -r status
    status_receiver is called.
    receiver agent is ready to transfer. [002]


---


## ページ 60

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForWin.htm

# Agent の起動（Windows）

Windows では、Agent をコマンドから起動する方法と、Windows サービスとして起動する方法があります。

ご利用環境に応じた起動方法をご確認ください。


---


## ページ 61

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForWinCommand.htm

# コマンドの場合

Agent をコマンドから起動します。

**注意**

この方法で起動した場合、ログオフ時に Agent プロセスが終了するのでご注意ください。

(1) 起動

a) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

b) 以下のコマンド（バッチファイル）を実行します。

集信 Agent 起動
    
    
    > agentctl -r start
    I120002 - 集信Agentを起動しました。

配信 Agent 起動
    
    
    > agentctl -s start
    I110002  - 配信Agentを起動しました。

上記のように出力されれば成功です。 

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

出力されるログについては、[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。

(2) 起動確認

a) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

b) 以下のコマンド（バッチファイル）を実行します。

集信 Agent 起動確認
    
    
    > agentctl -r status
    status_receiver is called.
    receiver agent is ready to transfer. [002]

配信 Agent 起動確認
    
    
    > agentctl -s status
    status_sender is called.
    sender agent is ready to transfer. [002]

上記のように出力されれば成功です。 

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

出力されるログについては、[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。


---


## ページ 62

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/ForWinServ.htm

# Windows サービスの場合

Agent を Windows サービスとして起動します。 

(1) 環境変数の設定

a) Windows に Java の環境変数を設定します。

  * JRE の場合 : 「JRE_HOME」を指定

  * JDK の場合 : 「JAVA_HOME」を指定




環境変数を省略した場合、Java インストール時に設定された OS のレジストリを参照します。

環境変数の設定方法については、OS のマニュアルを参照してください。

(2) Windows サービスの登録

a) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入フォルダ}/bin

b) 以下のコマンド（バッチファイル）を実行し、サービス登録を行います。
    
    
    > service install [任意のサービス名]
    Installing the service '[任意のサービス名]' ...
    Using JRE_HOME:         "C:\Program Files\Java\jre8"
    Using JVM:              "C:\Program Files\Java\jre8\bin\server\jvm.dll"
    "Install HULFT-WebConnect Agent Service..."
    The service '[任意のサービス名]' has been installed.

上記のように出力されれば成功です。

サービス名を省略した場合、以下の内容でサービス登録されます。

  * サービス名 : webconnect-agent

  * 表示名 : HULFT-WebConnect Agent




コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

(3) サービスの起動

コントロールパネルのサービスから起動

a) サービスを開きます。

  * [スタート] ボタン、[コントロールパネル]、[管理ツール]、[サービス] の順でサービスを開きます。




b) 詳細ペインで、以下のいずれかの操作を行います。

  * 登録したサービスをクリックし、操作メニューの [サービスの開始] をクリックします。

  * 登録したサービスを右クリックし、[開始] をクリックします。




コマンドから起動

a) コマンドプロンプトを起動します。

b) 以下のコマンドを入力します。
    
    
    > net start [サービス名]
    HULFT-WebConnect Agent サービスを開始します.
    HULFT-WebConnect Agent サービスは正常に開始されました。

上記のように出力されれば成功です。


---


## ページ 63

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/StartupAgent/StartupAgent.htm

# Agent の起動

各 OS ごとの Agent の起動方法について説明します。


---


## ページ 64

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForLinuxTerminateAgent.htm

# Agent の停止（Linux）


---


## ページ 65

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForLinuxTerminateAgentCommando.htm

# コマンドの場合

(1) ターミナル等のクライアントを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

(2) 以下のコマンドを実行します。

集信 Agent 停止
    
    
    # ./agentctl -r stop
    stop_receiver is called.
    receiver agent accept the request to stop. [000]

配信 Agent 停止 
    
    
    # ./agentctl -s stop
    stop_sender is called.
    sender agent accept the request to stop. [000]
    registry server has been stopped. [100] ＜- Agent の停止順によっては出力されない場合があります。

上記のように出力されれば成功です。

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

出力されるログについては、[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。


---


## ページ 66

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForLinuxTerminateAgentInit.htm

# init.d スクリプトの場合

init.d スクリプトによる停止と同様に、以下のコマンドを実行します。
    
    
    # /etc/init.d/sender_agent stop
    # /etc/init.d/receiver_agent stop


---


## ページ 67

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForLinuxTerminateAgentSystemd.htm

# systemd の場合

systemd による停止と同様に、以下のコマンドを実行します。
    
    
    # systemctl stop senderAgent
    # systemctl stop receiverAgent


---


## ページ 68

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForWinTerminateAgent.htm

# Agent の停止（Windows）

Agent をコマンドから起動した場合と、Windows サービスとして起動した場合では停止方法が異なります。

ご利用環境に応じた停止方法をご確認ください。 


---


## ページ 69

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForWinTerminateAgentCommand.htm

# コマンドの場合

(1) コマンドプロンプトを起動し、以下のディレクトリに移動します。
    
    
    {導入ディレクトリ}/bin

(2) 以下のコマンド（バッチファイル）を実行します。

集信 Agent 停止 
    
    
    > agentctl -r stop
    stop_receiver is called.
    receiver agent accept the request to stop. [000]

配信 Agent 停止 
    
    
    > agentctl -s stop
    stop_sender is called.
    sender agent accept the request to stop. [000]
    registry server has been stopped. [100] ＜- Agent の停止順によっては出力されない場合があります。

上記のように出力されれば成功です。 

コマンドの詳細については、[「コマンドリファレンス」](../CommandRef/CommandRef.htm)を参照してください。

出力されるログについては、[「Agent のログ」](../AgentLog/AgentLog.htm)を参照してください。


---


## ページ 70

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/ForWinTerminateAgentServ.htm

# Windows サービスの場合

コントロールパネルのサービスから停止

(1) サービスを開きます。

  * [スタート] ボタン、[コントロールパネル]、[管理ツール]、[サービス] の順でサービスを開きます。




(2) 詳細ペインで、以下のいずれかの操作を行います。

  * 登録したサービスをクリックし、操作メニューの [サービスの停止] をクリックします。

  * 登録したサービスを右クリックし、[停止] をクリックします。




コマンドから停止

(1) コマンドプロンプトを起動します。

(2) 以下のコマンドを入力します。
    
    
    > net stop [サービス名]
    HULFT-WebConnect Agent サービスを停止中です...
    HULFT-WebConnect Agent サービスは正常に停止されました。

上記のように出力されれば成功です。


---


## ページ 71

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-AGG/Content/Agent/TerminateAgent/TerminateAgent.htm

# Agent の停止

各 OS ごとの Agent の停止方法について説明します。


---

