from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Parser
from .serializers import ParserSerializer
import summary


class ParserView(APIView):

    def get(self, request):
        lang = request.GET.get('lang')
        limit = int(request.GET.get('limit'))

        if type(lang) != str:
            return Response('Неверный тип указанных данных для языка')
        elif lang != 'en' and lang != 'rus' and type(lang)== str:
            return Response('Язык не поддерживается')

        parser = Parser(summary.summary('/app/kinopoisk.html', lang, limit))

        serializer_for_request = ParserSerializer(instance=parser)

        return Response(serializer_for_request.data)
