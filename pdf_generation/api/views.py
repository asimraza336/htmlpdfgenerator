from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from datetime import datetime


from django.template.loader import get_template, render_to_string
from django.shortcuts import render
from django.conf import settings
from .converthtmltopdf import HtmlToPdf
from .serializers import GerneratePdfSerializer


class GerneratePdfView(APIView):
    """This claass has only post method which is responsible for generating pdf"""
    
    def post(self, request):
        """ this method takes html_string and context and returns a status, message, pdf-url
            html_string: required string
            context: optional dictionary 
        """
        try:

            Pdfbject = HtmlToPdf(doppio_api_key="24e61f430895698b2d030105")
            # template_src = 'pdf_reports/order_confirmation_page2.html'
            serializer = GerneratePdfSerializer(data=request.data)
            if serializer.is_valid():
                
                html_as_string = serializer.validated_data['html_string']
                context = serializer.validated_data['context']
                
                Pdfbject.set_html_string(html_as_string)
                output = Pdfbject.generate_pdf(context)

                if output['pdf-url']:
                    return Response(
                        {
                            "status": status.HTTP_200_OK,
                            "message": "Successfully PDF Generated",
                            "pdf-url": output['pdf-url']
                        }, status=status.HTTP_200_OK
                    )
                    
                else:
                    return Response(
                        {
                            "status": status.HTTP_400_BAD_REQUEST,
                            "message": "Bad request",
                        }, status=status.HTTP_400_BAD_REQUEST
                    )
                   
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
GeneratePdfView = GerneratePdfView.as_view()
