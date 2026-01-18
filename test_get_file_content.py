from functions.get_file_content import get_file_content

def run_tests():
   # 1. Test reading a top-level file
    print('get_file_content("calculator", "main.py"):')
    print("--- Result: ---")
    print(get_file_content("calculator", "main.py"))
    print("-" * 40)

    # 2. Test reading a file in a subdirectory
    print('get_file_content("calculator", "pkg/calculator.py"):')
    print("--- Result: ---")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("-" * 40)

    # 3. Test security (Accessing system files)
    print('get_file_content("calculator", "/bin/cat"):')
    print("--- Result: ---")
    print(f"    {get_file_content('calculator', '/bin/cat')}")
    print("-" * 40)

    # 4. Test a file that doesn't exist
    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    print("--- Result: ---")
    print(f"    {get_file_content('calculator', 'pkg/does_not_exist.py')}")
    print("-" * 40)

if __name__ == "__main__":
    run_tests()