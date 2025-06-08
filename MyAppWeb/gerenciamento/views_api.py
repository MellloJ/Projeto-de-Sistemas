from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from users.serializers import AddressSerializer
from users.models import Address, SupermarketUser
from users.serializers import SupermarketUserSerializer
from rest_framework.permissions import IsAuthenticated

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Address.objects.filter(user=self.request.user)

class AddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Address.objects.filter(user=self.request.user)

class CepLookupAPIView(APIView):
    def get(self, request, cep):
        # Limpa o CEP para garantir formato correto
        cep = ''.join(filter(str.isdigit, cep))
        if len(cep) != 8:
            return Response({'error': 'Invalid zip code'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if r.status_code == 200:
                data = r.json()
                if 'erro' in data:
                    return Response({'error': 'Zip code not found'}, status=status.HTTP_404_NOT_FOUND)
                # English field names
                return Response({
                    'zip_code': data.get('cep', ''),
                    'street': data.get('logradouro', ''),
                    'complement': data.get('complemento', ''),
                    'neighborhood': data.get('bairro', ''),
                    'city': data.get('localidade', ''),
                    'state': data.get('uf', ''),
                })
            return Response({'error': 'Error fetching zip code'}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DadosMercadoAPIView(APIView):
    def get(self, request):
        # Permite buscar por id via query param: /gerenciamento/api/dados-mercado/?id=123
        mercado_id = request.query_params.get('id')
        if not mercado_id:
            return Response({'error': 'Informe o id do mercado na query string.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            mercado = SupermarketUser.objects.get(id=mercado_id)
            serializer = SupermarketUserSerializer(mercado)
            return Response(serializer.data)
        except SupermarketUser.DoesNotExist:
            return Response({'error': 'Mercado não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        # Permite atualizar por id enviado no corpo JSON
        mercado_id = request.data.get('id')
        if not mercado_id:
            return Response({'error': 'Informe o id do mercado no corpo da requisição.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            mercado = SupermarketUser.objects.get(id=mercado_id)
        except SupermarketUser.DoesNotExist:
            return Response({'error': 'Mercado não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SupermarketUserSerializer(mercado, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
