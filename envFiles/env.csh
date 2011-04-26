#Only use this file to set environment variables that will override
#jobshell settings. In most cases this file should remain empty
#
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login
#set autolistsetenv MAYsource $TOOLS/config/devenv.cshA_SCRIPT_PATH $TOOLS/maya/mel/versionControl/:${MAYA_SCRIPT_PATH}


# needs by mpcMake and setup my env dev
source $TOOLS/config/devenv.csh

# default PATH set up
setenv PATH $HOME/tools/scripts:$HOME/tools/bin/${UNAME}:${PATH}



