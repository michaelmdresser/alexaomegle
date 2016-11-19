def lambda_handler(event, context):
    if event["request"]["intent"]["name"] == "StartConversationIntent":
        return {
          "version": "1.0",
          "response": {
            "outputSpeech": {
              "type": "PlainText",
              "text": "hi Michael"
            },
            "reprompt": {
              "outputSpeech": {
                "type": "PlainText",
                "text": ""
              }
            },
            "shouldEndSession": True
          },
          "sessionAttributes": {}
        }
