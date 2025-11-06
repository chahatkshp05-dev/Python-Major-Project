from tkinter import *
from tkinter import messagebox, ttk

# -------------------------------
# Bakery Items Data
# ------------------------------
menu_items = {
    "Chocolate Cake": {"price": 250, "recipe": "Flour, Cocoa, Sugar, Eggs, Butter, Baking Powder, Milk"},
    "Vanilla Cupcake": {"price": 60, "recipe": "Flour, Sugar, Butter, Eggs, Vanilla Essence"},
    "Blueberry Muffin": {"price": 80, "recipe": "Flour, Blueberries, Sugar, Eggs, Butter"},
    "Croissant": {"price": 100, "recipe": "Flour, Butter, Yeast, Sugar, Milk"},
    "Bread Loaf": {"price": 120, "recipe": "Flour, Yeast, Sugar, Salt, Water"},
    "Donut": {"price": 70, "recipe": "Flour, Yeast, Sugar, Butter, Milk"},
    "Cheese Tart": {"price": 150, "recipe": "Flour, Cream Cheese, Sugar, Eggs, Butter"},
    "Cinnamon Roll": {"price": 130, "recipe": "Flour, Cinnamon, Butter, Sugar, Yeast"},
    "Cookies": {"price": 50, "recipe": "Flour, Sugar, Butter, Chocolate Chips"}
}

orders = []  # To store order details

# -------------------------------
# Main Window
# -------------------------------
root = Tk()
root.title("Bakery Management System")
root.geometry("900x700")
root.config(bg="light blue")

title = Label(root, text=" Bakery Management System ", font=("times new roman", 22, "bold", "italic"), bg="beige", fg="Chocolate")
title.pack(pady=10)

# -------------------------------
# Tabs (Notebook)
# -------------------------------
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=True)

# Frames for tabs
menu_frame = Frame(notebook, bg="pink")
order_frame = Frame(notebook, bg="pink")
feedback_frame = Frame(notebook, bg="pink")

notebook.add(menu_frame, text="Menu & Recipes")
notebook.add(order_frame, text="Order Management")
notebook.add(feedback_frame, text="Feedback Form")

# -------------------------------
# MENU TAB
# -------------------------------
Label(menu_frame, text="Select Bakery Item:", font=("Times new Roman", 18, "bold", "italic"), bg="light blue").pack(pady=5)
selected_item = StringVar()
selected_item.set("Select Item")

menu_dropdown = OptionMenu(menu_frame, selected_item, *menu_items.keys())
menu_dropdown.config(font=("times new roman", 14,"underline" ), bg="light blue")
menu_dropdown.pack(pady=5)

recipe_text = Text(menu_frame, width=70, height=10, wrap=WORD, font=("Arial", 12))
recipe_text.pack(pady=10)

def show_recipe():
    item = selected_item.get()
    if item == "Select Item":
        messagebox.showwarning("Warning", "Please select a bakery item!")
        return
    recipe_text.delete(1.0, END)
    recipe = menu_items[item]["recipe"]
    price = menu_items[item]["price"]
    recipe_text.insert(END, f" {item}\n\nIngredients:\n{recipe}\n\nPrice: ₹{price}")

Button(menu_frame, text="Show Recipe", command=show_recipe, bg="gray", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

# -------------------------------
# ORDER TAB
# -------------------------------
Label(order_frame, text="Order Bakery Items", font=("Times new roman", 18, "bold", "italic"), bg="light blue").pack(pady=10)

item_label = Label(order_frame, text="Select Item:", font=("Times new roman", 14, "bold"), bg="beige")
item_label.place(x=100, y=80)
item_var = StringVar()
item_dropdown = ttk.Combobox(order_frame, textvariable=item_var, values=list(menu_items.keys()), font=("Times new roman", 14), width=25)
item_dropdown.place(x=230, y=80)

qty_label = Label(order_frame, text="Quantity:", font=("Times new roman", 18, "bold", "italic"), bg="beige")
qty_label.place(x=100, y=120)
qty_var = IntVar()
qty_entry = Entry(order_frame, textvariable=qty_var, font=("Times new roman", 14), width=10)
qty_entry.place(x=230, y=120)

order_list = ttk.Treeview(order_frame, columns=("Item", "Qty", "Price"), show='headings', height=10,)
order_list.heading("Item", text="Item")
order_list.heading("Qty", text="Qty")
order_list.heading("Price", text="Price (₹)")
order_list.column("Item", width=200)
order_list.column("Qty", width=100)
order_list.column("Price", width=120)
order_list.place(x=100, y=180)

def add_order():
    item = item_var.get()
    qty = qty_var.get()
    if item == "" or qty <= 0:
        messagebox.showerror("Error", "Select item and enter valid quantity!")
        return
    price = menu_items[item]["price"] * qty
    orders.append({"item": item, "qty": qty, "price": price})
    order_list.insert("", "end", values=(item, qty, price))
    messagebox.showinfo("Success", f"{item} added to order!")

def delete_order():
    selected = order_list.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select an order to delete!")
        return
    for sel in selected:
        order_list.delete(sel)
    messagebox.showinfo("Deleted", "Item removed successfully.")

def show_total():
    total = sum(o["price"] for o in orders)
    messagebox.showinfo("Total Amount", f"Total Bill Amount: ₹{total}")

Button(order_frame, text="Add to Order", command=add_order, bg="gray", fg="white", font=("times new roman", 14, "bold")).place(x=100, y=450)
Button(order_frame, text="Delete Item", command=delete_order, bg="gray", fg="white", font=("times new roman", 14, "bold")).place(x=300, y=450)
Button(order_frame, text="Total Bill", command=show_total, bg="gray", fg="white", font=("times new roman", 14, "bold")).place(x=500, y=450)

# -------------------------------
# FEEDBACK TAB
# -------------------------------
Label(feedback_frame, text="Customer Feedback Form", font=("Times new roman", 18, "bold", "italic"), bg="light blue").pack(pady=10)

Label(feedback_frame, text="Name:", font=("Times new roman", 14, "bold"), bg="beige").place(x=100, y=80)
name_var = StringVar()
Entry(feedback_frame, textvariable=name_var, font=("Times new roman", 12), width=30).place(x=250, y=80)

Label(feedback_frame, text="Rating (1-5):", font=("Times new roman", 14, "bold"), bg="beige").place(x=100, y=120)
rating_var = IntVar()
Entry(feedback_frame, textvariable=rating_var, font=("Times new roman", 12), width=10).place(x=250, y=120)

Label(feedback_frame, text="Comments:", font=("Times new roman", 14, "bold"), bg="beige").place(x=100, y=160)
feedback_text = Text(feedback_frame, width=60, height=8, font=("Arial", 14))
feedback_text.place(x=250, y=160)

def submit_feedback():
    name = name_var.get()
    rating = rating_var.get()
    feedback = feedback_text.get(1.0, END).strip()
    if name == "" or rating == 0 or feedback == "":
        messagebox.showwarning("Incomplete", "Please fill all fields!")
        return
    messagebox.showinfo("Thank You!", f"Thank you {name} for your feedback! ")
    name_var.set("")
    rating_var.set(0)
    feedback_text.delete(1.0, END)

Button(feedback_frame, text="Submit Feedback", command=submit_feedback, bg="gray", fg="white", font=("times new roman", 14, "bold")).place(x=350, y=370)

# -------------------------------
root.mainloop()