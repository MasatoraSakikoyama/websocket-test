# -*- coding: utf-8 -*-
import os

import channels.asgi
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

# application = get_wsgi_application()
channel_layer = channels.asgi.get_channel_layer
