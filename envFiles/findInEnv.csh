#! /bin/tcsh
##!/bin/csh -f

if ($#argv == 0) then
    goto out
endif

$discipline = "$argv[0]"
$job        = "$argv[1]"
$toFind     = "$argv[2]"

if ($?argv[3]) then
    $user   = "$argv[3]"


echo "DISCIPLINE :	" $1
echo "JOB :		" $2
echo "TO FIND :	" $3
echo " "
#echo `job -d $1 $2` | awk -F ' ' '{for(i=1;i<=NF;i++){print $i}}' | grep \.csh | xargs grep -n $3

