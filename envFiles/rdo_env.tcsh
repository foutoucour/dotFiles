#!/usr/bin/tcsh

# setup so the local dev is taken in count in python
# pycharm debug-eggs for remote debuging.
set ADDITIONAL_PYTHONPATH=$HOME/rdoenv/python_libs/pure:$HOME/pycharm/current/debug-eggs/pycharm-debug.egg

if ($?PYTHONPATH) then
    setenv PYTHONPATH ${ADDITIONAL_PYTHONPATH}:${PYTHONPATH}
else
    setenv PYTHONPATH ${ADDITIONAL_PYTHONPATH}
endif

alias ls        'ls --color=auto'

if ($?TERM) then

    alias whenchanged "/mnt/rodeo/setup/lib/python/pure/whenchanged/when-changed"

    echo "\033[0;32mSetting custom aliases:\033[0m"
    alias _virt 'setenv PROJECT_PROMPT "\!:1 " && source ~/virtualenvs/\!:1/bin/activate.csh'
    alias _v.py 'setenv PROJECT_PROMPT " py\!:1 " && source ~/virtualenvs/python\!:1/bin/activate.csh'
    alias _py27 '_v.py 2.7'
    alias _pySelenuim '_virt selenium'

    echo " * aliases to folders: (l.{} to local, p.{} to prod)"
    echo "   - x.pylibs"
    alias l.pylibs 'cd ~/rdoenv/python_libs/pure/rodeo'
    alias p.pylibs 'cd ~/prod/python_libs/pure/rodeo'
    echo "   - x.workgroup"
    alias l.workgroups 'cd ~/rdoenv/workgroups'
    alias p.workgroups 'cd ~/prod/workgroups'
    echo "   - x.tank_config"
    alias l.tank_config 'cd ~/rdoenv/tank/sandbox/rdo_Primary/config/'
    alias p.tank_config 'cd ~/prod/tank/config'
    echo "   - x.tank_local_apps"
    alias l.tank_local_apps 'cd ~/rdoenv/tank/sandbox/local_apps/'
    alias p.tank_local_apps 'cd ~/prod/tank/sandbox/local_apps/'

    alias logs 'cd /rodeo/setup/logs/'
    alias confs 'cd /rdo/rodeo/setup/etc/rodeofx/'
    alias my_ingest_bid '/sandbox/rdoenv/workgroups/toolbox/shotgun/ingestBid.py'
    alias admin_film_prod 'cd /mntx/admin/02_FILM/1-IN\ PRODUCTION'
endif
