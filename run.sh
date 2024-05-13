gunicorn -b 127.0.0.1:5000 app:app &

python -m streamlit run streamlit_app.py --server.port 8000 --server.address 0.0.0.0
