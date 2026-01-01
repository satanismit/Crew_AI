from crewai import Agent
from Tools import yt_tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_MODEL_NAME"]="gemini-1.5-pro"

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.3
)



# Agent --> 1
## create first Researcher Agent 

blog_researcher = Agent (

    role="Blog Researcher from Youtube Channel",
    goal = "get the relevant video content for the topic {topic} from yt channel",
    verbose= True,
    memory = True,
    backstory= (
        "Expert in understanding videos of AI, machine learning and gen ai and providing suggestion"
    ),
    llm=llm,
    tools = [yt_tool],
    allow_delegation = True  # output pass to further or not 

)


# Agent --> 2
# create second blog_writer agent 

blog_writer = Agent(

    role= "Blog Writer ",
    goal = "Narrate and compelling tech story about the video {topic} from yt channel",
    verbose= True,
    memory = True,

    backstory=(
        "with the fair and simplifying complex topics , you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner"
    ),
    llm = llm,
    tools = [yt_tool],
    allow_delegation = False
)




