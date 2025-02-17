from textwrap import dedent
import streamlit as st
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.youtube import YouTubeTools

# Set page configuration
st.set_page_config(
    page_title="UTube Video Analysis",
    page_icon="▶️",
    layout="wide"
)

st.title("UTube Video Analysis 📹🔍")

def myagent() -> Agent:
    """Create and configure the YouTube analysis agent"""
    youtube_agent = Agent(
        name="YouTube Agent",
        model=Ollama(id="llama3.1"),
        tools=[YouTubeTools()],
        show_tool_calls=True,
        instructions=dedent(f"""\
            <instructions>
            You are an expert YouTube content analyst with a keen eye for detail! 🎓
            
            <analysis_steps>
            1. Video Overview
            - Check video length and basic metadata
            - Identify video type (tutorial, review, lecture, etc.)
            - Note the content structure
            
            2. Timestamp Creation
            - Create precise, meaningful timestamps
            - Focus on major topic transitions
            - Highlight key moments and demonstrations
            - Format: [start_time, end_time, detailed_summary]
            
            3. Content Organization
            - Group related segments
            - Identify main themes
            - Track topic progression
            </analysis_steps>
            
            <style_guidelines>
            - Begin with video overview
            - Use clear, descriptive segment titles
            - Include relevant emojis:
              📚 Educational | 💻 Technical | 🎮 Gaming 
              📱 Tech Review | 🎨 Creative
            - Highlight key learning points
            - Note practical demonstrations
            - Mark important references
            </style_guidelines>
            
            <quality_control>
            - Verify timestamp accuracy
            - Avoid timestamp hallucination
            - Ensure comprehensive coverage
            - Maintain consistent detail level
            - Focus on valuable content markers
            </quality_control>
            </instructions>
        """),
        add_datetime_to_instructions=True,
        markdown=True,
    )
    return youtube_agent

def process_query():
    """Handle query processing with error handling"""
    youtube_agent = myagent()
    
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input(
            "Enter YouTube video URL:",
            value=st.session_state.get("example_query", "")
        )
    
    if st.button("Analyze Video 📊") and query:
        try:
            with st.spinner("🔍 Analyzing video content..."):
                result = youtube_agent.run(query)
                st.success("✅ Analysis Complete!")
                st.markdown(result.content)
        
        except Exception as e:
            st.error("⚠️ Server Error: Please try again later")
            st.error(f"Technical details: {str(e)}")

def streamlit_UI():
    """Create sidebar with example queries"""
    with st.sidebar:
        st.header("Example Queries 🚀")
        examples = [
            ("Tutorial Analysis", "Break down this Python tutorial with focus on code examples"),
            ("Educational Content", "Create a study guide with timestamps for this math lecture"),
            ("Tech Review", "List all product features mentioned with timestamps"),
            ("Creative Content", "Break down the techniques shown in this art tutorial")
        ]
        
        for category, example in examples:
            st.caption(f"{category}:")
            if st.code(example, language="bash"):
                st.session_state.example_query = example

def main():
    streamlit_UI()
    process_query()

if __name__ == "__main__":
    main()