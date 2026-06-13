# 煮物tube (Multi-Platform Deploy Version)

煮物tubeの各種クラウドデプロイサービス（Render等）に対応した完全版リポジトリです。Python (FastAPI) バックエンドによる高速な非同期プロキシ通信と、洗練されたディープブルーのモダンなフロントエンドUIをワンパッケージに統合しています。

---

## ✨ 特徴
* **洗練されたディープブルーUI**: グラスモルフィズムと柔らかな階層デザインを採用した、視覚的に美しいレスポンシブフロントエンド。
* **堅牢なFastAPIバックエンド**: `httpx` による非同期通信と厳格なタイムアウト管理（接続10秒、読み込み30秒）により、エラーの発生を極限まで抑制。
* **マルチデプロイ対応**: 主要な5つのPaaS（Render, Vercel, Zeabur, Railway, Netlify）へのワンクリック展開用構成ファイルを完備。

---

## 🔗 公式URL一覧
接続状況やサーバーの負荷に応じて、以下のいずれかのURLからアクセスしてください。すべてのURLで同様のサービスが提供されています。

* [公式URL 1](https://nimono-study-portal.detprod.com)
* [公式URL 2](https://nimono-study-portal.highdesertcoders.com)
* [公式URL 3](https://nimono-study-portal.mymywant.com)
* [公式URL 4](https://nimono-study-portal.anteroblue.com)
* [公式URL 5](https://nimono-study-portal.arybarbosa.com)
* [公式URL 6](https://nimono-study-portal.imupmyass.com)
* [公式URL 7](https://nimonotube.sitaci.com/)
* [公式URL 8](https://nimonotube.hardsoft.nu/)
* [公式URL 9](https://nimonotube.rainbowcup.com/)
* [公式URL 10](https://nimonotube.ezwebsites.com/)
* [公式URL 11](https://nimonotube.champagnewishesandrvdreams.com/)

---

## 🚀 ワンクリック・デプロイ
以下のボタンをクリックするだけで、対象のサービス上にあなた専用の「煮物tube」環境を自動的にビルド・公開できます。

| サービス名 | デプロイボタン |
| :--- | :--- |
| **Render** | [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/nomo-dayo-0206/nimonotube-public) |
| **Vercel** | [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/nomo-dayo-0206/nimonotube-public) |
| **Zeabur** | [![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/templates/ZEABUR?templateid=https://github.com/nomo-dayo-0206/nimonotube-public) |
| **Railway** | [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/deploy?repository=https://github.com/nomo-dayo-0206/nimonotube-public) |
| **Netlify** | [![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/nomo-dayo-0206/nimonotube-public) |

---

## 💻 ローカル環境での起動手順
ご自身のPC上で開発や動作確認を行う場合は、以下の手順に従ってください。

### 1. 依存ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 2. サーバーの起動
```bash
python app.py
```
起動後、ブラウザで `http://127.0.0.1:8000` にアクセスするとフロントエンド画面が表示されます。

---

## 🛠 API 仕様書

本システムは、クライアントからのリクエストをPythonサーバーが受領し、バックエンドの配信システムへと安全に仲介（リバースプロキシ）を行います。

### 1. 動画検索 API
指定されたキーワードに合致する動画のメタデータ一覧を配列で取得します。

* **エンドポイント**: `GET /api/search`
* **クエリパラメータ**:
  * `q` (文字列 / 必須): 検索キーワード
* **レスポンス構造**:
```json
{
  "results": [
    {
      "id": "pvoa6468XcQ",
      "title": "Video Title",
      "channel": "Channel Name",
      "duration": "9:51",
      "viewCount": "378816",
      "publishedAgo": "今日",
      "publishedDate": "2026年06月13日",
      "publishedText": "2026年06月13日 (今日)",
      "source": "yt-dlp",
      "thumbnails": {
        "medium": {
          "url": "[https://i.ytimg.com/vi/pvoa6468XcQ/mqdefault.jpg](https://i.ytimg.com/vi/pvoa6468XcQ/mqdefault.jpg)"
        }
      },
      "url": "[https://www.youtube.com/watch?v=pvoa6468XcQ](https://www.youtube.com/watch?v=pvoa6468XcQ)"
    }
  ]
}
```

### 2. ストリームURL取得 API
動画再生に必要な配信元バイナリデータ（googlevideo規格等）の直リンクURLを取得します。

* **エンドポイント**: `GET /api/stream/{video_id}`
* **パスパラメータ**:
  * `video_id` (文字列 / 必須): 動画の固有識別子ID
* **クエリパラメータ**:
  * `quality` (文字列 / 任意): 画質設定（デフォルト値: `360p`）
* **レスポンス構造**:
```json
{
  "isM3u8": false,
  "resolution": "360p",
  "source": "yt-dlp",
  "url": "[https://rr1---sn-j85aaxt-jv0s.googlevideo.com/videoplayback](https://rr1---sn-j85aaxt-jv0s.googlevideo.com/videoplayback)?..."
}
```

---

## 📬 フィードバック・お問い合わせ
機能の追加要望、不具合の報告、その他システムに関するご意見は以下のコミュニケーションボードにて受け付けております。

[Padlet 要望・受付窓口](https://padlet.com/nomo0206/new-v04juu3iw251p7v)

---

## 📄 ライセンス
このプロジェクトは **MIT License** の下に公開されています。詳細はリポジトリ内の `LICENSE` ファイルを参照してください。
