# 📝 Practice Modifying Object Attributes and Calling Methods

In this exercise, we practiced how to **create a table object, add columns, and call methods** using the `PrettyTable` Python library.

The goal was to understand how to:

* Import and use a class (`PrettyTable`)
* Modify an object by **adding columns**
* Call methods on the object to display structured data

---

## 📌 Code

```python
from prettytable import PrettyTable

# Step 1: Create a table object
table = PrettyTable()

# Step 2: Add a "Pokemon" column
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])

# Step 3: Add a "Type" column
table.add_column("Type", ["Electric", "Water", "Fire"])

# Step 4: Print the table
print(table)
```

---

## 📸 Output Screenshot

Below is the output generated when running the script:

<img width="184" height="103" alt="Screenshot 2025-09-12 at 19 13 07" src="https://github.com/user-attachments/assets/2d4c4a3d-09f8-403c-80e3-950700d613d3" />


---

## 🧠 Explanation

1. **Importing the Class**

   ```python
   from prettytable import PrettyTable
   ```

   * `PrettyTable` is a class from the `prettytable` library that allows us to create neatly formatted tables in Python.

2. **Creating an Object**

   ```python
   table = PrettyTable()
   ```

   * Here, `table` is an object (or instance) of the `PrettyTable` class.
   * Think of it like creating a blank spreadsheet: the table exists, but it has no content yet.

3. **Adding Columns**

   ```python
   table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
   table.add_column("Type", ["Electric", "Water", "Fire"])
   ```

   * `.add_column("Name", [list])` takes two inputs:

     * A **column title** (like `"Pokemon"` or `"Type"`)
     * A **list of values** that go under that column.
   * Each call to `.add_column()` modifies the table object by attaching new data.

4. **Displaying the Table**

   ```python
   print(table)
   ```

   * When printed, the `PrettyTable` object automatically formats the data into a grid.
   * This is possible because the `PrettyTable` class has a built-in **`__str__` method** that knows how to represent the table as text.

---

## ✅ What I Learned

* How to create an object from a Python class (`PrettyTable()`).
* How to use `.add_column()` to insert data into the object.
* How calling `print(table)` automatically formats the table for display.
* Objects can be **modified** by calling their **methods**.
