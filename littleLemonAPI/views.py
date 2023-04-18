from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer

# View Set

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title', 'category__name']
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

# Generic Views

# class MenuItemsView(generics.ListCreateAPIView):
#     serializer_class = MenuItemSerializer
      
#     def get_queryset(self):
#         queryset = MenuItem.objects.select_related('category').all()
              
#         category_name = self.request.query_params.get('category')
#         to_price = self.request.query_params.get('to_price')
#         search = self.request.query_params.get('search')
#         ordering = self.request.query_params.get('ordering')
#         perpage = self.request.query_params.get('perpage', default=2)
#         page = self.request.query_params.get('page', default=1)
        
#         if category_name:
#             queryset = queryset.filter(category__slug=category_name)
#         if to_price:
#             queryset = queryset.filter(price__lte=to_price)
#         if search:
#             queryset = queryset.filter(title__icontains=search)
#         if ordering:
#             ordering_fields = ordering.split(",")
#             queryset = queryset.order_by(*ordering_fields)
            
#         paginator = Paginator(queryset, per_page=perpage)
#         try:
#             queryset = paginator.page(number=page)
#         except EmptyPage:
#             queryset = []
    
#         return queryset
    
      
# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MenuItem.objects.select_related('category').all()
#     serializer_class = MenuItemSerializer
    
# @api_view()
# def categories(request):
#     categories = Category.objects.all()
#     serialized_categories = CategorySerializer(categories, many=True)
#     return Response(serialized_categories.data)
        
# @api_view()
# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     serialized_category = CategorySerializer(category)
#     return Response(serialized_category.data)
