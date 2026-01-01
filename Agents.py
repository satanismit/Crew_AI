from crewai import Agent

# Agent --> 1
## create first Researcher Agent 

Blog_researcher = Agent (

    role="Blog Researcher from Youtube Channel",
    goal = "get the relevant video content for the topic {topic} from yt channel",
    verbose= True,
    memory = True,
    backstory= (
        "Expert in understanding videos of AI, machine learning and gen ai and providing suggestion"
    ),

    tools = [],
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
    tools = [],
    allow_delegation = False
)




