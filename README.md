# schedule_recommend_api
工程表をリコメンドするAPI

## ローカル開発環境の準備(poetry)
[poetryをインストール後](https://python-poetry.org/docs/)


lockファイルやtomlファイルない場合
```
cd schedule_recommend_api
poetry init
```

lockファイルやtomlファイルある場合
```
cd schedule_recommend_api
poetry install
```


パッケージの追加・削除
```
# packageを追加
poetry add <package>

# packageを削除
poerty remove <package>
```

仮想環境の起動・停止
```
# 起動
poerty shell

# 停止
exit
```
## apiの起動
[swagger](http://127.0.0.1:8000/docs)にアクセス

```
cd src
uvicorn main:app --reload
```

## コンテナでAPIを起動

コンテナをビルド
```
cd schedule_recommend_api
docker build --platform=linux/amd64 -t schdule_recommend_api . 
```

コンテナを8001番:8000で起動
```
docker run -it --rm -p 8010:8000 schdule_recommend_api
```

## APIの説明 
### チャンネル
http://127.0.0.0.1:8000

| メソッド | HTTPリクエスト| 説 明 |
|:-------|:------|:-----|
| get_recommend | GET / get_recommend_schedule_id | 類似する工程表番号を取得 |


### パラメータ
| パラメータ | type | 説明 | required |
|:-------|:------|:-----|:-----|
| feature1 | int | {0, 1} | ✅ |
| feature2 | float | {0, 1} | ✅ |
| feature3 | int | {0, 1} |  |
| feature4 | int | {0, 1} | ✅ |
| feature5 | int | {0, 1} | ✅ |
