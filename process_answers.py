import os
import json
import re
import ast
import statistics
import math
import subprocess
import sys
import tempfile

def extract_code_blocks(text):
    # Regex to find content between ``` and ```
    # Captures the language identifier if present
    pattern = re.compile(r'```(\w+)?\n(.*?)\n```', re.DOTALL)
    blocks = pattern.findall(text)
    if blocks:
        return blocks
    
    # Fallback: if no language specified or slightly different format
    pattern_fallback = re.compile(r'```(.*?)```', re.DOTALL)
    blocks = pattern_fallback.findall(text)
    # Convert to same format (None, code)
    return [(None, b) for b in blocks]

def get_percentile(data, percentile):
    if not data:
        return 0
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

def execute_code(code, input_data=None):
    with tempfile.NamedTemporaryFile(suffix='.py', mode='w', delete=False) as tf:
        tf.write(code)
        temp_name = tf.name
    
    try:
        # Use an empty string if input_data is None to prevent waiting for stdin
        actual_input = input_data if input_data is not None else ""
        result = subprocess.run(
            [sys.executable, temp_name],
            input=actual_input,
            capture_output=True,
            text=True,
            timeout=5,
            cwd='/tmp'
        )
        output = result.stdout
        if result.stderr:
            output += "\n" + result.stderr
        
        # Success if return code is 0
        success = (result.returncode == 0)
        return output, success
    except subprocess.TimeoutExpired:
        return "Execution timed out after 5 seconds.", False
    except Exception as e:
        return f"Execution failed: {str(e)}", False
    finally:
        if os.path.exists(temp_name):
            os.remove(temp_name)

def main():
    exercises_dir = 'specifications'
    answers_dir = 'answers'
    output_dir = 'exercises'
    python_version = sys.version.split()[0]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    exercise_files = [f for f in os.listdir(exercises_dir) if f.startswith('exercise_') and f.endswith('.json')]
    exercise_files.sort()

    total_files = len(exercise_files)
    total_cases = 0
    no_blocks = 0
    many_blocks = 0
    ast_success_cases = 0
    execution_success_cases = 0
    program_lengths = []

    for idx, filename in enumerate(exercise_files):
        print(f"\rProcessing {idx+1}/{total_files}...", end="", flush=True)
        exercise_path = os.path.join(exercises_dir, filename)
        
        with open(exercise_path, 'r') as f:
            try:
                exercise_data = json.load(f)
            except json.JSONDecodeError:
                continue

        exercise_id = exercise_data.get('id')
        description = exercise_data.get('description', '')
        sample_input = exercise_data.get('sample_input')

        # Try to find the answer file
        answer_filename = f"{exercise_id}.json"
        if exercise_id == 0:
            answer_filename = "00000.json"
        
        answer_path = os.path.join(answers_dir, answer_filename)
        
        if not os.path.exists(answer_path):
            padded_answer_filename = f"{str(exercise_id).zfill(5)}.json"
            answer_path = os.path.join(answers_dir, padded_answer_filename)

        if not os.path.exists(answer_path):
            continue

        total_cases += 1

        with open(answer_path, 'r') as f:
            try:
                answer_data = json.load(f)
            except json.JSONDecodeError:
                continue

        answer_text = answer_data.get('answer', '')
        model_name = answer_data.get('model', 'Unknown Model')
        code_blocks = extract_code_blocks(answer_text)

        md_filename = f"exercise_{str(exercise_id).zfill(5)}.md"
        md_path = os.path.join(output_dir, md_filename)

        blocks_to_write = []
        if code_blocks:
            has_lang_tag = any(lang for lang, code in code_blocks if lang)
            for lang, block in code_blocks:
                if has_lang_tag and not lang:
                    continue
                blocks_to_write.append(block.strip())

        if len(blocks_to_write) == 0: no_blocks += 1
        if len(blocks_to_write) > 1: many_blocks += 1

        # Check if it parses with AST and execute
        is_valid_python = False
        execution_successful = False
        current_exercise_length = 0
        generated_outputs = []
        for block in blocks_to_write:
            current_exercise_length += len(block)
            success = False

            try:
                ast.parse(block)
                output, success = execute_code(block, sample_input)
                generated_outputs.append(output)
                if success:
                    execution_successful = True
                    break
                is_valid_python = True
            except SyntaxError:
                continue
        
        if is_valid_python:
            ast_success_cases += 1
        
        if execution_successful:
            execution_success_cases += 1
        
        program_lengths.append(current_exercise_length)

        with open(md_path, 'w') as f:
            f.write("## Exercise\n")
            f.write(f"{description}\n\n")
            f.write("## Reference Solution\n")
            for block in blocks_to_write:
                f.write("```python\n")
                f.write(block)
                f.write("\n```\n\n")
            
            if generated_outputs:
                f.write("## Generated Output\n")
                for output in generated_outputs:
                    f.write("```\n")
                    f.write(output.strip())
                    f.write("\n```\n\n")
                f.write(f"generated by python {python_version}\n\n")

            f.write(f"solution generated by {model_name}\n")

    print("\nDone.")
    print(f"Processed exercises into {output_dir}")
    if total_cases > 0:
        print(f"\nResults Statistics:")
        print(f"Total number of cases: {total_cases}")
        print(f"No blocks: {no_blocks}")
        print(f"many blocks: {many_blocks}")
        
        ast_proportion = ast_success_cases / total_cases
        print(f"Number of syntactically valid (AST) cases: {ast_success_cases} ({ast_proportion:.2%})")
        
        exec_proportion = execution_success_cases / total_cases
        print(f"Number of successfully executed cases: {execution_success_cases} ({exec_proportion:.2%})")
        
        if program_lengths:
            program_lengths.sort()
            median = statistics.median(program_lengths)
            min_len = min(program_lengths)
            max_len = max(program_lengths)
            p25 = get_percentile(program_lengths, 25)
            p75 = get_percentile(program_lengths, 75)
            p95 = get_percentile(program_lengths, 95)
            
            print(f"\nProgram Length Distribution (characters):")
            print(f"Median: {median}")
            print(f"Range: {min_len} - {max_len}")
            print(f"25th Percentile: {p25}")
            print(f"75th Percentile: {p75}")
            print(f"95th Percentile: {p95}")
    else:
        print("No cases found to process.")

if __name__ == "__main__":
    main()
