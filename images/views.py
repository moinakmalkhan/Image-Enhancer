from django.shortcuts import get_object_or_404,HttpResponse
from .models import Image


def stream_file(request, pk):
    pic = get_object_or_404(Image, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
