from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

groq_api_key = os.getenv("groq_api_key")
llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='groq_api_key')

blog_researcher = Agent(
    role = 'Blog researcher from youtube videos',
    goal = 'get the relevant video content for the topic {topic} from YT channel', 
    verbose = True,
    memory = True,
    backstory= (
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion"),
    tools = [yt_tool],
    llm = llm,
    allow_delegation=True
)

blog_writer = Agent(
    role='Blog writer',
    goal = "Narrate compelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=("With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."),
    tools = [yt_tool],
    allow_delegation=False
)