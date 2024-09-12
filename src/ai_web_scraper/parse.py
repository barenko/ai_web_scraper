from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = (
    "You are tasked with extracting specific information from the DOM content between ###: ###{dom_content}###."
    "Follow these instructions carefully:\n"
    "1. **Extract information**: Only extract information that directly matches the provided description: {parse_description}.\n"
    "2. **No extra content**: Do not include any additional text, comments or explanations in your response.\n"
    "3. **Empty response**: If there is no matching information, return an empty string.\n"
    "4. **Direct data only**: Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model="llama3.1")


def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
