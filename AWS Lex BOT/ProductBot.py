"""
Lex Code Hook Interface to serve a sample bot product orders.
"""
import math
import dateutil.parser
import datetime
import time
import os
import logging
import numpy as np
from product import Product,ProductService

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)




def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message, product_list):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            "message": {
                "contentType": "PlainText",
                "content": message
    },
        
        'responseCard': {
            "version": 3,
            "contentType": "application/vnd.amazonaws.card.generic",
            "genericAttachments": [
                 {
                    "title": "Provider",
                    "subTitle": "Select one",
                    
                    "buttons": [                    
                        {
                            "text": product_list[0].name ,
                             "value": product_list[0].code
                        },
                        {
                             "text": product_list[1].name,
                             "value": product_list[1].code
                        },
                        {
                             "text": product_list[2].name,
                             "value": product_list[2].code
                        }
                    ]
                }
            ]
        }
        
    }
    }
    
def get_slots(intent_request):
    return intent_request['currentIntent']['slots']
    
def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }

    return response

def delegate(session_attributes, slots):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Delegate',
            'slots': slots
        }
    }
    

def isvalid_location(location):
    locations = ['Paris', 'Orlando', 'California']
    return location in locations


def isvalid_date(date):
    try:
        dateutil.parser.parse(date)
        return True
    except ValueError:
        return False

def build_validation_result(isvalid, violated_slot, message_content):
    return {
        'isValid': isvalid,
        'violatedSlot': violated_slot,
        'message': {'contentType': 'PlainText', 'content': message_content}
    }

def fetchProductInfo(intent_request):
    """
    Performs dialog management and fulfillment .
    """
    
    slots = get_slots(intent_request)
    source = intent_request['invocationSource']
    
    if source == 'FulfillmentCodeHook':
        
        location = get_slots(intent_request)["location"]
        itinerary = get_slots(intent_request)["itinenaries"]
        departureDate = get_slots(intent_request)["date"]

        if departureDate:
            if not isvalid_date(departureDate):
                return build_validation_result(False, 'date', 'I did not understand your departure date.  When would you like to travel?')

        if location:
            if not isvalid_location(location):
                return build_validation_result(False, 'location', 'I did not understand your location.  Where would you like to travel?')


        logger.debug('Location {}'.format(location))
        if itinerary is None or itinerary =="":
            logger.debug('Provider is none {}'.format(itinerary))

            productUrl = 'https://myproductdata.s3.amazonaws.com/products.csv'
            productPriceUrl = 'https://myproductdata.s3.amazonaws.com/product_prices.csv'

            productService = ProductService(productUrl,productPriceUrl)
            product_list = productService.getProductByLocation(departureDate,location)
            return elicit_slot(intent_request['sessionAttributes'],intent_request['currentIntent']['name'], slots, 'Provider', 'Please select provider.')
            
        return close(intent_request['sessionAttributes'],
                     'Fulfilled',
                     {'contentType': 'PlainText',
                      'content': 'Weather at {} is {} dgrees centigrade'.format(city,np.random.randint(28,36))})

    return  delegate(intent_request['sessionAttributes'], slots)

def calculatePrice(itinerary,departureDate,adultCount, childCount):
    return 1000


def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    logger.debug('dispatch userId={}, intentName={}'.format(intent_request['userId'], intent_request['currentIntent']['name']))

    intent_name = intent_request['currentIntent']['name']

    # Dispatch to your bot's intent handlers
    if intent_name == 'DisneyBookingBot':
        return fetchProductInfo(intent_request)

    raise Exception('Intent with name ' + intent_name + ' not supported')


""" --- Main handler --- """


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    logger.debug('event: {}'.format(event))
    return dispatch(event)
