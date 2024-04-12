from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.shortcuts import render


def sendEmail(request, context, emailSubject, sendTo):
    sendFrom = settings.EMAIL_HOST_USER
    html_content = render_to_string('loadlist/mail.html', context, request=request)

    try:
        #I used EmailMultiAlternatives because I wanted to send both text and html
        emailMessage = EmailMultiAlternatives(subject=emailSubject, body=html_content, from_email=sendFrom, to=[sendTo,], reply_to=[sendFrom,])
        emailMessage.attach_alternative(html_content, "text/html")
        emailMessage.send(fail_silently=False)

    except SMTPException as e:
        print('There was an error sending an email: ', e) 
        error = {'message': ",".join(e.args) if len(e.args) > 0 else 'Unknown Error'}
        raise serializers.ValidationError(error)


# SEND EMAIL WIYH ATTACH FILES
def sendTheEmail(request):
    sendTo = 'masutier@gmail.com'
    subject = "Django mail with attach"
    message = 'We are testing the email address to send messages with 1 attachment'
    attachment = "static/docs/Plantilla_reporte_instructores.xlsx"

    if attachment:
        # EMAIL CON ATTACH FILE
        try:
            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [sendTo]
            )
            email.attach_file(attachment)
            email.send()
        except BadHeaderError:
            return HttpResponse("Invalid subject found.")
    else:
        # EMAIL NORMAL
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [sendTo],
                fail_silently=False
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

    context = {'title': "Loadings",}
    return render(request, "loadings/loadings.html", context)
