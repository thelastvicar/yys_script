
from enum import Enum
from dataclasses import dataclass
from pynput.mouse import Controller, Button
from .storage import Action, ActionType, ActionDelayTime, ActionList, ActionMap, PerformAction
from .storage import StorageInit as actionStorageInit
import time
import random


class ActionDomain:
    def __init__(self):
        actionStorageInit()

    def GetAllAction(self):
        return ActionList

    def GetActionById(self, action_id: int):
        return ActionMap.get(action_id, None)

    def PerformAction(self, action_id: int, posX:int, posY:int):
        action = ActionMap.get(action_id, None)
        if action:
            PerformAction(action, posX, posY)
        else:
            print(f"No action found with ID: {action_id}")

