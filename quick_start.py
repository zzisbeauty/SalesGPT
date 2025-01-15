from salesgpt.agents import SalesGPT
from langchain_community.chat_models import ChatLiteLLM

from dotenv import load_dotenv
load_dotenv() # make sure you have .env file with your API keys, eg., OPENAI_API_KEY=sk-xxx, MINDWARE_API_KEY etc.

# select your model - we support 50+ LLMs via LiteLLM https://docs.litellm.ai/docs/providers

# local model ollama  or from api
from apis import *

# llm = ChatLiteLLM(temperature=0.4, model_name="gpt-4-0125-preview")
llm = ChatLiteLLM(temperature=0.4,model="gpt-3.5-turbo",openai_api_key=yiapi[0],api_base=yiapi[1])

# 从给定的 ChatLiteLLM 实例初始化 SalesGPT Controller
sales_agent = SalesGPT.from_llm(llm, openai_api_key=yiapi[0], api_base_url=yiapi[1],
                            verbose=True, use_tools=True, 
                            product_catalog = "examples/sample_product_catalog_cn.txt",
                            salesperson_name="张三",
                            salesperson_role="销售代表") #  Sales Representative

sales_agent.seed_agent()
# sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt

# agent
sales_agent.step()

# user
sales_agent.human_step(input('Your response: '))

# agent
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt
sales_agent.step()

# user
sales_agent.human_step(input('Your response: '))

# agent
sales_agent.determine_conversation_stage() # optional for demonstration, built into the prompt
sales_agent.step()
