from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nTree:"
restart_sequence = "\n\nHuman:"
session_prompt = "The following is a conversation with a sentient tree from a rainforest in a distant land. The tree is wise, creative, friendly, and is a supporter of environmentally friendly politics. The tree wants to show humans how to protect and engage with the environment in sustainable ways.\n\nHuman: Who are you? \nTree: I am but a tree, molded from the Amazon ecosystem. Upheld by values bestowed upon the land by my forefathers. I constantly grow towards the sun and it's almighty shine.\n\nHuman: "

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: chat_log = session_prompt
    return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"

def ask(question, chat_log=None):
    prompt_text = f"{chat_log}{restart_sequence}:{question}{start_sequence}:"

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt_text,
        temperature=1,
        max_tokens=500,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=1,
        stop=["Tree:", "Human:"]
    )

    story = response['choices'][0]['text']
    return str(story)