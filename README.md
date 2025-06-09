# 🛍️ E-UNI E-commerce Backend

An E-Commerce application backend built using Django stateless server and REST FRAMEWORK. Used DRF for making APIs and JWT for stateless authentication. Mainly this application consist of 2 users - Customer and Shop. Customers can view, update their profile and browse products from different shops and order them. Shop can perform CRUD opertaions on the product, view/update their profile and view orders. NOTE: Shops can only perform CRUD if they complete thier registration, so after registering as a user complete the registration by calling the `PATCH   /api/shop/` endpoint

## ✨ Features

- Shop & Customer registration  
- Product CRUD  
- Customer product view  
- Token-based authentication (JWT)  
- Isolated permissions for Shop & Customer users  

## ⚙️ Installation

1. Clone the repo and enter the project folder  
2. Create virtual environment  
3. Install dependencies  
4. Run migrations  
5. Start the server  

## 📮 API Endpoints

### Registration, Login, Logout  
(Common endpoints for all users (Shop, Customers))

- **POST** `/api/register/` — Register a new user  
- **POST** `/api/login/` — Login an existing user  
- **POST** `/api/logout/` — Logout the current user  

---

### Shop based endpoints

- **GET / PATCH** `/api/shop/` — View or update shop details/profile  
- **GET** `/api/shop/products/` — View all products of the shop  
- **GET** `/api/shop/products/<id>/detail/` — View a single product  
- **POST** `/api/shop/products/create/` — Create a product  
- **PATCH / PUT** `/api/shop/products/<id>/update/` — Update product details  
- **DELETE** `/api/shop/products/<id>/delete/` — Delete a product  

- **GET** `/api/orders/shop/` — View all orders related to that shop  
- **GET** `/api/orders/shop/<int:pk>/detail/` — View a specific order  
- **PATCH** `/api/orders/shop/<int:pk>/update/` — Update an order  
- **DELETE** `/api/orders/shop/<int:pk>/delete/` — Delete an order  

---

### Customer based endpoints

- **GET** `/api/customer/` — View products from different shops  
- **GET / PATCH** `/api/customer/<id>/` — View or update a specific product  
- **GET / PATCH** `/api/customer/profile/` — View or update customer profile  

- **GET** `/api/orders/customer/` — View all orders related to that customer  
- **POST** `/api/orders/customer/create/` — Create a new order  
- **GET** `/api/orders/customer/<id>/detail` — View a specific order  

  
## 🛠️ Built With

- Python 
- Django
- Django REST Framework
- Simple JWT

## 📝 License

MIT License
