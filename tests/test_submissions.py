import importlib.util
from pathlib import Path


SUBMISSIONS_DIR = (
    Path(__file__).resolve().parents[1] / "src" / "git_practice" / "submissions"
)


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def submission_files() -> list[Path]:
    return [path for path in SUBMISSIONS_DIR.glob("*.py") if path.name != "__init__.py"]


def test_submissions_exist():
    assert submission_files(), (
        "Add a Python file under src/git_practice/submissions/<your_name>.py"
    )


def test_each_submission_prints_correct_name(capsys):
    for path in submission_files():
        module = load_module(path)
        expected_name = path.stem
        input_str = "hello"
        expected_message = f"{expected_name}: {input_str}"

        assert hasattr(module, "NAME"), f"{path.name} must define NAME"
        assert module.NAME == expected_name

        assert hasattr(module, "print_message"), (
            f"{path.name} must define print_message(input_str: str)"
        )

        result = module.print_message(input_str)
        captured = capsys.readouterr()

        assert captured.out.strip() == expected_message
        assert result == expected_message
