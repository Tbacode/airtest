# -*- encoding=utf8 -*-
__author__ = "talefun"

from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from airtest.core.android.android import Android
dev = Android
poco = UnityPoco()

def newUser_skip():
    if poco("PrivateAddAgree(Clone)"):
        poco("btn_terms").click()
        sleep(10)
        act_name = dev.get_top_activity_name()
        
        poco("btn_Privacy")
        poco("btn_continue")
