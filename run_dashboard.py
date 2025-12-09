import subprocess
import webbrowser
import time
import os

# Pfad zur app.py
APP_PATH = os.path.join(os.path.dirname(__file__), "app.py")

# Streamlit starten
p = subprocess.Popen(["streamlit", "run", APP_PATH])

# kurz warten
time.sleep(2)

# Webseite im Browser öffnen
webbrowser.open("http://localhost:8501")

# Prozess laufen lassen
p.wait()
