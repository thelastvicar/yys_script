from enum import Enum
from dataclasses import dataclass
import cv2
import sys
import os

# 将上级目录添加到模块搜索路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


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


class featureCompareType(Enum):
    pic = 1
    text = 2
    special = 3


@dataclass
class feature:
    # 无默认值参数（必填）
    Id: int
    FeatureKey: str  # 修正类型为 str（匹配传入的字符串）
    CompareType: featureCompareType
    CompareThreshold: float
    LimitEventKeys: list[str]
    MinScale: float
    MaxScale: float
    ScaleStep: int
    # 有默认值参数（可选）
    TemplatePath: str = ""
    Template: cv2.Mat = None  # 明确类型，放在最后


# 初始化：空列表（避免放入类本身）
featureList = []
featureMap = {}
featureKeyMap = {}


@once
def StorageInit():
    # 创建 feature 实例（参数名与 dataclass 一致）
    featureList.append(feature(
        Id=1,
        FeatureKey="feature_key_zhunbeianniu",
        CompareType=featureCompareType.pic,
        CompareThreshold=0.7,
        LimitEventKeys=["event_key_shuayuhun"],
        TemplatePath="templates\zhunbeianniu.png",
        MinScale=0.5,
        MaxScale=1.2,
        ScaleStep=5,
    ))

    # 加载模板图片（遍历实例，避免变量名覆盖）
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    for feat in featureList:
        path = os.path.join(current_script_dir, feat.TemplatePath)
        if feat.TemplatePath != "" and os.path.exists(path):
            feat.Template = cv2.imread(path)
        else:
            print(f"警告：模板路径 {path} 不存在")

    # 构建 Id 到实例的映射
    for feat in featureList:
        featureMap[feat.Id] = feat

    # 构建 FeatureKey 到实例的映射
    for feat in featureList:
        featureKeyMap[feat.FeatureKey] = feat