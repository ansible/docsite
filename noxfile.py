import os
from pathlib import Path

import nox

requirements_directory = Path("requirements").resolve()

requirements_files = [
    requirements_input_file_path.stem
    for requirements_input_file_path in requirements_directory.glob("*.in")
]


@nox.session(name="pip-compile", python=["3.11"])
@nox.parametrize(["req"], arg_values_list=requirements_files, ids=requirements_files)
def pip_compile(session: nox.Session, req: str):
    """Generate lock files from input files or upgrade packages in lock files."""
    # fmt: off
    session.install(
      "-r", str(requirements_directory / "pip-tools.in"),
      "-c", str(requirements_directory / "pip-tools.txt"),
    )
    # fmt: on

    # Use --upgrade by default unless a user passes -P.
    upgrade_related_cli_flags = ("-P", "--upgrade-package", "--no-upgrade")
    has_upgrade_related_cli_flags = any(
        arg.startswith(upgrade_related_cli_flags) for arg in session.posargs
    )
    injected_extra_cli_args = () if has_upgrade_related_cli_flags else ("--upgrade",)

    session.run(
        "pip-compile",
        "--output-file",
        os.path.join(requirements_directory_str, f"{req}.txt"),
        *session.posargs,
        *injected_extra_cli_args,
        os.path.join(requirements_directory_str, f"{req}.in"),
    )


@nox.session(python=["3.11"])  # The python version should match the readthedocs configuration.
def build(session: nox.Session):
    """Generate HTML files for the Ansible docsite."""
    requirements_directory_str = str(requirements_directory)
    # fmt: off
    session.install(
      "-r", os.path.join(requirements_directory_str, "requirements.in"),
      "-c", os.path.join(requirements_directory_str, "requirements.txt"),
    )
    # fmt: on
    session.run("python", "-I", "build.py", *session.posargs)
