from autogen import ConversableAgent
from config import llm


data_entry = ConversableAgent(name="DataEntry",
                              system_message="Your name is DataEntry and your task is to enter the data in excel sheet",
                              llm_config=llm,
                              human_input_mode="NEVER"
                              )

email_composer = ConversableAgent(name="Email_composer",
                                  system_message="Your name is Email_composer and your task is to compose a welcome email for visitors",
                                  llm_config=llm,
                                  human_input_mode="NEVER")

sender = ConversableAgent(name="Sender",
                              system_message="Your name is Sender and your task is to send email to visitor's email id",
                              llm_config=llm,
                              human_input_mode="NEVER")

linkedin_auto = ConversableAgent()