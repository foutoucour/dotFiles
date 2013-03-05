 
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login

# example mpcterm window size and font - uncomment to use
#setenv XTERM_FONT screen15
#setenv XTERM_GEOM 80x40



###########################################################################################################
# tab features
###########################################################################################################
set filec
set autolist


<<<<<<< HEAD
## shell title feature
alias _shellTitleFunc 'source /mpc/people/jordi-r/config/shellTitleFunc.tcsh'
||||||| merged common ancestors
## shell title feature
alias _shellTitleFunc 'source /mpc/people/jordi-r/config/shellTitleFunc.tcsh'
## Trick to not have a shell with the same size than the window of gvim.
### The eval create $COLUMNS and $LINES equal to the current size of the shell
### so we need to store them in variables.
alias _getSize      'eval `resize`;set columns=$COLUMNS;set lines=$LINES;'
alias _resizeShell  'resize -s $lines $columns;'
=======
>>>>>>> DAG

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
alias ls        'ls -h --color=auto'
alias la        'ls -a'
alias lt        'ls -lrt'

alias job		'source $TOOLS/scripts/job.csh \!*;_shellTitleFunc;cd -'
alias cd       	'cd \!:*;_prompt;'
alias popd     	'popd \!:*;_prompt;'
alias pushd    	'pushd \!:*;_prompt;'
alias _vim		/mpc/people/jordi-r/apps/vim/bin/vim
alias gvim      '_vim -c gvim'

###########################################################################################################
# Custom commands
###########################################################################################################
## Find in environment feature.
### Find a string in environment files use by a job.
alias findInEnv		'/mpc/people/jordi-r/config/findInEnv'
alias refresh 'cd;cd -'

alias gitka     'gitk --all &'

alias sourceMe  'source ~/config/cshrc.csh'



alias cleanTools    'rm -fr $DEVTOOLS/*'

alias m				'maya &'
alias mb            'maya -batch &'
alias bgColor		'echo -n "\033]11;\!*\033\\"'
alias bgBlack   	'bgColor black'
alias mayaNew 		'rm -fr $HOME/maya/$MAYA_VERSION-x64/prefs/shelves/*;maya &'

alias echoGitDiff   'echo "cd `echo $PWD` && git difftool -y && cd -"'
# clean all builds, make optmized install on 6 cores and if success show the finishing time
alias makeInstall		'make clean; rm .build -fr;make install VERBOSE=0 OPTIMIZED=1 -j 6 &&echo&&echo&&date&&echo&&echo'
alias makeI             'makeInstall'

# like MakeInstall but remove the tool folder first.
# Useful to be sure to have a clean environment.
alias makeNewInstall 	'rm -fr ~/tools/*;makeInstall'
alias makeN             'makeNewInstall'

alias makeSphinx        'makeInstall&& make sphinx'
alias makeS             'makeSphinx'


# Do the install and launch maya (lazyness throne ;) )
alias mmakeI            'makeI && maya&'
alias mmakeN            'makeN && maya&'

# Do the install and launch maya batch (lazyness throne ;) )
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

if ( $?PYTHON_VERSION ) then
    alias fixMpcMaya "cd ~/tools/python/$PYTHON_VERSION/$PLATFORM/maya/versions; ln -s v$MAYA_MAJOR_VERSION v`echo $MAYA_VERSION | sed -e 's/\./_/'`&& echo 'FIXED'; cd -"
endif

## RCS
alias Rco			'co -l'
alias Rci			'ci -u'
###########################################################################################################
# folder shortcuts
###########################################################################################################
alias softScripts		 	'cd /software/tools/scripts'
<<<<<<< HEAD
alias centralVersionPath 	'cd $TOOLS/config/environment/london/$MAYA_MAJOR_VERSION/$MUGGINS_VERSION/$PLATFORM'
alias disciplinesPath		'cd /software/tools/config/disciplines/'
||||||| merged common ancestors
alias w						'cd ~/workspace/'
alias wg					'cd ~/workspace/git/'
alias t						'cd ~/tools/'
alias T						'cd $TOOLS'
alias c						'cd ~/config/'
alias centralVersionPath 	'cd $TOOLS/config/environment/london/$MAYA_MAJOR_VERSION/$MUGGINS_VERSION/$PLATFORM'
alias disciplinesPath		'cd /software/tools/config/disciplines/'
=======
alias w						'cd ~/workspace/'
alias wg					'cd ~/workspace/git/'
alias t						'cd ~/tools/'
alias T						'cd $TOOLS'
alias c						'cd ~/config/'
alias centralVersionPath 'cd $TOOLS/config/environment/london/$MAYA_MAJOR_VERSION/$MUGGINS_VERSION/$PLATFORM'
alias disciplinesPath'cd /software/tools/config/disciplines/'
>>>>>>> DAG

alias cure 'echo "\!:1 >> \!:2 in `grep -l \!:1 *`";sed -i "s/\!:1/\!:2/g" `grep -rl \!:1 *`'




set nobeep


<<<<<<< HEAD
#vim like aliases
# As they are really short I prefer to use ":" in front of them to avoid clashes
alias w 'cd ~/workspace/'
alias wg 'cd ~/workspace/git/'
alias t 'cd ~/tools/'
alias T 'cd $TOOLS'
alias c 'cd ~/config/'
alias g 'gvim'
alias r 'refresh'
alias q 'exit'
alias e 'exit'
alias E 'exit'
alias ff 'firefox &'
alias hg 'history | grep \!*'
alias lg 'ls -1 | grep -i \!*'
alias cg 'cd `ls | grep -i \!*`'
alias go 'wg; cg'
alias eg 'env | grep -i \!*'
alias mmi 'mmakeI'
alias mmn 'mmakeN'
alias mi 'makeInstall'
alias ms 'makeSphinx'
alias mn 'makeNewInstall'
alias sm 'sourceMe'
alias ct 'cleanTools'
alias gc 'g ~/config/cshrc.csh'
alias ge 'g ~/config/env.csh'

if( $?prompt ) then
    #Need to be there to avoid to clash with git pulls
    oi -u
    bgBlack
endif

||||||| merged common ancestors
=======
# shortcut for MacOs
>>>>>>> DAG

