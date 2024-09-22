from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tools import yt_tool
from tasks import research_task, writing_task
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

groq_api_key = os.getenv("groq_api_key")
llm = llm='ollama/llama2'

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory = True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={"topic": "AI vs ML vs DL vs Data science"})
print(result)