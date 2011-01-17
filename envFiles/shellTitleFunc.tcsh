#!/bin/tcsh -f
# setting shellTitle, iconTitle and background color for different cases



if ( $?JOB) then
	if ( $?DISCIPLINE) then
		set discipline_tmp = $DISCIPLINE
	else
        #Need to feed the variable if we job without using any discipline.
		set discipline_tmp = "None"
	endif
	
	if ($?SHOT) then
			#set sTitle="$JOB/$SHOT $DIST $PWD"
			set sTitle="$JOB/$SHOT-$DIST-$discipline_tmp"
			set sIconTitle="$SHOT-$DIST"
			set sBgColor='$JOB_COLOUR'
	else # no SHOT.
		#set sTitle="$JOB $DIST $PWD"
		set sTitle="$JOB-$DIST-$discipline_tmp"
		set sIconTitle="$JOB-$DIST"
		set sBgColor="$JOB_COLOUR"
	endif # endif SHOT
else # no JOB
    set sTitle="$DIST"
    set sIconTitle="$DIST"
    set sBgColor="black"
    echo -n "\033]11;black\033\\"
endif # endif JOB




#KDE uses konsole and WM and Gnone use xterm.
if (`echo ${DESKTOP_SESSION}` == 'kde') then
    dcop $KONSOLE_DCOP_SESSION renameSession $sTitle 
else
    #Use xterm escape sequences to set window title.
    echo -n "\033]2;$sTitle\033\\"
    #Use xterm escape sequences to set icon title.
    echo -n "\033]1;$sIconTitle\033\\"
    #Use xterm escape sequences to set BG color.
    echo -n "\033]11;$sBgColor\033\\"
endif
 
