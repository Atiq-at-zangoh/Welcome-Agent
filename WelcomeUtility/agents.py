from autogen import AssistantAgent
from config import llm

email_composer = AssistantAgent(name="Email_composer",
                                  system_message="Your are an Email_composer and your task is to compose a welcome email for new visitor",
                                  llm_config={"model": llm},
                                  human_input_mode="NEVER")

sender = AssistantAgent(name="Sender",
                              system_message="Your name is Sender and your task is to send email on visitor's email id",
                              llm_config=llm,
                              human_input_mode="NEVER")

linkedin_auto = AssistantAgent()