from django.http import HttpResponse, JsonResponse
from rest_framework import status


def home_page(request):
    print("home page requested")
    # return JsonResponse({"status": "true", "messgae": "success"})
    return JsonResponse({"message": "hello"}, status=status.HTTP_200_OK)
