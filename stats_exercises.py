import os
import json
import statistics
import math
from collections import Counter

def get_percentile(data, percentile):
    if not data:
        return 0
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

def main():
    spec_dir = 'specifications'
    difficulty_counter = Counter()
    topics_counter = Counter()
    description_lengths = []

    if not os.path.exists(spec_dir):
        print(f"Directory {spec_dir} not found.")
        return

    files = [f for f in os.listdir(spec_dir) if f.startswith('exercise_') and f.endswith('.json')]
    
    for filename in files:
        file_path = os.path.join(spec_dir, filename)
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
                
                difficulty = data.get('difficulty')
                if difficulty:
                    difficulty_counter[difficulty] += 1
                
                topics = data.get('topics')
                if topics:
                    if isinstance(topics, list):
                        for topic in topics:
                            topics_counter[topic] += 1
                    else:
                        topics_counter[topics] += 1
                
                description = data.get('description', '')
                description_lengths.append(len(description))
            except json.JSONDecodeError:
                continue

    print("### Top 10 Difficulty Levels")
    for diff, count in difficulty_counter.most_common(10):
        print(f"* {diff}: {count}")

    print("\n### Top 10 Topics")
    for topic, count in topics_counter.most_common(10):
        print(f"* {topic}: {count}")

    if description_lengths:
        print("\n### Description Length Distribution (characters)")
        description_lengths.sort()
        median = statistics.median(description_lengths)
        min_len = min(description_lengths)
        max_len = max(description_lengths)
        p25 = get_percentile(description_lengths, 25)
        p75 = get_percentile(description_lengths, 75)
        p95 = get_percentile(description_lengths, 95)
        
        print(f"* Median: {median}")
        print(f"* Range: {min_len} - {max_len}")
        print(f"* 25th Percentile: {p25}")
        print(f"* 75th Percentile: {p75}")
        print(f"* 95th Percentile: {p95}")

if __name__ == "__main__":
    main()
