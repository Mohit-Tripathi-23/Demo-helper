# **Product Demo Assistant**

This project is a Streamlit app that utilizes the OpenAI API to generate a comprehensive product demo plan based on user-provided inputs. It includes steps for conducting a demo, handling product limitations, and structuring the demo presentation. The assistant generates a complete plan that can be downloaded as a text file.

## **Features**
- Accepts user input for:
  - Product Description
  - Technologies Used
  - Department (e.g., Marketing, Sales, IT, HR, Finance)
  - Product Limitations
- Generates the following outputs:
  1. **Demo Preparation Steps**: A step-by-step guide to conducting the product demo.
  2. **Product Limitations (Framed Positively)**: Provides a positive framing of the product's limitations.
  3. **Flow of Presentation**: A recommended flow for presenting the demo.
- Allows users to download the generated demo plan as a text file.

## **Requirements**

To run this app, you'll need the following:
- **Python 3.7+**
- **Streamlit**
- **OpenAI API Key**

### **Python Packages**

You can install the required packages using pip:

```bash
pip install streamlit openai
```

## **Getting Started**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd product-demo-assistant
   ```

2. **Install Dependencies**:
   Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your OpenAI API Key**:
   You will need an API key from OpenAI to interact with the API.
   - [Get your API Key here](https://platform.openai.com/account/api-keys)

4. **Run the App**:
   After setting up your API key, you can run the Streamlit app using:
   ```bash
   streamlit run app.py
   ```

5. **Enter the Inputs**:
   - Enter the **Product Description**, **Technologies Used**, **Department**, and **Product Limitations** in the input fields.
   - Click **Generate Demo Plan** to create the product demo.

6. **Download the Plan**:
   After generating the demo plan, you can click the **Download Demo Plan** button to download the output as a text file.

## **Project Structure**

```
|-- app.py                # Main Streamlit app script
|-- requirements.txt       # Python dependencies
|-- README.md              # Documentation (this file)
```

## **How It Works**

1. **OpenAI API**:
   - The app communicates with the OpenAI API via `openai.ChatCompletion.create`, sending specific prompts to generate a product demo tailored to the inputs.
   
2. **Streamlit Interface**:
   - Streamlit is used to create an interactive web interface that accepts input and displays results.
   
3. **Download Feature**:
   - After generating the demo plan, users can download the entire plan as a `.txt` file using Streamlit's `st.download_button`.

## **Customization**
- You can customize the prompts or adjust the logic in the `app.py` file to suit your specific requirements.
- Modify the input fields or change the flow for generating responses based on your desired use case.

## **Screenshots**

![Product Demo Assistant Interface](screenshot.png)  
_Screenshot of the app where users can input data and download the generated demo plan._

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Contact**
For any questions or feedback, feel free to reach out to [your-email@example.com].

---

### **Note**: Make sure to add the correct repository URL for cloning and your email for contact information. Additionally, you can take a screenshot of your app interface to add under the **Screenshots** section.