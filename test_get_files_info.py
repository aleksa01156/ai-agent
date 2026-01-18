from functions.get_files_info import get_files_info

def run_tests():
    # 1. Test the current directory within the 'calculator' folder
    print('get_files_info("calculator", "."):')
    print("Result for current directory:")
    print(get_files_info("calculator", "."))
    print("-" * 30)

    # 2. Test a subdirectory
    print('get_files_info("calculator", "pkg"):')
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print("-" * 30)

    # 3. Test an absolute path (security check)
    print('get_files_info("calculator", "/bin"):')
    print("Result for '/bin' directory:")
    print(f"    {get_files_info('calculator', '/bin')}")
    print("-" * 30)

    # 4. Test directory traversal (security check)
    print('get_files_info("calculator", "../"):')
    print("Result for '../' directory:")
    print(f"    {get_files_info('calculator', '../')}")

if __name__ == "__main__":
    run_tests()