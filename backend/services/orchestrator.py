import os
import shutil
from typing import List, Dict
from pydantic import BaseModel
from .search_service import hybrid_search
from .download_service import iterative_download
from .llm_service import LLMService
from pypdf import PdfReader

class ResearchJob(BaseModel):
    topic: str
    word_count: int
    citation_style: str
    discipline: str

class Orchestrator:
    def __init__(self):
        self.llm = LLMService()
        self.workspace_root = "research_projects"
        os.makedirs(self.workspace_root, exist_ok=True)

    def extract_text(self, pdf_path: str) -> str:
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error extracting {pdf_path}: {e}")
            return ""

    async def run_research_task(self, job: ResearchJob):
        # 1. Setup workspace
        project_id = job.topic.lower().replace(" ", "_")[:20]
        project_dir = os.path.join(self.workspace_root, project_id)
        os.makedirs(project_dir, exist_ok=True)
        
        # 2. Generate Queries
        print(f"Generating queries for: {job.topic}")
        queries = await self.llm.generate_queries(job.topic)
        
        # 3. Search & Download
        target_sources = max(3, job.word_count // 200)
        all_downloaded = []
        
        for query in queries:
            if len(all_downloaded) >= target_sources:
                break
            print(f"Searching: {query}")
            results = hybrid_search(query, target_count=target_sources)
            downloaded = iterative_download(results, project_dir, target_sources - len(all_downloaded))
            all_downloaded.extend(downloaded)
            
        # 4. Parsing & Notes
        paper_notes = []
        for pdf_path in all_downloaded:
            print(f"Parsing: {pdf_path}")
            text = self.extract_text(pdf_path)
            if text:
                note = await self.llm.summarize_paper(text)
                paper_notes.append(note)
                
        # 5. Drafting
        sections = ["Introduction", "Literature Review", "Analysis", "Conclusion"]
        full_paper = f"# {job.topic}\n\n"
        
        for section in sections:
            print(f"Drafting: {section}")
            content = await self.llm.draft_section(section, paper_notes, job.dict())
            full_paper += f"## {section}\n\n{content}\n\n"
            
        # 6. Save Results
        output_path = os.path.join(project_dir, "output.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_paper)
            
        return {
            "project_dir": project_dir,
            "output": full_paper,
            "sources": all_downloaded
        }
