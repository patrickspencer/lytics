from lytics import settings
from lytics.application import create_app

if __name__ == "__main__":
    app = create_app('settings.DevelopmentConfig')
    app.run(debug=True)

