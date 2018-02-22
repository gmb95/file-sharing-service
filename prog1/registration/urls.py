"""
Backwards-compatible URLconf for existing django-registration
installs; this allows the standard ``include('registration.urls')`` to
continue working, but that usage is deprecated and will be removed for
django-registration 1.0. For new installs, use
``include('registration.backends.default.urls')``.

"""

import warnings

warnings.warn("include('registration.urls') is deprecated; use include('registration.backends.default.urls') instead.",
              DeprecationWarning)

from registration.backends.default.urls import *
#from registration.view import activate
from registration.backends.default.views import RegistrationView
from registration.backends.default.views import ActivationView
from registration.forms import RegistrationFormUniqueEmail
class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail
urlpatterns = patterns('',
	#url(r'^accounts/', include('django.contrib.auth.urls')),
    # enable unique email registration feature
    url(r'^register/$', RegistrationView.as_view(form_class=RegistrationFormUniqueEmail), name='registration_register'),
    url('accounts/', include('registration.backends.default.urls')),
    url(r'^activate/$',  ActivationView.as_view(), name='registration_activate'),

)