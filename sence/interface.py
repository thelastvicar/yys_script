from .storage import Sence, SenceKeyMap, SenceMap, SenceList, StorageInit as SenceStorageInit
from .ast import EvaluateFeatureDsl

class SenceDomain:
    def __init__(self):
        SenceStorageInit()

    def GetSenceById(self, sence_id: int):
        return SenceMap.get(sence_id, None)
    
    def GetSenceByKey(self, sence_key: str):
        return SenceKeyMap.get(sence_key, None)
    
    def GetAllSence(self):
        return SenceList
    
    # 场景匹配
    def MatchSence(self, featureValues: dict):
        SenceList = self.GetAllSence()
        resSenceList = []
        for sence in SenceList:
            featureKey = sence.SenceFeatureDsl
            result = EvaluateFeatureDsl(sence.SenceFeatureDsl, featureValues)
            if result:
                resSenceList.append(sence)
        return resSenceList
