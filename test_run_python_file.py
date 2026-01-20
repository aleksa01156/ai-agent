from functions.run_python_file import run_python_file
import os

def run_tests():
    print("--- Running run_python_file Tests ---")
    
    # 1. Standard run (No args)
    # Expected: Calculator usage instructions from main.py
    res1 = run_python_file("calculator", "calculator/main.py")
    print(f"Test 1 (Usage): \n{res1}\n")

    # 2. Run with arguments
    # Expected: The result of 3 + 5 (formatted by the calculator)
    res2 = run_python_file("calculator", "calculator/main.py", ["3 + 5"])
    print(f"Test 2 (Calculation): \n{res2}\n")

    # 3. Running a different script
    # Expected: Test results from tests.py
    res3 = run_python_file("calculator", "calculator/tests.py")
    print(f"Test 3 (Internal Tests): \n{res3}\n")

    # 4. Security Check: Path Traversal
    # Expected: Error string regarding permitted working directory
    res4 = run_python_file("calculator", "../main.py")
    print(f"Test 4 (Security): {res4}\n")

    # 5. Existence Check
    # Expected: Error string saying file does not exist
    res5 = run_python_file("calculator", "nonexistent.py")
    print(f"Test 5 (Missing File): {res5}\n")

    # 6. Extension Check
    # Expected: Error string saying it's not a Python file
    res6 = run_python_file("calculator", "lorem.txt")
    print(f"Test 6 (Wrong Extension): {res6}\n")

if __name__ == "__main__":
    run_tests()