import os
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent

llm = ChatOpenAI(model="gpt-4-turbo")

tools = load_tools(["ddg-search", "wikipedia"], llm=llm)

agent = initialize_agent(
  tools,
  llm,
  agent= 'zero-shot-react-description',
  verbose= True
)

print(" - - - - -")


query= """
Vou viajar para Maragogi em novembro de 2024.
Quero que faça para um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem e com o preço de passagem de São Paulo para Maragogi.
"""


agent.run(query)