from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'GET':'/api/projects/id/vote'},

        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
        {'POST':'/api/users/token'},
    ]

    return Response(routes)