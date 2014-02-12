 
#Do not try to edit ~/.cshrc, ~/.tcshrc or .login

# example mpcterm window size and font - uncomment to use
#setenv XTERM_FONT screen15
#setenv XTERM_GEOM 80x40



###########################################################################################################
# tab features
###########################################################################################################
set filec
set autolist




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

###########################################################################################################
# Custom commands
###########################################################################################################
## Find in environment feature.
### Find a string in environment files use by a job.
alias refresh 'cd;cd -'

alias gitka     'gitk --all &'

alias sourceMe  'source ~/config/cshrc.csh'



alias cleanTools    'rm -fr $DEVTOOLS/*'




set nobeep



if( $?prompt ) then
    #Need to be there to avoid to clash with git pulls
    oi -u
    bgBlack
endif

||||||| merged common ancestors
=======
# shortcut for MacOs
>>>>>>> DAG

