#!/usr/bin/env bash
if [ ! -z "$PS1" ]; then
    echo -e "\033[0;32mSetting custom aliases:\033[0m"
    echo -e " * aliases to folders: (l.{} to local, p.{} to prod)"
    echo -e "   - x.pylibs"
    alias l.pylibs='cd ~/rdoenv/python_libs/pure'
    alias p.pylibs='cd /rodeo/setup/lib/python/pure'
    echo -e "   - x.workgroup"
    alias l.workgroups='cd ~/rdoenv/workgroups'
    alias p.workgroups='cd ~/prod/workgroups'
    echo -e "   - x.tank_config"
    alias l.tank_config='cd ~/rdoenv/tank/sandbox/rdo_Primary/config/'
    alias p.tank_config='cd ~/prod/tank/config'
    echo -e "   - x.tank_local_apps"
    alias l.tank_local_apps='cd ~/rdoenv/tank/sandbox/local_apps/'
    alias p.tank_local_apps='cd ~/prod/tank/sandbox/local_apps/'

    alias whenchanged="/mnt/rodeo/setup/lib/python/pure/whenchanged/when-changed"
    alias logs='cd /rodeo/setup/logs/'
    alias confs='cd /rdo/rodeo/setup/etc/rodeofx/'
    alias my_ingest_bid='$HOME/rdoenv/workgroups/toolbox/shotgun/ingestBid.py'
    alias ingest_bid='/rodeo/setup/bin/shotgun/ingestBid.py'
    alias admin_film_prod='cd /mntx/admin/02_FILM/1-IN\ PRODUCTION'
fi

# Darwin needs a bit more of attention to have a proper environment
if [ $(uname) == "Darwin" ]; then
    export RDO_PYTHONPATH=$HOME/rdoenv/python_libs/pure:/rodeo/repositories/_libs/bin/linters/lib/site-packages:/rdo/rodeo/workgroups/maya/scripts:/rodeo/setup/lib/python/pure:/software/alembic/linux/current/lib:/software/qube/osx/current/api/python:$PYTHONPATH
fi

echo "Sourcing rez"

export PATH=$PATH:/Users/jriera/rez/bin/rez
. /Users/jriera/rez/completion/complete.sh
export REZ_CONFIG_FILE=/rdo/rodeo/setup/rez/rdo_rez_config/rdo_rez_config.py

echo "PythonZ"
[[ -s $HOME/.pythonz/etc/bashrc ]] && source $HOME/.pythonz/etc/bashrc

