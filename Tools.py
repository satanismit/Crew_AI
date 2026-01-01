from crewai_tools import YoutubeVideoSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

# Ensure OpenAI API key is loaded
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

yt_tool = YoutubeVideoSearchTool()