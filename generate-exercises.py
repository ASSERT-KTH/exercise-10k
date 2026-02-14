#!/usr/bin/env python3
"""
Advanced exercise generator with optimized batching.
Can generate even larger batches to minimize API calls further.
"""

import os
import json
import time
from pathlib import Path
import requests
from typing import List, Dict
import random


class AdvancedExerciseGenerator:
    def __init__(self, api_key, batch_size=100):
        self.api_key =  api_key
        self.base_url = "http://localhost:8000/v1/chat/completions"
        self.batch_size = batch_size
        self.output_dir = Path("specifications")
        self.output_dir.mkdir(exist_ok=True)
        self.checkpoint_file = self.output_dir / "checkpoint.json"
        self.stats = {
            "api_calls": 0,
            "exercises_generated": 0,
            "errors": 0,
            "last_checkpoint": 0
        }
        self.load_checkpoint()
        
    def load_checkpoint(self):
        """Load progress from checkpoint file."""
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file, 'r') as f:
                self.stats = json.load(f)
            print(f"Resuming from checkpoint: {self.stats['exercises_generated']} exercises completed")
    
    def save_checkpoint(self):
        """Save current progress."""
        with open(self.checkpoint_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def create_smart_prompt(self, start_num, end_num):
        """Create an optimized prompt for generating multiple diverse exercises."""
        count = end_num - start_num + 1
        
        # Define topic categories to ensure diversity
        topics = [
            "variables and data types",
            "arithmetic operations",
            "string manipulation",
            "conditional statements (if/else)",
            "loops (for/while)",
            "lists and arrays",
            "functions",
            "dictionaries",
            "basic algorithms",
            "input/output"
        ]
        difficulty = ["easy", "medium", "hard", "superhard", "god"] 
        prompt = f"""Generate {count} diverse programming exercises for intro to programming students.

IMPORTANT: Ensure variety across different topics and difficulty levels.

Exercise topics to cover: {random.choice(topics)}

Each exercise must include:
1. Unique ID (from {start_num} to {end_num})
2. Clear title
3. Detailed description
4. Difficulty level ({random.choice(difficulty)})
5. Relevant topics list
6. Sample input
7. Expected output

Return a JSON array with this exact structure:
[
  {{
    "id": {start_num},
    "title": "Exercise title",
    "description": "What the student needs to do",
    "difficulty": "easy",
    "topics": ["topic1", "topic2"],
    "sample_input": "example input",
    "sample_output": "example output"
  }},
  ...
]

Generate all {count} exercises. Return ONLY the JSON array."""
        
        return prompt
    
    def call_api_with_retry(self, prompt, max_retries=3):
        """Make API call with automatic retry logic."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/exercise-generator",
            "X-Title": "Programming Exercise Generator"
        }
        
        data = {
            "model": "RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 1.1,
            "max_tokens": 7500  # Ensure enough tokens for large batches
        }
        
        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.base_url, 
                    headers=headers, 
                    json=data,
                    timeout=120
                )
                response.raise_for_status()
                
                result = response.json()
                content = result["choices"][0]["message"]["content"]
                
                # Parse JSON from response
                content = content.strip()
                if "```json" in content:
                    content = content.split("```json")[1].split("```")[0].strip()
                elif "```" in content:
                    content = content.split("```")[1].split("```")[0].strip()
                
                exercises = json.loads(content)
                
                # Validate response
                if not isinstance(exercises, list):
                    raise ValueError("Response is not a list")
                
                return exercises
                
            except Exception as e:
                self.stats["errors"] += 1
                print(f"  Attempt {attempt + 1} failed: {e}")
                
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 5
                    #print(f"  Retrying in {wait_time} seconds...")
                    #time.sleep(wait_time)
                else:
                    raise
    
    def save_exercises_batch(self, exercises: List[Dict]):
        """Save multiple exercises efficiently."""
        for exercise in exercises:
            exercise_id = exercise.get("id", 0)
            filename = self.output_dir / f"exercise_{exercise_id:05d}.json"
            
            with open(filename, 'w') as f:
                json.dump(exercise, f, indent=2)
    
    def generate_all(self, total=10000):
        """Generate all exercises with optimized batching."""
        start_from = self.stats["exercises_generated"] + 1
        start_from = 0
        
        print(f"\n{'='*60}")
        print(f"Programming Exercise Generator")
        print(f"{'='*60}")
        print(f"Target: {total} exercises")
        print(f"Batch size: {self.batch_size}")
        print(f"Estimated API calls: {(total - start_from + 1) // self.batch_size + 1}")
        print(f"Starting from: exercise {start_from}")
        print(f"{'='*60}\n")
        
        for start in range(start_from, total + 1, self.batch_size):
            
            exercise_id = start
            filename = self.output_dir / f"exercise_{exercise_id:05d}.json"
            if os.path.exists(filename): continue
            end = min(start + self.batch_size - 1, total)
            batch_num = (start - 1) // self.batch_size + 1
            total_batches = (total - start_from + 1) // self.batch_size + 1
            
            print(f"Batch {batch_num}/{total_batches}: Exercises {start}-{end}")
            
            try:
                prompt = self.create_smart_prompt(start, end)
                exercises = self.call_api_with_retry(prompt)
                self.stats["api_calls"] += 1
                
                # Save all exercises in batch
                self.save_exercises_batch(exercises)
                
                exercises_in_batch = len(exercises)
                self.stats["exercises_generated"] += exercises_in_batch
                self.stats["last_checkpoint"] = end
                
                print(f"  ✓ Saved {exercises_in_batch} exercises")
                print(f"  Progress: {self.stats['exercises_generated']}/{total} ({100*self.stats['exercises_generated']/total:.1f}%)")
                print(f"  API calls so far: {self.stats['api_calls']}")
                
                # Save checkpoint after each successful batch
                self.save_checkpoint()
                
                # Rate limiting
                if end < total:
                    time.sleep(2)
                    
            except Exception as e:
                print(f"  ✗ Batch failed: {e}")
                print(f"  Checkpoint saved. You can resume later.")
                self.save_checkpoint()
        
        print(f"\n{'='*60}")
        print(f"✓ Generation Complete!")
        print(f"{'='*60}")
        print(f"Total exercises: {self.stats['exercises_generated']}")
        print(f"Total API calls: {self.stats['api_calls']}")
        print(f"Errors encountered: {self.stats['errors']}")
        print(f"Average exercises per call: {self.stats['exercises_generated']/self.stats['api_calls']:.1f}")
        print(f"Output directory: {self.output_dir.absolute()}")
        print(f"{'='*60}\n")


def main():
    print("\n🎓 Programming Exercise Generator")
    print("   Generates 10,000 unique exercises with minimal API calls\n")
    
    # # Get API key
    # api_key = os.getenv("OPENROUTER_API_KEY")
    
    # if not api_key:
    #     print("OpenRouter API key not found in OPENROUTER_API_KEY environment variable.")
    #     api_key = input("Enter your OpenRouter API key: ").strip()
    
    # if not api_key:
    #     print("❌ Error: API key required")
    #     return
    
    # Choose batch size
    print("\nBatch size options:")
    print("  50  - Safe, 200 API calls")
    print("  100 - Recommended, 100 API calls")
    print("  200 - Aggressive, 50 API calls")
    
    batch_input = input("\nEnter batch size (default: 100): ").strip()
    batch_size = int(batch_input) if batch_input else 100
    
    # Create generator
    generator = AdvancedExerciseGenerator(None, batch_size=batch_size)
    
    # Generate
    try:
        generator.generate_all(total=10000)
    except KeyboardInterrupt:
        print("\n\n⚠️  Generation interrupted by user")
        print("Progress has been saved. Run again to resume.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        print("Progress has been saved. Run again to resume.")


if __name__ == "__main__":
    main()
