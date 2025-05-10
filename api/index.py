# api/index.py
import sys
import os
from vercel_wsgi import handle

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
handler = handle(app)
