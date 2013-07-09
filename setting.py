#!/usr/bin/python
""" Installs all the symlink from the project to replace the current environment."""
import logging

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)

import os
_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
_HOME_DIR = os.path.expanduser('~')

def create_symlink(src, dst):
    logger.debug('Symlinking {} to {}'.format(src, dst))

    if not os.path.exists(src):
        raise IOError(
            '{0} doesn\'t exists. Exit'.format(src)
        )

    if os.path.exists(dst):
        logger.warning(
            '{0} exists. Skipping.'.format(dst)
        )

    else:
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

# pylintrc file
#
create_symlink(
    '{0}/pylintrc'.format(_PROJECT_DIR),
    '{0}/.pylintrc'.format(_HOME_DIR)
)


# dev_env file
#
create_symlink(
    '{0}/envFiles/dev_env'.format(_PROJECT_DIR),
    '{0}/.dev_env'.format(_HOME_DIR)
)

