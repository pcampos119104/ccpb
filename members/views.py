from django.urls import reverse_lazy
from django.views import generic
from django.forms.models import inlineformset_factory

from members.models import Member, Phone


class ListView(generic.list.ListView):
    model = Member
    context_object_name = 'members_list'


class DetailView(generic.detail.DetailView):
    model = Member
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone_list'] = Phone.objects.filter(member__id=self.object.id)
        return context


class CreateView(generic.edit.CreateView):
    PhoneFormset = inlineformset_factory(Member, Phone, fields=('number', ))
    model = Member
    fields = ['name', 'address']
    success_url = reverse_lazy('members:list')

    def get_context_data(self, **kwargs):
        dt = super().get_context_data(**kwargs)
        if self.request.POST:
            dt['phone'] = self.PhoneFormset(self.request.POST)
        else:
            dt['phone'] = self.PhoneFormset()
        return dt

    def form_valid(self, form):
        context = self.get_context_data()
        phone = context['phone']
        self.object = form.save()
        if phone.is_valid():
            phone.instance = self.object
            phone.save()
        return super().form_valid(form)


class UpdateView(generic.edit.UpdateView):
    PhoneFormset = inlineformset_factory(Member, Phone, fields=('number', ))
    model = Member
    fields = ['name', 'address']
    success_url = reverse_lazy('members:list')

    def get_context_data(self, **kwargs):
        dt = super().get_context_data(**kwargs)
        if self.request.POST:
            dt['phone'] = self.PhoneFormset(self.request.POST, instance=self.object)
        else:
            dt['phone'] = self.PhoneFormset(instance=self.object)
        return dt

    def form_valid(self, form):
        context = self.get_context_data()
        phone = context['phone']
        self.object = form.save()
        if phone.is_valid():
            phone.instance = self.object
            phone.save()
        return super().form_valid(form)


class DeleteView(generic.edit.DeleteView):
    model = Member
    success_url = reverse_lazy('members:list')
