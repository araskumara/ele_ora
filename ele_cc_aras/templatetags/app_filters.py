from django import template

register = template.Library()

@register.filter(name='smsclassification')
def sms_classify(value):
    promotional = ['AM-PSBLRS']
    if value in promotional:
        return 'Promotional'
    else:
        return 'Transactional'