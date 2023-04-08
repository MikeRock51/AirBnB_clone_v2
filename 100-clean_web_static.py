#!/usr/bin/python3


from fabric.api import *
import os


env.hosts = ['54.237.86.166', '54.236.48.218']
env.user = 'ubuntu'


def do_clean(number=0):
    """Deletes outdated archives"""

    # Check if versions directory exists
    if os.path.isdir('versions'):
        # Get a list of archives in the directory
        archive_list = os.listdir('versions')

    # Remove the most recent archive from the list
    archive_list.remove(max(archive_list))

    # Check if more than one latest archive is required
    if number == 2:
        # Remove the second most recent archive from the list
        archive_list.remove(max(archive_list))

    
