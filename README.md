# schedule_recommend_api
工程表をリコメンドするAPI

## ローカル開発環境の準備
```ß
```


## コンテナでAPIを起動

コンテナをビルド
```
cd schedule_recommend_api
docker build ...
```

コンテナを8001番:8000で起動
```
docker run -it -rm ...
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
