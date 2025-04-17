import os
import sys

def create_problem_folder(problem_name):
    folder_path = os.path.join(os.getcwd(), problem_name)
    
    try:
        os.makedirs(folder_path, exist_ok=False)
    except FileExistsError:
        print(f"⚠️  Folder '{problem_name}' already exists.")
        return

    # Create main.py
    with open(os.path.join(folder_path, "main.py"), "w") as f:
        f.write(f'''"""
Problem: {problem_name.replace("-", " ").title()}
"""

def solve():
    pass

if __name__ == "__main__":
    solve()
''')

    # Create README.md
    with open(os.path.join(folder_path, "README.md"), "w") as f:
        f.write(f"# {problem_name.replace('-', ' ').title()}\n\n> Describe the challenge here.\n")

    print(f"✅ Created new problem folder: {problem_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_problem.py <problem-name>")
    else:
        create_problem_folder(sys.argv[1])
