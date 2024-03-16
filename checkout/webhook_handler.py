from django.http import HttpResponse


class StripeWH_Handler:
    """ 
    Handle Stripe Webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ 
        Handle a generic/unkown/unexpected webhook event
        """
        return HttpResponse(
            content =f'Unhandled Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ 
        Handle the payment_intent.succeeded webhook event
        from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content =f'Webhook recieved: {event["type"]}',
            status=200
        )
    
    def handle_payment_intent_payment_failed(self, event):
        """ 
        Handle the payment_intent.payment_failed webhook event
        from Stripe
        """
        return HttpResponse(
            content =f'Payment Failed Webhook recieved: {event["type"]}',
            status=200
        )