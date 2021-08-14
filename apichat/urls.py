# -*- coding: utf-8 -*-
from django.urls import path
from apichat import views


app_name = 'PublicChat'

urlpatterns = [
    path('messages/list/', views.ChatListView.as_view(), name='chat_list'),
    path('messages/single/<pk>/', views.ChatDetailView.as_view(), name='chat_detail'),
    path('messages/<pk>/add/', views.AddChatsView.as_view(), name='add_chat'),

]
