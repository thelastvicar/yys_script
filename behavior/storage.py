from enum import Enum
from dataclasses import dataclass


class BehaviorActionType(Enum):
    featurePos = 1
    fiexd = 2

@dataclass
class Behavior:
    Id: int
    Behaviorkey:str
    Name: str
    ScenceKey: str
    EventKey: str
    ActionId: int
    FeatureKey: str
    BehaviorActionType: BehaviorActionType
    Description: str


BehaviorList = [Behavior]
BehaviorMap = {}
BehaviorKeyMap = {}

def once(func):
    """装饰器：确保函数只执行一次"""
    executed = False
    result = None
    
    def wrapper(*args, **kwargs):
        nonlocal executed, result
        if not executed:
            result = func(*args, **kwargs)
            executed = True
        return result
    return wrapper

@once
def StorageInit ():
    BehaviorList.append(Behavior(
        Id=1, 
        Name="准备战斗",
        Behaviorkey="behavior_key_zhunbei",
        ScenceKey="sence_key_zhunbei",
        EventKey="event_key_shuayuhun",
        ActionId=1,
        FeatureId="feature_key_zhunbeianniu",
        BehaviorActionType=BehaviorActionType.featurePos,
        Description="准备战斗"
        ))
    
    for behavior in BehaviorList:
        BehaviorMap[behavior.Id] = behavior

    for behavior in BehaviorList:
        if behavior.Behaviorkey not in BehaviorKeyMap:
            BehaviorKeyMap[behavior.Behaviorkey] = behavior