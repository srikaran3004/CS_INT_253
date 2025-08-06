from django.shortcuts import render
from django.http import HttpResponse
import requests  

def hello(request):
    return HttpResponse("Hello world");

def home1(request):
    return HttpResponse("<h1 style='color:red'> Welcome to home page!!</h1>");

def dish(request):
    dishes = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos"]
    dish_list = "<ul>"
    for dish in dishes:
        dish_list += f"<li>{dish}</li>"
    dish_list += "</ul>"
    
    return HttpResponse(f"<h1>Our Dishes</h1>{dish_list}")

def itemDetails(request):
    items={
        "Pizza":{
            "price":250,
            "description": "Delicious cheezy pizza with toppings",
            "calories":300
        },
        "Burger":{
            "price":150,
            "description": "Juicy Veg Classic Burger",
            "calories":200
        },
    }
    res = "<h1>Item Details</h1><ul>"
    for item, details in items.items():
        res += f"<li><strong>{item}</strong>: ${details['price']}<br>"
        res += f"Description: {details['description']}<br>"
        res += f"Calories: {details['calories']}</li><br>"
    res += "</ul>"
    
    return HttpResponse(res)

def menuDisplay(request,item):
    items={
        "pizza":{
            "price":250,
            "description": "Delicious cheezy pizza with toppings",
            "calories":300
        },
        "burger":{
            "price":150,
            "description": "Juicy Veg Classic Burger",
            "calories":200
        },
        "pasta":{
            "price":220,
            "description":"Creamy alfardo pasta",
            "calories": 150
        }
    }
    item=item.lower()
    if item in items:
        details=items[item]
        return HttpResponse(f"""
            <h1>{item.capitalize()} Details</h1>
            <ul>
                <li><strong>Price:</strong> ${details['price']}</li>
                <li><strong>Description:</strong> {details['description']}</li>
                <li><strong>Calories:</strong> {details['calories']}</li>
            </ul>
        """)
    else:
        return HttpResponse("<h1>404 Bad Request</h1><br><h2>Item not found</h2>")
    

def menu(request, item_name):
    item_name = item_name.lower()

    if item_name == "pizza":
        price = 250
        description = "Delicious cheezy pizza with toppings"
        calories = 300
    elif item_name == "burger":
        price = 150
        description = "Juicy Veg Classic Burger"
        calories = 200
    elif item_name == "pasta":
        price = 220
        description = "Creamy alfredo pasta"
        calories = 150
    else:
        return HttpResponse("<h1>404 Bad Request</h1><br><h2>Item not found</h2>")

    return HttpResponse(f"""
        <h1>{item_name.capitalize()} Details</h1>
        <ul>
            <li><strong>Price:</strong> ${price}</li>
            <li><strong>Description:</strong> {description}</li>
            <li><strong>Calories:</strong> {calories}</li>
        </ul>
    """)

def fetch_data(request, id):
    try:
        api_url = f"https://jsonplaceholder.typicode.com/posts/{id}"
        # Fetch data from API
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            # Simple HTML display
            html = f"""
            <h1>Data for ID: {id}</h1>
            <p><strong>Title:</strong> {data.get('title', 'N/A')}</p>
            <p><strong>Body:</strong> {data.get('body', 'N/A')}</p>
            <p><strong>User ID:</strong> {data.get('userId', 'N/A')}</p>
            <p><strong>ID:</strong> {data.get('id', 'N/A')}</p>
            """
            return HttpResponse(html)
        else:
            return HttpResponse(f"<h1>Error: Item {id} not found</h1>")
    except:
        return HttpResponse("<h1>Error: Unable to fetch data</h1>")

def api_form(request):
    return HttpResponse("""
    <h1>Enter ID to Fetch Data</h1>
    <form>
        <input type="number" id="item_id" placeholder="Enter ID" required>
        <button type="button" onclick="window.location.href='/fetch/' + document.getElementById('item_id').value + '/'">Fetch Data</button>
    </form>
    """)

def add_form(request):
    """Display form for addition"""
    return HttpResponse("""
    <h1>Addition Calculator</h1>
    <form>
        <label>Value 1:</label>
        <input type="number" id="value1" placeholder="Enter first number" required><br><br>
        
        <label>Value 2:</label>
        <input type="number" id="value2" placeholder="Enter second number" required><br><br>
        
        <button type="button" onclick="calculate()">Add Numbers</button>
    </form>
    
    <script>
        function calculate() {
            var val1 = document.getElementById('value1').value;
            var val2 = document.getElementById('value2').value;
            window.location.href = '/add/?value1=' + val1 + '&value2=' + val2;
        }
    </script>
    """)

def add_numbers(request):
    """Perform addition using query parameters"""
    value1 = request.GET.get('value1', 0)
    value2 = request.GET.get('value2', 0)
    
    try:
        num1 = int(value1)
        num2 = int(value2)
        result = num1 + num2
        
        return HttpResponse(f"""
        <h1>Addition Result</h1>
        <p><strong>Value 1:</strong> {num1}</p>
        <p><strong>Value 2:</strong> {num2}</p>
        <p><strong>Result:</strong> {num1} + {num2} = {result}</p>
        <a href="/addform/">Calculate Again</a>
        """)
    except:
        return HttpResponse("<h1>Error: Please enter valid numbers</h1>")

