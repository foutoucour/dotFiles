#Only use this file to set environment variables that will override
#jobshell settings. In most cases this file should remain empty
#
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login
#set autolistsetenv MAYsource $TOOLS/config/devenv.cshA_SCRIPT_PATH $TOOLS/maya/mel/versionControl/:${MAYA_SCRIPT_PATH}


# needs by mpcMake and setup my env dev
source $TOOLS/config/devenv.csh

# default PATH set up
setenv PATH $HOME/tools/scripts:$HOME/tools/bin/${UNAME}:${PATH}


#setenv CHARACTERRENDERSCRIPTS_VERSION 5.18

setenv AUTORENDER_VERSION 3.0
#setenv AUTOLOAD_TICKLE 1
#setenv AUTOLOAD_TICKLEHUB 1
#setenv AUTOLOAD_TICKLERMAN 1
setenv TICKLE_VERSION 4.6
setenv TICKLERMAN_VERSION 4.6
#setenv AUTOLOAD_MUPPETRAY 1
#setenv AUTOLOAD_MR_DISPLAY_DRIVER 1
#setenv MUPPETRAY_VERSION 5.2
#setenv RIPPLE_CONFIG_FILES $DEVTOOLS/config/muppetRay/$MUPPETRAY_VERSION/ripple/ripple.conf:"${RIPPLE_CONFIG_FILES}"
