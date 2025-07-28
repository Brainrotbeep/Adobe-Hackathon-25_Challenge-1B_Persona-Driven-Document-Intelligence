import argparse
from extractor import extract

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run the Challenge 1B Extractor")
    parser.add_argument('--input_folder', type=str, required=True, help='Path to Collection folder (must include PDFs/ and challenge1b_input.json)')
    args = parser.parse_args()

    extract(args.input_folder)
