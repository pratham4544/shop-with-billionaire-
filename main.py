import streamlit as st

# Initial billionaire data
billionaire_data = {
    "Jeff Bezos": {"photo_url": 'https://th.bing.com/th?id=OSK.HEROaY-R5vlsG4Ec3nDpn1aWHaRa0U6mBgoqXWzRGm_TnoA&w=384&h=228&c=13&rs=2&o=6&oif=webp&pid=SANGAM', "net_worth": 11.5e9},
    # Add more billionaires if needed
}

# Available items for purchase
items = {
    "Ferrari": {"price": 500000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    "Lamborghini": {"price": 600000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    "Yacht": {"price": 1000000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    "Mansion": {"price": 2000000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    "Walmart": {"price": 500000000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    "HP": {"price": 300000000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    "Dell": {"price": 400000000, "image": "https://www.bing.com/th?id=OIP.9rssJewM8mcVHxy84ucVXgHaE8&w=170&h=106&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"},
    # Add more items if needed
}

# Function to update net worth based on purchased items
def update_net_worth(billionaire, purchased_items):
    for item, qty in purchased_items.items():
        billionaire_data[billionaire]["net_worth"] -= items[item]["price"] * qty

# Streamlit app
def main():
    st.title("Help Your Billionaire In Shopping...")

    # Greet friend and ask for their name
    friend_name = st.text_input("Enter Your Name Please Sir")

    if friend_name:
        st.write(f"Welcome, {friend_name}! Let's go shopping with your friend.")

        # Add Billionaire Form
        # st.header("Add Billionaire")
        # new_billionaire_name = st.text_input("Billionaire Name")
        # new_billionaire_photo_url = st.text_input("Billionaire Photo URL")
        # new_billionaire_net_worth = st.number_input("Billionaire Net Worth", step=1e6)

        # if st.button("Add Billionaire"):
        #     billionaire_data[new_billionaire_name] = {"photo_url": new_billionaire_photo_url, "net_worth": new_billionaire_net_worth}
        #     st.success("Billionaire added successfully!")

        # Add Item Form
        # st.header("Add Item")
        # new_item_name = st.text_input("Item Name")
        # new_item_price = st.number_input("Item Price", step=1e4)
        # new_item_image_url = st.text_input("Item Image URL")

        # if st.button("Add Item"):
        #     items[new_item_name] = {"price": new_item_price, "image": new_item_image_url}
        #     st.success("Item added successfully!")

        # Select a billionaire
        billionaire = st.selectbox("Select Your Billionaire Friend", list(billionaire_data.keys()))

        # Display billionaire information
        st.image(billionaire_data[billionaire]["photo_url"], caption=billionaire, use_column_width=True)
        st.write(f"Net Worth: ${billionaire_data[billionaire]['net_worth'] / 1e9:.2f} billion")

        # Display available items for purchase in a grid
        st.header("Available Items for Purchase")

        items_per_row = 4
        num_items = len(items)
        num_rows = (num_items + items_per_row - 1) // items_per_row

        for row in range(num_rows):
            cols = st.columns(items_per_row)
            for col in cols:
                index = row * items_per_row + cols.index(col)
                if index < num_items:
                    item = list(items.keys())[index]
                    item_info = items[item]
                    col.image(item_info["image"], caption=item, use_column_width=True)
                    col.write(f"{item}\nPrice: ${item_info['price']:,}")
                    item_key = f"{billionaire}_{item}"  # Unique key for the item
                    qty = col.number_input(f"Qty of {item}", min_value=0, step=1, key=item_key)
                    # if qty > 0:
                    #     st.write(f"Selected Qty: {qty}")

        # Add items to cart
        if st.button("Add to Cart"):
            selected_items = {}
            for item in items.keys():
                item_key = f"{billionaire}_{item}"  # Unique key for the item
                qty = st.session_state.get(item_key, 0)
                if qty > 0:
                    selected_items[item] = qty

            # Check if net worth is sufficient
            total_price = sum(items[item]["price"] * qty for item, qty in selected_items.items())
            if total_price > billionaire_data[billionaire]["net_worth"]:
                st.error("Insufficient funds to purchase selected items!")
            else:
                # Update net worth based on purchased items
                update_net_worth(billionaire, selected_items)
                # Display confirmation
                st.success("Items added to cart successfully!")

        # Display updated net worth
        st.write(f"Updated Net Worth: ${billionaire_data[billionaire]['net_worth'] / 1e9:.2f} billion")

        # Thank you message and button
        if st.button("Thank You for Shopping!"):
            st.write(f"Thank you, {friend_name} and {billionaire}, for shopping with us!")
    
    else:
        st.warning("Please enter your friend's name to start shopping.")

if __name__ == "__main__":
    main()
