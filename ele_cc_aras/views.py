import json
import os
import settings
import dateutil.parser
from datetime import datetime

from django.shortcuts import render

def readsms(request):
    #read the contents of the file
    contents = open(os.path.join(settings.BASE_DIR,"acb_messages.js")).read()
    #load them as json
    json_c = json.loads(contents)
    #in each sms datetime will be in unicode.. convert them to datetime object
    for each in json_c['messages']:
        each['datetime'] = dateutil.parser.parse(each['datetime'])
    return render(request, "ele_cc_aras/display_sms.html", locals())