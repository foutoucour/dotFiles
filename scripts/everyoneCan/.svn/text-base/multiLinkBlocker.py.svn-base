import maya.cmds as cmds
import lightRigTypes


class SharedMethods:
    """
    Methods shared by Linker and Finder classes
    """
    def getTag(self, string):
        """
        alTag is a custom attribut used to get the name of the object 
            created for a lightRig without to get the name of the object. 
            This way user can rename without break anything
        @type string: string
        @param string: the name of the object 
        @rtype: string 
        @return: alTag attribut value or Null if no alTag attribut
        """
        try :
            return cmds.getAttr('%s.alTag' %string)
        except :
            return 'Null'
    
    def getType(self, string):
        """
        alType is a custom attribut, custom type of object for lightRig.
            This tag gives more information on the selection
        @type string: string
        @param string: the name of the object 
        @rtype: string 
        @return: alType attribut value or Null if no alType attribut
        """
        try :
            return cmds.getAttr('%s.alType' %string)
        except :
            return 'Null'
    
    def transform2Shape(self, string):
        """
        find the shape from a tranform.
        @type string: string
        @param string: name of the transform node
        @rtype: string
        @return: first value of cmds.listRelatives
        """
        return cmds.listRelatives(string)[0]
    
    def shape2Transform(self, string):
        """
        find the transform from a shape
        @type string: string
        @param string: name of the shape node
        @rtype: string
        @return: first value of cmds.listRelatives(p=1)
        """
        return cmds.listRelatives(string, p=1)[0]

class Linker(SharedMethods, lightRigTypes.TypeLister):
    """
    class to link a light with a blocker
    Light and blocker need to have alTag and alType
            (check lightRigTypes.TypeLister class)
    """
    def __init__(self):
        self.__sSpacer= "--------------------------------"
        self.__listBlockerShaderParameters = ['Switch',
                                              'Density',
                                              'Mode',
                                              'Shape',
                                              'WidthEdge',
                                              'HeightEdge',
                                              'DepthEdge',
                                              'Gradient',
                                              'GradientAxis',
                                              'CoordSys']
        self.__sLineName = 'Line'
        self.__iDebug = 0
        
    def setLight(self,string):
        """
        setting the transform node and the shape of the light
        @type string: string
        @param string: name of the light
        """
        self.__sLight = string
        self.__sLightShape = self.transform2Shape(self.__sLight)
    
    def setBlocker(self,string):
        """
        setting the transform node and the shape of the blocker
        @type string: string
        @param string: name of the blocker
        """
        self.__sBlocker = string
        self.__sBlockerShape = self.transform2Shape(self.__sBlocker)
        
    def add(self):
        """
        create a link between the light and the blocker
        skipped if a link already exist
        also create a line going from the blocker to the light 
        """
        print self.__sSpacer 
        print 'adding'
        self.__setup()
        self.__checkBlockerConnection()
        if self.__iAlreadyLinked == 0:
            self.__findFreeSlotForBlocker()
            self.__linkBlocker2shader()
#            self.__createLine()
            print '%s linked to %s' %(self.__sBlocker,
                                             self.__sLight)
        else:
            print '%s already Linked to %s' %(self.__sBlocker,
                                             self.__sLight)
        print self.__sSpacer
    
    def remove(self):
        """
        remove the link between the light and the blocker
        skipped if no link
        also delete the line going from the blocker to the light
        """
        print self.__sSpacer 
        print 'removing'
        self.__setup()
        self.__checkBlockerConnection()
        if self.__iAlreadyLinked == 1:
            # need to parse parameters of the shader and reset them
            # all parameters are reset 
            # by disconnecting input and output
            # Except for the CoordSys parameter (last one of the array)
            # which it is not connected to anything. It just needs to
            # reset its value
            for parameter in self.__listBlockerShaderParameters:
                sSlot = '%s.Blocker_%s[%d]' %(self.__sShader, 
                                          parameter,
                                          self.__iSlot)
                if self.__listBlockerShaderParameters.index(parameter) == (
                            len(self.__listBlockerShaderParameters)-1):
                    cmds.setAttr(sSlot, "(null)", type='string')
                else :
                    sInputConnection = cmds.connectionInfo(sSlot, sfd=1)
                    sOutputConnection = cmds.connectionInfo(sSlot, dfs=1)
                    if sInputConnection :
                        print sSlot, sInputConnection
                        cmds.disconnectAttr(sInputConnection, sSlot)
                    cmds.setAttr(sSlot, 0)
            # Deleting the line which goes 
            # from the blocker to the light
#            self.__removeLine()
        else :
            print '%s is not linked to %s' %(self.__sBlocker,
                                             self.__sLight)
        print self.__sSpacer

    def __setup(self):
        """
        finding everything that need the script
            - shader
            - LineGrp
            - plusMinusAverage nodes
        """
        if self.__iDebug == 1:
            print '__setup'
        if self.__iDebug == 1:
            print '__findShader' 
        for sConnection in cmds.listConnections(self.__sLight):
            if self.getType(sConnection) == self.liquidLightShader:
                self.__sShader = sConnection
                break
        if self.__iDebug == 1:
            print 'shader : ', self.__sShader
            
        if self.__iDebug == 1:
            print '__setBlockerChildren'       
        for sConnection in cmds.listConnections(self.__sBlockerShape):
            if self.getType(sConnection) == self.plusMinusAverage:                
                if '_Add4ShapeType' in self.getTag(sConnection):
                    self.__sShapeNode = sConnection
                    break
        for sConnection in cmds.listRelatives(self.__sBlocker):
            if self.getTag(sConnection) == 'al_Blocker_LinesGrp':
                self.__sLinesGrp = sConnection
        for sConnection in cmds.listConnections(self.__sBlocker):
            if self.getType(sConnection) == self.plusMinusAverage:
                if '_Mode' in self.getTag(sConnection):
                    self.__sModeNode = sConnection
        if self.__iDebug == 1:
            print 'LinesGrp :', self.__sLinesGrp
            print 'ShapeNode :', self.__sShapeNode
            print 'ModeNode :', self.__sModeNode
        return
       
    def __checkBlockerConnection(self):
        """
        Check if the light is connected to the light
        """
        self.__iAlreadyLinked = 0
        self.__iSlot=0
        while self.__iSlot < 4:
            self.__sBlockerCoordSys = cmds.getAttr(
                            '%s.Blocker_CoordSys[%d]' %(self.__sShader,
                                                        self.__iSlot))
            if self.__sBlockerCoordSys == self.__sBlockerShape:
                self.__iAlreadyLinked = 1
                break
            self.__iSlot += 1
     
    def __findFreeSlotForBlocker(self):
        """
        find a free slot in the light shader.
        Based on CoordSys slot
        """       
        self.__iSlot=0
        while self.__iSlot < 3:
            self.__sBlockerCoordSys = cmds.getAttr(
                            '%s.Blocker_CoordSys[%d]' %(self.__sShader,
                                                        self.__iSlot))
            self.__sBlockerCoordSys
            if self.__sBlockerCoordSys == '' or (
                    self.__sBlockerCoordSys == '(null)'):
                break
            self.__iSlot += 1
            
    def __linkBlocker2shader(self):
        """
        creation of the link between the light and the blocker
        """
        #======================================================================
        # Input connections
        #======================================================================
        cmds.setAttr('%s.Blockers_Switch' %self.__sShader, 1)
        cmds.setAttr('%s.Blocker_Switch[%d]' %(self.__sShader, self.__iSlot)
                        , 1)
        cmds.connectAttr('%s.Density' %self.__sBlocker,
                         '%s.Blocker_Density[%d]' %(self.__sShader,
                                                    self.__iSlot),f=1)
        cmds.connectAttr('%s.output2D.output2Dx' %self.__sModeNode,
                        '%s.Blocker_Mode[%d]' %(self.__sShader,
                                                self.__iSlot))
        cmds.connectAttr('%s.output2D.output2Dx' %self.__sShapeNode,
                        '%s.Blocker_Shape[%d]' %(self.__sShader,
                                                self.__iSlot))
        cmds.setAttr('%s.Blocker_CoordSys[%d]' %(self.__sShader, self.__iSlot)
                        ,self.__sBlockerShape, type='string' )
        cmds.connectAttr('%s.BlurX' %self.__sBlocker,
                         '%s.Blocker_WidthEdge[%d]' %(self.__sShader,
                                                      self.__iSlot))
        cmds.connectAttr('%s.BlurY' %self.__sBlocker,
                         '%s.Blocker_HeightEdge[%d]' %(self.__sShader,
                                                      self.__iSlot))
        cmds.connectAttr('%s.BlurZ' %self.__sBlocker,
                         '%s.Blocker_DepthEdge[%d]' %(self.__sShader,
                                                      self.__iSlot))
    
    def __removeLine(self):
        """
        remove the line between the blocker and the light
        """
        for sChild in cmds.listRelatives(self.__sBlocker):
            if cmds.ls(sChild, st=1)[1] == 'transform': 
                if cmds.getAttr('%s.alTag' %sChild) == (
                                     'al_Blocker_LinesGrp'):
                    for sGrpChild in cmds.listRelatives(sChild):
                         if cmds.getAttr('%s.alLightName' %sGrpChild) == (
                                                    self.__sLight):
                             cmds.delete(sGrpChild)
        
    def __createLine(self):
        """
        Create a display showing the link between the blocker 
        and the light
        """
        self.__sLine = cmds.spaceLocator(p=(0,0,0))
        # Tagging 
        cmds.addAttr(self.__sLine[0], sn='alTag', dataType='string', h=1)
        cmds.addAttr(self.__sLine[0], sn='alType', dataType='string')
        cmds.setAttr('%s.alTag' %self.__sLine[0], 
                     self.__sLine[0], type='string')
        cmds.setAttr('%s.alType' %self.__sLine[0], 
                     'Display', type='string')
        cmds.addAttr(self.__sLine[0], sn='alLightName', dataType='string')
        cmds.setAttr('%s.alLightName' %self.__sLine[0], self.__sLight,
                     type='string')
        # Set Parent
        cmds.parent(self.__sLine[0], self.__sLinesGrp)
        # set line to the center of the blocker
        cmds.setAttr('%s.translateX' %self.__sLine[0],0)
        cmds.setAttr('%s.translateY' %self.__sLine[0],0)
        cmds.setAttr('%s.translateZ' %self.__sLine[0],0)
        # settings to have the line going from the center
        # of the blocker
        cmds.setAttr('%s.translateZ' %self.__sLine[0], 1)
        cmds.move(0,0,-1, '%s.scalePivot' %self.__sLine[0], r=1)
        cmds.move(0,0,-1, '%s.rotatePivot' %self.__sLine[0], r=1)
        cmds.makeIdentity(self.__sLine[0], a=1, r=1)
        # looks like a line
        cmds.setAttr('%s.scaleX' %self.__sLine[0], 0)
        cmds.setAttr('%s.scaleY' %self.__sLine[0], 0)
        # Pointing to the light
        cmds.aimConstraint(self.__sLight, self.__sLine[0], aim=(0,0,1)) 
        
        # Setting expression for self.__sLine.scaleZ
        # equation of distance between 2 points (blocker and light)
        X = '%s.translateX-%s.translateX' %(self.__sLight,self.__sBlocker)
        X = 'pow(%s, 2)' %X
        Y = '%s.translateY-%s.translateY' %(self.__sLight,self.__sBlocker)
        Y = 'pow(%s, 2)' %Y
        Z = '%s.translateZ-%s.translateZ' %(self.__sLight,self.__sBlocker)
        Z = 'pow(%s, 2)' %Z
        sExpressionEquation = '%s.scaleZ = sqrt(%s+%s+%s)/2' %(self.__sLine[0],
                                                       X,Y,Z)
        sExpression = cmds.expression(n='%s.scaleZ' %self.__sLine[0],
                        o=self.__sLine[0],
                        s=sExpressionEquation)
        # Tagging the expression
        cmds.addAttr(sExpression, sn='alTag', dataType='string')
        cmds.addAttr(sExpression, sn='alType', dataType='string')
        cmds.setAttr('%s.alTag' %sExpression, sExpression, type='string')
        cmds.setAttr('%s.alType' %sExpression, 'Expression', type='string')
        # set as not selectable 
        cmds.setAttr('%s.overrideEnabled' %self.__sLine[0], 1)
        cmds.setAttr('%s.overrideDisplayType' %self.__sLine[0], 1)
        
class Finder(SharedMethods,lightRigTypes.TypeLister):
    """
    Finder will find lights and blockers in selection
    and will create an instance of Linker to create links 
    between each couples
    """
    def __init__(self):
        self.__listLights = []
        self.__listBlockers = []
        self.__iDebug = 0
        
    def add(self):
        """
        call for creation of link between blocker and light
        """
        self.__setSelections()
        if len(self.__listLights) > 0 and len(self.__listBlockers)>0 :
            for sLight in self.__listLights:
                for sBlocker in self.__listBlockers:
                    oLinker = Linker()
                    oLinker.setLight(sLight)
                    oLinker.setBlocker(sBlocker)
                    oLinker.add()
                    self.__clearSelection()
        else :
            print 'Need to select at least 1 blocker and 1 light' 
    
    def remove(self):
        """
        call for delete a link blocker and light
        """ 
        self.__setSelections()
        if len(self.__listLights) > 0 and len(self.__listBlockers)>0 :
            for sLight in self.__listLights:
                for sBlocker in self.__listBlockers:
                    oLinker = Linker()
                    oLinker.setLight(sLight)
                    oLinker.setBlocker(sBlocker)
                    oLinker.remove()
                    self.__clearSelection()
        else :
            print 'Need to select at least 1 blocker and 1 light'
    
            
    def __setSelections(self):
        """
        find the blocker and the light in selection
        by tag alType
        """
        for sel in cmds.ls(sl=1, l=1):
            if self.getType(sel) == self.blocker:
                self.__listBlockers.append(sel)
            elif self.getType(sel) == self.light:
                self.__listLights.append(sel)
        if self.__iDebug == 1:
            print 'Lights : ',self.__listLights
            print 'Blocker : ',self.__listBlockers
        return

    def __clearSelection(self):
        """
        clear selection to not have the last created line selected
        """
        cmds.select(clear=1)
