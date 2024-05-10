import subprocess


def run_flask():
    subprocess.Popen(["gunicorn", "app:app"])


def run_streamlit():
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])


if __name__ == "__main__":
    run_flask()
    run_streamlit()
