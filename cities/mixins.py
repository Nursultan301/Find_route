from django.contrib import messages
from django.http import HttpResponseRedirect


class SuccessDeleteMessageMixin:
    success_message = ''

    def add_success_message(self, request):
        success_message = self.success_message % {"title": self.get_object().title}
        if success_message:
            messages.error(request, success_message)
