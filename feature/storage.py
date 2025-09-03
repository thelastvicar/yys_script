from enum import Enum
from dataclasses import dataclass

import sys
import os

#将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common import once



class featureCompareType(Enum):
    pic = 1
    text = 2
    special = 3

@dataclass
class feature:
    Id:int
    FeatureKey:int
    CompareType:featureCompareType
    CompareThreshold:int
    LimitEventKeys:list[str]


featureList = [feature]
featureMap = {}
featureKeyMap = {}

@once
def StorageInit():
    featureList.append(feature(
        id=1,
        FeatureKey="feature_key_zhunbeianniu",
        CompareType=featureCompareType.pic,
        CompareThreshold=80,
        LimitEventKeys=["event_key_shuayuhun"],
    ))

    for feature in featureList:
        featureMap[feature.Id] = feature

    for feature2 in featureKeyMap:
        featureKeyMap[feature2.FeatureKey] = feature2