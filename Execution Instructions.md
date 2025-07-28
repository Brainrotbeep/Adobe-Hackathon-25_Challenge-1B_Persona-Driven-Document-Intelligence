# Execution Instructions - Challenge 1B Submission

## Prerequisites:
- Docker installed on the system (Docker Desktop or CLI)
- Internet access (for initial model downloads)
- Folder structure as below:

challenge_1b_solution/
├── Dockerfile
├── extractor.py
├── test_runner.py
├── requirements.txt
├── approach_explanation.md
├── Collection_1/
│ ├── PDFs/
│ └── challenge1b_input.json
├── Collection_2/
│ ├── PDFs/
│ └── challenge1b_input.json
├── Collection_3/
│ ├── PDFs/
│ └── challenge1b_input.json


## Build Docker Image:
```bash
docker build -t challenge1b .
Run for a Specific Collection:
Replace Collection_2 with desired collection (Collection_1, Collection_3, etc.)

docker run --rm -v "${PWD}\Collection_3:/app/Collection_3" challenge1b python test_runner.py --input_folder Collection_3

The output JSON will be generated inside the respective Collection folder as challenge1b_output.json.

Notes:
The model is pre-downloaded during first run.

Ensure PDFs and challenge1b_input.json filenames are consistent as per input.

This solution works for all collections (generalized).


## ✅ Final Folder Structure for Submission:
challenge_1b_solution/
├── Dockerfile
├── requirements.txt
├── extractor.py
├── test_runner.py
├── approach_explanation.md
├── execution_instructions.md
├── Collection_1/...
├── Collection_2/...
├── Collection_3/...


