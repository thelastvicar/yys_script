from enum import Enum
from dataclasses import dataclass
import sys
import os

#将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common import once



class BehaviorActionType(Enum):
    featurePos = 1
    fiexd = 2

@dataclass
class Behavior:
    Id: int
    Behaviorkey:str
    Name: str
    SenceKey: str
    EventKey: str
    ActionId: int
    FeatureKey: str
    BehaviorActionType: BehaviorActionType
    Description: str


BehaviorList = []
BehaviorMap = {}
BehaviorKeyMap = {}

@once
def StorageInit ():
    BehaviorList.append(Behavior(
        Id=1, 
        Name="准备战斗",
        Behaviorkey="behavior_key_zhunbei",
        SenceKey="sence_key_zhunbei",
        EventKey="event_key_shuayuhun",
        ActionId=2,
        FeatureKey="feature_key_zhunbeianniu",
        BehaviorActionType=BehaviorActionType.featurePos,
        Description="准备战斗"
        ))
    
    for behavior in BehaviorList:
        BehaviorMap[behavior.Id] = behavior

    for behavior in BehaviorList:
        if behavior.Behaviorkey not in BehaviorKeyMap:
            BehaviorKeyMap[behavior.Behaviorkey] = behavior