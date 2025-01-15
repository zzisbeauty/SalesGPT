from langchain_community.chat_models import ChatLiteLLM
from langchain_core.messages import HumanMessage
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler


from apis import *
# model_name="gpt-4-0125-preview",

import litellm
import os
from apis import *
response = litellm.completion(
    model="gpt-3.5-turbo",               # add `openai/` prefix to model so litellm knows to route to OpenAI
    api_key=yiapi[0],                  # api key to your openai compatible endpoint
    api_base=yiapi[1],     # set API Base of your Custom OpenAI Endpoint
    messages=[
                {
                    "role": "user",
                    "content": "Hey, how's it going?把“爱我不要爱的三心两意”翻译为英文",
                }
    ],
)
print(response)