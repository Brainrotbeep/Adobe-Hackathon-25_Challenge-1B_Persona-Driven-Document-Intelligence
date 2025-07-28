# extractor.py
import os
import json
import fitz  # PyMuPDF
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")  # small, CPU-friendly

def extract_chunks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if len(text.split()) >= 20:
                chunks.append({
                    "text": text,
                    "page": page_num + 1
                })
    return chunks

def build_query(persona, task):
    return f"As a {persona}, {task}"

def extract(input_path):
    with open(os.path.join(input_path, "challenge1b_input.json")) as f:
        config = json.load(f)

    persona = config["persona"]["role"]
    task = config["job_to_be_done"]["task"]
    input_docs = config["documents"]
    query = build_query(persona, task)

    all_chunks = []
    for doc_meta in input_docs:
        pdf_name = doc_meta["filename"]
        title = doc_meta["title"]
        chunks = extract_chunks_from_pdf(os.path.join(input_path, "PDFs", pdf_name))
        for chunk in chunks:
            chunk.update({"document": pdf_name, "title": title})
        all_chunks.extend(chunks)

    query_embedding = model.encode(query, convert_to_tensor=True)
    chunk_texts = [c["text"] for c in all_chunks]
    chunk_embeddings = model.encode(chunk_texts, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, chunk_embeddings)[0]
    top_k = min(5, len(all_chunks))
    top_indices = scores.argsort(descending=True)[:top_k]

    extracted_sections = []
    subsection_analysis = []
    for rank, idx in enumerate(top_indices):
        chunk = all_chunks[idx]
        extracted_sections.append({
            "document": chunk["document"],
            "section_title": chunk["title"],
            "importance_rank": rank + 1,
            "page_number": chunk["page"]
        })
        subsection_analysis.append({
            "document": chunk["document"],
            "refined_text": chunk["text"],
            "page_number": chunk["page"]
        })

    output = {
        "metadata": {
            "input_documents": [d["filename"] for d in input_docs],
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(os.path.join(input_path, "challenge1b_output.json"), "w") as f:
        json.dump(output, f, indent=4)

    print(f"✅ Output written to {os.path.join(input_path, 'challenge1b_output.json')}")
