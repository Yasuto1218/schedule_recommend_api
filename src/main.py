import logging 

import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException


logging.basicConfig(level=logging.INFO)
app = FastAPI()

# csvのデータからdfを取得。場合によってはDBやCloudから取得する
import os
logging.info(os.listdir())

df =  pd.read_csv("./schedule_data/construction_data.csv")
name_list = df["name"].to_list()
df.drop(["name", "ID"], axis=1, inplace=True)


class ConstructionWorks(BaseModel):
    lgs_board_work: bool = Field(False, description="LGS・ボード工事")  
    sign_work: bool = Field(False, description="サイン工事")  
    temporary_work: bool = Field(False, description="仮設工事")  
    interior_finishing: bool = Field(False, description="内装工事仕上げ")  
    painting_work: bool = Field(False, description="塗装工事")  
    furniture_work: bool = Field(False, description="家具・什器工事")  
    plastering_tile_work: bool = Field(False, description="左官・タイル工事")  
    joinery_work: bool = Field(False, description="建具工事")  
    carpentry_work: bool = Field(False, description="木工事")  
    demolition_work: bool = Field(False, description="解体工事")  
    waterproofing_work: bool = Field(False, description="防水工事")  
    miscellaneous_metal_work: bool = Field(False, description="雑・金属工事")  
    miscellaneous_work: bool = Field(False, description="雑工事")  


class OutputNameAndIndex(BaseModel):
    construction_name: str = Field(description="工事名")
    best_cos_similarity: float = Field(description="コサイン類似度")


@app.post("/get_recommend/get_recommend_schedule_id")
def get_recommend_schedule_name(ConstructionWorks: ConstructionWorks) -> OutputNameAndIndex:
    """パラーメータから類似する工程表の番号を取得する
    """
    try:
        # NOTE:カラム順序を揃えてないので注意。あとでちゃんと揃えましょう。
        # dataclassからDataFrameを作成　-> numpy形式に変更
        work_dict = {}
        for cw in ConstructionWorks:
            work_dict[cw[0]] = cw[1]
        work_bec = np.array(list(work_dict.values()))

        # コサイン類似度の最も高いスケジュール名を取得
        best_name = "該当なし"
        best_similarity = 0
        for index_num, data_bec in df.iterrows():
            data_bec = data_bec.to_numpy()
            tmp_similarity = _calc_cosine_similarity(work_bec, data_bec)
            if best_similarity < tmp_similarity:
                best_similarity = tmp_similarity
                best_name = name_list[index_num]

        return OutputNameAndIndex(
            construction_name=best_name, 
            best_cos_similarity=best_similarity)
    except Exception as e:
        logging.error(f"エラーが発生しました: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/get_recommend/get_recommend_schedule_param")
def get_recommend_schedule_json(feature_1: int, feature_2: float, feature_3: int):
    return "WIP"


def _calc_cosine_similarity(bec_1: np.array, bec_2: np.array) -> float:
    dot_product = np.dot(bec_1, bec_2)
    norm_1 = np.linalg.norm(bec_1)
    norm_2 = np.linalg.norm(bec_2)
    return dot_product / (norm_1 * norm_2)


