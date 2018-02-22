"""
Views which allow users to create and activate accounts.

"""

from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
try:
    from django.utils.module_loading import import_string
except ImportError:
    from registration.utils import import_string
    
from registration.forms import RegistrationFormUniqueEmail

from registration import signals
#
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.core.urlresolvers import reverse
from django.views import generic

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from registration.forms import RegistrationForm
from registration.models import RegistrationProfile

#from registration.view import activate
# from registration.forms import RegistrationForm
def reg(request):
 	return render(request, 'registration/registration_form.html')

def login (request):
    return render(request, 'registration/activate.html')


REGISTRATION_FORM_PATH = getattr(settings, 'REGISTRATION_FORM', 'registration.forms.RegistrationForm')
REGISTRATION_FORM = import_string( REGISTRATION_FORM_PATH )


class _RequestPassingFormView(FormView):
    """
    A version of FormView which passes extra arguments to certain
    methods, notably passing the HTTP request nearly everywhere, to
    enable finer-grained processing.

    """
    def get(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        # Pass request to get_form_class and get_form for per-request
        # form control.
        form_class = self.get_form_class(request)
        form = self.get_form(form_class)
        if form.is_valid():
            # Pass request to form_valid.
            return self.form_valid(request, form)
        else:
            return self.form_invalid(form)

    def get_form_class(self, request=None):
        return super(_RequestPassingFormView, self).get_form_class()

    def get_form_kwargs(self, request=None, form_class=None):
        return super(_RequestPassingFormView, self).get_form_kwargs()

    def get_initial(self, request=None):
        return super(_RequestPassingFormView, self).get_initial()

    def get_success_url(self, request=None, user=None):
        # We need to be able to use the request and the new user when
        # constructing success_url.
        return super(_RequestPassingFormView, self).get_success_url()

    def form_valid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_valid(form)

    def form_invalid(self, form, request=None):
        return super(_RequestPassingFormView, self).form_invalid(form)


class RegistrationView(_RequestPassingFormView):
    """
    Base class for user registration views.

    """
    disallowed_url = 'registration_disallowed'
    form_class = REGISTRATION_FORM
    http_method_names = ['get', 'post', 'head', 'options', 'trace']
    success_url = None
    template_name = 'registration/registration_form.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Check that user signup is allowed before even bothering to
        dispatch or do other processing.

        """
        if not self.registration_allowed(request):
            return redirect(self.disallowed_url)
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, request, form):
        new_user = self.register(request, form)
        success_url = self.get_success_url(request, new_user)

        # success_url may be a simple string, or a tuple providing the
        # full argument set for redirect(). Attempting to unpack it
        # tells us which one it is.
        try:
            to, args, kwargs = success_url
            return redirect(to, *args, **kwargs)
        except ValueError:
            return redirect(success_url)

    def registration_allowed(self, request):
        """
        Override this to enable/disable user registration, either
        globally or on a per-request basis.

        """
        return True

    def register(request, success_url=None,
             #form_class=RegistrationForm,
             form_class=RegistrationFormUniqueEmail, 
             profile_callback=None,
             template_name='registration/registration_form.html',
             extra_context=None):
        raise NotImplementedError



class ActivationView(TemplateView):
    """
    Base class for user activation views.

    """
    http_method_names = ['get']
    template_name = 'registration/activate.html'
  

    def get(self, request, *args, **kwargs):
        activated_user = self.activate(request, *args, **kwargs)
        if activated_user:
            success_url = self.get_success_url(request, activated_user)
            try:
                to, args, kwargs = success_url
                return redirect(to, *args, **kwargs)
            except ValueError:
                return redirect(success_url)
        return super(ActivationView, self).get(request, *args, **kwargs)

   # def activate(self, request, *args, **kwargs):
        #"""
        #Implement account-activation logic here.

        #"""
        #raise NotImplementedError

    def activate(request, backend,
         template_name='registration/activate.html',
         success_url=None, extra_context=None, **kwargs):

        backend = get_backend(backend)
        account = backend.activate(request, **kwargs)

        if account:
            if success_url is None:
                to, args, kwargs = backend.post_activation_redirect(request, account)
                return redirect(to, *args, **kwargs)
            else:
                return redirect(success_url)

        if extra_context is None:
            extra_context = {}
        context = RequestContext(request)
        for key, value in extra_context.items():
            context[key] = callable(value) and value() or value

        return render_to_response(template_name,
                                  kwargs,
                                  context_instance=context)

    def get_success_url(self):
        return self.backend.get_activation_complete_url(self.activated_user)
   
