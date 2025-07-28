
## Approach Explanation

### Problem Statement
The task is to build a document intelligence system that extracts and ranks the most relevant sections from a set of input documents based on a given persona and a job-to-be-done.

### Generalized Strategy
Our solution generalizes across any document collection, persona, and task by using semantic similarity and lightweight NLP tools that can run efficiently on CPU within the given resource constraints.

### Core Pipeline
1. **PDF Parsing**: Extract page-level text chunks using PyMuPDF, with noise filtering.
2. **Query Embedding**: Persona and task are combined into a query and embedded using all-MiniLM-L6-v2 model.
3. **Chunk Embedding & Scoring**: PDF chunks are embedded and cosine similarity is computed with the query.
4. **Ranking and Selection**: Top scoring sections and refined sub-sections are ranked for output.
5. **Output Generation**: Final JSON output with proper structure is generated as challenge1b_output.json

### Resource Compliance
- ✅ CPU-only
- ✅ Model size < 1GB
- ✅ Processing time within 60 seconds

This ensures high relevance extraction and hackathon constraints are met.
