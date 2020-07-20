from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django_filters.views import FilterView

from members.models import Member, Phone
from pdfgen.views import HtmlPdfView
from members.filters import MemberFilter


class MemberListView(LoginRequiredMixin, FilterView):
    model = Member
    context_object_name = 'members_list'
    filter_class = MemberFilter
 
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MemberFilter(self.request.GET, queryset=self.get_queryset())
        return context
    '''

    def post(self, request, *args, **kwargs):
        request.session['print_members_id'] = self.request.POST.getlist('ck_members')
        return HttpResponseRedirect(reverse('pdfgen:pdfgenerator')) 


class DetailView(LoginRequiredMixin, generic.detail.DetailView):
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone_list'] = Phone.objects.filter(member__id=self.object.id)
        return context


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    PhoneFormset = inlineformset_factory(Member, Phone, fields=('number',))
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


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    PhoneFormset = inlineformset_factory(Member, Phone, fields=('number',))
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


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Member
    success_url = reverse_lazy('members:list')
