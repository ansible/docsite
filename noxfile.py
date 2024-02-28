import nox

@nox.session(python=["3.11"]) # The python version should match the readthedocs configuration.
def build(session: nox.Session):
    session.install(
      "-r", "requirements.in",
      "-c", "requirements.txt",
    )
    session.run("python", "-I", "build.py", *session.posargs)
