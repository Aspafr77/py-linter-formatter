def format_linter_error(error: dict) -> dict:
    return {"line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"),
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(char) for char in errors],
            "file_path": file_path,
            "status": "passed" if errors is None else "failed"}


def format_linter_report(report_file: dict) -> list:
    return [format_single_linter_file(key, value) for key,
            value in report_file.items()]
