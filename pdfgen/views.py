from django.views.generic import ListView
from django_weasyprint import WeasyTemplateResponseMixin
from members.models import Member


class PdfGeneratorView(WeasyTemplateResponseMixin, ListView):
    pdf_filename = 'carteirinha_membro.pdf'
    template_name = 'pdfgen/template_cards.html'
    context_object_name = 'members_list'

    def get_queryset(self):
        to_print = self.request.session.get('print_members_id')
        return Member.objects.filter(id__in=to_print)



class HtmlPdfView(ListView):
    # to_print = self.request.POST.getlist('ck_members')
    # model = 
    # context_object_name = 'members_list'
    pass

