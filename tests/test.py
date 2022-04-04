import os

solution = 'target/release/solution'
test_dir = 'tests'


def run_test_case(test_path: str) -> bool:
    test_out = test_path.replace('.in', '.out')
    expected_out = open(test_out).read()
    solution_out = os.popen(f"./{solution} < {test_path}").read()

    return expected_out == solution_out


def main():
    tests_total = 0
    tests_passed = 0

    for entry in os.scandir(test_dir):
        if entry.is_file() and entry.name.endswith('.in'):
            tests_total += 1
            if run_test_case(entry.path):
                print(f"{entry.name} passed!")
                tests_passed += 1
            else:
                print(f"{entry.name} failed!")

    if tests_total != tests_passed:
        exit(1)


if __name__ == '__main__':
    main()
