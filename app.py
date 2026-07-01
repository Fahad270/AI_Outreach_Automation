import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


load_dotenv()
key=os.getenv("api_key")
modelname="gemini-3.1-flash-lite"

subject_of_mail=input("Please Enter Subject of the Email:-\n")
email_id=input("Please Enter the correct emailid of the reciever.\n")
tone=input("Enter the tone in which the email is to be successfuly generated.\n")

#Model
model=ChatGoogleGenerativeAI(model=modelname,api_key=key)

#TemplatedPrompt
template=PromptTemplate(input_variables=["subject_of_mail","email_id","tone"],template="""Consider Yourself as the best person in this world who can write the best emails in the world and now generate an email for the given subject:- '{subject_of_maill}' for the given email id :- {email_idd}  and make sure to write the email in the given tone :- {tonee} make sure you dont mess up the things dont use unnesccary of commas and asterik marks write the email in a professional manner!""")


#FilledPrompt
filled_prompt=template.format(subject_of_maill=subject_of_mail,email_idd=email_id,tonee=tone)

#Model Call
response=model.invoke(filled_prompt)

print(response.text)