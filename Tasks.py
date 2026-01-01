from crewai import Task
from Tools import yt_tool
from Agents import blog_writer, blog_researcher

# task --1 
# research 

research_task = Task(

    description=(
        "Identify the video {topic}."
        "Identify the most relevant videos from this channel and extract "
        "key explanations, insights, workflows, and examples discussed in the videos. "
    ),

    expected_output='Summarize the info from the yt channel video on the topic of {topic} and create the content of the blog',

    tools=[yt_tool],

    agent= blog_researcher
)

# task --2 
# blog writing  

write_task = Task(

  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),

  expected_output='Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
 
  tools=[yt_tool],

  agent=blog_writer,

  async_execution=False,

  output_file='new-blog-post.md'  # Example of output customization
)