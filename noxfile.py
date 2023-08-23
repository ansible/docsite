import nox

@nox.session
def build(session: nox.Session):
    session.install(
      "-r", "requirements.in",
      "-c", "requirements.txt",
    )
    session.run("python", "-I", "build.py", *session.posargs)
