import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data['amount']
            
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
            )
            
            return JsonResponse({
                'clientSecret': intent.client_secret
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=403)
