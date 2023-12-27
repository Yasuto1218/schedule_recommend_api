import pandas as pd
import numpy as np
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

class ConstructionWork(BaseModel):
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


class OutputNameAndID(BaseModel):
    construction_name: str = Field(description="工事名")
    construction_id: str = Field(description="工事ID")  
    
@app.get("/get_recommend_schedule_id")
def get_recommend_schedule_id(ConstructionWork) -> OutputNameAndID:
    """パラーメータから類似する工程表の番号を取得する
    """
    # dataclassからDataFrameを作成　-> numpy形式に変更
    work_dict = {}
    for cw in ConstructionWork:
        work_dict[cw[0]] = [cw[1]]
    work_df = pd.DataFrame(work_dict)
    work_array = work_df.to_numpy()


    # pd.read_csv("schdule_data.csv")

    # コサイン類似度の最も高いidを列を取得
    best_name = None
    _calc_cosine_similatiry(work_array, work_array)

    return OutputNameAndID("工事名", 1)


@app.get("/get_recommend_schedule_param")
def get_recommend_schedule_param(feature_1: int, feature_2: float, feature_3: int):
    return "WIP"


def _calc_cosine_similatiry(bec_1: np.array, bec_2: np.array) -> np.array:
    dot_product = np.dot(bec_1, bec_2)
    norm_1 = np.linalg.norm(bec_1)
    norm_2 = np.linalg.norm(bec_2)

    return dot_product / (norm_1 * norm_2)

