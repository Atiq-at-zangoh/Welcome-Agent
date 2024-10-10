from autogen import ConversableAgent
from langchain_google_genai import ChatGoogleGenerativeAI


data_entry = ConversableAgent(name="DataEntry",
                              system_message="Your name is DataEntry and your task is to enter the data in excel sheet",
                              human_input_mode="NEVER",
                              )

email_composer = ConversableAgent()

sender = ConversableAgent()

linkedin_auto = ConversableAgent()