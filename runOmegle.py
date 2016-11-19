from pyomegle import OmegleHandler, OmegleClient

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
#        'card': {
#            'type': 'Simple',
#            'title': "SessionSpeechlet - " + title,
#            'content': "SessionSpeechlet - " + output
#        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def lambda_handler(event, context):
    if event["request"]["intent"]["name"] == "StartConversationIntent":
        return {}
