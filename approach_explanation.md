# Approach Explanation - Challenge 1B: Persona-Driven Document Intelligence

## Problem Statement
The objective is to develop an intelligent document analysis system that extracts and prioritizes the most relevant sections from a collection of documents based on a specified persona and their job-to-be-done. The solution must generalize across various domains and persona-task combinations while adhering to strict computational constraints: CPU-only execution, model size under 1GB, and a total processing time of less than 60 seconds.

## Overall Approach
We designed a modular pipeline that leverages semantic similarity techniques using lightweight transformer-based embeddings. The solution dynamically identifies and ranks document sections based on their relevance to the persona’s task, ensuring scalability and domain independence. The architecture emphasizes CPU efficiency, minimal memory footprint, and rapid processing, aligning with all hackathon constraints.

## Solution Pipeline

### 1. Document Parsing and Preprocessing
Each input PDF document is parsed using **PyMuPDF (fitz)** to extract page-level text blocks. To enhance precision, the parsing phase applies noise filtering that excludes irrelevant text fragments such as headers, footers, page numbers, and short insignificant chunks. This structured extraction ensures that only meaningful content proceeds to the semantic evaluation stage.

### 2. Query Formulation
The persona's role description and job-to-be-done task are concatenated into a single descriptive query sentence. This consolidated query is crafted to capture the core intent of the persona’s needs. For instance, for a travel planner persona with the task “Plan a 4-day trip for college friends,” the formulated query becomes: “Travel Planner planning a 4-day trip for college friends.” This query serves as the anchor for semantic similarity assessments.

### 3. Embedding Generation
Both the query and the extracted document chunks are embedded into a semantic vector space using the **all-MiniLM-L6-v2** Sentence Transformer model. The model is chosen specifically for its computational efficiency (model size ~22MB) and its ability to generate high-quality sentence embeddings suitable for similarity tasks, making it ideal for CPU-only environments.

### 4. Semantic Similarity Scoring
Cosine similarity is computed between the query embedding and each document chunk embedding to measure relevance. These similarity scores are used to rank document sections according to their semantic closeness to the persona’s intent. This approach ensures dynamic adaptability to different personas and tasks without domain-specific heuristics.

### 5. Ranking and Section Selection
The top five document chunks with the highest relevance scores are selected for output. These chunks are categorized under two sections in the final output:
- **Extracted Sections**: High-level metadata including document name, section title (derived from chunk text), page number, and importance rank.
- **Subsection Analysis**: Detailed refined text excerpts providing granular insights from the most relevant portions.

### 6. Output JSON Generation
A structured JSON output file (`challenge1b_output.json`) is generated in full compliance with the provided schema. The output includes metadata, extracted sections, and detailed sub-sections, encapsulated in a precise and easily evaluable format.

## Resource Compliance and Generalizability
The solution is designed to operate entirely on CPU, with a total model and code footprint well within the 1GB limit. The semantic similarity methodology enables the system to generalize seamlessly across different document domains, personas, and tasks, without hardcoded rules or custom configurations.

## Conclusion
This approach ensures a scalable, robust, and resource-efficient solution for persona-driven document intelligence. By leveraging semantic embeddings and a lightweight architecture, the system consistently delivers high-quality, prioritized document insights aligned with user personas in a hackathon environment.

