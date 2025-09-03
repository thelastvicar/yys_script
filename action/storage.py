import sys
import os

from enum import Enum
from dataclasses import dataclass
from pynput.mouse import Controller, Button
import time
import random
import pyautogui

#将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from common import once


class ActionType(Enum):
    SingleClick = 1
    DoubleClick = 2

class ActionDelayTime(Enum):
    Random = 1
    Fixed = 2

# 动作定义
@dataclass
class Action:
    Id: int
    ActionType: ActionType
    DelayTime: ActionDelayTime
    DelayTimeValue: int  # in milliseconds
    Description: str


def click(x, y):
    global Prex
    global Prey
    mouse = Controller()

    end_x = x+random.uniform(0, 100)
    end_y = y+random.uniform(-12, 120)

    # 移动鼠标到指定位置
    mouse.position = (end_x, end_y)

    # 按下鼠标左键
    mouse.press(Button.left)

    steps = int(20+random.uniform(-5, 5))  # 增加步数
    for i in range(steps):
        pyautogui.moveTo(Prex + (end_x - Prex) * i / steps, Prey + (end_y - Prey) * i / steps,
                         duration=0.005)


    Prex = end_x
    Prey = Prey

    # 模拟长按的时间（以秒为单位）
    time.sleep(random.uniform(0.05, 0.12))

    # 松开鼠标左键
    mouse.release(Button.left)
    position = pyautogui.position()
    Prex = position.x
    Prey = position.y


def PerformAction(action: Action, posX:int, posY:int):

    if action.DelayTime == ActionDelayTime.Random:
        delay = random.randint(0, action.DelayTimeValue) / 1000.0
    else:
        delay = action.DelayTimeValue / 1000.0

    # 动作延迟
    time.sleep(delay)


    if action.ActionType == ActionType.SingleClick:
        print(f"Performing single click at ({posX}, {posY}) after {delay:.2f} seconds delay.")
        click(posX, posY)
    elif action.ActionType == ActionType.DoubleClick:
        print(f"Performing double click at ({posX}, {posY}) after {delay:.2f} seconds delay.")
        click(posX, posY)
        time.sleep(0.1)  # Short delay between clicks
        click(posX, posY)
    else:
        print("Unknown action type.")
        

ActionList = [Action]
ActionMap = {}


@once
def StorageInit ():
    ActionList.append(Action(
        Id=1, 
        ActionType=ActionType.SingleClick,
        DelayTime=ActionDelayTime.Random,
        DelayTimeValue=500,
        Description="单击"
        ))
    ActionList.append(Action(
        Id=2,
        ActionType=ActionType.DoubleClick,
        DelayTime=ActionDelayTime.Random,
        DelayTimeValue=500,
        Description="双击"
        ))
    
    for action in ActionList:
        ActionMap[action.Id] = action