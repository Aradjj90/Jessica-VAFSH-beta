import json
import dialogflow
#from google.cloud import dialogflow
from google.protobuf.json_format import MessageToJson
import os
import Answer_Dictionary as say


def chatbotmessage(text):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your token"
    project_id = "your project id"
    session_id = "your id"
    language_code = "en"
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    phrase = text
    text_input = dialogflow.types.TextInput(text=phrase, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response_dialogflow = session_client.detect_intent(session=session, query_input=query_input)
    response = MessageToJson(response_dialogflow.query_result)
    responseJson = json.loads(response)
    response_message = responseJson['fulfillmentText']
    if response_message:
        return response_message
    else:
        return say.get('dialogflow')


if __name__ == "__main__":
    while True:
        print(chatbotmessage(input()))
