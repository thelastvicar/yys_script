import sys
import os

from enum import Enum
from dataclasses import dataclass
from pynput.mouse import Controller, Button
import time
import random
import pyautogui

import ctypes
import time
from ctypes import wintypes
# 定义Windows API常量
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_MOVE = 0x0001
user32 = ctypes.WinDLL("user32", use_last_error=True)

#将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

pyautogui.FAILSAFE = False

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


Prex = 1000
Prey = 1000

def click(x, y):
    global Prex
    global Prey
    mouse = Controller()

    end_x = x+random.uniform(0, 100)
    end_y = y+random.uniform(0, 120)

    # 移动鼠标到指定位置
    # mouse.position = (end_x, end_y)

    steps = int(10+random.uniform(-5, 5))  # 增加步数
    for i in range(steps):
        pyautogui.moveTo(Prex + (end_x - Prex) * i / steps, Prey + (end_y - Prey) * i / steps,
                         duration=0.001)


    Prex = end_x
    Prey = end_y

    
    # 按下鼠标左键
    mouse.press(Button.left)

    # 模拟长按的时间（以秒为单位）
    time.sleep(random.uniform(0.01, 0.03))

    # 松开鼠标左键
    mouse.release(Button.left)
    position = pyautogui.position()
    Prex = position.x
    Prey = position.y


def doubleClick(x, y):
    global Prex
    global Prey
    mouse = Controller()

    end_x = x+random.uniform(0, 100)
    end_y = y+random.uniform(0, 120)

    # 移动鼠标到指定位置
    # mouse.position = (end_x, end_y)

    steps = int(10+random.uniform(-5, 5))  # 增加步数
    for i in range(steps):
        pyautogui.moveTo(Prex + (end_x - Prex) * i / steps, Prey + (end_y - Prey) * i / steps,
                         duration=0.001)


    Prex = end_x
    Prey = end_y

    
    # 按下鼠标左键
    mouse.press(Button.left)

    # 模拟长按的时间（以秒为单位）
    time.sleep(random.uniform(0.01, 0.03))

    # 松开鼠标左键
    mouse.release(Button.left)
    position = pyautogui.position()
    
    time.sleep(random.uniform(0.01, 0.03))

    # 按下鼠标左键
    mouse.press(Button.left)

    # 模拟长按的时间（以秒为单位）
    time.sleep(random.uniform(0.01, 0.03))

    # 松开鼠标左键
    mouse.release(Button.left)
    position = pyautogui.position()
    Prex = position.x
    Prey = position.y

def doubleClickHard(x, y):
    global Prex
    global Prey

    end_x = x+random.uniform(-50,50)
    end_y = y+random.uniform(-50,50)

    # 移动鼠标到指定位置
    # mouse.position = (end_x, end_y)

    steps = int(10+random.uniform(-5, 5))  # 增加步数
    for i in range(steps):
        pyautogui.moveTo(Prex + (end_x - Prex) * i / steps, Prey + (end_y - Prey) * i / steps,
                         duration=0.001)

    end_x = int(round(end_x))
    end_y = int(round(end_y))

    Prex = end_x
    Prey = end_y

    """在(x,y)位置模拟硬件级点击"""
    # 移动鼠标
    user32.SetCursorPos(end_x, end_y)
    time.sleep(0.01)  # 等待移动完成
        
    # 按下左键
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, end_x, end_y, 0, 0)
    time.sleep(random.uniform(0.01, 0.03))
        
    # 释放左键
    user32.mouse_event(MOUSEEVENTF_LEFTUP, end_x, end_y, 0, 0)

    time.sleep(random.uniform(0.01, 0.03))

    user32.SetCursorPos(end_x, end_y)
    time.sleep(0.01)  # 等待移动完成
        
    # 按下左键
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN, end_x, end_y, 0, 0)
    time.sleep(random.uniform(0.01, 0.03))
        
    # 释放左键
    user32.mouse_event(MOUSEEVENTF_LEFTUP, end_x, end_y, 0, 0)
    


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
        doubleClickHard(posX, posY)
    else:
        print("Unknown action type.")
        

ActionList = []
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
        DelayTimeValue=10,
        Description="双击"
        ))
    
    for action in ActionList:
        ActionMap[action.Id] = action