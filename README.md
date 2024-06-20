# Fintech Application with Django and DRF APIs

Welcome to our fintech application repository, built using Django and Django Rest Framework (DRF). This application allows users to transfer and receive money, view transaction records, manage accounts with wallets and tags, and provides a dashboard for user interaction.

## Overview

This project aims to replicate basic functionalities of a fintech app. Key features include:

- **User Registration**: Users can create accounts, each associated with a unique tag and wallet.
- **Transfer and Receive**: Users can transfer money to others using the receiver's wallet tag.
- **Dashboard**: Provides a user-friendly dashboard to view account details and transaction history.
- **Transaction Record**: Maintains a record of all transactions between app customers.
- **APIs with DRF**: Backend APIs built using Django Rest Framework for seamless integration and scalability.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ehiremengold/fintech-app.git
   cd fintech-app
2. **Set up the environment**:
   - Ensure Python and Django are installed on your machine.
   - Create a virtual environment and install dependencies:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     pip install -r requirements.txt
3. Run migrations
4. Create superuser (for admin access)
5. Run the development server
6. Explore and use the application:
   - Access the Django admin at  `http://localhost:8000/admin/` to manage users, wallets, transactions, etc.
   - Use the provided APIs (built with DRF) for integration with frontend or other services.
