# 🛒 Demo Web Shop Automation Framework (Playwright + Pytest)

## 📌 Project Overview

This project is an **end-to-end web automation framework** built using **Playwright (Python)** and **Pytest** for the Demo Web Shop application.

It automates real user workflows in an e-commerce application, covering:

* Login functionality
* Product search
* Add to cart
* Cart validation
* Complete checkout process

The framework is designed using the **Page Object Model (POM)** to ensure clean code structure, reusability, and easy maintenance.

---

## 🧰 Tech Stack

* **Language:** Python
* **Automation Tool:** Playwright
* **Test Framework:** Pytest
* **Reporting:** Allure Reports
* **CI/CD:** Jenkins

---

## 📁 Project Structure

```
Pythonplaywright/
│
├── pages/              # Page Object classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── checkout_page.py
│
├── tests/              # Test cases
│   ├── test_login.py
│   ├── test_search.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_e2e.py
│
├── conftest.py         # Fixtures (browser setup)
├── pytest.ini          # Configuration
├── requirements.txt    # Dependencies
```

---

## ✅ Features

* End-to-End automation for key e-commerce flows
* Page Object Model (POM) design pattern
* Reusable and maintainable code structure
* Handles dynamic elements and synchronization issues
* Allure reporting integration
* Jenkins CI integration

---

## 🔄 Test Scenarios Covered

* Valid & Invalid Login
* Product Search
* Add to Cart
* Cart Verification
* Checkout Flow
* End-to-End Testing

---

## ▶️ How to Run Tests

### Install dependencies

```
pip install -r requirements.txt
```

### Install Playwright browsers

```
playwright install
```

### Run tests

```
pytest
```

### Generate Allure report

```
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 🚀 CI/CD Integration

This framework is integrated with **Jenkins**:

* Code is pulled from GitHub
* Dependencies are installed
* Tests are executed automatically
* Reports are generated

---

## 💡 Highlights

* Handles real-time UI challenges like dynamic elements
* Clean and scalable framework design
* Suitable for real-world automation projects

---

## 👩‍💻 Author

Kavya Sureddy
