#Only use this file to set environment variables that will override
#jobshell settings. In most cases this file should remain empty
#
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login
#set autolistsetenv MAYsource $TOOLS/config/devenv.cshA_SCRIPT_PATH $TOOLS/maya/mel/versionControl/:${MAYA_SCRIPT_PATH}

source /software/tools_RND_PATCH/autoRenderBeta/env.csh

# needs by mpcMake and setup my env dev
source $TOOLS/config/devenv.csh

# default PATH set up
setenv PATH $HOME/tools/scripts:$HOME/tools/bin/${UNAME}:${PATH}

setenv MOZ_DISABLE_PANGO 1


if ($?JOB) then

    #setenv GIGGLE_IMPORT_PATH ${DEVTOOLS}/gubbins/giggle/${GIGGLE_VERSION}/scripts/readPackageAPI/${READPACKAGEAPI_VERSION}:${GIGGLE_IMPORT_PATH}
    setenv HUBPKG_CHARACTER_CONFIG_PATH $DEVTOOLS/gubbins/giggle/$GIGGLE_VERSION/scripts/characterPackages/$CHARACTERPACKAGES_VERSION
    #setenv HUB_PACKAGE_CONFIGFILES ${HUBPKG_CHARACTER_CONFIG_PATH}/characterPackages.ggl:${HUBPKG_CHARACTER_CONFIG_PATH}/characterPackages.ggl:${HUB_PACKAGE_CONFIGFILES}
    #setenv MAYA_SCRIPT_PATH ${MAYA_SCRIPT_PATH}:${DEVTOOLS}/maya/2011/mel/CharacterPackages/${CHARACTERPACKAGES_VERSION}
endif

