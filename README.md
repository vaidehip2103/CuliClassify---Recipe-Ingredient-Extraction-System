# CuliClassify---Recipe-Ingredient-Extraction-System
CuliClassify automates recipe ingredient extraction using Machine Learning (ML) and Natural Language Processing (NLP) techniques like tokenization, part-of-speech tagging, and named entity recognition. This project tackles unstructured online recipes to build accurate, structured ingredient lists for culinary applications.

The extraction of ingredients from recipes is an essential task in modern food technology and culinary applications. Many online recipes lack clear ingredient lists or contain complex instructions, making ingredient extraction challenging.

This project uses **Machine Learning (ML)** and **Natural Language Processing (NLP)** to automate ingredient extraction from unstructured recipe data. Given the complexity and variability of recipe formats, traditional rule-based systems often fall short in accuracy and scalability.

**Key NLP techniques used:**
- Tokenization
- Part-of-Speech (POS) Tagging
- Named Entity Recognition (NER)

**Key ML methods:**
- Supervised learning models trained on labeled recipe datasets to improve extraction accuracy.

### 📌 Challenges Addressed
- Handling ambiguous ingredient names.
- Differentiating between quantities and units.
- Managing variations in formatting.
- Categorizing ingredients into groups like vegetables, dairy, grains, etc.
- Suggesting substitutes (e.g., flax egg for egg, vinegar for citric acid).

This tool helps beginner cooks or anyone needing a clear, categorized ingredient list for easier shopping and meal preparation. It also lays the groundwork for applications like personalized nutrition, smart kitchen assistants, and food industry analytics.

Future work aims to integrate domain-specific ontologies to further enhance extraction accuracy and efficiency.

---

## 📂 Project Structure

Recipe Ingredient Extraction/
│
├── final1.py # Main Python script
├── final.py # Supporting script
├── app.py # Application entry point
├── IndianRecipes.xlsx # Recipe dataset (Excel)
├── ingredient_model.pkl # Trained ML model
├── tfidf_vectorizer.pkl # TF-IDF vectorizer
├── categorized_ingredients.json # Ingredient categories
└── Report and Research Paper/ # Contains detailed report, research paper, and presentation (PPT)



---

## ✅ How to Use

1. Clone the repository.
2. Install dependencies.
3. Run the Python scripts to process recipes and extract ingredients.
4. Check the `Report and Research Paper` folder for detailed documentation and presentation materials.

---

Feel free to explore, modify, and build upon this project to contribute to the future of smart culinary applications!
