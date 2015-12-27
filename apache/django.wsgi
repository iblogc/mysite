"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import site
site.addsitedir('C:/Users/Tom/Envs/mysite/Lib/site-packages')
import os
import sys
sys.path.append("C:/Users/Tom/Envs/mysite/Lib/site-packages/misaka")
sys.path.append("C:/Users/Tom/Envs/mysite/Lib/site-packages/cffi")

sys.path.append('E:/workspace/mysite')
sys.path.append('E:/workspace/mysite/mysite')
sys.path.append('E:/workspace')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


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
