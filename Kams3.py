import unittest

from vba_script_reader import update

from test import Test

import os 

from twilio.rest import Client

from messenger import sms_messenger

 

if __name__ == "__main__":

    test_1 = "Machine name=GARY1;Datetime=20210729120005;Status=OK;Pct=0.05"

    text_message = update(STATUS_TEST=test_1)

    sms_messenger(update_message=text_message)

 

    test_2 = ""

    text_message_2 = update(STATUS_TEST=test_2)

    sms_messenger(update_message=text_message_2)

 

    test_3 = "Machine name=GARY1;Datetime=2021074120005;Status=OK;Pct=0.25"

    text_message_3 = update(STATUS_TEST=test_3, pct=True)

    for string in text_message_3:

        sms_messenger(update_message=string)

    unittest.main()

 

 

 

 

 

 

 

 

from logging import NullHandler

import os

from twilio.rest import Client

 

def sms_messenger(update_message: str = None) -> None:

    numbers= ["+18302990120", "+18506616302", "+12107652968", "+12817605716","+12106856432"]

    account_sid = 'AC3a38bad3a45b7ed3025d485ec14d3b12'

    auth_token = 'b9bf99ba54b0efb7b1963bdd9c72d40d'

    client = Client(account_sid, auth_token)

    for number in numbers:

        message = client.messages.create(body=update_message, from_="+18638692541", to=number)

    return None

 

 

 

 

 

 

 

 

 

 

 

import unittest

from vba_script_reader import update



