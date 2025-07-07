import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import re

# Load dataset
dataset_path = "IndianRecipes.csv"
df = pd.read_csv(dataset_path)

# Ingredient Categories
ingredient_categories = {
    "Dairy": ["milk", "butter", "cheese", "yogurt", "cream", "paneer", "ghee","khoya","curd","hung curd","mozarella cheese","Monterey Jack cheese","Parmigiano Reggiano cheese"],
    "Fruits": ["pomegranate","sugarcane","mango","mangoes","bananas","bananas","orange","oranges","apple","apples","custard apple","pineapple","coconut"],
    "Vegetables": ["onion","onions", "tomato", "potato", "carrot", "cabbage", "cauliflower", "spinach","tomatoes","eggplant","green chilies","carrots","potatoes","mashed potatoes","capsicum","bell peppers","okra","lemon","curry leaves","mint leaves","fenugreek leaves","mushrooms","mixed vegetables","lemon juice","beans","peas"],
    "Grains and Seeds": ["rice", "wheat", "flour", "maida", "rava", "corn", "barley","urad dal","fenugreek seeds","peanuts","fennel seeds","poppy seeds"],
    "Spices": ["turmeric", "cumin", "coriander", "mustard", "chili", "ginger", "garlic", "cardamom", "cloves","spices","garam masala","chaat masala","salt","goda masala","pav bhaji masala", "dabeli masala","black pepper","rasam powder","saffron","green cardomoms","cinnamon stick","bay leaf","red chilli powder"],
    "Legumes": ["lentils", "chickpeas", "beans", "peas", "moong", "masoor", "toor","pepper","baking powder","baking soda","sambar powder","tamarind"],
    "Oils": ["oil", "butter", "mustard oil", "olive oil"],
    "Sweeteners": ["sugar", "jaggery", "honey"],
    "Nuts & Dry Fruits": ["almonds", "cashews", "raisins", "pistachios", "walnuts","nuts"],
    "Chutney and sauces" : ["tamarind chutney","soy sauce","mint chutney","green chutney","mint water","schezwan sauce"],
    "Packaged items" : ["Noodles","yeast","bread crumbs","bread","spring roll wrappers","cornflour","kokum","sev","semolina","farsan"],
    "Meat and fish" : ["chicken","fish","sausage","beef","pork","mutton"],
    "Other": []
}

# Extract ingredients from text
def extract_ingredients(text):
    found_ingredients = set()
    for ingredient in df["Ingredients"]:
        for item in str(ingredient).split(","):
            item = item.strip().lower()
            if re.search(rf"\b{re.escape(item)}\b", text, re.IGNORECASE):
                found_ingredients.add(item)
    return list(found_ingredients)

# Categorize extracted ingredients
def categorize_ingredients():
    global extracted_ingredients
    if not extracted_ingredients:
        messagebox.showwarning("Warning", "No ingredients extracted yet!")
        return

    categorized_data = {category: [] for category in ingredient_categories}
    categorized_data["Other"] = []

    for ingredient in extracted_ingredients:
        category = next(
            (cat for cat, items in ingredient_categories.items()
             if any(re.search(rf"\b{item}\b", ingredient, re.IGNORECASE) for item in items)),
            "Other"
        )
        categorized_data[category].append(ingredient)

    display_categorized_ingredients(categorized_data)

# Display categorized ingredients in a tabular format
def display_categorized_ingredients(categorized_data):
    for widget in result_frame.winfo_children():
        widget.destroy()
    
    columns = list(categorized_data.keys())
    tree = ttk.Treeview(result_frame, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col, anchor="w")
        tree.column(col, width=120, anchor="w")
    
    max_rows = max(len(ingredients) for ingredients in categorized_data.values())
    
    for i in range(max_rows):
        row_values = [categorized_data[col][i] if i < len(categorized_data[col]) else "" for col in columns]
        tree.insert("", "end", values=row_values)
    
    tree.pack(expand=True, fill="both")

# Process input recipe
def process_recipe():
    global extracted_ingredients
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter the recipe text!")
        return

    extracted_ingredients = extract_ingredients(text)
    
    if not extracted_ingredients:
        messagebox.showinfo("No Ingredients Found", "No matching ingredients found in the dataset.")
    else:
        extracted_label.config(text="Extracted Ingredients:\n" + ", ".join(extracted_ingredients))

# GUI Setup
root = tk.Tk()
root.title("🌿 Recipe Ingredient Extractor 🌿")
root.geometry("900x700")
root.configure(bg="#f0f8ff")

# Title Label
tk.Label(root, text="🍛 Recipe Ingredient Extractor 🍛", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#ff5733").pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

text_input = tk.Text(input_frame, height=8, width=80, font=("Arial", 12))
text_input.grid(row=0, columnspan=2, pady=5)

# Buttons
extract_button = tk.Button(input_frame, text="🔍 Extract Ingredients", command=process_recipe, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
extract_button.grid(row=1, column=0, padx=10, pady=5)

sort_button = tk.Button(input_frame, text="📊 Sort Ingredients", command=categorize_ingredients, bg="#008CBA", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
sort_button.grid(row=1, column=1, padx=10, pady=5)

# Results Frame
extracted_label = tk.Label(root, text="Extracted Ingredients will appear here", font=("Arial", 12, "bold"), bg="#f0f8ff", fg="#333")
extracted_label.pack(pady=10)

result_frame = tk.Frame(root, bg="#ffcc80", relief=tk.RIDGE, borderwidth=2)
result_frame.pack(pady=10, fill="both", expand=True)

# Run the GUI
root.mainloop()
