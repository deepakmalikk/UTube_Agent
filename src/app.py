import streamlit as st
from textwrap import dedent
from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
import os 
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set page configuration
st.set_page_config(
    page_title="UTube Video Analysis",
    page_icon="▶️",
    layout="wide"
)

def myagent() -> Agent:
    """Create and configure the YouTube analysis agent"""
    youtube_agent = Agent(
        name="YouTube Agent",
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

def compact_sidebar():
    """Create a more compact sidebar with collapsible examples"""
    with st.sidebar:
        st.markdown("### Quick Analysis Templates 🎯")
        analysis_types = {
            "Tutorial": {
                "emoji": "💻",
                "description": "Code examples & steps",
                "prompt": "Analyze code examples and implementation steps"
            },
            "Educational": {
                "emoji": "📚",
                "description": "Learning material",
                "prompt": "Create study guide with key concepts"
            },
            "Review": {
                "emoji": "📱",
                "description": "Product analysis",
                "prompt": "Extract features and comparisons"
            },
            "Creative": {
                "emoji": "🎨",
                "description": "Art & design",
                "prompt": "Document techniques and methods"
            }
        }
        
        selected_type = st.selectbox(
            "Select Analysis Type",
            options=list(analysis_types.keys()),
            format_func=lambda x: f"{analysis_types[x]['emoji']} {x}"
        )
        
        with st.expander("Analysis Details", expanded=False):
            st.markdown(f"**{analysis_types[selected_type]['description']}**")
            st.markdown(f"Default prompt: _{analysis_types[selected_type]['prompt']}_")
        
        return selected_type, analysis_types[selected_type]['prompt']

def main_content(analysis_type, default_prompt):
    """Handle main content area with URL and prompt inputs"""
    st.title("UTube Video Analysis 📹🔍")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        video_url = st.text_input(
            "Enter YouTube URL:",
            placeholder="https://youtube.com/..."
        )
    
    with col2:
        custom_prompt = st.checkbox("Customize Analysis Prompt")
    
    if custom_prompt:
        analysis_prompt = st.text_area(
            "Analysis Instructions:",
            value=default_prompt,
            height=100
        )
    else:
        analysis_prompt = default_prompt
    
    if st.button("Analyze Video 🔍", type="primary"):
        if video_url:
            try:
                youtube_agent = myagent()
                with st.spinner("📊 Processing video content..."):
                    result = youtube_agent.run(f"URL: {video_url}\nInstructions: {analysis_prompt}")
                    st.success("✅ Analysis Complete!")
                    
                    with st.expander("View Analysis", expanded=True):
                        st.markdown(result.content)
            except Exception as e:
                st.error("⚠️ Analysis failed. Please check your URL and try again.")
                with st.expander("Technical Details"):
                    st.code(str(e))
        else:
            st.warning("⚠️ Please enter a YouTube URL")

def main():
    analysis_type, default_prompt = compact_sidebar()
    main_content(analysis_type, default_prompt)

if __name__ == "__main__":
    main()