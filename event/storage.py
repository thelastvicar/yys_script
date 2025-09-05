from enum import Enum
from dataclasses import dataclass

import sys
import os

#将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common import once


@dataclass
class Event:
    Id: int
    EventKey: str
    Description: str
    CheckFeatureKeys: list[str] = None
    
EventList = []
EventMap = {}
EventKeyMap = {}

@once
def StorageInit ():
    EventList.append(Event(
        Id=1, 
        EventKey="event_key_shuayuhun",
        Description="刷御魂",
        CheckFeatureKeys=["feature_key_zhunbeianniu", "feature_key_tiaozhananniu", "feature_key_shengli", "feature_key_shengli2"]
        ))
    
    for event in EventList:
        EventMap[event.Id] = event
        EventKeyMap[event.EventKey] = event