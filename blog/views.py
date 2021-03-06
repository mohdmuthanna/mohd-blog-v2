from django.shortcuts import render, get_object_or_404
from db.models import Category, Post
from .forms import ContactForm
from django.core.mail import send_mail

# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.core.mail import EmailMessage
# from django.template import Context
# # from sendgrid.message import SendGridEmailMessage
# # import sendgrid
thanks_message = """Thank You, We appreciate that you’ve taken the time to write us.
We’ll get back to you very soon.\n \n \n
------------------------------------\n \n
This is your message\n \n
------------------------------------\n \n
"""


def home(request):
    latest_project = Post.get_lastest_visible('project')
    latest_blog = Post.get_lastest_visible('blog')
    latest_arabic = Post.get_lastest_visible('arabic')

    return render(request, 'home.html', {
        'latest_project': latest_project,
        'latest_blog': latest_blog,
        'latest_arabic':latest_arabic,
    })

def cv(request):
    return render(request, 'cv.html',)

def smedia(request):
    return render(request, 'smedia.html',)

def contact(request):
    # new logic!
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact_email = form.cleaned_data.get('contact_email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            send_mail(
                subject,
                message,
                contact_email,
                ['m@mohd.im'],
                fail_silently=False,
            )

            message = thanks_message + message

            subject = "RE:" + subject

            send_mail(
                subject,
                message,
                'm@mohd.im',
                [contact_email],
                fail_silently=False,
            )
            return render(request, 'thanks-email.html',)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        # 'errors': errors,contactcontact
        # 'subject_val': subject_val,
        # 'contact_email_val': contact_email_val,
        # 'message_val': message_val,
        })

    def robots(request):
        return render(request, 'robots.txt',)

# def contact(request):
#     form_class = ContactForm
#
#     # new logic!
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#
#         contact_email = request.POST.get('contact_email', '')
#         content = request.POST.get('content', '')
#
#         sg = sendgrid.SendGridClient('SENDGRID_USERNAME', 'SENDGRID_PASSWORD')
#
#         message = sendgrid.Mail()
#         message.add_to('m@mohd.im')
#         message.set_subject('via CuntactMe')
#         message.set_text(content)
#         message.set_from(contact_email)
#         status, msg = sg.send(message)
#         return redirect('thank-u-email.html')
#
#     return render(request, 'contact.html', {
#         'form': form_class,
#     })

# def contact(request):
#     from django.core.mail import send_mail
#
#     send_mail(
#         'Subject here',
#         'Here is the message.',
#         'from@example.com',
#         ['mohd.muthanna+contact.mohd.im@gmail.com'],
#         fail_silently=False,
#     )
#
#     return render(request, 'contact.html',)

# our view
# def contact(request):
#     form_class = ContactForm
#
#
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#
#         if form.is_valid():
#             contact_email = request.POST.get('contact_email', '')
#             subject = request.POST.get('subject', '')
#             message = request.POST.get('message', '')
#
#             send_mail(
#                 subject,
#                 message,
#                 contact_email,
#                 ['m@mohd.im'],
#                 fail_silently=False,
#             )
#             message = """
#                 Thank You,\n We appreciate that you’ve taken the time to write us.
#                 We’ll get back to you very soon.\n \n \n
#                 ------------------------------------
#                 This is your message
#                 ------------------------------------
#                 """ + message
#             subject = "RE:" + subject
#             send_mail(
#                 subject,
#                 message,
#                 'm@mohd.im',
#                 [contact_email],
#                 fail_silently=False,
#             )
#
#
#
#             # return redirect('/thank-u-email.html/')
#             return render(request, 'thanks-email.html',)
#
#     return render(request, 'contact.html', {
#         'form': form_class,
#     })
#
#
