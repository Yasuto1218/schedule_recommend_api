from fastapi import FastAPI

app = FastAPI()

@app.get("/get_recommend_schedule_id")
def get_recommend_schedule_id(feature_1: int, feature_2: float, feature_3: int):
    """パラーメータを受け取り、類似する工程表番号を取得する関数
    feature_1: 説明1
    feature_2: 説明2
    feature_3: 説明3
    """

    return {
        "feature_1": feature_1,
        "feature_2": feature_2,
        "feature_3": feature_3,
        "comment": "All Need is the schdule"
    }


@app.get("/get_recommend_schedule_param")
def get_recommend_schedule_param(feature_1: int, feature_2: float, feature_3: int):
    return "WIP"
