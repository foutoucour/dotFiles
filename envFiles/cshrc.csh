#
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login

# example mpcterm window size and font - uncomment to use
#setenv XTERM_FONT screen15
#setenv XTERM_GEOM 80x40

# default PATH set up
setenv PATH /mpc/people/jordi-r/dotFiles/scripts:$HOME/tools/scripts:$HOME/tools/bin/${UNAME}:${PATH}


###########################################################################################################
# tab features
###########################################################################################################
set filec
set autolist

###########################################################################################################
# functions
###########################################################################################################

## prompt feature
#alias _prompt 'set prompt="%U%T%u:`whoami`:%B$cwd%b: > "'
alias _prompt 'set prompt="%U%T%u:`whoami`:%B%~%b > "'


## shell title feature
alias _shellTitleFunc 'source /mpc/people/jordi-r/config/shellTitleFunc.tcsh'
## Trick to not have a shell with the same size than the window of gvim.
### The eval create $COLUMNS and $LINES equal to the current size of the shell
### so we need to store them in variables.
alias _getSize      'eval `resize`;set columns=$COLUMNS;set lines=$LINES;'
alias _resizeShell  'resize -s $lines $columns;'

###########################################################################################################
# setting of shell
###########################################################################################################

## change of dir colors
eval `dircolors -c "${HOME}"/.dir_colors`

###########################################################################################################
# mapping of system commands
###########################################################################################################
alias cd.. 		'cd ..'
alias u         'cd ..'
alias .. 		'cd ..'
alias rm 		'rm -r'
alias cp 		'cp -r'
alias mkdir     'mkdir -p'
alias mv 		'mv -i'
alias grep      'grep --color=auto'

# only for linux
alias dir       'dir --color'
#alias ls        'ls -h --group-directories-first --color=auto'

alias job		'source $TOOLS/scripts/job.csh \!*;_shellTitleFunc;cd -'
alias cd       	'cd \!:*;_prompt;'
alias popd     	'popd \!:*;_prompt;'
alias pushd    	'pushd \!:*;_prompt;'
alias _vim		/mpc/people/jordi-r/apps/vim/bin/vim
alias gvim      '_vim -c gvim'

if ($?TERM) then
    if (`echo ${DESKTOP_SESSION}` == 'WindowMaker') then
        alias gvim      '_getSize;_vim -c gvim \!:*;_resizeShell;'
    endif
endif

###########################################################################################################
# Custom commands
###########################################################################################################
## Find in environment feature.
### Find a string in environment files use by a job.
alias findInEnv		'/mpc/people/jordi-r/config/findInEnv'
alias findInEnv2011	'/mpc/people/jordi-r/config/findInEnv2011'
alias nameShell 	'echo -n "\033]2;\!:*\033\\";echo -n "\033]1;\!:*\033\\"'

alias gitka     'gitk --all &'

alias g			'gvim'
alias ws 		'scite `which \!:*`'
alias sw 		'ws'

alias refresh     'cd;cd -'


alias cleanTools    'rm -fr $DEVTOOLS/*'

alias j2011 	'job -d maya2011_\!:*'
alias j2011rnd 	'job -d maya2011_\!:1 et2 rnd/rnd_pipeline'

alias m				'maya &'
alias mb            'maya -batch &'
alias hg			'history | grep \!*'
alias lg			'ls -1 | grep -i \!*'
alias cg            'cd `ls | grep -i \!*`'
alias bgColor		'echo -n "\033]11;\!*\033\\"'
alias bgBlack   	'bgColor black'
alias mayaNew 		'rm -fr $HOME/maya/$MAYA_VERSION-x64/prefs/shelves/*;maya &'

alias makeInstall		'make clean;make install OPTIMIZED=1 -j 6 && date'
alias makeI                 'makeInstall'
alias makeNewInstall 	'rm -fr ~/tools/*;makeInstall'
alias makeN                 'makeNewInstall'

alias mmakeI            'makeI && m'
alias mmakeN            'makeN && m'

alias bmakeI            'makeI && mb'
alias bmakeN            'makeN && mb'

alias topu	'top -u $USER'

## oi shortcut
### Quick oi
alias qoi	"echo \!:2 | oi -i \!:1"

alias soi "/mpc/people/jordi-r/config/oiSpam.py"
alias rob		'oi robert-t'
alias qRob		'qoi robert-t \!:1'
alias qrob		'qRob'
alias ben		'oi benoit-l'
alias qBen		'qoi benoit-l \!:1'
alias qben		'qBen'
alias nico		'oi nicolas-c'

## RCS
alias Rco			'co -l'
alias Rci			'ci -u'
###########################################################################################################
# folder shortcuts
###########################################################################################################
alias softScripts		 	'cd /software/tools/scripts'
alias w						'cd ~/workspace/'
alias wg					'cd ~/workspace/git/'
alias t						'cd ~/tools/'
alias T						'cd $TOOLS'
alias c						'cd ~/config/'
alias centralVersionPath 	'cd $TOOLS/config/environment/london/$MAYA_MAJOR_VERSION/$MUGGINS_VERSION/$PLATFORM'
alias disciplinesPath		'cd /software/tools/config/disciplines/'

alias cure             'echo "\!:1 >> \!:2 in `grep -l \!:1 *`";sed -i "s/\!:1/\!:2/g" `grep -l \!:1 *`'

if ($?TERM) then
    if ($?DESKTOP_SESSION) then
        _shellTitleFunc
        _prompt
        bgBlack
    endif
endif


set nobeep



