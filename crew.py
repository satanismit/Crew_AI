from crewai import Crew,Process
from Agents import blog_researcher,blog_writer
from Tasks import research_task,write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    
  agents=[blog_researcher, blog_writer],

  tasks=[research_task, write_task],

  process=Process.sequential,  # Optional: Sequential task execution is default

  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'MCP'})
print(result)