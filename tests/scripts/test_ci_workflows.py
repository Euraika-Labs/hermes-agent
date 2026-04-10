from pathlib import Path


WORKFLOW_PATH = Path(__file__).resolve().parents[2] / ".github" / "workflows" / "tests.yml"


def test_tests_workflow_includes_windows_matrix_job():
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "windows-latest" in text
    assert "ubuntu-latest" in text
    assert "strategy:" in text
    assert "matrix:" in text


def test_tests_workflow_has_windows_shell_steps():
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "if: runner.os == 'Windows'" in text
    assert "if: runner.os != 'Windows'" in text
    assert "uv venv .venv --python 3.11" in text


def test_tests_workflow_runs_for_all_pull_requests():
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "pull_request:\n    branches: [main]" not in text
