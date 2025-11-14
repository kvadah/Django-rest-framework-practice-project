 Django REST API: Product Management

This is a simple **Django REST Framework (DRF)** project to manage products.  
It allows you to **create, read, update, and delete products** through RESTful API endpoints.  

This project is built for **learning purposes**, especially for practicing **Django REST API development** and integrating with a frontend like **React**.

 Features

- List all products (`GET /api/products-list/`)
- Get a single product by ID (`GET /api/get-product/<id>/`)
- Create a new product (`POST /api/create-product/`)
- Delete a product (`DELETE /api/delete-product/<id>/`)


 Product Model

Each product has the following fields:

 Field         Type            Description                    

 id            Integer         Auto-incremented primary key   
 name         CharField       Name of the product            
 description   TextField       Product description            
 price         DecimalField   Product price                  
  created_at   DateTimeField   Timestamp when product created 

---

 Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
