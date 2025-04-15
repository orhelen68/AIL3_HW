# Homework 23 Submission by Helen Or
# Convert Homework 2 to SQLMdoel 
#Part 1.  Create Ikea Furniture Database
from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session
from pydantic import BaseModel

# Class IkeaFurniture using pydantic BaseModel
class IkeaFurniture(BaseModel):
    name : str | None = Field(default=None, primary_key=True)
    series : str 
    furniture_type : str 
    children_furniture : bool = Field(default=False)
    price : float
    width : float
    height : float
    depth : float
    qty_in_stock : int
    
        
# Child Classes:  Ikea Chairs, Tables, and Shelves 
class IkeaChair(SQLModel, IkeaFurniture, table=True):
    id : Optional[int] | None = Field(default=None, primary_key=True)
    has_arms : bool  
    
class IkeaTable(SQLModel, IkeaFurniture, table=True):
    id : Optional[int] | None = Field(default=None, primary_key=True)    
    shape : str 
    capacity : int
    
class IkeaShelf(SQLModel, IkeaFurniture, table=True):
    id : Optional[int] | None = Field(default=None, primary_key=True)
    colour : str 
    shelf_type : str
        
    
# Define class for a simple shopping cart item 
class Choice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="shoppingcart.id")
    
    # Store furniture type, ID, and quantity as simple fields
    furniture_type: str  # "Chair", "Table", or "Shelf"
    furniture_id: int
    quantity: int = 1

# Define class for shopping cart to hold different types of IKEA furniture
class ShoppingCart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    #created_date: date = Field(default_factory=date.today)
    customer_name: str
    customer_email: Optional[str] = None
    
    """
    def add_item(self, session: Session, furniture: any, quantity: int = 1):
        # Add a furniture item to the cart
        # Determine furniture type
        furniture_type_map = {
            IkeaChair: "Chair",
            IkeaTable: "Table",
            IkeaShelf: "Shelf"
        }
        
        furniture_type = furniture_type_map.get(type(furniture))
        if not furniture_type:
            raise ValueError(f"No items for this furniture type: {type(furniture)}")
        
        # Get the furniture data directly from the database to ensure all fields are loaded
        session.refresh(furniture)
        
        # Convert furniture to dictionary for storage
        furniture_dict = {
            # Common fields for all furniture types
            'id': furniture.id,
            'name': furniture.name,
            'price': furniture.price,
            'qty_in_stock': furniture.qty_in_stock,
            #'date_added': furniture.date_added.isoformat() if isinstance(furniture.date_added, date) else str(furniture.date_added)
        }
                
        # Create cart item
        cart_item = CartItem(
            cart_id=self.id,
            furniture_type=furniture_type,
            furniture_id=furniture.id,
            quantity=quantity,
            furniture_price=furniture_price
        )
        
        session.add(cart_item)
        session.commit()
        return cart_item
       """
        
# Create a SQLite database and engine
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
 
engine = create_engine(sqlite_url, echo=True)
 
SQLModel.metadata.create_all(engine)

# Create instances of IkeaFurniture
Ikea1 = IkeaChair(name="Office Chair", series="Markus", furniture_type="Chair", children_furniture=False, price=499.99, width=200.0, height=90.0, depth=100.0, qty_in_stock=10, id=1, has_arms=True)
Ikea2 = IkeaTable(name="Dining Table", series="Lack", furniture_type="Table", children_furniture=False, price=299.99, width=150.0, height=75.0, depth=90.0, qty_in_stock=5, id=2, shape="Round", capacity=6)
Ikea3 = IkeaShelf(name="Bookshelf", series="Billy", furniture_type="Shelf", children_furniture=False, price=199.99, width=80.0, height=200.0, depth=30.0, qty_in_stock=15, id=3, colour="Black", shelf_type="Wall-mounted")
Ikea4 = IkeaChair(name="Dining Chair", series="Lack", furniture_type="Chair", children_furniture=False, price=299.99, width=200.0, height=90.0, depth=100.0, qty_in_stock=20, id=4, has_arms=True)
Ikea5 = IkeaTable(name="Long Dining Table", series="Stylo", furniture_type="Table", children_furniture=False, price=599.99, width=250.0, height=75.0, depth=90.0, qty_in_stock=5, id=5, shape="Rectangle", capacity=10)
Ikea6 = IkeaShelf(name="White Bookshelf", series="Billy", furniture_type="Shelf", children_furniture=False, price=99.99, width=40.0, height=50.0, depth=30.0, qty_in_stock=12, id=6, colour="White", shelf_type="Wall-mounted")
Ikea7 = IkeaChair(name="Children Chair", series="Lack", furniture_type="Chair", children_furniture=True, price=99.99, width=100.0, height=50.0, depth=80.0, qty_in_stock=10, id=7, has_arms=True)
Ikea8 = IkeaTable(name="Child Table", series="Lack", furniture_type="Table", children_furniture=True, price=199.99, width=100.0, height=65.0, depth=100.0, qty_in_stock=10, id=8, shape="Square", capacity=2)
Ikea9 = IkeaShelf(name="Wooden Bookshelf", series="Markus", furniture_type="Shelf", children_furniture=False, price=159.99, width=100.0, height=100.0, depth=30.0, qty_in_stock=5, id=9, colour="Oak", shelf_type="standing")

# Create instances of Shopping Cart
Cart1 = ShoppingCart(id = 1, customer_name="Helen", customer_email="oh@gmail.com")

Choice1 = Choice(id=1, cart_id=1, furniture_type="Chair", furniture_id=1, quantity=2)
Choice2 = Choice(id=2, cart_id=1, furniture_type="Table", furniture_id=2, quantity=1)


with Session(engine) as session:

    # Create a session to add instances to the various Ikea Furniture Databases
    session.add(Ikea1)
    session.add(Ikea2)
    session.add(Ikea3)
    session.add(Ikea4)
    session.add(Ikea5)
    session.add(Ikea6)
    session.add(Ikea7)
    session.add(Ikea8)
    session.add(Ikea9)
    session.commit()
    print("Ikea Furniture items added to databases")
    
    session.add(Cart1)
    session.commit()
    print("Shopping Cart created")

    session.add(Choice1)
    session.add(Choice2)
    session.commit()
    print("Customer's Choices added to Shopping Cart")

    
