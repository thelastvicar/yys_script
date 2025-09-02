from . import Event, EventList, EventMap
from . import StorageInit as EventStorageInit

class EventDomain:
    def __init__(self):
        EventStorageInit()
    def get_event_by_id(event_id: int):
        return EventMap.get(event_id)
    def get_all_events():
        return EventList
    def get_event_by_key(event_key: str):
        return [e for e in EventList if e.EventKey == event_key]