from customersupport import app
import os

app.secret_key = "TESTING SECRET KEY"
if __name__ == "__main__":
    app.run(debug=True)
