#Only use this file to set environment variables that will override
#jobshell settings. In most cases this file should remain empty
#
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login
#set autolistsetenv MAYsource $TOOLS/config/devenv.cshA_SCRIPT_PATH $TOOLS/maya/mel/versionControl/:${MAYA_SCRIPT_PATH}


# needs by mpcMake and setup my env dev
source $TOOLS/config/devenv.csh

###########################################################################################################
# custom environment variable
###########################################################################################################
setenv ECLIPSE_VERSION 3.6.0
setenv J_SVN 'http://svn.mpc.local/repos'
setenv JOBVERBOSE 1


###########################################################################################################
# Local setting depending on DIST 
###########################################################################################################





setenv MAYA_PRELOAD ${DEVTOOLS}/maya/${MAYA_MAJOR_VERSION}/preload/lib64/XtWidgetIntercept.so
unsetenv MAYA_PRELOAD



