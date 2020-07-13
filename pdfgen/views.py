from django.views.generic import ListView
from django_weasyprint import WeasyTemplateResponseMixin
from members.models import Member


class PdfGeneratorView(WeasyTemplateResponseMixin, ListView):
    model = Member
    pdf_filename = 'carteirinha_membro.pdf'
    template_name = 'pdfgen/template_cards.html'
    context_object_name = 'members_list'

