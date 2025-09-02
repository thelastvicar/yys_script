from enum import Enum
from dataclasses import dataclass

@dataclass
class Event:
    Id: int
    EventKey: str
    Description: str
    
EventList = [Event]
EventMap = {}
EventKeyMap = {}

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
    EventList.append(Event(
        Id=1, 
        EventKey="event_key_shuayuhun",
        Description="刷御魂"
        ))
    
    for event in EventList:
        EventMap[event.Id] = event
        EventKeyMap[event.EventKey] = event