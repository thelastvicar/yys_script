from enum import Enum
from dataclasses import dataclass
import cv2

import sys
import os

@dataclass
class Sence:
    Id: int
    SenceKey: str
    Name: str
    Description: str
    SenceFeatureDsl: str



SenceList = []
SenceMap = {}
SenceKeyMap = {}


def StorageInit():
    SenceList.append(Sence(
        Id=1,
        SenceKey="sence_key_zhunbei",
        Name="准备界面",
        Description="准备界面",
        SenceFeatureDsl="feature_key_zhunbeianniu"
    ))

    SenceList.append(Sence(
        Id=2,
        SenceKey="sence_key_tiaozhan",
        Name="御魂挑战界面",
        Description="御魂挑战界面",
        SenceFeatureDsl="feature_key_tiaozhananniu"
    ))

    SenceList.append(Sence(
        Id=3,
        SenceKey="sence_key_shengli",
        Name="御魂结算界面",
        Description="御魂结算界面",
        SenceFeatureDsl="feature_key_shengli"
    ))

    SenceList.append(Sence(
        Id=4,
        SenceKey="sence_key_shengli2",
        Name="御魂结算界面2",
        Description="御魂结算界面2",
        SenceFeatureDsl="feature_key_shengli2"
    ))

    for sence in SenceList:
        SenceMap[sence.Id] = sence

    for sence in SenceList:
        if sence.SenceKey not in SenceKeyMap:
            SenceKeyMap[sence.SenceKey] = sence