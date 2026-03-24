from __future__ import annotations

from {{ package_name }} import __version__
from {{ package_name }} .__main__ import main


def test_version() -> None:
    assert __version__ == "0.1.0"


def test_cli_output(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert "{{ project_name }}" in captured.out
