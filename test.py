from WelcomeUtility.agents import email_composer

task="Write a welcome email for the visitor, an event is scheduled at Zangoh. So email should be in 150 words"
email_body=email_composer.generate_reply(messages=[{"content": task, "role": "user"}])

print(email_body)