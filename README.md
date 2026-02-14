# Exercise-10k: A Dataset of Programming Exercises in Python

This repository contains a collection of 10,000 AI-generated programming exercises and their corresponding AI-generated solutions. Exercises are meant to be for an introduction to programming course.

```bibtex
@misc{exercise-10k,
  author = {Martin Monperrus},
  title = {Exercise-10k: A Dataset of Programming Exercises in Python},
  year = {2026},
  url = {https://github.com/ASSERT-KTH/exercise-10k}
}
```

## Repository Structure

- `specifications/`: Contains 10,000 JSON files (1-10000). Each file includes:
  - `id`: Unique identifier.
  - `title`: Short name of the exercise.
  - `description`: The actual problem statement.
  - `difficulty`: easy/medium/hard.
  - `topics`: List of tags (e.g., "strings", "input/output").
  - `sample_input/output`: Example test cases.
- `answers/`: Contains the model-generated solutions in JSON format.
  - Each file contains the `answer` (Markdown text with code blocks) and the `model` name.
- `exercises/`: (Generated) The final processed exercises in Markdown format.
- `generate-exercises.py`: Script used for generating the initial exercise prompts.
- `solve_exercises.py`: Script used for managing the model inference process.
- `process_answers.py`: Script to process the solution and generate markdown

## Statistics

### Exercise stats

Task Length (characters):
* Median: 92.0
* Range: 22 - 721
* 25th Percentile: 73
* 75th Percentile: 129
* 95th Percentile: 252

Difficulty Levels:
* medium: 3117
* easy: 3078
* hard: 2616
* superhard: 1030
* god: 159

Top 10 Topics:
* conditional statements: 1728
* functions: 1512
* arithmetic operations: 1412
* loops: 1258
* input/output: 1125
* string manipulation: 1025
* dictionaries: 935
* if/else: 927
* variables: 853
* strings: 824

### Program stats

AI output with no code blocks: 87 cases

AI output with multiple code blocks: 1097 cases. In this case, we only execute the first one.

Program Length Distribution (characters):
- Median: 735.0
- Range: 0 - 5121
- 25th Percentile: 498
- 75th Percentile: 1102
- 95th Percentile: 1962

Syntactically Valid Python (AST): 9,533 (95.32%)

**Execution:**

Number of successfully executed cases: 7168 (71.70%)


## Related work

This dataset is the largest ever dataset of programming problems. It is unknown whether the tasks are of similar difficulty compared to those related datasets, this is left to future work.

## [IBM Project CodeNet](https://github.com/IBM/Project_CodeNet)
Dataset containing 4,053 coding problems. Available on GitHub and the IBM Data Asset Exchange. It includes code in 55+ programming languages, problem descriptions, rich metadata including CPU time, memory usage, and acceptance status, sample inputs and outputs

## [Description2Code](https://github.com/ethancaballero/description2code)
Contains approximately 7,764 programming challenges from CodeChef, Codeforces, and Hackerearth. Each challenge includes problem descriptions, multiple solutions, and test cases.

## [Mostly Basic Programming Problems (MBPP)](https://github.com/google-research/google-research/tree/master/mbpp)
Contains around 1,000 crowd-sourced Python programming problems designed for entry-level programmers. Each problem includes a task description, code solution, and automated test cases.

## [CodeWorkout Dataset](https://sites.google.com/ncsu.edu/csedm-dc-2021/dataset)
Contains 50 Java problems with 65,000+ code submissions from CS1 students. Includes submission scores and compiler messages.



