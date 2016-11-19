from pyomegle import OmegleHandler, OmegleClient

unreadMessages = []
oHandler = OmegleHandler(unreadMessages, loop=True)
oClient = OmegleClient(oHandler, wpm=47, lang='en')


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
        oClient.start()
        return build_speechlet_response("", "finding conversation", "", "true")
    elif event["request"]["intent"]["name"] == "ReadMessagesIntent":
        unread = ""
        for message in unreadMessages:
            unread += message + " "
        return build_speechlet_response("", unread, "", "true")
