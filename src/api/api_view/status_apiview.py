from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from subscription.models import SubscriptionModel

@swagger_auto_schema(
    method='get',
   responses={200: openapi.Response('Description of response', examples={'application/json': {"status": "Status de la souscription"}}),
               404: openapi.Response('Description of response', examples={'application/json': {"status": "Souscription non trouvée"}})
               },
)
@api_view(['GET'])
def get_status(request, pk):
    try:
        subscription = SubscriptionModel.objects.get(id=pk)
    except SubscriptionModel.DoesNotExist:
        return Response({'detail': 'Souscription non trouvée.'}, status=status.HTTP_404_NOT_FOUND)

    # Si la méthode est GET, on renvoie uniquement le statut actuel de la souscription
    return Response({'statut': subscription.statut}, status=status.HTTP_200_OK)