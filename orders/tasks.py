from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully sent an order.\n\nYour order id is {}'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'mihfazhillah@gmail.com', [order.email])
    return mail_sent

