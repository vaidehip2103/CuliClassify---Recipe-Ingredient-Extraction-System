# Tkinter GUI
root = tk.Tk()
root.title("Ingredient Categorizer")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

# Table Headers
columns = list(ingredient_categories.keys())
tree = ttk.Treeview(frame, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.grid(row=1, column=0, sticky='nsew')

# Insert data into table
max_rows = max(len(items) for items in all_categorized_ingredients.values())
for i in range(max_rows):
    row = [all_categorized_ingredients[col][i] if i < len(all_categorized_ingredients[col]) else "" for col in columns]
    tree.insert("", "end", values=row)

# Run the GUI
root.mainloop()