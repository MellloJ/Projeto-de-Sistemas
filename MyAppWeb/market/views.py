from django.shortcuts import render
from market.services.signupMarket import signupMarket
from .forms import createMarketForm
from market.models import Supermarket
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from market.serializers import MarketSeriallizer
from core.consts import CATEGORIAS_ALIMENTOS

class CreateMarket(View):
    def get(self, request):
        return render(request, 'market/create.html', {'form': createMarketForm()})
    def post(self, request):
        form = createMarketForm(request.POST)
        if form.is_valid():
            market, message = signupMarket.register(
                name=form.cleaned_data['name'],
                cnpj=form.cleaned_data['cnpj'],
                password=request.POST.get('password'),
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email']
            )
            if market is None:
                context = {
                    'form': form,
                    'errors': message,
                }
                return render(request, 'market/create.html', context)
            else:
                # sendMail(request, market)
                context = {
                    'title': 'Traz Aí | Home',
                    'categories': CATEGORIAS_ALIMENTOS,
                }
                return render(request, "index.html",context)
        else:
            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'market/create.html', context)

class SupermarketView(APIView):
    queryset = Supermarket.objects.all()
    serializer_class = MarketSeriallizer

    def post(self, request):
        serializer = MarketSeriallizer(data=request.data)
        
        if serializer.is_valid():
            try:
                market, message = serializer.save()
            except Exception as e:
                return Response({'errors': str(e)}, status=status.HTTP_400_BAD_REQUEST)

            if market is not None:
                return Response({
                    'user': {
                        'messsage' : message,
                        'email': market.email,
                        'name': market.name,
                    }
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({'errors': message}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)