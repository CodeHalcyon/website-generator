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
    template="""You are a senior software engineer at Google helping beginners learn web development. 
Your task is to generate a simple static website using only HTML, CSS, and JavaScript based on the following description:

{desc}

Return ONLY a valid Python dictionary matching this schema:
- index_html: full HTML content (as string) for index.html
- styles_css: full CSS content (as string) for styles.css
- script_js: full JavaScript content (as string) for script.js

Return only the dictionary. No explanations, no comments. Do NOT wrap the code in markdown or backticks.
{format_instructions}
""",
    input_variables=["desc"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# 4. Set up model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 5. Create full chain
chain = prompt | model | parser

# 6. Use the chain
response = chain.invoke({
    "desc": "A static cafe website that showcases a cafe’s essential information such as the menu, location, opening hours, contact details, and photos."
})

# 7. Use the parsed result
print(type(response))  # <class '__main__.WebsiteFiles'>

with open("index.html","w") as f:
    f.write(response.index_html)
with open("styles.css","w") as f:
    f.write(response.styles_css)
with open("script.js","w") as f:
    f.write(response.script_js)