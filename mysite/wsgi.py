"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""
'''
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''
import django
import os
import sys
sys.path.append("/home/bae/app/deps/misaka/")
sys.path.append("/home/bae/app/deps/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings") 

from django.core.wsgi import get_wsgi_application 
from bae.core.wsgi import WSGIApplication 
application = WSGIApplication(get_wsgi_application())



# import traceback
# import sys
# import signal
# import time
# if 'SERVER_SOFTWARE' in os.environ:  # BAE
#     from bae.core.wsgi import WSGIApplication
#     application = WSGIApplication(get_wsgi_application())
# else:
#     application = get_wsgi_application()

# try:
#     application = get_wsgi_application()
#     print 'WSGI without exception'
# except Exception:
#     print 'handling WSGI exception'
#     # Error loading applications
#     if 'mod_wsgi' in sys.modules:
#         traceback.print_exc()
#         os.kill(os.getpid(), signal.SIGINT)
#         time.sleep(2.5)
