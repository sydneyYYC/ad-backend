from django.forms import model_to_dict
from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.decorators import api_view
#import upload file
from compiler.models import UploadFile


# from adBack.compiler.models import UploadFile


# from bots.models import Sandbox
# def bot(request: HttpRequest):
#     pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def upload(request: HttpRequest):
    if request.method == 'GET':
        return get_file(request)
    if request.method == 'POST':
        return post_file(request)
    return JsonResponse({}, status=200, safe=False)

def get_file(request: HttpRequest):
    # return JsonResponse({}, status=200, safe=False)
    name: str = request.GET.get('name')
    if name:
        try:
            found = UploadFile.objects.get(name=name)
            return JsonResponse(model_to_dict(found), status=200, safe=False)
        except:
            return JsonResponse({}, status=404, safe=False)
    return JsonResponse({}, status=404, safe=False)

def post_file(request: HttpRequest):
    name: str = request.data.get('name')
    if not name:
        return JsonResponse(
            {'message': f"unable to create with invalid {name=}"}, status=400,
            safe=False)
    name = name.strip()
    founds = UploadedFile.objects.filter(name=name)
    # width_m = request.data.get('width_m')
    # height_m = request.data.get('height_m')

    if founds and founds.count() > 0:
        found: UploadedFile = founds[0]
        found.deleted = False
        found.width_m = width_m
        found.height_m = height_m
        found.save()
        return JsonResponse(model_to_dict(found), status=200, safe=False)
    created = UploadedFile.objects.create(name=name, width_m=width_m,
                                    height_m=height_m)
    return JsonResponse(model_to_dict(created), status=200, safe=False)
