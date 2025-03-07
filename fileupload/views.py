import pandas as pd
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from fileupload.models import DataEntry
from fileupload.serializers import FileUploadSerializer
#from rest_framework.exceptions import ParserError

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            try:
                file = request.FILES['file']
            except KeyError:
                return Response({"file": ["This field is required."]})
            df = pd.read_excel(file) if file.name.endswith('.xlsx') else pd.read_csv(file)
            with transaction.atomic():
                for index, row in df.iterrows():
                    DataEntry.objects.create(name=row['name'], value=row['value'], date=row['date'])
            return Response({"status": "success"}, status=201)
        else:
            return Response(file_serializer.errors, status=400)
