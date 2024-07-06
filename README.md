# Qiita Supporter Bot

**Version: 0.1.0**

<img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python">
<img src="https://img.shields.io/badge/-Docker-1488C6.svg?logo=docker">

## About
定期的にQiitaのRSSをチェックし、記事の更新があった場合にDiscordに通知します。

その他にも機能を拡張する予定です。

## Future

現段階では単にWebhookで通知を送るだけなので、
将来的にbotとして運用できるようにしたいな～と

## How to use

### 1. configファイルをカスタマイズ
`config.template.yaml`を`config.yaml`に名前を変え、
設定を好きなように書き換えてください。
詳しくはファイルにコメントが書いてあります。

### 2. docker compose up
コンテナを立ち上げます。