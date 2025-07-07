import sys
import os
import pandas as pd
import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QTextEdit, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# Dataset path
dataset_path = "IndianRecipes.csv"

# Check if dataset exists
if not os.path.exists(dataset_path):
    print(f"Error: Dataset '{dataset_path}' not found!")
    sys.exit(1)

# Load dataset
df = pd.read_csv(dataset_path)

# Ingredient Categories
ingredient_categories = {
    "Dairy": ["milk", "butter", "cheese", "yogurt", "cream", "paneer", "ghee", "khoya", "curd", "hung curd",
              "mozarella cheese", "Monterey Jack cheese", "Parmigiano Reggiano cheese"],
    "Fruits": ["pomegranate", "sugarcane", "mango", "mangoes", "bananas", "orange", "oranges", "apple",
               "apples", "custard apple", "pineapple", "coconut"],
    "Vegetables": ["onion", "onions", "tomato", "potato", "carrot", "cabbage", "cauliflower", "spinach",
                   "tomatoes", "eggplant", "green chilies", "carrots", "potatoes", "mashed potatoes", 
                   "capsicum", "bell peppers", "okra", "lemon", "curry leaves", "mint leaves",
                   "fenugreek leaves", "mushrooms", "mixed vegetables", "lemon juice", "beans", "peas"],
    "Grains and Seeds": ["rice", "wheat", "flour", "maida", "rava", "corn", "barley", "urad dal",
                         "fenugreek seeds", "peanuts", "fennel seeds", "poppy seeds"],
    "Spices": ["turmeric", "cardamom", "cumin", "coriander", "mustard", "chili", "ginger", "garlic",
               "cloves", "spices", "garam masala", "chaat masala", "salt", "goda masala",
               "pav bhaji masala", "dabeli masala", "black pepper", "rasam powder", "saffron",
               "green cardamoms", "cinnamon stick", "bay leaf", "red chilli powder"],
    "Legumes": ["lentils", "chickpeas", "beans", "peas", "moong", "masoor", "toor", "pepper",
                "baking powder", "baking soda", "sambar powder", "tamarind"],
    "Oils": ["oil", "butter", "mustard oil", "olive oil"],
    "Sweeteners": ["sugar", "jaggery", "honey"],
    "Nuts & Dry Fruits": ["almonds", "cashews", "raisins", "pistachios", "walnuts", "nuts"],
    "Chutney and Sauces": ["tamarind chutney", "soy sauce", "mint chutney", "green chutney",
                            "mint water", "schezwan sauce"],
    "Packaged Items": ["Noodles", "yeast", "bread crumbs", "bread", "spring roll wrappers",
                       "cornflour", "kokum", "sev", "semolina", "farsan"],
    "Meat and Fish": ["chicken", "fish", "sausage", "beef", "pork", "mutton"],
    "Other": []
}

class IngredientExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.extracted_ingredients = []  # Store extracted ingredients
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Recipe Ingredient Extractor")
        self.setGeometry(200, 100, 900, 600)

        layout = QVBoxLayout()

        self.titleLabel = QLabel("🍛 Recipe Ingredient Extractor 🍛")
        self.titleLabel.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.titleLabel.setStyleSheet("background-color: #fff0db")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.titleLabel)

        self.textInput = QTextEdit()
        self.textInput.setPlaceholderText("Enter your recipe here...")
        self.textInput.setStyleSheet("background-color: #FFCFCF;")
        layout.addWidget(self.textInput)

        self.extractButton = QPushButton("🔍 Extract Ingredients")
        self.extractButton.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px;")
        self.extractButton.clicked.connect(self.process_recipe)
        layout.addWidget(self.extractButton)

        self.sortButton = QPushButton("📊 Sort Ingredients")
        self.sortButton.setStyleSheet("background-color: #008CBA; color: white; font-size: 14px;")
        self.sortButton.clicked.connect(self.categorize_ingredients)
        layout.addWidget(self.sortButton)

        self.resultTable = QTableWidget()
        self.resultTable.setColumnCount(len(ingredient_categories))
        self.resultTable.setHorizontalHeaderLabels(ingredient_categories.keys())
        self.resultTable.setStyleSheet("background-color: #B1F0F7;")
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.resultTable)

        self.setLayout(layout)

    def extract_ingredients(self, text):
        found_ingredients = set()
        text = text.lower()  # Normalize input text

        for ingredient in df["Ingredients"]:
            for item in str(ingredient).split(","):
                item = item.strip().lower()
                if re.search(rf"\b{re.escape(item)}\b", text, re.IGNORECASE):
                    found_ingredients.add(item)

        return list(found_ingredients)

    def process_recipe(self):
        self.extracted_ingredients = []
        text = self.textInput.toPlainText().strip()

        if not text:
            self.show_message("Warning", "Please enter a recipe!")
            return

        self.extracted_ingredients = self.extract_ingredients(text)

        if not self.extracted_ingredients:
            self.show_message("Info", "No ingredients found in the dataset.")
        else:
            self.show_message("Success", f"Extracted {len(self.extracted_ingredients)} ingredients!")

    def categorize_ingredients(self):
        if not self.extracted_ingredients:
            self.show_message("Warning", "No ingredients extracted yet!")
            return

        categorized_data = {category: [] for category in ingredient_categories}
        categorized_data["Other"] = []

        for ingredient in self.extracted_ingredients:
            category = next(
                (cat for cat, items in ingredient_categories.items()
                 if any(re.search(rf"\b{re.escape(item)}\b", ingredient, re.IGNORECASE) for item in items)),
                "Other"
            )
            categorized_data[category].append(ingredient)

        self.display_categorized_ingredients(categorized_data)

    def display_categorized_ingredients(self, categorized_data):
        self.resultTable.setRowCount(max(len(items) for items in categorized_data.values()))

        for col, category in enumerate(categorized_data.keys()):
            for row, ingredient in enumerate(categorized_data[category]):
                self.resultTable.setItem(row, col, QTableWidgetItem(ingredient))

    def show_message(self, title, message):
        messagebox = QMessageBox()
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IngredientExtractor()
    window.show()
    sys.exit(app.exec())
