import requests
import os
import re
from typing import List, Optional
from .search_service import SearchResult

def sanitize_filename(filename: str) -> str:
    return re.sub(r'(?u)[^-\w.]', '_', filename)

def download_pdf(url: str, output_path: str) -> bool:
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return False

def iterative_download(results: List[SearchResult], project_dir: str, target_count: int) -> List[str]:
    pdf_dir = os.path.join(project_dir, "pdfs")
    os.makedirs(pdf_dir, exist_ok=True)
    
    downloaded_paths = []
    
    for res in results:
        if len(downloaded_paths) >= target_count:
            break
            
        if not res.pdf_url:
            continue
            
        filename = sanitize_filename(res.title[:50]) + ".pdf"
        output_path = os.path.join(pdf_dir, filename)
        
        print(f"Downloading: {res.title}...")
        if download_pdf(res.pdf_url, output_path):
            downloaded_paths.append(output_path)
            
    return downloaded_paths
