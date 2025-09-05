

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

from feature import FeatureDomain
from behavior import BehaviorDomain
from event import EventDomain
from sence import SenceDomain
from action import ActionDomain

# BehaviorDomain, EventDomain, FeatureDomain, SenceDomain


@dataclass
class Context:
    CurrentScreen = None  # 当前屏幕截图
    CurrentSenceKey: str = ""
    CurrentEventKey: str = ""
    CurrentBehaviorKey: str = ""
    CurrentFeatureKeys: list[str] = None
    CurrentFeaturePosDict: dict = None
    CurrentBehaviorKey: list[str] = None


if __name__ == "__main__":
    print("scan features for event:")
    context = Context()
    context.CurrentFeatureKeys = []
    context.CurrentFeaturePosDict = {}
    context.CurrentBehaviorKey = []
    featureDomain = FeatureDomain()
    behaviorDomain = BehaviorDomain()
    eventDomain = EventDomain()
    senceDomain = SenceDomain()
    actionDomain = ActionDomain()
    
    # 获取执行事件
    event = eventDomain.get_event_by_id(1)
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
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 显示图像
        # cv2.imshow('Screen Capture', frame)

        context.CurrentScreen = frame

        #特征匹配
        featureHitMap = dict()
        features = event.CheckFeatureKeys
        for featureKey in features:
            featurePoses = featureDomain.matchFeature(featureKey, context.CurrentScreen)
            if len(featurePoses) > 0:
                featureHitMap[featureKey] = True
                context.CurrentFeatureKeys.append(featureKey)
                context.CurrentFeaturePosDict[featureKey] = featurePoses
                print(f"Feature {featureKey} matched at positions: {featurePoses}")    
        
        #场景匹配
        hitSences = senceDomain.MatchSence(featureHitMap)
        for sence in hitSences:
            print(f"Matched Sence: {sence.SenceKey}")
            context.CurrentSenceKey = sence.SenceKey
        
        #行为匹配
        hitBehaviors = behaviorDomain.get_behaviors_by_scene_and_event(sence.SenceKey, event.EventKey)
        for behavior in hitBehaviors:
            print(f"Matched Behavior: {behavior.Behaviorkey}- {behavior.ActionId}")
            context.CurrentBehaviorKey.append(behavior.Behaviorkey)
            
            #执行行为
            action = actionDomain.GetActionById(behavior.ActionId)
            for pos in context.CurrentFeaturePosDict.get(behavior.FeatureKey, []):
                print(f"Performing Action: {action.Id} at position {pos}")
                actionDomain.PerformAction(action.Id, pos[0],pos[1])
                

        # context清理
        context = Context()
        time.sleep(0.5)
        break

