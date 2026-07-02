import os 

import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
key=os.getenv("api_key")
modelname="gemini-3.1-flash-lite"
parser = JsonOutputParser()


sender_email = input("Sender Email: ").strip()
recipient_email = input("Recipient Email: ").strip()
recipient_name = input("Recipient Name: ").strip()
your_name = input("Your Name: ").strip()
your_phone = input("Your Phone Number: ").strip()
your_linkedin = input("Your LinkedIn Profile URL: ").strip()
subject_of_mail = input("Subject of Mail: ").strip()
tone = input("Tone (e.g., Professional, Casual, Urgent): ").strip()

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

#Model
model=ChatGoogleGenerativeAI(model=modelname,api_key=key)

#TemplatedPrompt
template=PromptTemplate(input_variables=["subject_of_mail","email_id","tone","name","link","phone","rec_name"],template="""Hi!!Gemini My is name is {name} Senders name is {name} Consider Yourself as the best person in this world who can write the best emails in the world and now generate an email for the recievers name is {rec_name} given subject:- '{subject_of_mail}' for the given email id :- {email_id}  and make sure to write the email in the given tone :- {tone} make sure you dont mess up the things dont use unnesccary of commas and asterik marks write the email in a professional manner!Generate ONLY using the information provided below. Do not invent, assume, or include any contact details other than the ones explicitly supplied. If any required field is missing, leave it blank instead of creating one.Heres my linked in url: {link} my phone number :{phone} The Mail Words must be in the range of atleast  50 - 120 words and if and only if the given subject of the mail  looks  vague or too small add some good words but make sure the context and the meaning of the subject remains the given one only!!and Return ONLY valid JSON.
everytime end the mail by adding  a line break then Yours faithfully  and the Senders name
Do not wrap it inside markdown.

Do not use ```json.

Follow exactly these format instructions:

{format_instructions}""",partial_variables={"format_instructions":parser.get_format_instructions()})

#LCEL Chain only works with Runnable objects!

#The Main working Chain!!

#Dictionary(Stored Variable Values!!)->Template(Nothing but Prompt)->LLM ->Parser ->Output
chain=template|model|parser

response=chain.invoke({"subject_of_mail":subject_of_mail,"email_id":recipient_email,"tone":tone,"name":your_name,"link":your_linkedin,"phone":your_phone,"rec_name":recipient_name})
print("To:\n"+response["to"]+"\n")
print("Subject:\n"+response["subject"]+"\n")
print("Body:\n"+response["body"])

creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
   
    
    #Creating EmailMessage Object then adding all the necessary info!!

    message = EmailMessage()
    message.set_content(response["body"])#the actual mail!!!!
    message["To"]=recipient_email
    message["From"]=sender_email
    message["subject"]=response["subject"] #Passing what our LLM Generated !!
 
    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    create_message = {"raw": encoded_message}
    
    # pylint: disable=E1101
    #OG PART!!

    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
  
   
    print(f'Message Id: {send_message["id"]}')

except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

