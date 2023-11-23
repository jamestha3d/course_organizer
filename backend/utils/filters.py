from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

# class AllDjangoFilterBackend(DjangoFilterBackend):
#     """
#     A filter backend that uses django-filter.
#     """

#     def get_filterset_class(self, view, queryset=None):
#         '''
#         Return the django-filters `FilterSet` used to filter the queryset.
#         '''
#         filter_class = getattr(view, 'filter_class', None)
#         filter_fields = getattr(view, 'filter_fields', None)


#         if filter_class or filter_fields:
#             return super().get_filterset_class(view, queryset)

#         class AutoFilterSet(self.filterset_base):
#             class Meta:
#                 fields = "__all__"
#                 model = queryset.model

#         return AutoFilterSet
    
# class UsrFilter(filters.FilterSet):
#     firstname = filters.CharFilter(field_name="firstname", lookup_expr='icontains')
#     lastname = filters.CharFilter(field_name="lastname", lookup_expr='icontains')
#     email = filters.CharFilter(field_name="email", lookup_expr='icontains')
#     role = filters.CharFilter(field_name="role__rolename", lookup_expr='exact')
#     class Meta:
#         model = User
#         fields = ('firstname', 'lastname', 'email','role__rolename')
