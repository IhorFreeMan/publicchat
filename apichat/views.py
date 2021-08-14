from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from apichat.models import ChatModel
from .serializers import ChatSerializer, ChatAddSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class PaginationChat(PageNumberPagination):
    """Pagination Chat"""
    page_size = 10
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

class ChatListView(generics.ListAPIView):
    """This class forms a list of 10 messages.
    /api/messages/list/?page=1"""
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer
    pagination_class = PaginationChat



class ChatDetailView(generics.RetrieveAPIView):
    """Chat Detail. Information about the content of one message.
    /api/messages/single/11/"""
    queryset = ChatModel.objects.all()
    serializer_class = ChatSerializer


# add chats
class AddChatsView(generics.CreateAPIView):
    """Create chat. Add mail and message text.
    Validators check email and message text.
    The number of characters in the message text (100) is controlled by the serializer.
    /api/messages/<pk>/add/"""
    serializer_class = ChatAddSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response({"error": serializer.errors})
