from flask import Flask, render_template
from WebScraper import scraper

app = Flask(__name__)

@app.route('/')
def index():
    laptops = scraper.get_laptop_data()

    # Define the js variable with your JavaScript code
    js = """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var buttons = document.querySelectorAll('.buy-button');
            buttons.forEach(function(button) {
                button.addEventListener('click', function() {
                    alert('You clicked the Buy button!');
                });
            });
        });
    </script>
    """
    
    return render_template('index.html', laptops=laptops, js=js)

if __name__ == '__main__':
    app.run(debug=True)
