from .storage import Behavior, BehaviorMap, BehaviorActionType, BehaviorList, BehaviorMap, BehaviorKeyMap
from .storage import StorageInit as BehaviorStorageInit

class BehaviorDomain:
    def __init__(self):
        BehaviorStorageInit()
    def get_behavior_by_id(self, behavior_id: int):
        return BehaviorMap.get(behavior_id)
    def get_all_behaviors():
        return BehaviorList
    def get_behaviors_by_scene_and_event(self, scene_key: int, event_key: int):
        return [b for b in BehaviorList if b.SenceKey == scene_key and b.EventKey == event_key]   
    def get_behavior_by_key(self, behavior_key: str):
        return BehaviorKeyMap.get(behavior_key)