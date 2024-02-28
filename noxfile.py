from pathlib import Path

import nox

requirements_files = list(
    {path.name.replace(".in", "") for path in Path(".").glob("*in")}
)


@nox.session(name="pip-compile", python=["3.11"])
@nox.parametrize(["req"], requirements_files, requirements_files)
def pip_compile(session: nox.Session, req: str):
    # .pip-tools.toml was introduced in v7
    session.install("pip-tools >= 7")

    # Use --upgrade by default unless a user passes -P.
    upgrade_related_cli_flags = "-P", "--upgrade-package", "--no-upgrade"
    has_upgrade_related_cli_flags = any(
        arg.startswith(upgrade_related_cli_flags) for arg in session.posargs
    )
    injected_extra_cli_args = () if has_upgrade_related_cli_flags else ("--upgrade",)

    session.run(
        "pip-compile",
        "--output-file",
        f"{req}.txt",
        *session.posargs,
        *injected_extra_cli_args,
        f"{req}.in",
    )


@nox.session(
    python=["3.11"]
)  # The python version should match the readthedocs configuration.
def build(session: nox.Session):
    # fmt: off
    session.install(
      "-r", "requirements.in",
      "-c", "requirements.txt",
    )
    # fmt: on
    session.run("python", "-I", "build.py", *session.posargs)
