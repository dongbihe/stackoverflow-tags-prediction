import subprocess


def run_flask():
    subprocess.Popen(["gunicorn", "app:app"])


def run_streamlit():
    subprocess.Popen(
        [
            "python",
            "-m",
            "streamlit",
            "run",
            "streamlit_app.py",
            "--server.port",
            "8001",
            "--server.address",
            "0.0.0.0",
        ]
    )


if __name__ == "__main__":
    run_flask()
    run_streamlit()
