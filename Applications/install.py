#!/usr/bin/python
# -*- coding: utf-8 -*- 
import glob
import os

import logging
logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.INFO)

class Install_menu(object):
    def __init__(self):
        """ Print out a menu giving all the applications to install or uninstall."""
        # differents modes
        #
        modes = {
            '1': self.install,
            '2': self.uninstall
        }

        # First Menu, getting the choice between install and uninstall.
        #
        for mode in sorted(modes.keys()):
            method = modes[mode]
            print('%s: %s' % (mode, method.__name__))

        pick = raw_input('Pick the number of a mode to use: ')

        if pick:

            if pick.isdigit():
                method = modes[pick]

            else:
                return None

        applications = glob.glob('%s/*.app' % os.getcwd())

        print('0: all')

        for i, app in enumerate(sorted(applications)):
            app_name = os.path.splitext(os.path.basename(app))[0]
            print('%s: %s' % (i+1, app_name))

        pick = raw_input('Pick the number of an app to install: ')

        if pick:

            if pick.isdigit():

                pick = int(pick)

                if pick == 0:

                    for application in applications:
                        method(application)

                # install only one app
                #
                else:
                    method(applications[pick])

    def install(self, application):
        logger.info('Installing: %s' % application)
        try:
            os.symlink(
                application,
                '/Applications/%s' % os.path.basename(application)
            )

        # os.symlink will raise OSError if the application already exists in /Applications
        # 
        except OSError, e:
            logger.warning(e)
            logger.info(
                '%s Already exists in /Applications. Uninstall it then retry.' % application
            )

    def uninstall(self, application):
        logger.info('Uninstalling: %s' % application)
        app_path = '/Applications/%s' % os.path.basename(application)

        try:
            os.remove(app_path)
            logger.info('%s has been uninstall.' % app_path)

        # os.remove raise OSError if the path doesn't exists.
        #
        except OSError, e:
            logger.warning(e)

if __name__ == '__main__':
    Install_menu()

