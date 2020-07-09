from django.views import generic


class LoginView(generic.ListView):
    model = None
    context_object_name = 'members_list'
