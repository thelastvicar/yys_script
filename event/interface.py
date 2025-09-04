from .storage import Event, EventList, EventMap
from .storage import StorageInit as EventStorageInit

class EventDomain:
    def __init__(self):
        EventStorageInit()
    def get_event_by_id(self, event_id: int):
        return EventMap.get(event_id)
    def get_all_events(self):
        return EventList
    def get_event_by_key(self, event_key: str):
        return [e for e in EventList if e.EventKey == event_key]