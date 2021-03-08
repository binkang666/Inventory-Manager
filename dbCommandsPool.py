
def C_catagories():
    return "create table categories(categoryName VARCHAR(50) NOT NULL,CONSTRAINT categories_pk PRIMARY KEY (categoryName))"

def C_states():
    return"""create table states(
  abbreviation VARCHAR(2) NOT NULL,
  stateName VARCHAR(20),
  CONSTRAINT states_pk PRIMARY KEY (abbreviation),
  CONSTRAINT states_ck UNIQUE (stateName)
)"""
def C_zipLocation():
    return """create table zipLocations(
  zipCode INTEGER NOT NULL,
  city VARCHAR(30),
  state VARCHAR(2) NOT NULL,
  CONSTRAINT zipLocations_pk PRIMARY KEY (zipCode),
  CONSTRAINT state_zipLocations_fk FOREIGN KEY (state) REFERENCES states(abbreviation)
)"""

def C_venders():
    return """create table vendors(
  vendorName VARCHAR(50) NOT NULL,
  phoneNumber VARCHAR(20),
  email VARCHAR(50),
  streetAddress VARCHAR (50),
  websiteURL VARCHAR(50),
  CONSTRAINT vendors_pk PRIMARY KEY (vendorName)
)"""

def C_products():
    return """create table products(
  prodCode VARCHAR (15) NOT NULL,
  prodDesc VARCHAR (150) NOT NULL,
  vendor VARCHAR(50) NOT NULL,
  category VARCHAR (50) NOT NULL,
  CONSTRAINT products_pk PRIMARY KEY (prodCode, vendor),
  CONSTRAINT vendors_products_fk FOREIGN KEY (vendor) REFERENCES vendors(vendorName),
  CONSTRAINT categories_states_fk FOREIGN KEY(category) REFERENCES categories (categoryName)
)"""

def C_venderPrice():
    return """create table vendorprices(
    vendor VARCHAR(50) NOT NULL,
    product VARCHAR(15) NOT NULL,
    unitListPrice DOUBLE NOT NULL,
    timeChecked DateTime NOT NULL,
    CONSTRAINT vendorprices_pk PRIMARY KEY (vendor, product, timeChecked),
    CONSTRAINT products_vendorprices_fk FOREIGN KEY (vendor, product) REFERENCES products(vendor, prodCode)
)"""

def C_status():
    return"""create table status(
  status VARCHAR(10) NOT NULL,
  CONSTRAINT status_pk PRIMARY KEY (status)
)"""
def C_orders():
    return """CREATE TABLE orders(
    orderID VARCHAR (30) NOT NULL,
    orderDate DATETIME,
    vendor VARCHAR (50) NOT NULL,
    CONSTRAINT orderID_pk PRIMARY KEY (orderID),
    CONSTRAINT orders_vendorprice_fk FOREIGN KEY (vendor) REFERENCES vendorprices(vendor)
)"""

def C_orderLines():
    return"""CREATE TABLE orderLines(
    orderID VARCHAR (30) NOT NULL,
    quantity DOUBLE NOT NULL,
    unitSalePrice DOUBLE NOT NULL,
    vendor VARCHAR (50) NOT NULL,
    product VARCHAR(15) NOT NULL,
    timeChecked DateTime NOT NULL,
    CONSTRAINT orderLines_pk PRIMARY KEY (orderID, vendor, product, timeChecked),
    CONSTRAINT orders_orderLines_fk FOREIGN KEY (orderID) REFERENCES orders(orderID),
    CONSTRAINT vendorprice_orderLines_fk FOREIGN KEY (vendor, product, timeChecked) REFERENCES vendorprices(vendor, product, timeChecked)
)"""

def C_inventory():
    return"""CREATE TABLE inventory(
    unitsInStock double NOT NULL,
    reorderQuantity double NOT NULL,
    reorderLevel double NOT NULL,
    prodCode VARCHAR (15) NOT NULL,
    CONSTRAINT inventory_pk PRIMARY KEY (prodCode, unitsInStock),
    CONSTRAINT product_inventory_fk FOREIGN KEY (prodCode) REFERENCES products(prodCode)
)"""

def insertStates():
    return """INSERT INTO states
VALUES ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
     ('WY', 'Wyoming')"""

