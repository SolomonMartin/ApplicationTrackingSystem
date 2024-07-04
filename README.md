# ApplicationTrackingSystem

ApplicationTrackingSystem is a LangChain and Streamlit application that evaluates resumes against job descriptions using Google Generative AI. It provides detailed evaluations and percentage matches to help users understand how well their resumes align with specific job roles.

## Features

- **Resume Upload:** Users can upload resumes in PDF format.
- **Job Description Input:** Users can input job descriptions to compare against the uploaded resumes.
- **Detailed Evaluation:** Provides a professional evaluation highlighting the strengths and weaknesses of the resume.
- **Percentage Match:** Calculates a percentage match to the job description and identifies missing keywords.
- **User-Friendly Interface:** Built with Streamlit, providing a simple and intuitive user experience.

## Technologies Used

- **LangChain:** Integrates various language processing tasks such as text extraction and natural language understanding.
- **Streamlit:** Creates interactive web applications directly from Python scripts.
- **Google Generative AI:** Provides advanced text generation capabilities for evaluating resumes.
- **PIL (Python Imaging Library) & pdf2image:** Handles image processing tasks such as converting PDF files to images.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ResumeATSApp.git
   cd ResumeATSApp
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
3. Set up your Google API key:

    Create a .env file in the root directory of the project.
    Add your Google API key to the .env file:
    ```makefile
    GOOGLE_API_KEY=your_api_key_here
4. Run the Streamlit app:
    ```bash
    streamlit run app.py
Usage
  ```
  Open the app in your browser.
  Upload a resume in PDF format.
  Enter the job description for comparison.
  Click on "Tell me about the resume" to receive a detailed evaluation.
  Click on "Percentage match" to see how well the resume aligns with the job description.
