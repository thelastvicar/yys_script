from .storage import featureCompareType, feature, featureList, featureKeyMap, StorageInit as featureStorageInit
from .compare import CompareImages


class FeatureDomain:
    def __init__(self):
        featureStorageInit()

    def findFeature(self, feature_key:str):
        return featureKeyMap.get(self, feature_key)
    
    def getAllFeatures(self):
        return featureList
    
    def matchFeature(self, feature_key:str, screen):
        feature = featureKeyMap.get(feature_key)
        if feature is None:
            print("No feature found with key: {feature_key}")
            return None
        if feature.CompareType == featureCompareType.pic:
            match_result = CompareImages(screen, feature.Template, feature.CompareThreshold, feature.MinScale, feature.MaxScale, feature.ScaleStep)
            return match_result
        return None