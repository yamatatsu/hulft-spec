# HULFT WebConnect - SiteAPI

このドキュメントは 100 ページから生成されました。

---


## ページ 1

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/APIComSpeci.htm

# API 共通仕様

HULFT-WebConnect Site API の共通仕様について説明します。

すべてのリクエストおよびレスポンスインタフェースの文字コードは、UTF-8 を使用します。

レスポンスフォーマットは JSON フォーマットです。

また、HTTPS 通信（TLS 1.2）のみ受け付けます。


---


## ページ 2

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/APIKey.htm

# API キー

HULFT-WebConnect Site API では、API キーによる認証・認可が必要です。

API キーの発行は HULFT-WebConnect Management Console（以下、Management Console）の [API キー管理] 画面で行います。

![APIキー管理画面](../../Resources/Images/HWC-SAP/APIComSpeci/0010_registration-of-api-key_scr.jpg)

**注意**

API キーは新規発行時に 1 度だけ表示されますので、大切に保管してください。


---


## ページ 3

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/CommParam.htm

# 共通パラメータ

共通パラメータについて説明します。


---


## ページ 4

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/ErrResp.htm

# エラーレスポンス

HULFT-WebConnect Site API でリクエストされた処理に失敗した場合、以下の JSON フォーマットでエラーレスポンスを返却します。
    
    
    {
        "code":"E300003",
        "message":"The data is already registered."
    }

Property Name |  Value |  Description  
---|---|---  
code |  string |  Error code  
message |  string |  Error message


---


## ページ 5

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/QuePara.htm

# クエリパラメータ  
  
Parameter Name |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
startIndex |  integer (0 to 10000) |  false |  Index of the first row of a data to retrieve |  0  
maxResults |  integer (1 to 1000) |  false |  The maximum number of indexes included in a response data |  30  
from |  string (YYYYMMDD format) |  false |  Start date (search condition) |  Blank  
to |  string (YYYYMMDD format) |  false |  End date (search condition) |  Blank  
timezone |  string |  false |  Time Zone Settings (Example: timezone=Asia/Tokyo) |  UTC


---


## ページ 6

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/RateLimit.htm

# レートリミット  
  
HULFT-WebConnect Site API には、レートリミット（リクエスト数制限）を設定しています。

以下のレートリミットを考慮して API を使用してください。

レートリミット

1 契約アカウント当たり 1 分間に最大 100 リクエストまで送信できます。

リミット超過時の動作

超過以降のリクエストを 10 分間受け付けません（リクエスト禁止期間）。

リクエスト禁止期間の解除日時は、レスポンスヘッダの「Retry-After」から確認できます。

カウンターのリセット

レートリミット判定用のカウンターは毎分リセットされます。

ただし、リミットを超過していた場合は、リクエスト禁止期間を経過した後にリセットされます。


---


## ページ 7

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIComSpeci/ReqHeader.htm

# リクエストヘッダ

Request Parameter |  Value |  Required |  Description  
---|---|---|---  
Authorization |  Bearer <API-Key> |  true |  Specifies your API key.  
  
Example Request
    
    
    GET /relay/log?maxResults=30 HTTP/1.1
    Host: www.webconnect.hulft.com
    Authorization: Bearer abcdefg890abcdefg890abcdefg890ab
    Accept: application/json


---


## ページ 8

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccessDenialListGet.htm

# リスト取得

接続拒否履歴のリストを取得します。

Request Interface

HTTP Request
    
    
    GET /access-denial/log

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスが返却されます。
    
    
    {
        "totalSize":10,
        "fetchSize":10,
        "startIndex":0,
        "maxResults":30,
        "accessDenialLogs":[
            {
                "loginAccount":"xxxxxxxxxxxxxxxxxxxxxx",
                "accessedAt":"xxxxxxxxxxxxxxxxxxxxxx",
                "connectionType":"xxxxxxxxxxxxxxxxxxxxxx",
                "sourceIp":"xxxxxxxxxxxxxxxxxxxxxx",
                "destinationEndpoint":"xxxxxxxxxxxxxxxxxxxxxx",
                "connectionId":["abc", "xyz"],
                "agentId":"xxxxxxxxxxxxxxxxxxxxxx",
                "userAgent":"xxxxxxxxxxxxxxxxxxxxxx",
                "denialReason":"xxxxxxxxxxxxxxxxxxxxxx",
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
loginAccount (*1) |  string |  Account (email address)  
accessedAt |  string |  Date and time of access  
connectionType |  string |  Connection type  
sourceIp |  string |  Access source IP  
destinationEndpoint |  string |  Access destination endpoint (public host name)  
connectionId (*2) |  array |  Connection ID  
agentId (*2) |  string |  Agent ID  
userAgent |  string |  User agent  
denialReason |  string |  Cause of denied access  
  
*1 :Data Transfer Site ログイン時に接続拒否の場合は、loginAccountに値が設定されます。connectionIdとagentIdに値は設定されません。

*2 :HULFT-WebConnectサービスで接続拒否の場合は、connectionId、agentIdに値が設定されます。loginAccountに値は設定されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/access-denial/log");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/access-denial/log',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 9

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccessDenialLog.htm

# 接続拒否履歴

HULFT-WebConnect の接続拒否履歴を取得します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 10

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountListGet.htm

# リスト取得

参照可能なアカウントのリストを取得します。

Request Interface

HTTP Request
    
    
    GET /accounts/definition

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
      "limit": 10000,
      "totalSize": 1,
      "fetchSize": 1,
      "startIndex": 0,
      "maxResults": 30,
      "accounts": [
        {
          "id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          "mailAddress": "sample@example.com",
          "statusCode": 0,
          "isVerifiedMailAddress": true,
          "passwordValidityPeriod": 0,
          "ipFilterGroupName": null,
          "memo": "xxxxxxxxxxxxxxxxxxxxxx"
        }
      ]
    }
    			

Property Name |  Value |  Description  
---|---|---  
limit |  integer |  The maximum number of accounts settings that can be registered. (Fixed to 10000)  
totalSize |  integer |  The total number of data.  
fetchSize |  integer |  The number of the obtained data.  
startIndex |  integer |  Index of the first row of a data to retrieve.  
maxResults |  integer |  The maximum number of indexes included in a response data.  
accounts | array | Object array of the account settings.  
id |  string |  ID of the registered account.  
mailAddress |  string |  Email address.  
statusCode | number | Status code of the account. (0: New, 1: In use, 2: Changing password management method, 3: Changing email address)  
isVerifiedMailAddress |  boolean |  Whether the email address is verified or not. True if it is verified.  
passwordValidityPeriod |  number |  Password validity period. The unit is days.  
ipFilterGroupName |  string |  IP filter group name that is used to restrict access based on source IP address.  
memo |  string |  Note for the account.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/accounts/definition");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = 
    		new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/accounts/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 11

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountPassWordSet.htm

# アカウントパスワード設定依頼

アカウントに登録されているメールアドレスに対してパスワード設定依頼を行います。

パスワード設定依頼のメールを送信できるのは以下のいずれかの場合です。

  * アカウント設定の新規登録時
  * メールアドレス変更時でパスワード未設定状態の場合



以下の場合はエラーとなります。

  * メールアドレスそのものが実在しない（送信先が確認できない、またはメールが届かない）場合
  * 受信側で拒否された実績がある場合



当 API を通してパスワード設定依頼のメールが送信された場合、一定時間はメールの再送信がされずにエラーとなります。（現在の再送制限をしている間隔時間： 600 sec）

Request Interface

HTTP Request
    
    
    POST /accounts/password/set-request

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
accountId |  string |  true |  ID that uniquely distinguishes the account (32 alphabet characters) |  -  
  
Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/accounts/password/set-request");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{\"accountId\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\"}";
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
            	writer.write(postData);
            }
            System.out.println(connection.getResponseMessage()); 
    			// The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/accounts/password/set-request',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
      "accountId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 12

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountSet.htm

# アカウント管理

HULFT-WebConnect のアカウント設定を取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 13

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountSet1Get.htm

# 1 件取得

アカウント情報を 1 件取得します。

Request Interface

HTTP Request
    
    
    GET /accounts/definition/{accountId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
accountId |  string |  true |  ID of the account to get(32 alphanumeric characte) |  -  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"mailAddress": "sample@example.com",
    	"statusCode": 0,
    	"isVerifiedMailAddress": true,
    	"passwordValidityPeriod": 0,
    	"ipFilterGroupName": null,
    	"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    }

Property Name |  Value |  Description  
---|---|---  
id |  string |  ID of the registered account.  
mailAddress |  string |  Email address  
statusCode |  number |  Status code of the account. (0: New, 1: In use, 2: Changing password management method, 3: Changing email address)  
isVerifiedMailAddress | boolean | Whether the email address is verified or not. True if it is verified.  
passwordValidityPeriod |  number |  Password validity period. The unit is days.  
ipFilterGroupName  | string | IP filter group name that is used to restrict access based on source IP address.  
memo | string | Note for the account.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String accountId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
          URL url = new URL(host + "/api/v2/accounts/definition/" + accountId);
          HttpURLConnection connection = (HttpURLConnection) url.openConnection();
          connection.setRequestMethod("GET");
          connection.setRequestProperty("Authorization", "Bearer " + apiKey);
          try (BufferedReader reader = 
    	new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var accountId = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/accounts/definition/' + accountId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 14

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountSetDelete.htm

# 削除

アカウントを削除します。ブラウザ転送設定グループ もしくは、D-Client 設定と紐付いているアカウントは削除できずにエラーが返されます。

Request Interface

HTTP Request
    
    
    DELETE /accounts/definition/{accountId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
accountId |  string |  true |  ID of the account to delete.(32 alphanumeric character) |  -  
  
Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String accountId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/accounts/definition/" + accountId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); 
    				// The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var accountId  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/accounts/definition/' + accountId ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 15

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountSetRegistration.htm

# 登録

アカウント設定を新規登録します。

Request Interface

HTTP Request
    
    
    POST /accounts/definition

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
mailAddress |  string |  true |  It must be unique within the HULFT-WebConnect service. It is also used to identify the account.(String of 256 characters in email address format.) |  -  
passwordValidityPeriod |  number |  false |  Password validity period. The unit is days. If 0 is specified, there is no expiration date.(0, or from 30 to 365) |  0  
ipFilterGroupName |  string |  false |  IP filter group name that is used to restrict access based on source IP address.(String of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens)) |  null  
memo |  string |  false |  String within 256 characters Note for the account.(String within 256 character) |  Blank  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。

また、登録したリソースの URI をレスポンスヘッダ「Location」に格納します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"mailAddress": "sample@example.com",
    	"statusCode": 0,
    	"isVerifiedMailAddress": true,
    	"passwordValidityPeriod": 0,
    	"ipFilterGroupName": null,
    	"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    }

Property Name |  Value |  Description  
---|---|---  
id |  string |  ID of the registered account  
mailAddress |  string |  Email address.  
statusCode |  number |  Status code of the account. (0: New, 1: In use, 2: Changing password management method, 3: Changing email address)  
isVerifiedMailAddress |  boolean |  Whether the email address is verified or not. True if it is verified.  
passwordValidityPeriod | number | Password validity period. The unit is days.  
ipFilterGroupName |  string |  IP filter group name that is used to restrict access based on source IP address.  
memo |  string |  Note for the account.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/accounts/definition");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{\"mailAddress\": \"sample@example.com\","
    				+ "\"passwordValidityPeriod\": 0,"
    				+ "\"ipFilterGroupName\": \"ipFilterGroupName\","
    				+ "\"memo\": \"memo\"}";
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
    	 try (BufferedReader reader = 
    		new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
    		String line;
    		while ((line = reader.readLine()) != null) {
    			System.out.println(line);
    		}
    	  }
    	} catch (IOException ex) {
    		// error
           }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/accounts/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
                "mailAddress": "sample@example.com",
                "passwordValidityPeriod": 0,
                "ipFilterGroupName": "ipFilterGroupName",
                "memo": "memo"
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 16

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AccountSetUpdate.htm

# 更新

アカウント設定を更新します。メールアドレスが更新された場合はパスワードもリセットされます。

Request Interface

HTTP Request
    
    
    PUT /accounts/definition/{accountId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
accountId |  string |  true |  ID of the account to updat (32 alphanumeric character) |  -  
Request Parameter |  Value |  Description  
---|---|---  
mailAddress |  string |  It must be unique within the HULFT-WebConnect service. It is also used to identify the account. (String of 256 characters in email address forma)  
passwordValidityPeriod |  string |  Password validity period. The unit is days. If 0 is specified, there is no expiration dat (0, or from 30 to 365)  
ipFilterGroupName |  string |  IP filter group name that is used to restrict access based on source IP address. If you specify an empty string, the setting of the item is cleared.(String of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens), or an empty string (""))  
memo |  string |  Note for the account.(String within 256 characte)  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"mailAddress": "sample@example.com",
    	"statusCode": 0,
    	"isVerifiedMailAddress": true,
    	"passwordValidityPeriod": 0,
    	"ipFilterGroupName": null,
    	"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    }

Property Name |  Value |  Description  
---|---|---  
id |  string |  ID of the registered accunt.  
mailAddress |  string |  Email addres.  
statusCode |  number |  Status code of the account. (0: New, 1: In use, 2: Changing password management method, 3: Changing email address)  
isVerifiedMailAddress |  boolean |  Whether the email address is verified or not. True if it is verified.  
passwordValidityPeriod |  number |  Password validity period. The unit isdays  
ipFilterGroupName | string | IP filter group name that is used to restrict access based on source IP address.  
memo | string | Note for the account.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String accountId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/accounts/definition/" + accountId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String putData = "{\"mailAddress\": \"sample@example.com\","
    			+ "\"passwordValidityPeriod\": 0,"
    			+ "\"ipFilterGroupName\": \"ipFilterGroupName\","
    			+ "\"memo\": \"memo\"}";		
            connection.setRequestMethod("PUT");
            connection.setDoOutput(true);
            connection.setDoInput(true);		
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
            try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
    				writer.write(putData);
                   }
            try (BufferedReader reader = 
    		new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
    		String line;
    		while ((line = reader.readLine()) != null) {
    		System.out.println(line);
    		}
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var accountId = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
        type: 'PUT',
        url: host + '/api/v2/accounts/definition/' + accountId ,
        headers: {
          Authorization: 'Bearer ' + apiKey
        },
        contentType: 'application/json',
        data: JSON.stringify({
                  "mailAddress": "sample@example.com",
                  "passwordValidityPeriod": 0,
                  "ipFilterGroupName": "ipFilterGroupName",
                  "memo": "memo"
              })
      }).done(function(data, status, xhr) {
        console.log(data);
      }).fail(function(data, status, xhr) {
        console.log(data);
      });


---


## ページ 17

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AgentConnectStatus.htm

# Agent 接続状況

HULFT-WebConnect に接続中の Agent 一覧（Agent 接続状況）を取得します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 18

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AgentConnectStatusAllGet.htm

# 全件取得

Agent 接続状況を全件取得します。

Request Interface

HTTP Request
    
    
    GET /agent/status

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続 Agent」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":1,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":30,
        "status":[
            {
                "agentId":"agent1",
                "direction":"receive",
                "connectionId":["id1","id22"],
                "endpoint":"california-service1.webconnect.hulft.com",
                "startConnection":"2016-06-30 14:22:00.942",
                "sessionId":"dfBqpCYBFcQZNRx9z6q_A6rQ0Yv7y3yZ3IJJf2aJ",
                "agentVersion":"2.0.0",
                "willBeClosed":false,
                "supportingDisconnectApi":true
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
status |  array |  Array of the elements described below  
agentId |  string |  Agent ID of the connected Agent  
direction |  string |  Transfer direction of Agent  
connectionId |  array |  Connection ID to be used when Agent connects to HULFT-WebConnect  
endpoint |  string |  Access point of HULFT-WebConnect that Agent currently connecting to  
startConnection |  string |  The date and time at which Agent was connected  
sessionId |  string |  Session ID between Agent and HULFT-WebConnect  
agentVersion |  string |  Version of Agent  
willBeClosed |  boolean |  Whether the disconnection request is received or not  
supportingDisconnectApi |  boolean |  Whether the disconnection API is accepted or not  
  
Examples

Java JavaScript
    
    
                                           
    public static void main(String[] args) {
            String host = "https://www.webconnect.hulft.com";
            String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
            try {
                    URL url = new URL(host + "/api/v2/agent/status");
                    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET");
                    connection.setRequestProperty("Authorization", "Bearer " + apiKey);
                    try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                            String line;
                            while((line = reader.readLine()) != null) {
                                    System.out.println(line);
                            }
                    }
            } catch (IOException ex) {
                    // error
            }
    }
                    
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/agent/status',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 19

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AgentConnectStatusDirGet.htm

# 転送方向を指定して取得

転送方向を指定して Agent 接続状況を取得します。

Request Interface

HTTP Request
    
    
    GET /agent/status/{direction}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
direction |  string |  true |  Transfer direction of Agent (send | receive) |  Blank  
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続 Agent」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":1,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":30,
        "status":[
            {
                "agentId":"agent1",
                "direction":"receive",
                "connectionId":["id1","id22"],
                "endpoint":"california-service1.webconnect.hulft.com",
                "startConnection":"2016-06-30 14:22:00.942",
                "sessionId":"dfBqpCYBFcQZNRx9z6q_A6rQ0Yv7y3yZ3IJJf2aJ",
                "agentVersion":"2.0.0",
                "willBeClosed":false,
                "supportingDisconnectApi":true
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
status |  array |  Array of the elements described below  
agentId |  string |  Agent ID of the connected Agent  
direction |  string |  Transfer direction of Agent  
connectionId |  array |  Connection ID to be used when Agent connects to HULFT-WebConnect  
endpoint |  string |  Access point of HULFT-WebConnect that Agent currently connecting to  
startConnection |  string |  The date and time at which Agent was connected  
sessionId |  string |  Session ID between Agent and HULFT-WebConnect  
agentVersion |  string |  Version of Agent  
willBeClosed |  boolean |  Whether the disconnection request is received or not  
supportingDisconnectApi |  boolean |  Whether the disconnection API is accepted or not  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String direction = "receive";
        try {
            URL url = new URL(host + "/api/v2/agent/status/" + direction);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var direction = 'receive';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/agent/status/' + direction,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 20

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AgentDisconnect.htm

# Agent 切断

HULFT-WebConnect に接続中の Agent を切断します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 21

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/AgentDisconnectParameter.htm

# 切断

指定した Agent を強制的に切断します。

切断できる Agent のバージョンは 1.2.0 以降です。

**注意**

ファイル転送中に切断すると、転送が異常終了するのでご注意ください。

Request Interface

HTTP Request
    
    
    POST /agent/disconnection

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
sessionId |  string |  true |  Session ID between Agent and HULFT-WebConnect |   
endpoint |  string |  true |  Access point of HULFT-WebConnect that Agent currently connecting to |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、 「接続 Agent」の「切断」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/agent/disconnection");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{\"sessionId\":\"xxxxxxxxxxxxxxxx\", \"endpoint\":\"california-service1.webconnect.hulft.com\"}";
    
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
            System.out.println(connection.getResponseMessage()); // The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/agent/disconnection',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({sessionId: 'xxxxxxxxxxxxxxxx', endpoint: 'california-service1.webconnect.hulft.com'})
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 22

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/APIDetail.htm

# API 詳細

各 HULFT-WebConnect Site API のインタフェースについて説明します 。


---


## ページ 23

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransGroup.htm

# ブラウザ転送設定グループ

HULFT-WebConnect のブラウザ転送設定グループを取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 24

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransGroup1Get.htm

# 1 件取得

参照可能なブラウザ転送グループ設定を1 件取得します 。

Request Interface

HTTP Request
    
    
    GET /browser-transfer-groups/{browserTransferGroupId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserTransferGroupId |  string |  true |  ID of the Browser Transfer Group to get. (32 alphanumeric characters) |  -  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"name": "xxxxxxxx",
    	"account": {
    		"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"mailAddress": "sample@example.com"
    	},
    	"browserToHulftDefinitions":[{"id":"xxxxxxxx","description":null}],
    	"hulftToBrowserDefinitions":[{"id":"xxxxxxxx","description":null}],
    	"enabled": true,
    	"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    }
    		

Property Name |  Value |  Description  
---|---|---  
id |  string |  ID of the registered Browser Transfer Group.  
name |  string |  Name of the Browser Transfer Group.  
account |  object |  Account that is assigned to the group.  
id |  string |  Account ID.  
mailAddress |  string |  Email address of the account.  
browserToHulftDefinitions |  array |  Object array of the grouped Browser Send File settings.  
hulftToBrowserDefinitions |  array |  Object array of the grouped Browser Send Request settings.  
enabled |  boolean |  Availability of the Browser Transfer Group.  
memo |  string |  Note for the Browser Transfer Group.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
            String host = "https://www.webconnect.hulft.com";
            String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
            String browserTransferGroupId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
            try {
                    URL url = new URL(host + "/api/v2/browser-transfer-groups/" + browserTransferGroupId);
                    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET");
                    connection.setRequestProperty("Authorization", "Bearer " + apiKey);
                    try (BufferedReader reader = 
    		   new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                            String line;
                            while((line = reader.readLine()) != null) {
                                    System.out.println(line);
                            }
                    }
            } catch (IOException ex) {
                    // error
            }
    }
                    
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserTransferGroupId = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/browser-transfer-groups/' + browserTransferGroupId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 25

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransGroupDelete.htm

# 削除

ブラウザ転送設定グループを削除します。

Request Interface

HTTP Request
    
    
    DELETE /browser-transfer-groups/{browserTransferGroupId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserTransferGroupId |  string |  true |  ID of the Browser Transfer Group to delete.(32 alphanumeric characters) |  -  
  
Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    	String host = "https://www.webconnect.hulft.com";
    	String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	String browserTransferGroupId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	try {
    		URL url = new URL(host + "/api/v2/browser-transfer-groups/" + browserTransferGroupId);
    		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    		connection.setRequestMethod("DELETE");
    		connection.setRequestProperty("Authorization", "Bearer " + apiKey);
    		System.out.println(connection.getResponseMessage());
    			 // The response does not contain the response body.
    	} catch (IOException ex) {
    	// error
    	}
    }
    
    
    
    //load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserTransferGroupId = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/browser-transfer-groups/' + browserTransferGroupId ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 26

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransGroupListGet.htm

# リスト取得

参照可能なブラウザ転送設定グループのリストを取得します。

Request Interface

HTTP Request
    
    
    GET /browser-transfer-groups

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"limit": 10000,
    	"totalSize": 2,
    	"fetchSize": 2,
    	"startIndex": 0,
    	"maxResults": 30,
    	"browserTransferGroups": [
    		{
    		"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"name": "xxxxxxxx",
    		"account": {
    		"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"mailAddress": "sample@example.com"
    		},
    		"browserToHulftDefinitions":[{"id":"xxxxxxxx","description":null}],
    		"hulftToBrowserDefinitions":[{"id":"xxxxxxxx","description":null}],
    		"enabled": true,
    		"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    		},
    		{
    		"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"name": "xxxxxxxx",
    		"account": null,
    		"browserToHulftDefinitions":[{"id":"xxxxxxxx","description":null}],
    		"hulftToBrowserDefinitions":[{"id":"xxxxxxxx","description":null}],
    		"enabled": false,
    		"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    		}
    	]
    }
    			

Property Name |  Value |  Description  
---|---|---  
limit |  integer |  The maximum number of Browser Transfer Group settings that can be registered. (Fixed to 10000)  
totalSize |  integer |  The total number of data.  
fetchSize |  integer |  The number of the obtained data.  
startIndex |  integer |  Index of the first row of a data to retrieve.  
maxResults |  integer |  The maximum number of indexes included in a response data.  
browserTransferGroups |  array |  Object array of the Browser Transfer Groups.  
id |  string |  ID of the registered Browser Transfer Group.  
name |  string |  Name of the Browser Transfer Group.  
account |  object |  Account that is assigned to the group.  
id |  string |  Account ID.  
mailAddress |  string |  Email address of the accunt.  
browserToHulftDefinitions |  array |  Object array of the grouped Browser Send File settings.  
hulftToBrowserDefinitions |  array |  Object array of the grouped Browser Send Request settings.  
enabled |  boolean |  Availability of the Browser Transfer Group.  
memo |  string |  Note for the Browser Transfer Group.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer-groups");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = 
    	  new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/browser-transfer-groups',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 27

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransGroupRegistration.htm

# 登録

ブラウザ転送設定グループを登録します。

Request Interface

HTTP Request
    
    
    POST /browser-transfer-groups

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
name | string | true | Name of the Browser Transfer Group. It must be unique under the contractor account. (String of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens). Names consisting of only "." (one dot) or ".." (two dots) are not allowe) | -  
accountId | string | false | Account ID of a HULFT-WebConne Ver.3 account that uses the corresponding Browser Transfer Group. If you omit this parameter, the item is not set. (String of 32 characters in UUID format (no hyphens) or an empty string ( "" )) | null  
browserToHulftDefinitionIds |  string |  false |  Browser Send File settings to group together. If you do not want to group them, specify an empty array or null. (Array that can contain strings of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens). Up to 30 elements. Names consisting of only "." (one dot) or ".." (two dots) are not allowed.) |  empty  
hulftToBrowserDefinitionIds |  number |  false |  Browser Send Request settings to group together. If you do not want to group them, specify an empty array or null. (Array that can contain strings of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens). Up to 30 elements. Names consisting of only "." (one dot) or ".." (two dots) are not allowe) |  empty  
enabled |  string |  false |  Specify availability of the settings. "true" enables the settings. ("true" or " "false") |  false  
memo |  string |  false |  Note for the Browser Transfer Group. (String within 256 characters) |  Blank  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"name": "xxxxxxxx",
    	"account": {
    		"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"mailAddress": "sample@example.com"
    	},
    	"browserToHulftDefinitions":[{"id":"xxxxxxxx","description":null}],
    	"hulftToBrowserDefinitions":[{"id":"xxxxxxxx","description":null}],
    	"enabled": true,
    	"memo": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
    		

Property Name |  Value |  Description  
---|---|---  
id |  string |  ID of the registered Browser Transfer Group.  
name |  string |  Name of the Browser Transfer Group.  
account |  object |  Account that is assigned to the Group.  
id |  string |  Account ID.  
mailAddress |  string |  Email address of the account.  
browserToHulftDefinitions |  array | Object array of the grouped Browser Send File settings.  
hulftToBrowserDefinitions |  array | Object array of the grouped Browser Send Request settings.  
enabled |  boolean |  Availability of the Browser Transfer Group.  
memo |  string |  Note for the Browser Transfer Group.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    	String host = "https://www.webconnect.hulft.com";
    	String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	try {
    	URL url = new URL(host + "/api/v2/browser-transfer-groups");
    	HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    	String postData = "{\"name\": \"sample\","
    		 +  "\"accountId\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\","
    		 +  "\"browserToHulftDefinitionIds\": [\"browserToHulftDefinitionId\"],"
    		 +  "\"hulftToBrowserDefinitionIds\": [\"hulftToBrowserDefinitionId\"],"
    		 +  "\"enabled\": true,"
    		 +  "\"memo\": \"memo\"}";
    	connection.setRequestMethod("POST");
    	connection.setDoOutput(true);
    	connection.setDoInput(true);
    	connection.setRequestProperty("Authorization", "Bearer " + apiKey);
    	connection.setRequestProperty("Content-Type", "application/json");
    	connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
    	try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
    		writer.write(postData);
    		}
    	try (BufferedReader reader = 
    		new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
    	String line;
    	while ((line = reader.readLine()) != null) {
    		System.out.println(line);
    		}
    	}
    	} catch (IOException ex) {
    	// error
    	}
    }
    
    
    // load jquery
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
    	type: 'POST',
    	url: host + '/api/v2/browser-transfer-groups',
    	headers: {
    			Authorization: 'Bearer ' + apiKey
    	},
    	contentType: 'application/json',
    	data: JSON.stringify({
    		"name": "sample",
    		"accountId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"browserToHulftDefinitionIds": ["browserToHulftDefinitionId"],
    		"hulftToBrowserDefinitionIds": ["hulftToBrowserDefinitionId"],
    		"enabled": true,
    		"memo": "memo" 
    	})
    }).done(function(data, status, xhr) {
    	console.log(data);
    }).fail(function(data, status, xhr) {
    	console.log(data);
    });
    			


---


## ページ 28

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransGroupUpdate.htm

# 更新

ブラウザ転送設定グループを更新します。

Request Interface

HTTP Request
    
    
    PUT /browser-transfer-groups/{browserTransferGroupId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserTransferGroupId |  string |  true |  ID of the Browser Transfer Group to update. (32 alphanumeric characters) |  -  
Request Parameter |  Value |  Description  
---|---|---  
name | string | Name of the Browser Transfer Group. It must be unique under the contractor account. (String of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens). Names consisting of only "." (one dot) or ".." (two dots) are not allowed.)  
accountId | string | Account ID of a HULFT-WebConnect Ver.3 account that uses the corresponding Browser Transfer Group. If you specify an empty string, the setting of the item is cleared. (String of 32 characters in UUID format (no hyphens) or an empty string ( "" ))  
browserToHulftDefinitionIds |  string |  Browser Send File settings to group together. If you do not want to group them, specify an empty array or null. (Array that can contain strings of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens). Up to 30 elements. Names consisting of only "." (one dot) or ".." (two dots) are not allowed.)  
hulftToBrowserDefinitionId |  number |  Browser Send Request settings to group together. If you do not want to group them, specify an empty array or null. (Array that can contain strings of 1 to 32 alphabet characters, "." (dots), and "-" (hyphens). Up to 30 elements. Names consisting of only "." (one dot) or ".." (two dots) are not allowed.)  
enable |  string |  Specify availability of the settings. "true" enables the settings. ("true" or " "false")  
memo |  string |  Note for the Browser Transfer Group. (String within 256 characters)  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"name": "xxxxxxxx",
    	"account": {
    		"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"mailAddress": "sample@example.com"
    	},
    	"browserToHulftDefinitions":[{"id":"xxxxxxxx","description":null}],
    	"hulftToBrowserDefinitions":[{"id":"xxxxxxxx","description":null}],
    	"enabled": true,
    	"memo": "xxxxxxxxxxxxxxxxxxxxxx"
    }
    		

Property Name |  Value |  Description  
---|---|---  
id |  string |  ID of the registered Browser Transfer Group.  
name |  string |  Name of the Browser Transfer Group.  
account |  object |  Account that is assigned to the group.  
id |  string |  Account ID.  
mailAddress |  string |  Email address of the account.  
browserToHulftDefinitions |  array |  Object array of the grouped Browser Send File settings.  
hulftToBrowserDefinitions |  array |  Object array of the grouped Browser Send Request settings.  
enabled |  boolean |  Availability of the Browser Transfer Group.  
memo |  string |  Note for the Browser Transfer Group.  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    String host = "https://www.webconnect.hulft.com";
    String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    String browserTransferGroupId = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    try {
      URL url = new URL(host + "/api/v2/browser-transfer-groups/" + browserTransferGroupId);
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();
      String putData = "{\"name\": \"sample\","
         + "\"accountId\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\","
         + "\"browserToHulftDefinitionIds\": [\"browserToHulftDefinitionId\"],"
         + "\"hulftToBrowserDefinitionIds\": [\"hulftToBrowserDefinitionId\"],"
         + "\"enabled\": true,"
         + "\"memo\": \"memo\"}";
      connection.setRequestMethod("PUT");
      connection.setDoOutput(true);
      connection.setDoInput(true);
      connection.setRequestProperty("Authorization", "Bearer " + apiKey);
      connection.setRequestProperty("Content-Type", "application/json");
      connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
      try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
        writer.write(putData);
      }
      try (BufferedReader reader =
    		 new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
        String line;
         while ((line = reader.readLine()) != null) {
            System.out.println(line);
          }
        }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserTransferGroupId = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
    	type: 'PUT',
    	url: host + '/api/v2/browser-transfer-groups/' + browserTransferGroupId,
    	headers: {
    		Authorization: 'Bearer ' + apiKey
    	},
    	contentType: 'application/json',
    	data: JSON.stringify({
    		"name": "sample",
    		"accountId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"browserToHulftDefinitionIds": ["browserToHulftDefinitionId"],
    		"hulftToBrowserDefinitionIds": ["hulftToBrowserDefinitionId"],
    		"enabled": true,
    		"memo": "memo"
    	})
    }).done(function(data, status, xhr) {
     console.log(data);
    }).fail(function(data, status, xhr) {
     console.log(data);
    });


---


## ページ 29

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSet.htm

# ブラウザ転送設定

HULFT-WebConnect のブラウザ転送設定を取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 30

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSet1Get.htm

# 1 件取得

ブラウザ転送設定を1 件取得する場合の、HULFT-WebConnect Site API のインタフェースについて説明します 。


---


## ページ 31

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSet1GetSnd.htm

# 送信要求の場合

転送設定 ID を指定してブラウザ転送設定（送信要求）を 1 件取得します。

Request Interface

HTTP Request
    
    
    GET /browser-transfer/definition/hulft-to-browser/{hulftToBrowserDefinitionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
hulftToBrowserDefinitionId |  string |  true |  Transfer Settings ID |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ送信要求」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
       "hulftToBrowserDefinitionId":"browser1",
        "description":"xxxxxxxxxxxxx",
        "fileId":"FILEID1",
        "memo":"memo1",
        "browser":{
                "connectionId":"id1",
                "agentId":"agent1",
                "hostName":"HWC-BROWSER"
                "useReceiveFileName":"true",
                "receiveFileName":"file1"
        },
        "hulft":{
                "connectionId":"id2",
                "agentId":"agent2",
                "hostName":"host",
                "hulftRequestAcknowledgePort":31000,
                "msg0":"xxxxxxxxxxxxx",
                "msg1":"xxxxxxxxxxxxx",
                "msg2":"xxxxxxxxxxxxx",
                "msg3":"xxxxxxxxxxxxx",
                "msg4":"xxxxxxxxxxxxx",
                "msg5":"xxxxxxxxxxxxx",
                "msgl0":"xxxxxxxxxxxxx",
                "msgl1":"xxxxxxxxxxxxx"
        }
    }

Property Name |  Value |  Description  
---|---|---  
hulftToBrowserDefinitionId |  string |  Transfer Settings ID  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
useReceiveFileName |  string |  Whether to specify the Receive file name displayed on the browser side  
receiveFileName |  string |  Receive file name displayed on the browser side  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftRequestAcknowledgePort |  integer |  Request Acknowledge Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String hulftToBrowserDefinitionId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer/definition/hulft-to-browser/" + hulftToBrowserDefinitionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var hulftToBrowserDefinitionId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/browser-transfer/definition/hulft-to-browser/' + hulftToBrowserDefinitionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 32

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSet1GetSnding.htm

# 配信要求の場合

転送設定 ID を指定してブラウザ転送設定（配信要求）を 1 件取得します。

Request Interface

HTTP Request
    
    
    GET /browser-transfer/definition/browser-to-hulft/{browserToHulftDefinitionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserToHulftDefinitionId |  string |  true |  Transfer Settings ID |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ配信要求」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "browserToHulftDefinitionId":"browser1",
        "description":"xxxxxxxxxxxxx",
        "fileId":"FILEID1",
        "memo":"memo1",
        "browser":{
                "connectionId":"id1",
                "agentId":"agent1",
                "hostName":"HWC-BROWSER"
        },
        "hulft":{
                "connectionId":"id2",
                "agentId":"agent2",
                "hostName":"host",
                "hulftReceivingPort":30000,
                "msg0":"xxxxxxxxxxxxx",
                "msg1":"xxxxxxxxxxxxx",
                "msg2":"xxxxxxxxxxxxx",
                "msg3":"xxxxxxxxxxxxx",
                "msg4":"xxxxxxxxxxxxx",
                "msg5":"xxxxxxxxxxxxx",
                "msgl0":"xxxxxxxxxxxxx",
                "msgl1":"xxxxxxxxxxxxx"
        }
    }

Property Name |  Value |  Description  
---|---|---  
browserToHulftDefinitionId |  string |  Transfer Settings ID  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftReceivingPort |  integer |  Receive Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String browserToHulftDefinitionId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer/definition/browser-to-hulft/" + browserToHulftDefinitionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserToHulftDefinitionId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/browser-transfer/definition/browser-to-hulft/' + browserToHulftDefinitionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 33

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetAllGet.htm

# 全件取得

ブラウザ転送設定を全件取得する場合の、HULFT-WebConnect Site API のインタフェースについて説明します 。


---


## ページ 34

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetAllGetSnd.htm

# 送信要求の場合

ブラウザ転送設定（送信要求）を全件取得します。

クエリパラメータを指定することで、検索条件に該当するブラウザ転送設定を取得することもできます。

Request Interface

HTTP Request
    
    
    GET /browser-transfer/definition/hulft-to-browser

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ送信要求」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":50,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":1,
        "hulftToBrowserDefinitions":[
            {
                "hulftToBrowserDefinitionId":"browser1",
                "description":"xxxxxxxxxxxxx",
                "fileId":"FILEID1",
                "memo":"memo1",
                "browser":{
                        "connectionId":"id1",
                        "agentId":"agent1",
                        "hostName":"HWC-BROWSER",
                        "useReceiveFileName":"true",
                        "receiveFileName":"file1"
                },
                "hulft":{
                        "connectionId":"id2",
                        "agentId":"agent2",
                        "hostName":"host",
                        "hulftRequestAcknowledgePort":31000,
                        "msg0":"xxxxxxxxxxxxx",
                        "msg1":"xxxxxxxxxxxxx",
                        "msg2":"xxxxxxxxxxxxx",
                        "msg3":"xxxxxxxxxxxxx",
                        "msg4":"xxxxxxxxxxxxx",
                        "msg5":"xxxxxxxxxxxxx",
                        "msgl0":"xxxxxxxxxxxxx",
                        "msgl1":"xxxxxxxxxxxxx"
                }
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
hulftToBrowserDefinitions |  array |  Transfer settings  
hulftToBrowserDefinitionId |  string |  Transfer Settings ID  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
useReceiveFileName |  string |  Whether to specify the Receive file name displayed on the browser side  
receiveFileName |  string |  Receive file name displayed on the browser side  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftRequestAcknowledgePort |  integer |  Request Acknowledge Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer/definition/hulft-to-browser");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/browser-transfer/definition/hulft-to-browser',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 35

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetAllGetSnding.htm

# 配信要求の場合

ブラウザ転送設定（配信要求）を全件取得します。

クエリパラメータを指定することで、検索条件に該当するブラウザ転送設定を取得することもできます。

Request Interface

HTTP Request
    
    
    GET /browser-transfer/definition/browser-to-hulft

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ配信要求」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":50,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":1,
        "browserToHulftDefinitions":[
            {
                "browserToHulftDefinitionId":"browser1",
                "description":"xxxxxxxxxxxxx",
                "fileId":"FILEID1",
                "memo":"memo1",
                "browser":{
                        "connectionId":"id1",
                        "agentId":"agent1",
                        "hostName":"HWC-BROWSER"
                },
                "hulft":{
                        "connectionId":"id2",
                        "agentId":"agent2",
                        "hostName":"host",
                        "hulftReceivingPort":30000,
                        "msg0":"xxxxxxxxxxxxx",
                        "msg1":"xxxxxxxxxxxxx",
                        "msg2":"xxxxxxxxxxxxx",
                        "msg3":"xxxxxxxxxxxxx",
                        "msg4":"xxxxxxxxxxxxx",
                        "msg5":"xxxxxxxxxxxxx",
                        "msgl0":"xxxxxxxxxxxxx",
                        "msgl1":"xxxxxxxxxxxxx"
                }
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
browserToHulftDefinitions |  array |  Transfer settings  
browserToHulftDefinitionId |  string |  Transfer Settings ID  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftReceivingPort |  integer |  Receive Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com"; 
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer/definition/browser-to-hulft");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/browser-transfer/definition/browser-to-hulft',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 36

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetDelete.htm

# 削除

ブラウザ転送設定を削除する場合の、HULFT-WebConnect Site API のインタフェースについて説明します 。


---


## ページ 37

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetDeleteSnd.htm

# 送信要求の場合

指定したブラウザ転送設定（送信要求）を削除します。

Request Interface

HTTP Request
    
    
    DELETE /browser-transfer/definition/hulft-to-browser/{hulftToBrowserDefinitionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
hulftToBrowserDefinitionId |  string |  true |  Transfer Settings ID to be deleted |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ送信要求」の「削除」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String hulftToBrowserDefinitionId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/browser-transfer/definition/hulft-to-browser/" + hulftToBrowserDefinitionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); // The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserToHulftDefinitionId = 'xxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/browser-transfer/definition/hulft-to-browser/' + hulftToBrowserDefinitionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 38

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetDeleteSnding.htm

# 配信要求の場合

指定したブラウザ転送設定（配信要求）を削除します。

Request Interface

HTTP Request
    
    
    DELETE /browser-transfer/definition/browser-to-hulft/{browserToHulftDefinitionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserToHulftDefinitionId |  string |  true |  Transfer Settings ID to be deleted |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ配信要求」の「削除」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String browserToHulftDefinitionId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/browser-transfer/definition/browser-to-hulft/" + browserToHulftDefinitionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); // The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserToHulftDefinitionId  = 'xxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/browser-transfer/definition/browser-to-hulft/' + browserToHulftDefinitionId ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 39

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetRegistration.htm

# 登録

ブラウザ転送設定を登録する場合の、HULFT-WebConnect Site API のインタフェースについて説明します 。


---


## ページ 40

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetRegistrationSnd.htm

# 送信要求の場合

ブラウザ転送設定（送信要求）を新規登録します。

Request Interface

HTTP Request
    
    
    POST /browser-transfer/definition/hulft-to-browser

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
hulftToBrowserDefinitionId |  string |  true |  Transfer Settings ID (32 characters or less) |   
description |  string |  false |  Description of the transfer settings |  Blank  
fileId |  string |  true |  File ID of HULFT on the remote machine |   
memo |  string |  false |  Note for the settings |  Blank  
browser |  object |  true |  Browser Definition |   
connectionId |  string |  true |  Connection ID of the browser side that is registered in the Connection Settings |   
agentId |  string |  true |  ID to identify the browser (25 characters or less) |   
useReceiveFileName |  string |  true |  Whether to specify the Receive file name displayed on the browser side |   
receiveFileName |  string |  false |  Receive file name displayed on the browser side (this field is mandatory if you specify the Receive file name) |  Send file name of HULFT  
hulft |  object |  true |  Agent / HULFT Definition |   
connectionId |  string |  true |  Connection ID of the remote machine that is registered in the Connection Settings |   
agentId |  string |  true |  Agent ID of the remote machine (25 characters or less) |   
hostName |  string |  true |  Host information of HULFT on the remote machine |   
hulftRequestAcknowledgePort |  integer |  false |  Request Acknowledge Port No. of HULFT on the remote machine |  31000  
msg0 |  string |  false |  Message sent as 'msg0' to HULFT on the remote machine |  Blank  
msg1 |  string |  false |  Message sent as 'msg1' to HULFT on the remote machine |  Blank  
msg2 |  string |  false |  Message sent as 'msg2' to HULFT on the remote machine |  Blank  
msg3 |  string |  false |  Message sent as 'msg3' to HULFT on the remote machine |  Blank  
msg4 |  string |  false |  Message sent as 'msg4' to HULFT on the remote machine |  Blank  
msg5 |  string |  false |  Message sent as 'msg5' to HULFT on the remote machine |  Blank  
msgl0 |  string |  false |  Message sent as 'msgl0' to HULFT on the remote machine |  Blank  
msgl1 |  string |  false |  Message sent as 'msgl1' to HULFT on the remote machine |  Blank  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ送信要求」の「登録」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。

また、登録したリソースの URI をレスポンスヘッダ「Location」に格納します。
    
    
    {
       "hulftToBrowserDefinitionId":"browser1",
        "description":"xxxxxxxxxxxxx",
        "fileId":"FILEID1",
        "memo":"memo1",
        "browser":{
                "connectionId":"id1",
                "agentId":"agent1",
                "hostName":"HWC-BROWSER"
                "useReceiveFileName":"true",
                "receiveFileName":"file1"
        },
        "hulft":{
                "connectionId":"id2",
                "agentId":"agent2",
                "hostName":"host",
                "hulftRequestAcknowledgePort":31000,
                "msg0":"xxxxxxxxxxxxx",
                "msg1":"xxxxxxxxxxxxx",
                "msg2":"xxxxxxxxxxxxx",
                "msg3":"xxxxxxxxxxxxx",
                "msg4":"xxxxxxxxxxxxx",
                "msg5":"xxxxxxxxxxxxx",
                "msgl0":"xxxxxxxxxxxxx",
                "msgl1":"xxxxxxxxxxxxx"
        }
    }

Property Name |  Value |  Description  
---|---|---  
hulftToBrowserDefinitionId |  string |  Transfer Settings ID  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side that is registered in the Connection Settings  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
useReceiveFileName |  string |  Whether to specify the Receive file name displayed on the browser side  
receiveFileName |  string |  Receive file name displayed on the browser side  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine that is registered in the Connection Settings  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftRequestAcknowledgePort |  integer |  Request Acknowledge Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer/definition/hulft-to-browser");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{ \"hulftToBrowserDefinitionId\":\"xxxxxxxx\",\"description\":\"xxxxxxxx\",\"fileId\":\"TEST\",\"memo\":\"xxxxxxxx\","
                    + "\"browser\":{\"useReceiveFileName\":\"true\",\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\",\"receiveFileName\":\"xxxxxxxx\"},"
                    + "\"hulft\":{\"hulftRequestAcknowledgePort\":31000,\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\",\"hostName\":\"xxxxxxxx\","
                    + "\"msg0\":\"xxxxxxxx\",\"msg1\":\"xxxxxxxx\",\"msg2\":\"xxxxxxxx\",\"msg3\":\"xxxxxxxx\",\"msg4\":\"xxxxxxxx\",\"msg5\":\"xxxxxxxx\","
                    + "\"msgl0\":\"xxxxxxxx\",\"msgl1\":\"xxxxxxxx\"} }";
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/browser-transfer/definition/hulft-to-browser',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
        "hulftToBrowserDefinitionId":"xxxxxxxx","description":"xxxxxxxx","fileId":"TEST","memo":"xxxxxxxx",
        "browser":{"useReceiveFileName":"true","connectionId":"xxxxxxxx","agentId":"xxxxxxxx","receiveFileName":"xxxxxxxx"},
        "hulft":{
          "hulftRequestAcknowledgePort":31000,"connectionId":"xxxxxxxx","agentId":"xxxxxxxx","hostName":"xxxxxxxx",
          "msg0":"xxxxxxxx","msg1":"xxxxxxxx","msg2":"xxxxxxxx","msg3":"xxxxxxxx","msg4":"xxxxxxxx","msg5":"xxxxxxxx",
          "msgl0":"xxxxxxxx","msgl1":"xxxxxxxx"
        }
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 41

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetRegistrationSnding.htm

# 配信要求の場合

ブラウザ転送設定（配信要求）を新規登録します。

Request Interface

HTTP Request
    
    
    POST /browser-transfer/definition/browser-to-hulft

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserToHulftDefinitionId |  string |  true |  Transfer Settings ID (32 characters or less) |   
description |  string |  false |  Description of the transfer settings |  Blank  
fileId |  string |  true |  File ID of HULFT on the remote machine |   
memo |  string |  false |  Note for the settings |  Blank  
browser |  object |  true |  Browser Definition |   
connectionId |  string |  true |  Connection ID of the browser side that is registered in the Connection Settings |   
agentId |  string |  true |  ID to identify the browser (25 characters or less) |   
hulft |  object |  true |  Agent / HULFT Definition |   
connectionId |  string |  true |  Connection ID of the remote machine that is registered in the Connection Settings |   
agentId |  string |  true |  Agent ID of the remote machine (25 characters or less) |   
hostName |  string |  true |  Host information of HULFT on the remote machine |   
hulftReceivingPort |  integer |  false |  Receive Port No. of HULFT on the remote machine |  30000  
msg0 |  string |  false |  Message sent as 'msg0' to HULFT on the remote machine |  Blank  
msg1 |  string |  false |  Message sent as 'msg1' to HULFT on the remote machine |  Blank  
msg2 |  string |  false |  Message sent as 'msg2' to HULFT on the remote machine |  Blank  
msg3 |  string |  false |  Message sent as 'msg3' to HULFT on the remote machine |  Blank  
msg4 |  string |  false |  Message sent as 'msg4' to HULFT on the remote machine |  Blank  
msg5 |  string |  false |  Message sent as 'msg5' to HULFT on the remote machine |  Blank  
msgl0 |  string |  false |  Message sent as 'msgl0' to HULFT on the remote machine |  Blank  
msgl1 |  string |  false |  Message sent as 'msgl1' to HULFT on the remote machine |  Blank  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ配信要求」の「登録」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。

また、登録したリソースの URI をレスポンスヘッダ「Location」に格納します。
    
    
    {
        "browserToHulftDefinitionId":"browser1",
        "description":"xxxxxxxxxxxxx",
        "fileId":"FILEID1",
        "memo":"memo1",
        "browser":{
                "connectionId":"id1",
                "agentId":"agent1",
                "hostName":"HWC-BROWSER"
        },
        "hulft":{
                "connectionId":"id2",
                "agentId":"agent2",
                "hostName":"host",
                "hulftReceivingPort":30000,
                "msg0":"xxxxxxxxxxxxx",
                "msg1":"xxxxxxxxxxxxx",
                "msg2":"xxxxxxxxxxxxx",
                "msg3":"xxxxxxxxxxxxx",
                "msg4":"xxxxxxxxxxxxx",
                "msg5":"xxxxxxxxxxxxx",
                "msgl0":"xxxxxxxxxxxxx",
                "msgl1":"xxxxxxxxxxxxx"
        }
    }

Property Name |  Value |  Description  
---|---|---  
browserToHulftDefinitionId |  string |  Transfer Settings ID  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side that is registered in the Connection Settings  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine that is registered in the Connection Settings  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftReceivingPort |  integer |  Receive Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/browser-transfer/definition/browser-to-hulft");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{ \"browserToHulftDefinitionId\":\"xxxxxxxx\",\"description\":\"xxxxxxxx\",\"fileId\":\"TEST\",\"memo\":\"xxxxxxxx\","
                    + "\"browser\":{\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\"},"
                    + "\"hulft\":{\"hulftReceivingPort\":30000,\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\",\"hostName\":\"xxxxxxxx\","
                    + "\"msg0\":\"xxxxxxxx\",\"msg1\":\"xxxxxxxx\",\"msg2\":\"xxxxxxxx\",\"msg3\":\"xxxxxxxx\",\"msg4\":\"xxxxxxxx\",\"msg5\":\"xxxxxxxx\","
                    + "\"msgl0\":\"xxxxxxxx\",\"msgl1\":\"xxxxxxxx\"} }";
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/browser-transfer/definition/browser-to-hulft',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
        "browserToHulftDefinitionId":"xxxxxxxx", "description":"xxxxxxxx", "fileId":"TEST", "memo":"xxxxxxxx", 
        "browser":{"connectionId":"xxxxxxxx", "agentId":"xxxxxxxx"},
        "hulft":{
          "hulftReceivingPort":30000, "connectionId":"xxxxxxxx", "agentId":"xxxxxxxx", "hostName":"xxxxxxxx", 
          "msg0":"xxxxxxxx", "msg1":"xxxxxxxx", "msg2":"xxxxxxxx", "msg3":"xxxxxxxx", "msg4":"xxxxxxxx", "msg5":"xxxxxxxx", 
          "msgl0":"xxxxxxxx", "msgl1":"xxxxxxxx"
        } 
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 42

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetUpdate.htm

# 更新

ブラウザ転送設定を更新する場合の、HULFT-WebConnect Site API のインタフェースについて説明します 。


---


## ページ 43

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetUpdateSnd.htm

# 送信要求の場合

指定したブラウザ転送設定（送信要求）を更新します。

Request Interface

HTTP Request
    
    
    PUT /browser-transfer/definition/hulft-to-browser/{hulftToBrowserDefinitionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
hulftToBrowserDefinitionId |  string |  true |  Transfer Settings ID to be updated |   
Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
description |  string |  false |  Description of the transfer settings |  No update  
fileId |  string |  false |  File ID of HULFT on the remote machine |  No update  
memo |  string |  false |  Note for the settings |  No update  
browser |  object |  false |  Browser Definition |  No update  
connectionId |  string |  false |  Connection ID of the browser side |  No update  
agentId |  string |  false |  ID to identify the browser |  No update  
useReceiveFileName |  string |  false |  Whether to specify the Receive file name displayed on the browser side |  No update  
receiveFileName |  string |  false |  Receive file name displayed on the browser side (this field is mandatory if you specify the Receive file name) |  No update  
hulft |  object |  false |  Agent / HULFT Definition |  No update  
connectionId |  string |  false |  Connection ID of the remote machine |  No update  
agentId |  string |  false |  Agent ID of the remote machine |  No update  
hostName |  string |  false |  Host information of HULFT on the remote machine |  No update  
hulftRequestAcknowledgePort |  integer |  false |  Request Acknowledge Port No. of HULFT on the remote machine |  No update  
msg0 |  string |  false |  Message sent as 'msg0' to HULFT on the remote machine |  No update  
msg1 |  string |  false |  Message sent as 'msg1' to HULFT on the remote machine |  No update  
msg2 |  string |  false |  Message sent as 'msg2' to HULFT on the remote machine |  No update  
msg3 |  string |  false |  Message sent as 'msg3' to HULFT on the remote machine |  No update  
msg4 |  string |  false |  Message sent as 'msg4' to HULFT on the remote machine |  No update  
msg5 |  string |  false |  Message sent as 'msg5' to HULFT on the remote machine |  No update  
msgl0 |  string |  false |  Message sent as 'msgl0' to HULFT on the remote machine |  No update  
msgl1 |  string |  false |  Message sent as 'msgl1' to HULFT on the remote machine |  No update  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ送信要求」の「更新」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "hulftToBrowserDefinitionId":"browser1",
        "description":"xxxxxxxxxxxxx",
        "fileId":"FILEID1",
        "memo":"memo1",
        "browser":{
                "connectionId":"id1",
                "agentId":"agent1",
                "hostName":"HWC-BROWSER"
                "useReceiveFileName":"true",
                "receiveFileName":"file1"
        },
        "hulft":{
                "connectionId":"id2",
                "agentId":"agent2",
                "hostName":"host",
                "hulftRequestAcknowledgePort":31000,
                "msg0":"xxxxxxxxxxxxx",
                "msg1":"xxxxxxxxxxxxx",
                "msg2":"xxxxxxxxxxxxx",
                "msg3":"xxxxxxxxxxxxx",
                "msg4":"xxxxxxxxxxxxx",
                "msg5":"xxxxxxxxxxxxx",
                "msgl0":"xxxxxxxxxxxxx",
                "msgl1":"xxxxxxxxxxxxx"
        }
    }

Property Name |  Value |  Description  
---|---|---  
hulftToBrowserDefinitionId |  string |  Transfer Settings ID to be updated  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
useReceiveFileName |  string |  Whether to specify the Receive file name displayed on the browser side  
receiveFileName |  string |  Receive file name displayed on the browser side  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftRequestAcknowledgePort |  integer |  Request Acknowledge Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String hulftToBrowserDefinitionId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/browser-transfer/definition/hulft-to-browser/" + hulftToBrowserDefinitionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String putData = "{ \"description\":\"xxxxxxxx\",\"fileId\":\"TEST\",\"memo\":\"xxxxxxxx\","
                    + "\"browser\":{\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\",\"useReceiveFileName\":\"true\",\"receiveFileName\":\"xxxxxxxx\"},"
                    + "\"hulft\":{\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\",\"hostName\":\"xxxxxxxx\",\"hulftRequestAcknowledgePort\":31000,"
                    + "\"msg0\":\"xxxxxxxx\",\"msg1\":\"xxxxxxxx\",\"msg2\":\"xxxxxxxx\",\"msg3\":\"xxxxxxxx\",\"msg4\":\"xxxxxxxx\",\"msg5\":\"xxxxxxxx\","
                    + "\"msgl0\":\"xxxxxxxx\",\"msgl1\":\"xxxxxxxx\"} }";
            connection.setRequestMethod("PUT");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(putData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var hulftToBrowserDefinitionId = 'xxxxxxxx';
    $.ajax({
      type: 'PUT',
      url: host + '/api/v2/browser-transfer/definition/hulft-to-browser/' + hulftToBrowserDefinitionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
        "description":"xxxxxxxx","fileId":"TEST","memo":"xxxxxxxx",
        "browser":{"connectionId":"xxxxxxxx","agentId":"xxxxxxxx","useReceiveFileName":"true","receiveFileName":"xxxxxxxx"},
        "hulft":{
          "connectionId":"xxxxxxxx","agentId":"xxxxxxxx","hostName":"xxxxxxxx","hulftRequestAcknowledgePort":31000,
          "msg0":"xxxxxxxx","msg1":"xxxxxxxx","msg2":"xxxxxxxx","msg3":"xxxxxxxx","msg4":"xxxxxxxx","msg5":"xxxxxxxx",
          "msgl0":"xxxxxxxx","msgl1":"xxxxxxxx"
        }
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 44

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/BrowsTransSetUpdateSnding.htm

# 配信要求の場合

指定したブラウザ転送設定（配信要求）を更新します。

Request Interface

HTTP Request
    
    
    PUT /browser-transfer/definition/browser-to-hulft/{browserToHulftDefinitionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
browserToHulftDefinitionId |  string |  true |  Transfer Settings ID to be updated |   
Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
description |  string |  false |  Description of the transfer settings |  No update  
fileId |  string |  false |  File ID of HULFT on the remote machine |  No update  
memo |  string |  false |  Note for the settings |  No update  
browser |  object |  false |  Browser Definition |  No update  
connectionId |  string |  false |  Connection ID of the browser side |  No update  
agentId |  string |  false |  ID to identify the browser |  No update  
hulft |  object |  false |  Agent / HULFT Definition |  No update  
connectionId |  string |  false |  Connection ID of the remote machine |  No update  
agentId |  string |  false |  Agent ID of the remote machine |  No update  
hostName |  string |  false |  Host information of HULFT on the remote machine |  No update  
hulftReceivingPort |  integer |  false |  Receive Port No. of HULFT on the remote machine |  No update  
msg0 |  string |  false |  Message sent as 'msg0' to HULFT on the remote machine |  No update  
msg1 |  string |  false |  Message sent as 'msg1' to HULFT on the remote machine |  No update  
msg2 |  string |  false |  Message sent as 'msg2' to HULFT on the remote machine |  No update  
msg3 |  string |  false |  Message sent as 'msg3' to HULFT on the remote machine |  No update  
msg4 |  string |  false |  Message sent as 'msg4' to HULFT on the remote machine |  No update  
msg5 |  string |  false |  Message sent as 'msg5' to HULFT on the remote machine |  No update  
msgl0 |  string |  false |  Message sent as 'msgl0' to HULFT on the remote machine |  No update  
msgl1 |  string |  false |  Message sent as 'msgl1' to HULFT on the remote machine |  No update  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「ブラウザ送信要求」の「登録」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "browserToHulftDefinitionId":"browser1",
        "description":"xxxxxxxxxxxxx",
        "fileId":"FILEID1",
        "memo":"memo1",
        "browser":{
                "connectionId":"id1",
                "agentId":"agent1",
                "hostName":"HWC-BROWSER"
        },
        "hulft":{
                "connectionId":"id2",
                "agentId":"agent2",
                "hostName":"host",
                "hulftReceivingPort":30000,
                "msg0":"xxxxxxxxxxxxx",
                "msg1":"xxxxxxxxxxxxx",
                "msg2":"xxxxxxxxxxxxx",
                "msg3":"xxxxxxxxxxxxx",
                "msg4":"xxxxxxxxxxxxx",
                "msg5":"xxxxxxxxxxxxx",
                "msgl0":"xxxxxxxxxxxxx",
                "msgl1":"xxxxxxxxxxxxx"
        }
    }

Property Name |  Value |  Description  
---|---|---  
browserToHulftDefinitionId |  string |  Transfer Settings ID to be updated  
description |  string |  Description of the transfer settings  
fileId |  string |  File ID of HULFT on the remote machine  
memo |  string |  Note for the settings  
browser |  object |  Browser Definition  
connectionId |  string |  Connection ID of the browser side  
agentId |  string |  ID to identify the browser  
hostName |  string |  Host information of the browser side (fixed value)  
hulft |  object |  Agent / HULFT Definition  
connectionId |  string |  Connection ID of the remote machine  
agentId |  string |  Agent ID of the remote machine  
hostName |  string |  Host information of HULFT on the remote machine  
hulftReceivingPort |  integer |  Receive Port No. of HULFT on the remote machine  
msg0 |  string |  Message sent as 'msg0' to HULFT on the remote machine  
msg1 |  string |  Message sent as 'msg1' to HULFT on the remote machine  
msg2 |  string |  Message sent as 'msg2' to HULFT on the remote machine  
msg3 |  string |  Message sent as 'msg3' to HULFT on the remote machine  
msg4 |  string |  Message sent as 'msg4' to HULFT on the remote machine  
msg5 |  string |  Message sent as 'msg5' to HULFT on the remote machine  
msgl0 |  string |  Message sent as 'msgl0' to HULFT on the remote machine  
msgl1 |  string |  Message sent as 'msgl1' to HULFT on the remote machine  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String browserToHulftDefinitionId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/browser-transfer/definition/browser-to-hulft/" + browserToHulftDefinitionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String putData = "{ \"description\":\"xxxxxxxx\",\"fileId\":\"TEST\",\"memo\":\"xxxxxxxx\","
                    + "\"browser\":{\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\"},"
                    + "\"hulft\":{\"connectionId\":\"xxxxxxxx\",\"agentId\":\"xxxxxxxx\",\"hostName\":\"xxxxxxxx\",\"hulftReceivingPort\":30000,"
                    + "\"msg0\":\"xxxxxxxx\",\"msg1\":\"xxxxxxxx\",\"msg2\":\"xxxxxxxx\",\"msg3\":\"xxxxxxxx\",\"msg4\":\"xxxxxxxx\",\"msg5\":\"xxxxxxxx\","
                    + "\"msgl0\":\"xxxxxxxx\",\"msgl1\":\"xxxxxxxx\"} }";
            connection.setRequestMethod("PUT");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(putData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var browserToHulftDefinitionId = 'xxxxxxxx';
    $.ajax({
      type: 'PUT',
      url: host + '/api/v2/browser-transfer/definition/browser-to-hulft/' + browserToHulftDefinitionId ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
        "description":"xxxxxxxx","fileId":"TEST","memo":"xxxxxxxx",
        "browser":{"connectionId":"xxxxxxxx","agentId":"xxxxxxxx"},
        "hulft":{
          "connectionId":"xxxxxxxx","agentId":"xxxxxxxx","hostName":"xxxxxxxx","hulftReceivingPort":30000,
          "msg0":"xxxxxxxx","msg1":"xxxxxxxx","msg2":"xxxxxxxx","msg3":"xxxxxxxx","msg4":"xxxxxxxx","msg5":"xxxxxxxx",
          "msgl0":"xxxxxxxx","msgl1":"xxxxxxxx"
        }
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 45

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ConnectSet.htm

# 接続設定

HULFT-WebConnect の接続設定を取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 46

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ConnectSetAllGet.htm

# 全件取得

接続設定を全件取得します。

クエリパラメータを指定することで、検索条件に該当する接続設定を取得することもできます。

Request Interface

HTTP Request
    
    
    GET /connections/definition

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":2,
        "fetchSize":2
        "startIndex":0,
        "maxResults":30,
        "limit":{"connectionIdLimit":10},
        "definitions":[
            {
                "connectionId":"id1",
                "connectableClientType":["hulft", "data_transfer_api"],
                "ipFilterGroupName":"group1",
                "memo":"memo1"
            },
            {
                "connectionId":"id2",
                "connectableClientType":["data_transfer_api"],
                "memo":"memo2"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
limit |  object |  Object of connectionIdLimit  
connectionIdLimit |  integer |  The maximum number of Connection IDs  
definitions |  array |  Array of the elements described below  
connectionId |  string |  Connection ID  
connectableClientType |  array |  Client type that can be used with Connection ID  
ipFilterGroupName |  string |  IP Filter Group Name that is linked to the account. This parameter contains null in this response if an IP Filter Group Name is not set to the Connection ID  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/connections/definition");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/connections/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 47

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ConnectSetConnectId.htm

# コネクション ID を指定して取得

コネクション ID を指定して接続設定を取得します。

Request Interface

HTTP Request
    
    
    GET /connections/definition/{connectionId}

Parameter

Path Parameter |  Value |  Required |  Description  
---|---|---|---  
ConnectionId |  string |  true |  Connection ID  
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "connectionId":"id1",
        "connectableClientType":["hulft"],
        "ipFilterGroupName":"group1",
        "memo":"memo1"
    }

Property Name |  Value |  Description  
---|---|---  
connectionId |  string |  Connection ID  
connectableClientType |  array |  Client type that can be used with Connection ID  
ipFilterGroupName |  string |  IP Filter Group Name that is linked to the account. This parameter contains null in this response if an IP Filter Group Name is not set to the Connection ID  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String connectionId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/connections/definition/" + connectionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/connections/definition/' + connectionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 48

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ConnectSetDelete.htm

# 削除

指定した接続設定を削除します。

**注意**

コネクション ID が削除された場合、関連する中継許可設定およびブラウザ転送設定も同時に削除されますのでご注意ください。

Request Interface

HTTP Request
    
    
    DELETE /connections/definition/{connectionId}

Parameter

Path Parameter |  Value |  Required |  Description  
---|---|---|---  
connectionId |  string |  true |  Connection ID to be deleted  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続設定」の「削除」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String connectionId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/connections/definition/" + connectionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); // The response does not contain the response body. 
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/connections/definition/' + connectionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 49

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ConnectSetRegistration.htm

# 登録

接続設定を新規登録します。

Request Interface

HTTP Request
    
    
    POST /connections/definition

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  New Connection ID you intend to register (16 characters or less) |   
passwd |  string |  true |  New Connection Password you intend to register (8 characters or more and 256 characters or less) |   
connectableClientType |  array |  true |  Connectable client type you intend to register (Specifiable value: hulft, data_transfer_api, hwc_browser, dclient) |   
ipFilterGroupName(*) |  string |  false |  IP Filter Group Name that is linked to the account (32 characters or less. Use alphanumeric characters and symbols (. -). You cannot specify only '.' or '..' for this value) |  (You can omit this parameter itself)  
memo |  string |  false |  Note for the settings (256 characters or less) |  Blank  
  
*: 「connectableClientType」に "hwc_browser" だけを指定する場合、「ipFilterGroupName」は設定できません。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続設定」の「登録」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。

また、登録したリソースの URI をレスポンスヘッダ「Location」に格納します。
    
    
    {
        "connectionId":"id1",
        "connectableClientType":["hulft", "data_transfer_api"],
        "ipFilterGroupName":"group1",
        "memo":"memo1"
    }

Property Name |  Value |  Description  
---|---|---  
connectionId |  string |  New Connection ID you intend to register  
connectableClientType |  array |  Connectable client type you intend to register  
ipFilterGroupName |  string |  IP Filter Group Name that is linked to the account. This parameter contains null in this response if an IP Filter Group Name is not set to the Connection ID  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/connections/definition");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{\"connectionId\":\"xxxxxxxx\", \"passwd\":\"xxxxxxxx\", \"connectableClientType\":[\"hulft\"], \"ipFilterGroupName\":\"group1\", \"memo\":\"xxxxxxxx\"}";
    
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/connections/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({connectionId: 'xxxxxxxxx', passwd: 'xxxxxxxx', connectableClientType: ["hulft"], ipFilterGroupName: 'group1', memo: 'xxxxxxx'})
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 50

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ConnectSetUpdate.htm

# 更新

指定した接続設定を更新します。

Request Interface

HTTP Request
    
    
    PUT /connections/definition/{connectionId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID to be updated |   
Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
passwd |  string |  false |  Connection Password (8 characters or more and 256 characters or less) |  No update  
connectableClientType |  array |  false |  Connectable client type (Specifiable value: hulft, data_transfer_api, hwc_browser, dclient) |  No update  
ipFilterGroupName(*1)(*2) |  string |  false |  IP Filter Group Name that is linked to the account (32 characters or less. Use alphanumeric characters and symbols (. -). You cannot specify only '.' or '..' for this value) When you release the IP Filter Group being specified, specify null for this parameter. |  No update  
memo |  string |  false |  Note for the settings (256 characters or less) |  No update  
  
*1: 「connectableClientType」に "hwc_browser" だけが指定されている場合、「ipFilterGroupName」は設定できません。

*2: 「ipFilterGroupName」がすでに設定されている場合に、「connectableClientType」の設定値を "hwc_browser" だけに変更すると、「ipFilterGroupName」は無効になります。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「接続設定」の「更新」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "connectionId":"id1",
        "connectableClientType":["hulft"],
        "ipFilterGroupName":"group1",
        "memo":"memo1"
    }

Property Name |  Value |  Description  
---|---|---  
connectionId |  string |  Connection ID to be updated  
connectableClientType |  array |  Connectable client type  
ipFilterGroupName |  string |  IP Filter Group Name that is linked to the account. This parameter contains null in this response if an IP Filter Group Name is not set to the Connection ID  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String connectionId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/connections/definition/" + connectionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String putData = "{\"passwd\":\"xxxxxxxx\", \"connectableClientType\":[\"hulft\"], \"ipFilterGroupName\":\"group1\", \"memo\":\"xxxxxxx\"}";
    
            connection.setRequestMethod("PUT");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(putData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    $.ajax({
      type: 'PUT',
      url: host + '/api/v2/connections/definition/' + connectionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({passwd: 'xxxxxxxx', connectableClientType: ["hulft"], ipFilterGroupName: 'group1', memo: 'xxxxxxx'})
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 51

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClienRegistration.htm

# 登録

D-Client設定を新規登録します。

Request Interface

HTTP Request
    
    
    POST /dclient/definition

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
dclientId |  string |  true |  D-Client ID |  -  
connectionId | string |  true | Connection ID | -  
accountId |  string |  false |  Account ID (UUID of the account) |  Blank  
memo |  string |  false |  Note (Character string) |  Blank  
useable |  boolean |  false |  Availability (true/false) |  false  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"dclientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"connectionId": "xxxxxxxxxxxxxxxx",
    		"account":
    		{
    			"id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"mailAddress":"sample@example.com"
    		},
    	"memo": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"useable": true,
    	"clientVersion": "1,0,0",
    	"connectionStatus": "online"
    }

Property Name |  Value |  Description  
---|---|---  
id |  string |  D-Client UUID (UUID)  
dclientId |  string |  D-Client ID   
connectionId | string | Connection ID  
account |  object |  Accounts that is assigned to the D-Client settings.  
memo  | string | Note (Character string)  
useable | boolean | Availability (true/false)  
clientVersion | string | Client version (Version information in x.y.z. format)  
connectionStatus | string | Connection status (online/offline)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/dclient/definition");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{\"dclientId\": \"sample\","
                        + "\"connectionId\": \"connectionId\","
                        + "\"accountId\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\","
                        + "\"memo\": \"memo\","
                        + "\"useable\": true}";
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = 
    	     new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
            try (BufferedReader reader = 
    	     new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/dclient/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({
                "dclientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "connectionId": "connectionId",
                "accountId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "memo": "memo",
                "useable": true
      })
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 52

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClient1Get.htm

# 1 件取得

D-Client設定を 1 件取得します。

Request Interface

HTTP Request
    
    
    GET /dclient/definition/{dclientUuid}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
dclientUuid |  string |  true |  ID of the D-Client to get.(32 alphanumeric character). |  -  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"dclientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"connectionId": "xxxxxxxxxxxxxxxx",
    		"account":
    		{
    			"id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"mailAddress":"sample@example.com"
    		},
    	"memo": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"useable": true,
    	"clientVersion": "1,0,0",
    	"connectionStatus": "online"
    }

Property Name |  Value |  Description  
---|---|---  
id |  string |  D-Client UUID (UUID)  
dclientId |  string |  D-Client ID   
connectionId | string | Connection ID  
account | object | Accounts that is assigned to the D-Client settings.  
memo  | string | Note (Character string)  
useable | boolean | Availability (true/false)  
clientVersion | string | Client version (Version information in x.y.z. format)  
connectionStatus | string | Connection status (online/offline)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String dclientUuid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/dclient/definition/" + dclientUuid);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = 
    	     new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var dclientUuid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/dclient/definition/' + dclientUuid,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 53

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClientDelete.htm

# 削除

D-Client設定を削除します。

Request Interface

HTTP Request
    
    
    DELETE /dclient/definition/{dclientUuid}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
dclientUuid |  string |  true |  ID of the D-Client to delete.(32 alphanumeric character) |  -  
  
Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String dclientUuid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/dclient/definition/" + dclientUuid);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); 
    			// The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var dclientUuid  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/dclient/definition/' + dclientUuid ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 54

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClientListGet.htm

# リスト取得

D-Client設定のリストを取得します。

Request Interface

HTTP Request
    
    
    GET /dclient/definition

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"totalSize": 10,
    	"fetchSize": 10,
    	"startIndex": 0,
    	"maxResults": 30,
    	"limit": 10000,
    	"dclients": [
    		{
    			"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"dclientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"connectionId": "xxxxxxxxxxxxxxxx",
    			"account":
    				{
    				"id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    				"mailAddress":"sample@example.com\"
    				},
    			"memo": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"useable": true,
    			"clientVersion": "1,0,0",
    			"connectionStatus": "online"
    			},
    		{
    			"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"dclientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"connectionId": "xxxxxxxxxxxxxxxx",
    			"account":
    				{
    				"id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    				"mailAddress":"sample@example.com\"
    				},
    			"memo": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"useable": true,
    			"clientVersion": "1,0,0",
    			"connectionStatus": "online"
    		},
    	]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data.  
fetchSize |  integer |  The number of the obtained data.  
startIndex |  integer |  Index of the first row of a data to retrieve.  
maxResults |  integer |  The maximum number of indexes included in a response data.  
limit |  integer |  The maximum number of D-Client settings that can be registered. (Fixed to 10000)  
dclients | array | Object array of D-Client Transfer Settings  
id |  string |  D-Client UUID (UUID)  
dclientId |  string |  D-Client ID   
connectionId | string | Connection ID  
account | object | Accounts that is assigned to the D-Client settings.  
memo  | string | Note (Character string)  
useable | boolean | Availability (true/false)  
clientVersion | string | Client version (Version information in x.y.z. format)  
connectionStatus | string | Connection status (online/offline)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    	String host = "https://www.webconnect.hulft.com";
    	String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	try {
    	   URL url = new URL(host + "/api/v2/dclient/definition");
    	   HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    	   connection.setRequestMethod("GET");
    	   connection.setRequestProperty("Authorization", "Bearer " + apiKey);
    	   try (BufferedReader reader = 
    		new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
    		String line;
    		while((line = reader.readLine()) != null) {
    		System.out.println(line);
    		}
    	   }
    	} catch (IOException ex) {
    	// error
    	}
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/dclient/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 55

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClientMailRequest.htm

# D-Client利用案内送信依頼

アカウントに登録されているメールアドレスに対してD-Client利用案内送信依頼を行います。

Request Interface

HTTP Request
    
    
    POST /dclient/user-guide/mail-request/{dclientUuid}

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
dclientUuid |  string |  true |  ID to specify the D-Client.(32 alphanumeric character) |  -  
  
Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String dclientUuid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/dclient/user-guide/mail-request/" + dclientUuid);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            System.out.println(connection.getResponseMessage()); 
    			// The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var dclientUuid  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/dclient/user-guide/mail-request/' + dclientUuid,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 56

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClientSet.htm

# D-Client設定

HULFT-WebConnect のD-Client設定を取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 57

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/DClienUpdate.htm

# 更新

D-Client設定を更新します。

Request Interface

HTTP Request
    
    
    PUT /dclient/definition/{dclientUuid}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
dclientUuid |  string |  true |  ID of the D-Client to update.(32 alphanumeric character) |  -  
Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  false |  Connection ID |  Existing data  
accountId |  string |  false |  Account ID (UUID of the account) |  Existing data  
memo |  string |  false |  Note (Character string) |  Existing data  
useable |  boolean |  false |  Availability (true/false) |  Existing data  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"dclientId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"connectionId": "xxxxxxxxxxxxxxxx",
    		"account":
    		{
    			"id":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    			"mailAddress":"sample@example.com"
    		},
    	"memo": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"useable": true,
    	"clientVersion": "1,0,0",
    	"connectionStatus": "online"
    }

Property Name |  Value |  Description  
---|---|---  
id |  string |  D-Client UUID (UUID)  
dclientId |  string |  D-Client ID   
connectionId | string | Connection ID  
account |  object |  Accounts that is assigned to the D-Client settings.  
memo  | string | Note (Character string)  
useable | boolean | Availability (true/false)  
clientVersion | string | Client version (Version information in x.y.z. format)  
connectionStatus | string | Connection status (online/offline)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String dclientUuid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/dclient/definition/" + dclientUuid);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String putData = "{\"connectionId\": \"connectionId\","
                        + "\"accountId\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\","
                        + "\"memo\": \"memo\","
                        + "\"useable\": true}";
            connection.setRequestMethod("PUT");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
            try (BufferedWriter writer = 
    	    new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(putData);
               }
            try (BufferedReader reader = 
    	     new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var dclientUuid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
        type: 'PUT',
        url: host + '/api/v2/dclient/definition/' + dclientUuid,
        headers: {
          Authorization: 'Bearer ' + apiKey
        },
        contentType: 'application/json',
        data: JSON.stringify({
                  "connectionId": "connectionId",
                  "accountId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                  "memo": "memo",
                  "useable": true
              })
      }).done(function(data, status, xhr) {
        console.log(data);
      }).fail(function(data, status, xhr) {
        console.log(data);
      });


---


## ページ 58

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/IPFilterGroup.htm

# IPフィルタグループ

HULFT-WebConnect のIPフィルタグループを取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 59

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/IPFilterGroup1Get.htm

# 1 件取得

IPフィルタグループを1 件取得します 。

Request Interface

HTTP Request
    
    
    GET /ip-filter/group/{ipFilterGroupName}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
ipFilterGroupName |  string |  true |  IP filter group name |  -  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"description": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"allowlist": [
    		"xxx.xxx.xxx.xxx",
    		"xxx.xxx.xxx.xxx"
    	]
    }
    		

Property Name |  Value |  Description  
---|---|---  
ipFilterGroupName |  string |  IP filter group name  
description |  string |  Description of IP filter group  
allowlist |  array |  Allowlist of IP addresses  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
            String host = "https://www.webconnect.hulft.com";
            String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
            String ipFilterGroupName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
            try {
                    URL url = new URL(host + "/api/v2/ip-filter/group/" + ipFilterGroupName);
                    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET");
                    connection.setRequestProperty("Authorization", "Bearer " + apiKey);
                    try (BufferedReader reader = 
    		   new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                            String line;
                            while((line = reader.readLine()) != null) {
                                    System.out.println(line);
                            }
                    }
            } catch (IOException ex) {
                    // error
            }
    }
                    
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var ipFilterGroupName = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/ip-filter/group/' + ipFilterGroupName,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 60

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/IPFilterGroupDelete.htm

# 削除

IPフィルタグループを削除します。

Request Interface

HTTP Request
    
    
    DELETE /ip-filter/group/{ipFilterGroupName}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
ipFilterGroupName |  string |  true |  IP filter group name |  -  
  
Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

リクエストが正常に処理されなかった場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"code": "xxxxxxx",
    	"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"connectionIdList":[
    		"connectionId1",
    		"connectionId2"
    	],
    	"secondaryAccountList":[
    		"connectionId1",
    		"connectionId2"
    	]
    }
    		

Property Name |  Value |  Description  
---|---|---  
code |  string |  Error code  
message |  string |  Error message  
connectionIdList |  array |  List of connection IDs that are using the ipFilterGroupName to be deleted  
secondaryAccountList | array | List of secondary account that are using the ipFilterGroupName to be deleted  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    	String host = "https://www.webconnect.hulft.com";
    	String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	String ipFilterGroupName= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	try {
    		URL url = new URL(host + "/api/v2/ip-filter/group/" + ipFilterGroupName);
    		HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    		connection.setRequestMethod("DELETE");
    		connection.setRequestProperty("Authorization", "Bearer " + apiKey);
    		System.out.println(connection.getResponseMessage());
    			 // The response does not contain the response body.
    	} catch (IOException ex) {
    	// error
    	}
    }
    
    
    
    //load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var ipFilterGroupName = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/ip-filter/group/' + ipFilterGroupName ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 61

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/IPFilterGroupListGet.htm

# リスト取得

IPフィルタグループのリストを取得します。

Request Interface

HTTP Request
    
    
    GET /ip-filter/group

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"totalSize": 10,
    	"fetchSize": 10,
    	"startIndex": 0,
    	"maxResults": 30,
    	"ipFilter": [
    		{
    		"ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxx",
    		"description": "xxxxxxxxxxxxxxxxxxxxxxx",
    		"allowlist": [
    		  "xxx.xxx.xxx.xxx",
    		  "xxx.xxx.xxx.xxx"
    		  ]
    		 }
    		 {
    		"ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxx",
    		"description": "xxxxxxxxxxxxxxxxxxxxxxx",
    		"allowlist": [
    		  "xxx.xxx.xxx.xxx",
    		  ]
    		 }
    		]
    	   }
        	

Property Name |  Value |  Description  
---|---|---  
ipFilterGroupName |  string |  IP filter group name  
description |  string |  Description of IP filter group  
allowlist |  array |  Allowlist of IP addresses  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/ip-filter/group");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = 
    	  new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/ip-filter/group',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });
    


---


## ページ 62

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/IPFilterGroupRegistration.htm

# 登録

IPフィルタグループを登録します。

Request Interface

HTTP Request
    
    
    POST /ip-filter/group

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
ipFilterGroupName | string | true |  IP filter group name. 32 characters or less. Use alphanumeric characters and symbols (only "-" and "." allowed). You cannot specify "." or ".." by itself. Duplicate specifications in the same account are not allowed. Case-sensitive. | -  
description |  string |  false |  Description of IP filter group. 256 characters or less. |  Blank  
allowlist | string | true |  Allowlist of IP addresses. Array of strings. Use numeric characters and certain symbols (. /) only. Empty arrays are not allowed. | -  
  
IPフィルタグループの登録数は、契約アカウントに対して100が上限です。

IPアドレスの登録数は、IPフィルタグループに対して100が上限です。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"description": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"allowlist": [
    		"xxx.xxx.xxx.xxx",
    		"xxx.xxx.xxx.xxx"
    	]
    }
    		

Property Name |  Value |  Description  
---|---|---  
ipFilterGroupName |  string |  IP filter group name  
description |  string |  Description of IP filter group  
allowlist |  array |  Allowlist of IP addresses  
  
リクエストが正常に処理されなかった場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"code": "xxxxxxx",
    	"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"ipAddressError": [
    		{
    		"code": "xxxxxxx",
    		"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"index": 0
    		},
    		{
    		"code": "xxxxxxx",
    		"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"index": 1
    		}
    	]
    }
    		

Property Name |  Value |  Description  
---|---|---  
code |  string |  Error code  
message |  string |  Error message  
ipAddressError |  array |  IP address with an error  
code | string | Error code for the input IP address  
message | string | Error message for the input IP address  
index | integer | Array element number for the input IP address (zero-based)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    	String host = "https://www.webconnect.hulft.com";
    	String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    	try {
    	URL url = new URL(host + "/api/v2/ip-filter/group");
    	HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    	String postData = "{\"ipFilterGroupName\": \"group1\","
    		 +  "\"allowlist\": [\"192.0.2.0/24\"],"
    		 +  "\"description\": \"description1\""
    		 +  "}";
    	connection.setRequestMethod("POST");
    	connection.setDoOutput(true);
    	connection.setDoInput(true);
    	connection.setRequestProperty("Authorization", "Bearer " + apiKey);
    	connection.setRequestProperty("Content-Type", "application/json");
    	connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
    	try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
    		writer.write(postData);
    		}
    	try (BufferedReader reader = 
    		new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
    	String line;
    	while ((line = reader.readLine()) != null) {
    		System.out.println(line);
    		}
    	}
    	} catch (IOException ex) {
    	// error
    	}
    }
    
    
    // load jquery
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
    	type: 'POST',
    	url: host + '/api/v2/ip-filter/group',
    	headers: {
    			Authorization: 'Bearer ' + apiKey
    	},
    	contentType: 'application/json',
    	data: JSON.stringify({
    		"ipFilterGroupName": "group1",
    		"allowlist": ["192.0.2.0/24"],
    		"description": "description1" 
    	})
    }).done(function(data, status, xhr) {
    	console.log(data);
    }).fail(function(data, status, xhr) {
    	console.log(data);
    });
    			


---


## ページ 63

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/IPFilterGroupUpdate.htm

# 更新

IPフィルタグループを更新します。

Request Interface

HTTP Request
    
    
    PUT /ip-filter/group/{ipFilterGroupName}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
ipFilterGroupName |  string |  true |  IP filter group name |  -  
Request Parameter |  Value | Required |  Description |  Default Value  
---|---|---|---|---  
description | string | false |  Description of IP filter group. 256 characters or less. | No update  
allowlist | array | false |  Allowlist of IP addresses. Array of strings. Use numeric characters and certain symbols (. /) only. Empty arrays are not allowed. | No update  
  
Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"description": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"allowlist": [
    		"xxx.xxx.xxx.xxx",
    		"xxx.xxx.xxx.xxx"
    	]
    }
    		

Property Name |  Value |  Description  
---|---|---  
ipFilterGroupName |  string |  IP filter group name  
description |  string |  Description of IP filter group  
allowlist |  array |  Allowlist of IP addresses  
  
リクエストが正常に処理されなかった場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
    	"code": "xxxxxxx",
    	"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    	"ipAddressError": [
    		{
    		"code": "xxxxxxx",
    		"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"index": 0
    		},
    		{
    		"code": "xxxxxxx",
    		"message": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    		"index": 1
    		}
    	]
    }
    		

Property Name |  Value |  Description  
---|---|---  
code |  string |  Error code  
message |  string |  Error message  
ipAddressError |  array |  IP address with an error  
code | string | Error code for the input IP address  
message | string | Error message for the input IP address  
index | integer | Array element number for the input IP address (zero-based)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
    String host = "https://www.webconnect.hulft.com";
    String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    String ipFilterGroupName = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
    try {
      URL url = new URL(host + "/api/v2/ip-filter/group/" + ipFilterGroupName);
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();
      String putData = "{\"allowlist\": [\"192.0.2.0/24\"],"
         + "\"description\": \"description1\""
         + "}";
      connection.setRequestMethod("PUT");
      connection.setDoOutput(true);
      connection.setDoInput(true);
      connection.setRequestProperty("Authorization", "Bearer " + apiKey);
      connection.setRequestProperty("Content-Type", "application/json");
      connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
      try (BufferedWriter writer = 
    		new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
        writer.write(putData);
      }
      try (BufferedReader reader =
    		 new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
        String line;
         while ((line = reader.readLine()) != null) {
            System.out.println(line);
          }
        }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var ipFilterGroupName = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
    	type: 'PUT',
    	url: host + '/api/v2/ip-filter/group/' + ipFilterGroupName,
    	headers: {
    		Authorization: 'Bearer ' + apiKey
    	},
    	contentType: 'application/json',
    	data: JSON.stringify({
    		"allowlist": ["192.0.2.0/24"],
    		"description": "description1"
    	})
    }).done(function(data, status, xhr) {
     console.log(data);
    }).fail(function(data, status, xhr) {
     console.log(data);
    });


---


## ページ 64

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSet.htm

# 中継許可設定

HULFT-WebConnect の中継許可設定を取得、登録、更新、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 65

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSet1Get.htm

# 1 件取得

コネクション ID 、相手先コネクション ID および転送方向を指定して中継許可設定を 1 件取得します。

Request Interface

HTTP Request
    
    
    GET /relay/permission/{connectionId}/{remoteConnectionId}/{direction}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID |   
remoteConnectionId |  string |  true |  Connection ID of the remote machine |   
direction |  string |  true |  Transfer direction to enable the relay transfer (send | receive) |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":1,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":30,
        "permission":[
            {
                "connectionId":"id1",
                "remoteConnectionId":"id2",
                "direction":"send",
                "enabled":"false",
                "memo":"memo1"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
permission |  array |  Array of the elements described below  
connectionId |  string |  Connection ID  
remoteConnectionId |  string |  Connection ID of the remote machine  
direction |  string |  Transfer direction to enable the relay transfer  
enabled |  string |  Whether Relay Authorization Settings are enabled or not  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String connectionId = "xxxxxxxx";
        String remoteConnectionId = "xxxxxxxx";
        String direction = "send";
        try {
            URL url = new URL(host + "/api/v2/relay/permission/" + connectionId + "/" + remoteConnectionId + "/" + direction);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    var remoteConnectionId = 'xxxxxxxx';
    var direction = 'send';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/permission/' + connectionId + '/' + remoteConnectionId + '/' + direction,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 66

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSetAllGet.htm

# 全件取得

中継許可設定を全件取得します。

クエリパラメータを指定することで、検索条件に該当する中継許可設定を取得することもできます。

Request Interface

HTTP Request
    
    
    GET /relay/permission

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":1,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":30,
        "permission":[
            {
                "connectionId":"id1",
                "remoteConnectionId":"id2",
                "direction":"send",
                "enabled":"false",
                "memo":"memo1"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
permission |  array |  Array of the elements described below  
connectionId |  string |  Connection ID  
remoteConnectionId |  string |  Connection ID of the remote machine  
direction |  string |  Transfer direction to enable the relay transfer  
enabled |  string |  Whether Relay Authorization Settings are enabled or not  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/relay/permission");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/permission',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 67

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSetConnectId.htm

# コネクション ID を指定して取得

コネクション ID を指定して中継許可設定を取得します。

Request Interface

HTTP Request
    
    
    GET /relay/permission/{connectionId}

Parameter

Query Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID |   
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":1,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":30,
        "permission":[
            {
                "connectionId":"id1",
                "remoteConnectionId":"id2",
                "direction":"send",
                "enabled":"false",
                "memo":"memo1"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
permission |  array |  Array of the elements described below  
connectionId |  string |  Connection ID  
remoteConnectionId |  string |  Connection ID of the remote machine  
direction |  string |  Transfer direction to enable the relay transfer  
enabled |  string |  Whether Relay Authorization Settings are enabled or not  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String connectionId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/relay/permission/" + connectionId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/permission/' + connectionId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 68

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSetDelete.htm

# 削除

指定した中継許可設定を削除します。

Request Interface

HTTP Request
    
    
    DELETE /relay/permission/{connectionId}/{remoteConnectionId}/{direction}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID of the local machine to be deleted |   
remoteConnectionId |  string |  true |  Connection ID of the remote machine to be deleted |   
direction |  string |  true |  Transfer direction to be deleted |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「削除」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String connectionId = "xxxxxxxx";
        String remoteConnectionId = "xxxxxxxx";
        String direction = "send";
        try {
            URL url = new URL(host + "/api/v2/relay/permission/" + connectionId + "/" + remoteConnectionId + "/" + direction);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); // The response does not contain the response body. 
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    var remoteConnectionId = 'xxxxxxxx';
    var direction = 'send';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/relay/permission/' + connectionId + '/' + remoteConnectionId + '/' + direction,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 69

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSetRegistration.htm

# 登録

中継許可設定を新規登録します。

Request Interface

HTTP Request
    
    
    POST /relay/permission

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID of the local machine registered in Connection Settings |   
remoteConnectionId |  string |  true |  Connection ID of the remote machine for Relay Authorization Settings |   
direction |  string |  true |  Transfer direction to enable the relay transfer (send | receive) |   
enabled |  string |  false |  Whether to enable Relay Authorization Settings or not |  false  
memo |  string |  false |  Note for the settings |  Blank  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「登録」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。

また、登録したリソースの URI をレスポンスヘッダ「Location」に格納します。
    
    
    {
        "connectionId":"id1",
        "remoteConnectionId":"id2",
        "direction":"send",
        "enabled":"true",
        "memo":"memo1"
    }

Property Name |  Value |  Description  
---|---|---  
connectionId |  string |  Connection ID of the local machine registered in Connection Settings  
remoteConnectionId |  string |  Connection ID of the remote machine for Relay Authorization Settings  
direction |  string |  Transfer direction to enable the relay transfer  
enabled |  string |  Whether to enable Relay Authorization Settings or not  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/relay/permission");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String postData = "{\"connectionId\":\"xxxxxxxx\", \"remoteConnectionId\":\"xxxxxxxx\", \"direction\":\"send\", \"enabled\":\"true\", \"memo\":\"xxxxxxxxx\"}";
    
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(postData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'POST',
      url: host + '/api/v2/relay/permission',
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({connectionId: 'xxxxxxxxx', remoteConnectionId: 'xxxxxxxx', direction: 'send', enabled: 'true', memo: 'xxxxxxx'})
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 70

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSetTransfer.htm

# コネクション ID および転送方向を指定して取得

コネクション ID および転送方向を指定して中継許可設定を取得します。

Request Interface

HTTP Request
    
    
    GET /relay/permission/{connectionId}/{direction}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID |   
direction |  string |  true |  Transfer direction to enable the relay transfer (send | receive) |   
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":1,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":30,
        "permission":[
            {
                "connectionId":"id1",
                "remoteConnectionId":"id2",
                "direction":"send",
                "enabled":"false",
                "memo":"memo1"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
permission |  array |  Array of the elements described below  
connectionId |  string |  Connection ID  
remoteConnectionId |  string |  Connection ID of the remote machine  
direction |  string |  Transfer direction to enable the relay transfer  
enabled |  string |  Whether Relay Authorization Settings are enabled or not  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String connectionId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/relay/permission/" + connectionId + "/send");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/permission/' + connectionId + '/send',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 71

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayAuthoSetUpdate.htm

# 更新

指定した中継許可設定を更新します。

Request Interface

HTTP Request
    
    
    PUT /relay/permission/{connectionId}/{remoteConnectionId}/{direction}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
connectionId |  string |  true |  Connection ID of the local machine to be updated |   
remoteConnectionId |  string |  true |  Connection ID of the remote machine to be updated |   
direction |  string |  true |  Transfer direction to be updated |   
  
Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
enabled |  string |  false |  Whether to enable Relay Authorization Settings or not |  No update  
memo |  string |  false |  Note for the settings |  No update  
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継許可設定」の「更新」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "connectionId":"id1",
        "remoteConnectionId":"id2",
        "direction":"send",
        "enabled":"true",
        "memo":"memo1"
    }

Property Name |  Value |  Description  
---|---|---  
connectionId |  string |  Connection ID of the local machine to be updated  
remoteConnectionId |  string |  Connection ID of the remote machine to be updated  
direction |  string |  Transfer direction to be updated  
enabled |  string |  Whether to enable Relay Authorization Settings or not  
memo |  string |  Note for the settings  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String connectionId = "xxxxxxxx";
        String remoteConnectionId = "xxxxxxxx";
        String direction = "send";
        try {
            URL url = new URL(host + "/api/v2/relay/permission/" + connectionId + "/" + remoteConnectionId + "/" + direction);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            String putData = "{\"enabled\":\"true\", \"memo\":\"xxxxxxxxx\"}";
    
            connection.setRequestMethod("PUT");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(putData.length()));
            try (BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(connection.getOutputStream()))) {
                writer.write(putData);
            }
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var connectionId = 'xxxxxxxx';
    var remoteConnectionId = 'xxxxxxxx';
    var direction = 'send';
    $.ajax({
      type: 'PUT',
      url: host + '/api/v2/relay/permission/' + connectionId + '/' + remoteConnectionId + '/' + direction,
      headers: {
        Authorization: 'Bearer ' + apiKey
      },
      contentType: 'application/json',
      data: JSON.stringify({enabled: 'true', memo: 'xxxxxxx'})
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 72

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayLog.htm

# 中継履歴

HULFT-WebConnect の中継履歴を取得します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 73

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayLogAllGet.htm

# 全件取得

中継履歴を全件取得します。

クエリパラメータを指定することで、検索条件に該当する中継履歴を取得することもできます。

Request Interface

HTTP Request
    
    
    GET /relay/log

Parameter

Query Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
senderConnectionId |  string |  false |  Connection ID of the sending side |  Blank  
receiverConnectionId |  string |  false |  Connection ID of the receiving side |  Blank  
senderSecondaryAccount |  string |  false |  Previous secondary account for Browser Transfer of the sending side (email address) in the Relay Log to retrieve |  Blank  
receiverSecondaryAccount |  string |  false |  Previous secondary account for Browser Transfer of the receiving side (email address) in the Relay Log to retrieve |  Blank  
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継履歴」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスが返却されます。データstartTimeの新しい日時から順に、降順で返却されます。
    
    
    {
        "totalSize":50,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":1,
        "logs":[
            {
                "status":"1",
                "startTime":"2016-06-30 12:13:01.226",
                "endTime":"2016-06-30 12:13:02.226",
                "senderConnectionId":"id1",
                "senderAgentId":"agent1",
                "senderHostName":"host1",
                "receiverConnectionId":"id2",
                "receiverAgentId":"agent2",
                "receiverHostName":"host2",
                "fileId":"FILEID1",
                "fileName":"example",
                "processingId":"CCC3D6B33DF4F42EA4734BD88519525A32",
                "dataSize":"60",
                "dataSizeOnRoute":"60",
                "transferRate":"60",
                "senderClientType":"hulft",
                "receiverClientType":"data_transfer_api"
                "senderSecondaryAccount":"sender@hulft.com",
                "receiverSecondaryAccount":"receiver@hulft.com"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
logs |  array |  Array of the elements described below  
status |  string |  Status code (1: Normal end, 2: Error)  
startTime |  string |  Transfer start date and time  
endTime |  string |  Transfer end date and time  
senderConnectionId |  string |  Connection ID of the sending side  
senderAgentId |  string |  Agent ID of the sending side  
senderHostName |  string |  Host name of Agent on the sending side  
receiverConnectionId |  string |  Connection ID of the receiving side  
receiverAgentId |  string |  Agent ID of the receiving side  
receiverHostName |  string |  Host name of Agent on the receiving side  
fileId |  string |  File ID of HULFT  
fileName |  string |  File name to be transferred  
processingId |  string |  Processing identifier  
dataSize |  string |  Actual data size (Unit: bytes)  
dataSizeOnRoute |  string |  Data size on transfer route (Unit: bytes)  
transferRate |  string |  Transfer rate (bytes/second)  
senderClientType |  string |  Client type of the sending side  
receiverClientType |  string |  Client type of the receiving side  
senderSecondaryAccount |  string |  Previous secondary account for Browser Transfer of the sending side (email address) in the Relay Log to retrieve  
receiverSecondaryAccount |  string |  Previous secondary account for Browser Transfer of the receiving side (email address) in the Relay Log to retrieve  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/relay/log");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/log',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 74

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayLogFileId.htm

# ファイル ID を指定して取得

ファイル ID を指定して中継履歴を取得します

Request Interface

HTTP Request
    
    
    GET /relay/log?fileId={fileId}

Parameter

Query Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
fileId |  string |  true |  File ID of HULFT |   
senderConnectionId |  string |  false |  Connection ID of the sending side |  Blank  
receiverConnectionId |  string |  false |  Connection ID of the receiving side |  Blank  
senderSecondaryAccount |  string |  false |  Previous secondary account for Browser Transfer of the sending side (email address) in the Relay Log to retrieve |  Blank  
receiverSecondaryAccount |  string |  false |  Previous secondary account for Browser Transfer of the receiving side (email address) in the Relay Log to retrieve |  Blank  
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継履歴」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスが返却されます。データstartTimeの新しい日時から順に、降順で返却されます。
    
    
    {
        "totalSize":50,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":1,
        "logs":[
            {
                "status":"1",
                "startTime":"2016-06-30 12:13:01.226",
                "endTime":"2016-06-30 12:13:02.226",
                "senderConnectionId":"id1",
                "senderAgentId":"agent1",
                "senderHostName":"host1",
                "receiverConnectionId":"id2",
                "receiverAgentId":"agent2",
                "receiverHostName":"host2",
                "fileId":"FILEID1",
                "fileName":"example",
                "processingId":"CCC3D6B33DF4F42EA4734BD88519525A32",
                "dataSize":"60",
                "dataSizeOnRoute":"60",
                "transferRate":"60",
                "senderClientType":"hulft",
                "receiverClientType":"data_transfer_api"
                "senderSecondaryAccount":"sender@hulft.com",
                "receiverSecondaryAccount":"receiver@hulft.com"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
logs |  array |  Array of the elements described below  
status |  string |  Status code (1: Normal end, 2: Error)  
startTime |  string |  Transfer start date and time  
endTime |  string |  Transfer end date and time  
senderConnectionId |  string |  Connection ID of the sending side  
senderAgentId |  string |  Agent ID of the sending side  
senderHostName |  string |  Host name of Agent on the sending side  
receiverConnectionId |  string |  Connection ID of the receiving side  
receiverAgentId |  string |  Agent ID of the receiving side  
receiverHostName |  string |  Host name of Agent on the receiving side  
fileId |  string |  File ID of HULFT  
fileName |  string |  File name to be transferred  
processingId |  string |  Processing identifier  
dataSize |  string |  Actual data size (Unit: bytes)  
dataSizeOnRoute |  string |  Data size on transfer route (Unit: bytes)  
transferRate |  string |  Transfer rate (bytes/second)  
senderClientType |  string |  Client type of the sending side  
receiverClientType |  string |  Client type of the receiving side  
senderSecondaryAccount |  string |  Previous secondary account for Browser Transfer of the sending side (email address) in the Relay Log to retrieve  
receiverSecondaryAccount |  string |  Previous secondary account for Browser Transfer of the receiving side (email address) in the Relay Log to retrieve  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String fileId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/relay/log?fileId=" + fileId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var fileId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/log?fileId=' + fileId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 75

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/RelayLogProcessId.htm

# 処理識別子を指定して取得

処理識別子を指定して中継履歴を取得します。

Request Interface

HTTP Request
    
    
    GET /relay/log/{processingId}

Parameter

Path Parameter |  Value |  Required |  Description  
---|---|---|---  
processingId |  string |  true |  Processing identifier  
  
Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「中継履歴」の「取得」を選択する必要があります

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスが返却されます。データstartTimeの新しい日時から順に、降順で返却されます。
    
    
    {
        "totalSize":50,
        "fetchSize":1,
        "startIndex":0,
        "maxResults":1,
        "logs":[
            {
                "status":"1",
                "startTime":"2016-06-30 12:13:01.226",
                "endTime":"2016-06-30 12:13:02.226",
                "senderConnectionId":"id1",
                "senderAgentId":"agent1",
                "senderHostName":"host1",
                "receiverConnectionId":"id2",
                "receiverAgentId":"agent2",
                "receiverHostName":"host2",
                "fileId":"FILEID1",
                "fileName":"example",
                "processingId":"CCC3D6B33DF4F42EA4734BD88519525A32",
                "dataSize":"60",
                "dataSizeOnRoute":"60",
                "transferRate":"60",
                "senderClientType":"hulft",
                "receiverClientType":"data_transfer_api"
                "senderSecondaryAccount":"sender@hulft.com",
                "receiverSecondaryAccount":"receiver@hulft.com"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
logs |  array |  Array of the elements described below  
status |  string |  Status code (1: Normal end, 2: Error)  
startTime |  string |  Transfer start date and time  
endTime |  string |  Transfer end date and time  
senderConnectionId |  string |  Connection ID of the sending side  
senderAgentId |  string |  Agent ID of the sending side  
senderHostName |  string |  Host name of Agent on the sending side  
receiverConnectionId |  string |  Connection ID of the receiving side  
receiverAgentId |  string |  Agent ID of the receiving side  
receiverHostName |  string |  Host name of Agent on the receiving side  
fileId |  string |  File ID of HULFT  
fileName |  string |  File name to be transferred  
processingId |  string |  Processing identifier  
dataSize |  string |  Actual data size (Unit: bytes)  
dataSizeOnRoute |  string |  Data size on transfer route (Unit: bytes)  
transferRate |  string |  Transfer rate (bytes/second)  
senderClientType |  string |  Client type of the sending side  
receiverClientType |  string |  Client type of the receiving side  
senderSecondaryAccount |  string |  Previous secondary account for Browser Transfer of the sending side (email address) in the Relay Log to retrieve  
receiverSecondaryAccount |  string |  Previous secondary account for Browser Transfer of the receiving side (email address) in the Relay Log to retrieve  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String processingId = "CCC3D6B33DF4F42EA4734BD88519525A32";
        try {
            URL url = new URL(host + "/api/v2/relay/log/" + processingId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var processingId = 'CCC3D6B33DF4F42EA4734BD88519525A32';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/relay/log/' + processingId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 76

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ServiceStatus.htm

# サービス稼働状況

HULFT-WebConnect の稼働状況を取得します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 77

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/ServiceStatusGet.htm

# 取得

稼働状況を取得します。

Request Interface

HTTP Request
    
    
    GET /service/status

Parameter

リクエストパラメータはありません。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「サービス稼働状況」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
        "totalSize":6,
        "fetchSize":6,
        "startIndex":0,
        "maxResults":6,
        "totalStatus":"0",
        "serviceStatus":[
            {
                "region":"California",
                "endpoint":"california-service1.webconnect.hulft.com",
                "status":"0"
            },
                .
                .
                .
            {
                "region":"Tokyo",
                "endpoint":"service2.tokyo.webconnect.hulft.com",
                "status":"0"
            },
        "dataTransferSiteStatus":[
            {
                "region":"California",
                "endpoint":"california-ap.webconnect.hulft.com",
                "status":"0"
            },
                .
                .
                .
            {
                "region":"Tokyo",
                "endpoint":"service-ap.tokyo.webconnect.hulft.com",
                "status":"0"
            }
        ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data (endpoints of Agent, CLI and Data Transfer Site)  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
totalStatus |  sting |  Operation status of the HULFT-WebConnect service (0: Operating normally, 1: Service disruption, 9: Performance issues)  
serviceStatus |  array |  Array of the elements described below  
region |  string |  Region of the access point to HULFT-WebConnect of Agent / CLI  
endpoint |  string |  Access point to HULFT-WebConnect of Agent / CLI  
status |  string |  Access point status (0: Operating normally, 1: Service disruption, 9: Performance issues)  
dataTransferSiteStatus |  array |  Array of the elements described below  
region |  string |  Region of the access point to HULFT-WebConnect of Data Transfer Site  
endpoint |  string |  Access point to HULFT-WebConnect of Data Transfer Site  
status |  string |  Access point status (0: Operating normally, 1: Service disruption, 9: Performance issues)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/service/status");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/service/status',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 78

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/SubAccountSet.htm

# 旧ブラウザ転送サブアカウント設定

**注意**

旧ブラウザ転送サブアカウントは廃止されたためご利用いただけません。ご利用を継続する場合はアカウントへ移行してください。

HULFT-WebConnect の旧ブラウザ転送サブアカウント設定を取得、削除します。

特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 79

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/SubAccountSet1Get.htm

# 1 件取得

旧ブラウザ転送サブアカウント ID を指定して旧ブラウザ転送サブアカウント設定を 1 件取得します。

Request Interface

HTTP Request
    
    
    GET /secondary-account/definition/{secondaryAccountId}

Parameter

Path Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
secondaryAccountId |  string |  true |  ID to specify a previous secondary account for Browser Transfer |   
  
Authorization

Management Console の ［API キー管理］ 画面の「スコープ」で、「旧ブラウザ転送サブアカウント設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
      "secondaryAccountId": "xxxxxxxxxxxxxxxxxxxxxx",
      "secondaryAccount": "xxxxxxxxxxxxxxxxxxxxxxx",
      "passwordPolicy": {
        "passwordManagement": 1,
        "passwordExpireOn": 30
      },
      "browserToHulftDefinitions": [
        {
          "id": "hoge",
          "description": "…"
        },
        {
          "id": "fuga",
          "description": "…"
        }
      ],
      "hulftToBrowserDefinitions": [],
      "ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxxx",
      "memo": "xxxxxxxxxxxxxxxxxxxxxxx",
      "isAvailableMail": false,
      "statusCode": 0
    }

Property Name |  Value |  Description  
---|---|---  
secondaryAccountId |  string |  ID to specify a previous secondary account for Browser Transfer  
secondaryAccount |  string |  Previous secondary account for Browser Transfer (email address)  
passwordPolicy |  object |  The password policy  
passwordManagement |  integer |  Password Management Method (0: Management by a user with a previous secondary account for Browser Transfer, 1: Management by the contractor)  
passwordExpireOn |  integer |  The password validity period (0 (the password never expires) or 30 to 365 days)  
browserToHulftDefinitions |  array |  Transfer settings (for Send File)  
id |  string |  Transfer Settings ID (for Send File)  
description |  string |  Description of the transfer settings (for Send File)  
hulftToBrowserDefinitions |  array |  Transfer settings (for Send Request)  
id |  string |  Transfer Settings ID (for Send Request)  
description |  string |  Description of the transfer settings (for Send Request)  
ipFilterGroupName |  string |  IP Filter Group Name  
memo |  string |  Note for the previous secondary account for Browser Transfer  
isAvailableMail |  boolean |  Whether or not to send an email to the email address  
statusCode |  integer |  The status of the previous secondary account for Browser Transfer (0: New creation, 1: In use, 2: While changing Password Management Method, 3: While changing the email address)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        String secondaryAccountId = "xxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/secondary-account/definition/" + secondaryAccountId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var secondaryAccountId = 'xxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/secondary-account/definition/' + secondaryAccountId,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 80

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/SubAccountSetAllGet.htm

# 全件取得

旧ブラウザ転送サブアカウント設定を全件取得します。

Request Interface

HTTP Request
    
    
    GET /secondary-account/definition

Parameter

個別のパラメータはありません。

Site API 共通のリクエストパラメータについては、[「共通パラメータ」](../APIComSpeci/CommParam.htm)を参照してください。

Authorization

Management Console の [API キー管理] 画面の「スコープ」で、 「旧ブラウザ転送サブアカウント設定」の「取得」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、以下の JSON フォーマットでレスポンスを返却します。
    
    
    {
      "totalSize": 10,
      "fetchSize": 10,
      "startIndex": 0,
      "maxResults": 30,
      "existUnavailableMail": false,
      "secondaryAccounts": [
        {
          "secondaryAccountId": "xxxxxxxxxxxxxxxxxxxxxx",
          "secondaryAccount": "xxxxxxxxxxxxxxxxxxxxxxx",
          "passwordPolicy": {
            "passwordManagement": 1,
            "passwordExpireOn": 30
          },
          "browserToHulftDefinitions": [
            {
              "id": "foo",
              "description": "…"
            },
            {
              "id": "bar",
              "description": "…"
            }
          ],
          "hulftToBrowserDefinitions": [
            {
              "id": "hoge",
              "description": "…"
            },
            {
              "id": "fuga",
              "description": "…"
            }
          ],
          "ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxxx",
          "memo": "xxxxxxxxxxxxxxxxxxxxxxx",
          "isAvailableMail": true,
          "statusCode": 1
        },
        {
          "secondaryAccountId": "xxxxxxxxxxxxxxxxxxxxxx",
          "secondaryAccount": "xxxxxxxxxxxxxxxxxxxxxxx",
          "passwordPolicy": {
            "passwordManagement": 0,
            "passwordExpireOn": 0
          },
          "browserToHulftDefinitions": [],
          "hulftToBrowserDefinitions": [],
          " ipFilterGroupName": "xxxxxxxxxxxxxxxxxxxxxxx",
          "memo": "xxxxxxxxxxxxxxxxxxxxxxx",
          "isAvailableMail": false,
          "statusCode": 0
        }
      ]
    }

Property Name |  Value |  Description  
---|---|---  
totalSize |  integer |  The total number of data  
fetchSize |  integer |  The number of the obtained data  
startIndex |  integer |  Index of the first row of a data to retrieve  
maxResults |  integer |  The maximum number of indexes included in a response data  
existUnavailableMail |  boolean |  Whether there is an email address for which sending an email is stopping now  
secondaryAccountId |  string |  ID to specify a previous secondary account for Browser Transfer  
secondaryAccount |  string |  Previous secondary account for Browser Transfer (email address)  
passwordPolicy |  object |  The password policy  
passwordManagement |  integer |  Password Management Method (0: Management by a user with a previous secondary account for Browser Transfer, 1: Management by the contractor)  
passwordExpireOn |  integer |  The password validity period (0 (the password never expires) or 30 to 365 days)  
browserToHulftDefinitions |  array |  Transfer settings (for Send File)  
id |  string |  Transfer Settings ID (for Send File)  
description |  string |  Description of the transfer settings (for Send File)  
hulftToBrowserDefinitions |  array |  Transfer settings (for Send Request)  
id |  string |  Transfer Settings ID (for Send Request)  
description |  string |  Description of the transfer settings (for Send Request)  
ipFilterGroupName |  string |  IP Filter Group Name  
memo |  string |  Note for the previous secondary account for Browser Transfer  
isAvailableMail |  boolean |  Whether or not to send an email to the email address  
statusCode |  integer |  The status of the previous secondary account for Browser Transfer (0: New creation, 1: In use, 2: While changing Password Management Method, 3: While changing the email address)  
  
Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            URL url = new URL(host + "/api/v2/secondary-account/definition");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
                String line;
                while((line = reader.readLine()) != null) {
                    System.out.println(line);
                }
            }
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    $.ajax({
      type: 'GET',
      url: host + '/api/v2/secondary-account/definition',
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 81

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIDetail/SubAccountSetDelete.htm

# 削除

指定した旧ブラウザ転送サブアカウント設定を削除します。

Request Interface

HTTP Request
    
    
    DELETE /secondary-account/definition/{secondaryAccountId}

Parameter

Request Parameter |  Value |  Required |  Description |  Default Value  
---|---|---|---|---  
secondaryAccountId |  string |  true |  ID to specify a previous secondary account for Browser Transfer |   
  
Authorization

Management Console の [API キー管理] 画面の「スコープ」で、「旧ブラウザ転送サブアカウント設定」の「削除」を選択する必要があります。

Response Interface

リクエストが正常に処理された場合、レスポンスボディは返却されません。

Examples

Java JavaScript
    
    
    public static void main(String[] args) {
        String host = "https://www.webconnect.hulft.com";
        String apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
        try {
            String secondaryAccountId = "xxxxxxxx";
            URL url = new URL(host + "/api/v2/secondary-account/definition/" + secondaryAccountId);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("DELETE");
            connection.setRequestProperty("Authorization", "Bearer " + apiKey);
            System.out.println(connection.getResponseMessage()); // The response does not contain the response body.
        } catch (IOException ex) {
            // error
        }
    }
    
    
    // load jquery 
    var host = 'https://www.webconnect.hulft.com';
    var apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
    var secondaryAccountId  = 'xxxxxxxx';
    $.ajax({
      type: 'DELETE',
      url: host + '/api/v2/secondary-account/definition/' + secondaryAccountId ,
      headers: {
        Authorization: 'Bearer ' + apiKey
      }
    }).done(function(data, status, xhr) {
      console.log(data);
    }).fail(function(data, status, xhr) {
      console.log(data);
    });


---


## ページ 82

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/AccessDenial_APIList.htm

# 接続拒否履歴

HTTP Request |  Description  
---|---  
GET /access-denial/log |  Lists Connection Refusing Log.


---


## ページ 83

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/AccountSet_APIList.htm

# アカウント管理  
  
HTTP Request |  Description  
---|---  
GET /accounts/definition |  Lists account information.  
GET /accounts/definition/{accountId} |  Gets one piece of account information.  
POST /accounts/definition |  Registers an account.  
POST /accounts/password/set-request | Executes Password Setup Request for the specified account.  
PUT /accounts/definition/{accountId} |  Updates an account  
DELETE /accounts/definition/{accountId} |  Deletes an account.


---


## ページ 84

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/AgentConnectStatus_APIList.htm

# Agent 接続状況  
  
HTTP Request |  Description  
---|---  
GET /agent/status |  Lists Agent connection statuses.  
GET /agent/status/{direction} |  Gets Agent connection statuses by specifying the transfer direction.


---


## ページ 85

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/AgentDisconnect_APIList.htm

# Agent 切断  
  
HTTP Request |  Description  
---|---  
POST /agent/disconnection |  Disconnects the specified Agent.


---


## ページ 86

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/APIList.htm

# API 一覧  
  
特に明記がない限り、URI は https://www.webconnect.hulft.com/api/v2 の相対 URI を表しています。


---


## ページ 87

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/BrowsTransGroups_APIList.htm

# ブラウザ転送設定グループ設定

HTTP Request |  Description  
---|---  
GET /browser-transfer-groups |  Lists the Browser Transfer Group Settings..  
GET /browser-transfer-groups/{browserTransferGroupId} |  Get one piece of the Browser Transfer Group Settings.  
POST /browser-transfer-groups |  Registers a new Browser Transfer Group Settings.  
PUT /browser-transfer-groups/{browserTransferGroupId} |  Updates Browser Transfer Group Settings.  
DELETE /browser-transfer-groups/{browserTransferGroupId} |  Deletes Browser Transfer Group Settings.


---


## ページ 88

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/BrowsTransSet_APIList.htm

# ブラウザ転送設定  
  
HTTP Request |  Description  
---|---  
GET /browser-transfer/definition/browser-to-hulft |  Lists the Browser Transfer Settings information (for Send File).  
GET /browser-transfer/definition/hulft-to-browser |  Lists the Browser Transfer Settings information (for Send Request).  
GET /browser-transfer/definition/browser-to-hulft/{browserToHulftDefinitionId} |  Gets one piece of Browser Transfer Settings information (for Send File) by specifying Transfer Settings ID.  
GET /browser-transfer/definition/hulft-to-browser/{hulftToBrowserDefinitionId} |  Gets one piece of Browser Transfer Settings information (for Send Request) by specifying Transfer Settings ID.  
POST /browser-transfer/definition/browser-to-hulft |  Registers a new Browser Transfer Settings information (for Send File).  
POST /browser-transfer/definition/hulft-to-browser |  Registers a new Browser Transfer Settings information (for Send Request).  
PUT /browser-transfer/definition/browser-to-hulft/{browserToHulftDefinitionId} |  Updates the specified Browser Transfer Settings information (for Send File).  
PUT /browser-transfer/definition/hulft-to-browser/{hulftToBrowserDefinitionId} |  Updates the specified Browser Transfer Settings information (for Send Request).  
DELETE /browser-transfer/definition/browser-to-hulft/{browserToHulftDefinitionId} |  Deletes the specified Browser Transfer Settings information (for Send File).  
DELETE /browser-transfer/definition/hulft-to-browser/{hulftToBrowserDefinitionId} |  Deletes the specified Browser Transfer Settings information (for Send Request).


---


## ページ 89

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/ConnectSet_APIList.htm

# 接続設定  
  
HTTP Request |  Description  
---|---  
GET /connections/definition |  Lists the Connection Settings information.  
GET /connections/definition/{connectionId} |  Gets the Connection Settings information by specifying Connection ID.  
POST /connections/definition |  Registers new Connection Settings information.  
PUT /connections/definition/{connectionId} |  Updates the specified Connection Settings information.  
DELETE /connections/definition/{connectionId} |  Deletes the specified Connection Settings information.


---


## ページ 90

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/DClient_APIList.htm

# D-Client設定  
  
HTTP Request |  Description  
---|---  
GET /dclient/definition |  Lists D-Client Settings.  
GET /dclient/definition/{dclientUuid} |  Gets one piece of D-Client Settings information.  
POST /dclient/definition |  Registers D-Client Settings.  
POST /dclient/user-guide/mail-request/{dclientUuid} | Request for Sending D-Client Usage Instruction.  
PUT /dclient/definition/{dclientUuid} |  Updates D-Client Settings.  
DELETE /dclient/definition/{dclientUuid} |  Deletes D-Client Settings.


---


## ページ 91

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/IpFilter_APIList.htm

# IPフィルタグループ  
  
HTTP Request |  Description  
---|---  
GET /ip-filter/group |  Lists IP Filter Group Settings.  
GET /ip-filter/group/{ipFilterGroupName} |  Gets one piece of IP Filter Group Settings information.  
POST /ip-filter/group |  Registers IP Filter Group Settings.  
PUT /ip-filter/group/{ipFilterGroupName} |  Updates IP Filter Group Settings.  
DELETE /ip-filter/group/{ipFilterGroupName} |  Deletes IP Filter Group Settings.


---


## ページ 92

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/RelayAuthoSet_APIList.htm

# 中継許可設定  
  
HTTP Request |  Description  
---|---  
GET /relay/permission |  Lists the Relay Authorization Settings information.  
GET /relay/permission/{connectionId} |  Gets the Relay Authorization Settings information by specifying Connection ID.  
GET /relay/permission/{connectionId}/{direction} |  Gets the Relay Authorization Settings information by specifying Connection ID and the transfer direction.  
GET /relay/permission/{connectionId}/{remoteConnectionId}/{direction} |  Gets one piece of Relay Authorization Settings information by specifying Connection ID, Connection ID of the remote machine and the transfer direction.  
POST /relay/permission |  Registers new Relay Authorization Settings information.  
PUT /relay/permission/{connectionId}/{remoteConnectionId}/{direction} |  Updates the specified Relay Authorization Settings information.  
DELETE /relay/permission/{connectionId}/{remoteConnectionId}/{direction} |  Deletes the specified Relay Authorization Settings information.


---


## ページ 93

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/RelayLog_APIList.htm

# 中継履歴  
  
HTTP Request |  Description  
---|---  
GET /relay/log |  Lists relay logs.  
GET /relay/log/{processingId} |  Gets relay logs by specifying the processing identifier.  
GET /relay/log?fileId={fileId} |  Gets relay logs by specifying the file ID.


---


## ページ 94

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/ServiceStatus_APIList.htm

# サービス稼働状況  
  
HTTP Request |  Description  
---|---  
GET /service/status |  Lists HULFT-WebConnect statuses.


---


## ページ 95

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/APIList/SubAccount_APIList.htm

# 旧ブラウザ転送サブアカウント設定  
  
**注意**

旧ブラウザ転送サブアカウントは廃止されたためご利用いただけません。ご利用を継続する場合はアカウントへ移行してください。

HTTP Request |  Description  
---|---  
GET /secondary-account/definition |  Gets all setting records of previous secondary accounts for Browser Transfer.  
GET /secondary-account/definition/{secondaryAccountId} |  Gets a setting record of a previous secondary account for Browser Transfer by specifying Secondary Account ID.  
DELETE /secondary-account/definition/{secondaryAccountId} |  Deletes the setting record of the specified previous secondary account for Browser Transfer.


---


## ページ 96

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/Changes/Changes_SAP.htm

# 変更内容一覧  
  
Ver. 3.0.9での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.6 |  Ver 3.0.9 |  変更箇所  
---|---|---|---|---  
1 |  Response InterfaceのIpFilgerGroupNameのDescriptionの修正 |  This parameter is not displayed と記載 |  This parameter contains nullに修正 |  [「全件取得」](../APIDetail/ConnectSetAllGet.htm) [「コネクション ID を指定して取得」](../APIDetail/ConnectSetConnectId.htm) [「登録」](../APIDetail/ConnectSetRegistration.htm) [「更新」](../APIDetail/ConnectSetUpdate.htm)  
2 |  Response InterfaceのtotalStatusのValueの修正 |  integerと記載 |  stringに修正 |  [「取得」](../APIDetail/ServiceStatusGet.htm)  
3 |  画面の変更 |  「旧ブラウザ転送アカウント設定」に「登録」「更新」「パスワード設定依頼」のチェックボックスあり |  「登録」「更新」「パスワード設定依頼」のチェックボックスなし |  [「API キー」](../APIComSpeci/APIKey.htm)  
4 |  目次の項番を修正 | 項番に「.」が過剰または不足 | 項番を修正 |  [「1 件取得」](../APIDetail/DClient1Get.htm) [「更新」](../APIDetail/DClienUpdate.htm)  
5 |  旧ブラウザ転送サブアカウントの廃止によりPOSTとPUTを削除 |  記載あり |  記載を削除 |  [「旧ブラウザ転送サブアカウント設定」](../APIList/SubAccount_APIList.htm)  
6 |  旧ブラウザ転送サブアカウントの廃止により記載を修正 |  記載あり |  記載を修正 |  [「旧ブラウザ転送サブアカウント設定」](../APIDetail/SubAccountSet.htm)  
  
Ver. 3.0.6での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.5 |  Ver 3.0.6 |  変更箇所  
---|---|---|---|---  
1 |  Request Parameter(connectableClientType)の修正 |  dclientの記載なし |  dclientを追記 |  [「登録」](../APIDetail/ConnectSetRegistration.htm) [「更新」](../APIDetail/ConnectSetUpdate.htm)  
  
Ver. 3.0.5での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.4 |  Ver 3.0.5 |  変更箇所  
---|---|---|---|---  
1 |  レートリミットの記載変更 |  1アカウント当たりの説明 |  1契約アカウントの記載に変更 |  [「レートリミット」](../APIComSpeci/RateLimit.htm)  
  
Ver. 3.0.4での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.3 |  Ver 3.0.4 |  変更箇所  
---|---|---|---|---  
1 |  IPフィルタグループの追記 |  記載なし |  追記 |  [「IPフィルタグループ」](../APIList/IpFilter_APIList.htm)  
2 | 接続拒否履歴の追記 |  記載なし |  追記 |  [「接続拒否履歴」](../APIList/AccessDenial_APIList.htm)  
3 | 画面の変更 | Ver 3.0.3の画面 | Ver 3.0.4の画面 |  [「API キー」](../APIComSpeci/APIKey.htm)  
4 | IPフィルタグループ APIの追記 | 記載なし | 追記 |  [「IPフィルタグループ」](../APIDetail/IPFilterGroup.htm)  
5 | 接続拒否履歴 APIの追記 | 記載なし | 追記 |  [「接続拒否履歴」](../APIDetail/AccessDenialLog.htm)  
6 | 旧ブラウザ転送サブアカウント廃止の注意事項を追記 | 注意事項の記載なし |  注意事項の追記 |  [「旧ブラウザ転送サブアカウント設定」](../APIList/SubAccount_APIList.htm) [「旧ブラウザ転送サブアカウント設定」](../APIDetail/SubAccountSet.htm)  
  
Ver. 3.0.3での変更内容は次のとおりです。

# |  変更内容 |  Ver 3.0.2 |  Ver 3.0.3 |  変更箇所  
---|---|---|---|---  
1 |  ブラウザ転送設定グループ APIの追記 |  記載なし |  追記 |  [「ブラウザ転送設定グループ」](../APIDetail/BrowsTransGroup.htm)  
2 | アカウント管理 APIの追記 |  記載なし |  追記 |  [「アカウント管理」](../APIDetail/AccountSet.htm)  
3 | D-Client設定 APIの追記 |  記載なし |  追記 |  [「D-Client設定」](../APIDetail/DClientSet.htm)


---


## ページ 97

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/HTTPStatusCode/HTTPStatusCode.htm

# HTTP ステータスコード  
  
HULFT-WebConnect Site API が返却する主な HTTP ステータスコードについて説明します

HTTPステータスコードの詳細は、RFC 2616 および RFC 6585 を参照してください。

HTTP Status Code |  Method  
---|---  
200 OK |  GET/POST/PUT/DELETE  
201 Created |  POST  
204 No Content |  GET  
400 Bad Request |  GET/POST/PUT/DELETE  
401 Unauthorized |  GET/POST/PUT/DELETE  
403 Forbidden |  GET/POST/PUT/DELETE  
404 Not Found |  PUT/DELETE  
405 Method Not Allowed |  GET/POST/PUT/DELETE  
429 Too Many Requests |  GET/POST/PUT/DELETE  
500 Internal Server Error |  GET/POST/PUT/DELETE


---


## ページ 98

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/Preface/preface.htm

# Site API Developer's Guide \- はじめに  
  
このたびは、本製品をご利用いただき、誠にありがとうございます。

本ガイドでは、API を使用した Web アプリケーション開発経験者を対象に、HULFT-WebConnect Site API の概要およびリクエスト・レスポンスインタフェースについて説明しています。


---


## ページ 99

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/Preface/Transcription.htm

# 表記について

製品名等の固有名詞は、各メーカーの商標または登録商標です。


---


## ページ 100

**URL:** https://www.hulft.com/help/ja-jp/WebConnect-V3/HWC-SAP/Content/SiteAPI/WebCTSiteAPI/WebCTSiteAPI.htm

# HULFT-WebConnect Site API について

HULFT-WebConnectでは、HULFT-WebConnect Management Console（以下、Management Console）の機能を REST API として公開しています。

ユーザはHULFT-WebConnect Site API の仕様に基づいてリクエストやレスポンスの解析を行うことで、独自のクライアントを作成することができます。


---

