from app import app
from config import *


def main():
    app.run(host="0.0.0.0", port="5000", debug=True)


if __name__ == "__main__":
    main()