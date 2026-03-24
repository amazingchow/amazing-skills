"""CLI entrypoint for {{ project_name }}."""

from __future__ import annotations

from colorama import Fore, Style


def main() -> None:
    """Run the sample CLI."""
    print(
        f"{Fore.GREEN}{{ project_name }}{Style.RESET_ALL}: "
        "{{ project_description }}"
    )


if __name__ == "__main__":
    main()
