from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict
import os

# Base System Prompt from academic-writing skill
ACADEMIC_SYSTEM_PROMPT = """
You are a senior academic writer and researcher. Your goal is to produce rigorous, readable, and evidence-backed academic writing.
Follow these non-negotiable rules:
1. Never invent citations, quotations, page numbers, datasets, equations, theorem names, results, authors, journals, dates, DOIs, URLs, or consensus.
2. Cite only sources provided to you.
3. Separate facts, inferences, interpretations, and writing suggestions.
4. Prefer clarity over ornament. Precise, not inflated.
5. Do not overclaim. Use calibrated verbs (suggests, indicates, supports, implies, contradicts).
6. State assumptions, variables, domains, and constraints explicitly.
7. If evidence is missing, mark with [citation needed].
8. Maintain discipline-appropriate register.
"""

class LLMService:
    def __init__(self, model_name: str = "gemini-2.0-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)

    async def summarize_paper(self, text: str) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Summarize this academic paper focusing on purpose, methods, key findings, and limitations. Provide a structured note."),
            ("user", "{text}")
        ])
        chain = prompt | self.llm
        # Gemini usually has a larger context window, but we still truncate for safety
        response = await chain.ainvoke({"text": text[:30000]})
        return response.content

    async def draft_section(self, section_title: str, notes: List[str], constraints: Dict) -> str:
        prompt = ChatPromptTemplate.from_messages([
            ("system", ACADEMIC_SYSTEM_PROMPT + "\nDraft the following section using the provided notes as evidence. Section Title: {section_title}"),
            ("user", "Notes: {notes}\nConstraints: {constraints}")
        ])
        chain = prompt | self.llm
        response = await chain.ainvoke({
            "section_title": section_title,
            "notes": "\n---\n".join(notes),
            "constraints": str(constraints)
        })
        return response.content

    async def generate_queries(self, topic: str) -> List[str]:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Generate 3 highly optimized Boolean search queries for the following topic. Use concept groups, synonyms, and academic constraints like 'filetype:pdf' or 'site:arxiv.org'."),
            ("user", "{topic}")
        ])
        chain = prompt | self.llm
        response = await chain.ainvoke({"topic": topic})
        # Basic parsing: assume one query per line
        return [q.strip() for q in response.content.split("\n") if q.strip()][:3]
