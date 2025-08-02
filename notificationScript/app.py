from flask import Flask, render_template_string
import notificationScript  # Import your notifier script

app = Flask(__name__)

@app.route("/")
def home():
 return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Amazon Price Notifier</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container py-5">
            <div class="card shadow-sm mx-auto" style="max-width: 500px;">
                <div class="card-body text-center">
                    <h1 class="card-title mb-4">Amazon Price Notifier</h1>
                    <p class="card-text">Click the button below to check the product price:</p>
                    <form action="/run">
                        <button type="submit" class="btn btn-primary btn-lg">Run Price Check</button>
                    </form>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

@app.route("/run")
def run_script():
    result = notificationScript.main()  # Call the main() function
    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Price Check Result</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <div class="container py-5">
            <div class="card shadow-sm mx-auto" style="max-width: 500px;">
                <div class="card-body text-center">
                    <h1 class="card-title mb-4">Price Check Result</h1>
                    <p class="card-text fs-4">{result}</p>
                    <a href="/" class="btn btn-secondary mt-3">Back</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Run Flask app on port 8000
