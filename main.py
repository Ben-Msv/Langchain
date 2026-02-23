from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from prompts import prompt_template_plan

llm = OpenAI(temperature=0.8)

prompt_value_plan = prompt_template_plan.format(age="23", weight="88", height="187", gender="male", goal="low_calorie")
