# langchain_helper.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret_key import GOOGLE_API_KEY
import os

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def generate_major_and_universities(province):
    # Step 1: Province to Major
    prompt_template_major = PromptTemplate(
        input_variables=['province'],
        template="""
        Based on current trends and job market demand, suggest the top 3 trending university majors for students in {province}. 
        Return only the names of the majors as a comma-separated list.
        """
    )
    major_chain = LLMChain(llm=llm, prompt=prompt_template_major, output_key="major")

    # Step 2: Major to Universities
    prompt_template_universities = PromptTemplate(
        input_variables=['major', 'province'],
        template="""
        List top universities in Canada that offer {major} in that {province}. Return as a comma-separated list.
        """
    )
    university_chain = LLMChain(llm=llm, prompt=prompt_template_universities, output_key="text")

    chain = SequentialChain(
        chains=[major_chain, university_chain],
        input_variables=['province'],
        output_variables=['major', 'text'],
        verbose=False
    )

    response = chain({'province': province})
    return response

if __name__ == "__main__":
    print(generate_major_and_universities("Ontario"))
