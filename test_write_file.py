from functions.write_files import write_file
import os

def run_tests():
    # Setup: Ensure the 'calculator' directory exists for testing
    if not os.path.exists("calculator"):
        os.makedirs("calculator")

    print("--- Running write_file Tests ---")

    # Test Case 1: Simple write in the working directory
    # Expected: Success
    res1 = write_file("calculator", "calculator/lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Test 1 (Standard Write): {res1}")

    # Test Case 2: Writing to a nested subdirectory that doesn't exist yet
    # Expected: Success (should create 'pkg' folder automatically)
    res2 = write_file("calculator", "calculator/pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Test 2 (Nested Write): {res2}")

    # Test Case 3: Attempting to write outside the working directory
    # Expected: Error (Security Block)
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Test 3 (Out of Bounds): {res3}")

if __name__ == "__main__":
    run_tests()
