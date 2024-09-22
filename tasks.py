from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

#Research task 
research_task = Task(
    description=(
        "Identify the video {topic}."
        "Get the detailed information about the video from the channel"
    ),
    expected_output="A 3 paragraph long report based on the {topic} of the video",
    tools = [yt_tool],
    agent=blog_researcher
)

#Writing task
writing_task = Task(
    description=(
        "get the info from the youtube channel on the {topic}"
    ),
    expected_output="Summarize the info about the video on the topic {topic}",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new_blog_post.md"
)