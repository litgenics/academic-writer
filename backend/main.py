from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from services.orchestrator import Orchestrator, ResearchJob

load_dotenv()

app = FastAPI(title="Academic Writer API")
orchestrator = Orchestrator()

# Enable CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store for job status (MVP only)
jobs = {}

@app.get("/")
async def root():
    return {"message": "Academic Writer API is running"}

@app.post("/research")
async def create_research(job: ResearchJob, background_tasks: BackgroundTasks):
    job_id = f"job_{len(jobs) + 1}"
    jobs[job_id] = {"status": "processing", "data": None}
    
    async def run_task():
        try:
            result = await orchestrator.run_research_task(job)
            jobs[job_id] = {"status": "completed", "data": result}
        except Exception as e:
            print(f"Job failed: {e}")
            jobs[job_id] = {"status": "failed", "error": str(e)}

    background_tasks.add_task(run_task)
    return {"job_id": job_id}

@app.get("/research/{job_id}")
async def get_job(job_id: str):
    return jobs.get(job_id, {"status": "not_found"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
