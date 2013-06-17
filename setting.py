#!/usr/bin/python

import os
_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
_HOME_DIR = os.path.expanduser('~')

def create_symlink(src, dst):
    if not os.path.exists(src):
        raise IOError(
            '{0} doesn\'t exists. Exit'.format(src)
        )

    if os.path.exists(dst):
        raise IOError(
            '{0} exists. Exit'.format(dst)
        )

    os.symlink(src, dst)


# cshrc file
#
create_symlink(
    '{0}/envFiles/cshrc'.format(_PROJECT_DIR),
    '{0}/.cshrc'.format(_HOME_DIR)
)

# Git
#
create_symlink(
    '{0}/gitconfig'.format(_PROJECT_DIR),
    '{0}/.gitconfig'.format(_HOME_DIR)
)

# Vim
#
create_symlink(
    '{0}/vim'.format(_PROJECT_DIR),
    '{0}/.vim'.format(_HOME_DIR)
)

create_symlink(
    '{0}/vimrc'.format(_PROJECT_DIR),
    '{0}/.vimrc'.format(_HOME_DIR)
)

