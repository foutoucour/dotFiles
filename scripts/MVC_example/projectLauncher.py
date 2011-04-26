# -*- coding: utf-8 -*-
import sys

sCurrentScriptPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(sCurrentScriptPath)

import ProjectUI as PUI
reload(PUI)
import ProjectControl as PCtrl
reload(PCtrl)

oGui = PUI.UI()
oCtrl = PCtrl.Control(oGui )

