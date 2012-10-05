# Create your views here.
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
import tarfile

def dist_download(request, file_name):
    response = HttpResponse(open('dists/%s' % file_name, 'rb').read(), content_type='application/gzip')
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    return response
