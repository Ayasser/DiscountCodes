import string
import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from discount_code.models import DiscountCode
from discount_code.serializers import DiscountCodeSerializer
from django.forms import model_to_dict


def generate_discount_code():
    size = 12
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    print(chars)
    discount_code = ''.join(random.choice(chars) for _ in range(size))
    print(discount_code)

    return discount_code


@api_view(['POST'])
def create_discount_code(request):
    """
    | create a discount code.
        parameters :
        -start_date: datatime
        -expire_date : datatime
        -created_by : system_user id
        -modified_by: system_user id
        -customer_id: customer id
    """
    if request.method == 'POST':
        data = request.data
        data['code'] = generate_discount_code()
        serializer = DiscountCodeSerializer(data=data)
        serializer.is_valid(raise_exception=True)


        discount_code = DiscountCode(**data)
        discount_code.save()
        discount_code_dict = model_to_dict(discount_code)

        return Response(discount_code_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_discount_code(request, id):
    """
    | get a discount code.
        parameters :
        -id: id of discount code
    """
    if request.method == 'GET':
        discount_code = DiscountCode.objects.get(id=id)
        discount_code_dict = model_to_dict(discount_code)

        return Response(discount_code_dict, status=status.HTTP_200_OK)
