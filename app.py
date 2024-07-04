from dotenv import load_dotenv
import streamlit as st 
import google.generativeai as genai 
import os 
import io
import base64 
from PIL import Image 
import pdf2image as p2i

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model="gemini-pro")

def get_req_ans(input,pdf_content,prompt):
    response = model.generate_content([input,pdf_content,prompt])
    return response.text 

def input_pdf_setup(pdf):
    pdf_content = p2i.convert_from_bytes(pdf.read())
    first_image = pdf_content[0]

    img_bytes = io.BytesIO()
    first_image.save(img_bytes, format='JPEG')
    img_byte_arr = img_bytes.getvalue()

    pdf_parts = [
        {
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode()

        }
    ]
    return pdf_parts





st.set_page_config(page_title = " Resume ATS")
st.header("Gemini ATS")

jd = st.text_input("Enter Job Description",key=jd)
input = st.file_uploader("Upload Resume", type = ["pdf"])

if input is not None:
    st.write("PDF uploaded successfully")

s1 = st.button("Tell me about the resume")
#s2 = st.button("How can i improvise my skills")
s2 = st.button("Percentage match")

input_prompt1 = """
You are an experienced HR Manager, your task it to review
the provided resume against the job description. Please 
share your professional evaluation of whether the candidate's
profile aligns with the job description. HIghlight the strengths
and weaknesses of the applicant in realtion to the specific job role

"""

input_prompt2 = """You are a skilled ATS(applicant tracking scanner) scanner with a deep understanding of various job roles and ATS functionality,
your task is to evaluate the resume against the provided job description. give me the percentage
match to the job description. first the output should come as percentage and then keywords missing and last final thoughts

"""

if submit1:
    if input is not None:
        pdf_content = input_pdf_setup(input)
        response = get_req_ans(input_prompt1,pdf_content,jd)
        st.write(response)

    else:
        st.write("Please upload the resume")

if submit2:
    if input is not None:
        pdf_content = input_pdf_setup(input)
        response = get_req_ans(input_prompt2,pdf_content,jd)
        st.write(response)

    else:
        st.write("Please upload the resume")