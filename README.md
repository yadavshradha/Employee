# Employee
## ⚙️ Database Setup Note for Team

Before running this project on your laptop, please configure your local PostgreSQL database credentials:

1. **Create a `.env` file** in the root (`Employee_CRUD`) folder.
2. **Add your own local PostgreSQL password** inside the `.env` file like this:
   ```env
   DATABASE_URL=postgresql+psycopg2://postgres:YOUR_LOCAL_PASSWORD@localhost:5432/postgres
   ```
3. *(If running the code as-is without `.env`)*: Make sure your local PostgreSQL `postgres` user password is set to **`password`**, or update line 6 in `main.py` with your own local password before running. **Do not push your personal password to GitHub.**

4.if the above database setup don't work try this<br>
5. from sqlalchemy.engine import URL<br>

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="your_actual_password",  # Enter raw password without %40
    host="localhost",
    port=5432,
    database="postgres",
)

