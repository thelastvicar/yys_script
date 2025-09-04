

import pyautogui
import numpy as np
import cv2
import sys
import os
import time

#将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from enum import Enum
from dataclasses import dataclass

from . import ActionDomain, BehaviorDomain, EventDomain, FeatureDomain, SenceDomain


@dataclass
class Context:
    CurrentScreen = None  # 当前屏幕截图
    CurrentSenceKey: str = ""
    CurrentEventKey: str = ""
    CurrentBehaviorKey: str = ""
    CurrentFeatureKeys: list[str] = None
    CurrentFeaturePosDict: dict[str, tuple[int, int, int, int, int]] = None
    CurrentBehaviorKey: list[str] = None


def main():
    context = Context()
    FeatureDomain = FeatureDomain()
    return
    while True:
        print("scan start")

        # 获取屏幕尺寸
        screen_width, screen_height = pyautogui.size()
        # 捕获屏幕图像
        img = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
        # print(screen_width, screen_height)
        # 将图像转换为 numpy 数组
        frame = np.array(img)
        # 将颜色从 BGR 转换为 RGB
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 显示图像
        # cv2.imshow('Screen Capture', frame)

        context.CurrentScreen = img

        
        #特征匹配
        


