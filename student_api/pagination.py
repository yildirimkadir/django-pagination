from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class SmallPageNumberPagination(PageNumberPagination):
    page_size = 8
    # page_size_query_param="sayfa"


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    # limit_query_param = 'how_many'  # Defaults to 'limit'.

class MycursorPagination(CursorPagination):
    page_size=6
    ordering = "id"