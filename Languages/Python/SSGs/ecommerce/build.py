from jinja2 import Environment, FileSystemLoader
from ezspreadsheet import Spreadsheet

# Create a Jinja2 environment with a file system loader
env = Environment(loader=FileSystemLoader("templates"))


# Load the template from a file
homepage = env.get_template("index.jinja")
product_page = env.get_template("product.jinja")

# Define data to be used in the template

with Spreadsheet('products.xlsx') as product_sheet:
    product_data = product_sheet.load("Product")

products = dict()

for item in product_data[1]:
    if item.Name:
        products[item.Name] = {
            "name":item.Name,
            "image":item.Image, 
            "price": item.Price, 
            "description":item.Description, 
        }  

# Render the template with the provided data
rendered_homepage = homepage.render(items=products)

with open("index.html", "w+") as out:
    out.write(rendered_homepage)

for item in products:
    with open(f"products/{item}.html", "w+") as out:
        out.write(product_page.render(item = products[item]))


# Print the rendered template
# print(rendered_template)