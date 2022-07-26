# importation of the solution function to test
from file_owners.file import solution


def test_solution_valid_inputs():
    """This is the test for the implemented solution"""
    valid_inputs = [
        {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"},
        {
            "file.txt": "Dave",
            "info.py": "Alan",
            "log.txt": "Goku",
            "books.txt": "Kkbcg",
            "file_vf.txt": "Dave",
            "info_vf.py": "Alan",
            "log_vf.txt": "Goku",
            "books_vf.txt": "Kkbcg",
        },
    ]
    expected_outputs = [
        {"Randy": ["Input.txt", "Output.txt"], "Stan": ["Code.py"]},
        {
            "Dave": ["file.txt", "file_vf.txt"],
            "Alan": ["info.py", "info_vf.py"],
            "Goku": ["log.txt", "log_vf.txt"],
            "Kkbcg": ["books.txt", "books_vf.txt"],
        },
    ]
    outputs = []

    for input in valid_inputs:
        outputs.append(solution(input))

    assert outputs == expected_outputs
