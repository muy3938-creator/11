import os
import argparse
from deepeye.core import DeepEyeSQL
from dotenv import load_dotenv

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="DeepEye-SQL MVP")
    parser.add_argument("--db", type=str, default="school.db", help="Path to SQLite database")
    parser.add_argument("--question", default="List all courses in Computer Science.",type=str,help="Natural language question")
    parser.add_argument("--api_key", type=str, required=False, help="OpenAI API Key")
    parser.add_argument("--base_url", type=str, required=False, help="OpenAI Baseurl")
    parser.add_argument("--model", type=str, required=False, help="Model")
    args = parser.parse_args()
    
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    base_url = args.base_url or os.environ.get("OPENAI_API_BASE")
    model = args.model or os.environ.get("MODEL")
    if not api_key:
        print("Error: OpenAI API Key is required. Pass it via --api_key or set OPENAI_API_KEY env var.")
        return

    if not os.path.exists(args.db):
        print(f"Error: Database file {args.db} not found. Run create_dummy_db.py first.")
        return

    pipeline = DeepEyeSQL(db_path=args.db, openai_api_key=api_key,openai_base_url=base_url,model=model)
    
    try:
        result = pipeline.run(args.question)
        print("\n" + "="*50)
        print(f"FINAL SQL: {result}")
        print("="*50)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
