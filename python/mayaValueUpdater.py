class MayaValueUpdater(object):
	""" Class to update value in Maya from Nuke

		:type host: string
		:param host: name of the machine hosting.
	"""
	__noSurfaceInteractionWarning = 'STOP. No changes have been made as I was unable to tweak the diffuse and spec for some/all of your lights.'
	__noSurfaceInteractionWarning += 'Please add surface interaction components to all of your lights and try again.'

	__surfaceInteractionLightComponent ='tklRManSurfaceInteractionLightComponent'
	__surfaceInteractionLightComponents = [
		__surfaceInteractionLightComponent,
		'%s1' %__surfaceInteractionLightComponent
	]

	__tickleLightTypes = [
		'tklInfiniteAreaLight',
		'tklDistantLight',
		'tklSpotLight',
		'tklAreaLight'
	]

	_dictTickleParms = {
		'diffuse' : 'tklParmFdiffuseStrength',
		'specular' : 'tklParmFspecularStrength',
		'exposure' : 'tklParmFexposure',
		'tint' : 'tklParmCtintAdjust',
		'color' : 'tklParmClightColor',
	}


	@staticmethod
	def getImport():
		"""
		"""
		return "from mpc.nukeSee.mayaValueUpdater import MayaValueUpdater"

	@staticmethod
	def getMessage(dictValues, lightRig):
		"""
		"""
		message = 'mayaValueUpdater = MayaValueUpdater(%s, %s);' %(dictValues or '', lightRig)
		message += 'mayaValueUpdater.updateValues()'
		message += '");'
		return message

	def __init__(self, dictValues, lightRig):
		""" ctr.
		"""
		# import of maya here to avoid to have an import error while call the staticmethods.
		import maya.cmds as cmds

		self.__dictValues = dictValues
		self.__lightRig = lightRig

		self.__dictComponentFunctions = {
			'diffuse' : self.__diffuse,
			'specular' : self.__specular,
			'exposure' : self.__exposure,
			'tint' : self.__tint,
			'color' : self.__tint
		}

	def updateValues(self):
		"""
		"""

		cmds.select(self.__lightRig)

		# what is this list ?
		list =  cmds.listRelatives(cmds.ls(sl=1), ad=True)

		listTickleLight = [cmds.listRelatives(node, p = True) for node in list if cmds.nodeType(node) in self.__tickleLightTypes]
		listTickleLightShape = [node for node in list if cmds.nodeType(node) in self.__tickleLightTypes]
		listTickleSurfInter = [cmds.listRelatives(node, p = True) for node in listTickleLight if cmds.nodeType(node) == self.__surfaceInteractionLightComponent ]


		detectSurfInter = []

		for node in listTickleLight:

			for item in cmds.listRelatives(node, ad = True):

				if cmds.nodeType(item) == self.__surfaceInteractionLightComponent:
					cmds.confirmDialog(
						title='surfInterComponent Problem',
						message=self.__noSurfaceInteractionWarning,
						button=['OK'],
						defaultButton='Yes',
						cancelButton='No',
						dismissString='No'
					)

		for node in listTickleLight:
			nodeShape = cmds.listRelatives(node)[0]
			MLcategorie = cmds.getAttr(nodeShape + '.tklParmSaovCategory')

			for component in cmds.listRelatives(node):
				componentShape = cmds.listRelatives(component)

				if cmds.nodeType(componentShape) in self.__surfaceInteractionLightComponents:
					surfInteractLightComp = componentShape[0]
					break

				# TODO : is that at the good indentation level ???

				#Mathematical operation, addtition or subtration, between the current value and the new value for each
				#That pick up the current version in maya and addition or subtract the difference between Maya and Nuke

				channel = 0
				while channel < 8 : # onlu 8 channels available.

					if MLcategorie == "multilight%s" %str(channel):
						for key, param in self._dictTickleParms.items():
							function = self.__dictComponentFunctions[key]

							if key in self.__dictValues.keys() :
								function(
									componentShape = componentShape,
									nodeShape = nodeShape,
									attribut = param,
									value = self.__dictValues[key]
								)

	def __diffuse(self, **kwargs):
		""" Method to set the diffuse tickle parameter.
			Needed keys :
				- componentShape
				- attribut
				- value

			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.

			:raise: KeyError if missing key in kwargs
		"""
		return self.__multiply(
			kwargs['componentShape'],
			kwargs['attribut'],
			kwargs['value']
		)

	def __specular(self, **kwargs):
		""" Method to set the specular tickle parameter.
			Needed keys :
				- componentShape
				- attribut
				- value

			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.

			:raise: KeyError if missing key in kwargs
		"""
		return self.__multiply(
			kwargs['componentShape'],
			kwargs['attribut'],
			kwargs['value']
		)

	def __exposure(self, **kwargs):
		""" Method to set the exposure tickle parameter.
			Needed keys :
				- nodeShape
				- attribut
				- value

			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.

			:raise: KeyError if missing key in kwargs
		"""
		return self.__add(
			kwargs['nodeShape'],
			kwargs['attribut'],
			kwargs['value']
		)

	def __tint(self, **kwargs):
		""" Method to set the new values to the tint or color.
			The attribut needs to be a double3.
			Needed keys :
				- nodeShape
				- attribut
				- value : value here has to be a tuple !


			:rtype: bool
			:return: True if the new value was set to the attribut, False otherwise.
		"""
		attr = '%s.%s' %(
			kwargs['nodeShape'],
			kwargs['attribut']
		)
		values = kwargs['value']

		if cmds.objExists(attr):
			cmds.setAttr(
				attr,
				(cmds.getAttr(attr)[0][0]) * values[0],
				(cmds.getAttr(attr)[0][1]) * values[1],
				(cmds.getAttr(attr)[0][2]) * values[2],
				type = 'double3'
			)
			return True

		else :
			return False

	def __add(self, shape, attribut, value):
		""" Method to add the default value of the attribut and the value.
			The method will also set the result of the multiplication to the attribut.

			:type shape: string
			:param shape: name of the shape to work on.
			:type attribut: string
			:param attribut: name of the attribut to work on.
			:type value: int
			:param value: value to multiply with.

			:rtype: bool
			:return: True if the add and the set ran well, otherwise False
		"""
		attr = '%s.%s' %( shape, attribut)

		if cmds.objExists(attr):
			defaultValue = cmds.getAttr(attr)
			cmds.setAttr(attr, (defaultValue + value))
			return True

		else :
			return False

	def __multiply(self, shape, attribut, value):
		""" Method to multiply the default value of the attribut and the value.
			The method will also set the result of the multiplication to the attribut.

			:type shape: string
			:param shape: name of the shape to work on.
			:type attribut: string
			:param attribut: name of the attribut to work on.
			:type value: int
			:param value: value to multiply with.

			:rtype: bool
			:return: True if the multiplication and the set ran well, otherwise False
		"""
		attr = '%s.%s' %( shape, attribut)

		if cmds.objExists(attr):
			defaultValue = cmds.getAttr(attr)
			cmds.setAttr(attr, (defaultValue * value))
			return True

		else :
			return False

# Ni !
