from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions

from django.contrib.auth.models import User
from crim.renderers.custom_html_renderer import CustomHTMLRenderer
from crim.serializers.person import CRIMPersonListSerializer, CRIMPersonDetailSerializer
from crim.models.person import CRIMPerson
from rest_framework.response import Response
from rest_framework import status


class PersonListHTMLRenderer(CustomHTMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        for p in data:
            # Put roles into a single text field
            p['unique_roles'] = ', '.join(p['roles'])

        template_names = ['person/person_list.html']
        template = self.resolve_template(template_names)
        context = self.get_template_context({'content': data}, renderer_context)
        return template.render(context)


class PersonDetailHTMLRenderer(CustomHTMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Put roles into a single text field
        data['unique_roles'] = ', '.join(data['roles'])

        template_names = ['person/person_detail.html']
        template = self.resolve_template(template_names)
        context = self.get_template_context({'content': data}, renderer_context)
        return template.render(context)


class PersonList(generics.ListAPIView):
    model = CRIMPerson
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CRIMPersonListSerializer
    renderer_classes = (PersonListHTMLRenderer, JSONRenderer,)

    def get_queryset(self):
        order_by = self.request.GET.get('order_by', 'name_sort')
        return CRIMPerson.objects.all().order_by(order_by)


class PersonDetail(generics.RetrieveAPIView):
    model = CRIMPerson
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CRIMPersonDetailSerializer
    renderer_classes = (PersonDetailHTMLRenderer, JSONRenderer,)
    queryset = CRIMPerson.objects.all()

    def get_object(self):
        url_arg = self.kwargs['pk']
        person = CRIMPerson.objects.filter(person_id=url_arg)
        if not person.exists():
            person = CRIMPerson.objects.filter(name_sort__iexact=url_arg)

        obj = get_object_or_404(person)
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        remarks_text = request.DATA.get('remarks', None)
        current_user = User.objects.get(pk=request.user.id)
        person = current_user.profile.person

        if person:
            person.remarks = remarks_text
            person.save()

            serialized = CRIMPersonDetailSerializer(person).data

            return Response(serialized, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)