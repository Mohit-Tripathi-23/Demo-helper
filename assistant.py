import streamlit as st
from openai import OpenAI

# Set your OpenAI API Key here
api_key = st.text_input("Enter your OpenAI API key", type="password")
client = OpenAI(api_key=api_key)
st.title("Product Demo Assistant")
# Set your OpenAI API Key here

st.title("🤖 Product Demo Assistant")
st.markdown("Welcome to the **Product Demo Assistant**! 🎉 Let me help you create a comprehensive and engaging product demo plan for your clients. 🚀")

# User inputs with emojis
st.header("📝 Product Details")
product_description = st.text_area("📄 Product Description", "Enter a brief description of the product")
technologies_used = st.text_area("💻 Technologies Used", "List technologies used in the product")
department = st.selectbox("🏢 Department", ["Marketing", "Sales", "IT", "HR", "Finance"])
product_highlights = st.text_area("✨ Product Highlights", "List the key highlights of your product")
product_limitations = st.text_area("⚠️ Product Limitations", "List known product limitations")
target_audience = st.multiselect("🎯 Target Audience", ["CTO", "CEO", "Directors", "Clients"], help="Select your target audience")

generate_button = st.button("🛠️ Generate Demo Plan")

# Function to interact with OpenAI ChatCompletion
def generate_openai_chat_response(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo" depending on availability
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# System Instruction (Prompt Engineering)
system_prompt = {
    "role": "system",
    "content": (
        "You are a demo assistant designed to provide engaging and insightful product demonstrations for potential clients. "
        "Based on the product's description, technologies used, product highlights, and known limitations, create a tailored demo. "
        "Your output should highlight key strengths, outline steps for a successful product demo, explain the product’s limitations positively, "
        "and provide a recommended flow for the presentation. Adjust the demo based on the selected target audience (CTO, CEO, Directors, or Clients). "
        "Be concise but clear, and focus on the value for the specific department."
    )
}

# Generate results when the user clicks the button
if generate_button and api_key:
    st.write("### Generating Product Demo Plan... 🔄")

    # Initialize an empty plan
    complete_plan = ""

    # Prompt for demo steps
    steps_prompt = {
        "role": "user",
        "content": f"""
        Create a step-by-step guide to provide a demo for the {department} department.
        Product Description: {product_description}
        Technologies Used: {technologies_used}
        Product Highlights: {product_highlights}
        Target Audience: {", ".join(target_audience)}
        Highlight features relevant to {department}.
        """
    }

    # Prompt for limitations with positive framing
    limitations_prompt = {
        "role": "user",
        "content": f"""
        Based on the following product limitations, explain how these can be seen as opportunities for future development or customization.
        Frame the limitations in a positive light for the {department} department and the target audience ({", ".join(target_audience)}).
        Limitations: {product_limitations}
        """
    }

    # Prompt for presentation flow
    flow_prompt = {
        "role": "user",
        "content": f"""
        Create a presentation flow for a demo that engages {department} and the target audience ({", ".join(target_audience)}).
        Include an introduction, feature showcase, interactive section, addressing product limitations positively, and conclusion.
        Product Description: {product_description}
        Technologies Used: {technologies_used}
        Product Highlights: {product_highlights}
        Limitations: {product_limitations}
        """
    }

    # Demo preparation steps
    st.write("#### 📋 Demo Preparation Steps")
    steps_messages = [system_prompt, steps_prompt]
    steps_response = generate_openai_chat_response(steps_messages)
    st.write(steps_response)
    complete_plan += "## Demo Preparation Steps\n" + steps_response + "\n\n"

    # Product limitations with positive framing
    st.write("#### ⚙️ Product Limitations (Framed Positively)")
    limitations_messages = [system_prompt, limitations_prompt]
    limitations_response = generate_openai_chat_response(limitations_messages)
    st.write(limitations_response)
    complete_plan += "## Product Limitations (Framed Positively)\n" + limitations_response + "\n\n"

    # Flow of the presentation
    st.write("#### 🎤 Flow of Presentation")
    flow_messages = [system_prompt, flow_prompt]
    flow_response = generate_openai_chat_response(flow_messages)
    st.write(flow_response)
    complete_plan += "## Flow of Presentation\n" + flow_response + "\n\n"

    # Allow downloading the complete plan as a text file
    st.write("### 📥 Download the Complete Plan")
    st.download_button(
        label="📄 Download Demo Plan",
        data=complete_plan,
        file_name="product_demo_plan.txt",
        mime="text/plain"
    )
else:
    if not api_key:
        st.warning("⚠️ Please enter your OpenAI API key to generate the demo plan.")
