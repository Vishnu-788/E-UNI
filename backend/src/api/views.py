from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

class home_view(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self, request):

        return Response({
            "message": "Welcome to my app",
            "description": "Create an account either as customer or shop, since to access other endpoints or routes you need to authenticate. Refer to docs for more info.",
            "usage": {
                "shop_endpoints": {
                    "list_shop": {
                        "method": "GET",
                        "url": "/api/shop/"
                    },
                    "list_products": {
                        "method": "GET",
                        "url": "/api/shop/products/"
                    },
                    "product_detail": {
                        "method": ["PATCH", "PUT"],
                        "url": "/api/shop/products/<id>/detail/"
                    },
                    "product_update": {
                        "method": "PUT",
                        "url": "/api/shop/products/<id>/update/"
                    },
                    "product_delete": {
                        "method": "DELETE",
                        "url": "/api/shop/products/<id>/delete/"
                    }
                },
                "customer_endpoints": {
                    "list_customer": {
                        "method": "GET",
                        "url": "/api/customer/"
                    },
                    "customer_patch": {
                        "method": "PATCH",
                        "url": "/api/customer/"
                    }
                }
            }
        })
