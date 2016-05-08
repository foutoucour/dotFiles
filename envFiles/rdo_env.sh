#!/usr/bin/env bash
if [ ! -z "$PS1" ]; then
    echo -e "\033[0;32mSetting custom aliases:\033[0m"
    echo -e " * aliases to folders: (l.{} to local, p.{} to prod)"
    echo -e "   - x.pylibs"
    alias l.pylibs='cd ~/rdoenv/python_libs/pure/rodeo'
    alias p.pylibs='cd ~/prod/python_libs/pure/rodeo'
    echo -e "   - x.workgroup"
    alias l.workgroups='cd ~/rdoenv/workgroups'
    alias p.workgroups='cd ~/prod/workgroups'
    echo -e "   - x.tank_config"
    alias l.tank_config='cd ~/rdoenv/tank/sandbox/rdo_Primary/config/'
    alias p.tank_config='cd ~/prod/tank/config'
    echo -e "   - x.tank_local_apps"
    alias l.tank_local_apps='cd ~/rdoenv/tank/sandbox/local_apps/'
    alias p.tank_local_apps='cd ~/prod/tank/sandbox/local_apps/'
fi
