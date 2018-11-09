from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from info.serializers import InfoSerializer
from .models import Info
from django.shortcuts import render

def info_landing(request):
    info_object = Info.objects.get(first_name='Vladislav')
    return render(request, 'landing.html', {'info_object': info_object})

@csrf_exempt
def info_list(request):
    if request.method == "GET":
        info = Info.objects.all()
        serializer = InfoSerializer(info, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = InfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def info_detail(request, pk):
#     try:
#         info =  Info.objects.get(pk=pk)
#     except Info.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == "GET":
#         serializer = InfoSerializer(info)
#         return JsonResponse(serializer.data)
#
#     elif request.method == "PATCH":
#         data = JSONParser().parse(request)
#         serializer = InfoSerializer(info, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == "DELETE":
#         info.delete()
#         return HttpResponse(status=204)

from rest_framework import generics


class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

info_detail = InfoDetail.as_view()
