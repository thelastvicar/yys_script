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



SenceList = [Sence]
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

    for sence in SenceList:
        SenceMap[sence.Id] = sence

    for sence in SenceList:
        if sence.SenceKey not in SenceKeyMap:
            SenceKeyMap[sence.SenceKey] = sence