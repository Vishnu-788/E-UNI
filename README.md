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
- Registration, Login, logout (Common endpoints for all userS(Shop, Customers))
    -> `POST /api/register/`
    -> `POST /api/login/`
    -> `POST /api/logout/`

- Shop based endpoints
    -> `GET/PATCH   /api/shop/`
    -> `GET         /api/shop/products/`
    -> `GET         /api/shop/products/<id>/detail/`
    -> `PATCH/PUT   /api/shop/products/<id>/update/`
    -> `DESTROY     /api/shop/products/<id>/delete/`

- Customer based endpoints
    -> `GET/PATCH   /api/customer/`
    -> `GET         `


## 🛠️ Built With
- Python 🐍
- Django
- Django REST Framework
- Simple JWT

## 📝 License
MIT License
