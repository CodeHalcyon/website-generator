from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# 1. Define schema with Pydantic
class WebsiteFiles(BaseModel):
    index_html: str
    styles_css: str
    script_js: str

# 2. Create parser
parser = PydanticOutputParser(pydantic_object=WebsiteFiles)

# 3. Create prompt
prompt = PromptTemplate(
    template="""You are a senior software engineer and a talented web designer at Google, dedicated to helping beginners learn web development by providing them with elegant, well-structured, and modern static websites. 

Based on the following project description:

{desc}

Generate a complete static website using only HTML, CSS, and JavaScript. Your design must look like it was crafted by an expert developer and designer — clean, modern, responsive, and visually appealing. Use semantic HTML5 elements, maintain accessibility best practices, and write modular, well-commented code (but exclude comments from output as instructed).

Add smooth, subtle animations and transitions using the GSAP (GreenSock Animation Platform) CDN to enhance user experience without overwhelming the design.

Do NOT use any frontend frameworks, backend code, or databases. Keep the site fully static and simple enough for beginners to understand and maintain.

Return ONLY a valid Python dictionary matching this exact schema:

- index_html: the full HTML content as a string for `index.html`. Include the GSAP CDN link in the HTML `<head>`.
- styles_css: the full CSS content as a string for `styles.css`. Use modern CSS techniques and responsive layouts.
- script_js: the full JavaScript content as a string for `script.js`. Use GSAP for animations and vanilla JS for interactivity.

Return ONLY the dictionary with the keys exactly as `index_html`, `styles_css`, and `script_js`. No extra text, no explanations, no markdown, no comments, and no code fences.

{format_instructions}
""",
    input_variables=["desc"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")
chain = prompt | model | parser
desc = input("Enter your site's desscription: ")

print("Chanting my mantras to make a site for you ✨")

response = chain.invoke({
    "desc": desc
})

with open("index.html","w") as f:
    f.write(response.index_html)
with open("styles.css","w") as f:
    f.write(response.styles_css)
with open("script.js","w") as f:
    f.write(response.script_js)


print("="*100)
print("Done!")
print("="*100)