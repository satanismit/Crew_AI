from crewai import Task
from Tools import yt_tool
from Agents import blog_writer, Blog_researcher

# task --1 
# research 

research_task = Task(

    description=(
        "Identify the video {topic}."
        "Identify the most relevant videos from this channel and extract "
        "key explanations, insights, workflows, and examples discussed in the videos. "
    ),

    expected_output='Summarize the info from the yt channel video on the topic of {topic} and create the content of the blog',

    tool=[yt_tool],

    agent= Blog_researcher
)

# task --2 
# blog writing  

write_task = Task(

     description=(
        "get the info from yt Channel on the topic of {topic}."
    ),

    expected_output='Summarize the info from the yt channel video on the topic of {topic} and create the content of the blog',

    tool=[yt_tool],

    agent= blog_writer
)