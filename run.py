from threading import Thread
from app import create_app
from app.admintools.console import start
from config import Config

app = create_app()

server_thread = None

def run_app():
    app.run(debug=False)

if __name__ == '__main__':
    if Config.ENABLE_CONSOLE == True:
        server_thread = Thread(target=run_app)
        server_thread.start()

        console_thread = Thread(target=start)
        console_thread.start()

        server_thread.join()
        console_thread.join()
    else:
        run_app()