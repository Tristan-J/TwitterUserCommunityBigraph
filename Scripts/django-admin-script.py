#!f:\workspace\rutgers\intro_to_alg\final_proj\src\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==1.10.6','console_scripts','django-admin'
__requires__ = 'Django==1.10.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('Django==1.10.6', 'console_scripts', 'django-admin')()
    )
