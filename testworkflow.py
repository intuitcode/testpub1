import os
import subprocess
from pathlib import Path


def _resolve_candidate_path(filename: str, base_dir: Path) -> Path:
    """Resolve ``filename`` against ``base_dir`` while enforcing sandboxing.

    The helper expands ``~`` to the caller's home directory before performing
    the absolute/relative checks.  It then resolves the resulting path and
    verifies that it still resides inside ``base_dir`` by using
    :meth:`Path.relative_to`.

    Parameters
    ----------
    filename:
        The user supplied path fragment.
    base_dir:
        The directory that acts as the sandbox root.

    Returns
    -------
    pathlib.Path
        The resolved candidate path.

    Raises
    ------
    ValueError
        If the resolved path escapes ``base_dir``.

    Examples
    --------
    >>> from pathlib import Path
    >>> base = Path.cwd()
    >>> _ = (base / "data.txt").write_text("example")
    >>> _resolve_candidate_path("~/data.txt", base)  # doctest: +SKIP
    base / "data.txt"
    """
    resolved_base = Path(base_dir).resolve()
    user_path = Path(filename).expanduser()

    if user_path.is_absolute():
        candidate = user_path.resolve()
    else:
        candidate = (resolved_base / user_path).resolve()

    # Raises ValueError if the candidate escapes the working directory.
    candidate.relative_to(resolved_base)
    return candidate


def check_file_status() -> None:
    """Run a directory listing for a user supplied path within the sandbox."""
    base_dir = Path.cwd().resolve()
    filename = input("Enter a filename to check (e.g., 'data.txt'): ").strip()

    if not filename:
        print("No filename provided. Aborting.")
        return

    try:
        candidate = _resolve_candidate_path(filename, base_dir)
    except ValueError:
        print("Error: The requested path is outside the working directory.")
        return

    if os.name == "nt":
        command = ["cmd", "/c", "dir", str(candidate)]
    else:
        command = ["ls", "-l", str(candidate)]

    print(f"Executing command: {' '.join(command)}")
    subprocess.run(command, check=False)


if __name__ == "__main__":
    check_file_status()
