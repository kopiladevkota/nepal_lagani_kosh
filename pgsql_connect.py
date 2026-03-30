# investment_app.py
from db_connection import get_connection

conn = get_connection()
if not conn:
    print("Cannot continue without DB connection. Exiting...")
    exit()

cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS investments (
        id SERIAL PRIMARY KEY,
        investor_name VARCHAR(100),
        monthly_deposit NUMERIC,
        years INT,
        total_investment NUMERIC
    );
""")
conn.commit()

while True:
    print("\n----- Investment Menu -----")
    print("1. Add new investment")
    print("2. Update investment")
    print("3. Delete investment")
    print("4. View all investments")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Insert
        name = input("Enter investor name: ")
        monthly_deposit = float(input("Enter monthly deposit: "))
        years = int(input("Enter investment years: "))
        total_investment = monthly_deposit * 12 * years

        cur.execute(
            "INSERT INTO investments (investor_name, monthly_deposit, years, total_investment) VALUES (%s, %s, %s, %s)",
            (name, monthly_deposit, years, total_investment)
        )
        conn.commit()
        print("Investment added successfully!")

    elif choice == "2":
        # Update
        update_id = int(input("Enter ID to update: "))
        cur.execute("SELECT * FROM investments WHERE id=%s", (update_id,))
        record = cur.fetchone()

        if record:
            print(f"Current Record: {record}")
            new_name = input("Enter new investor name (leave blank to keep same): ")
            new_deposit_input = input("Enter new monthly deposit (leave blank to keep same): ")
            new_years_input = input("Enter new number of years (leave blank to keep same): ")

            new_name = new_name if new_name.strip() else record[1]
            new_deposit = float(new_deposit_input) if new_deposit_input.strip() else float(record[2])
            new_years = int(new_years_input) if new_years_input.strip() else int(record[3])
            new_total = new_deposit * 12 * new_years

            cur.execute(
                "UPDATE investments SET investor_name=%s, monthly_deposit=%s, years=%s, total_investment=%s WHERE id=%s",
                (new_name, new_deposit, new_years, new_total, update_id)
            )
            conn.commit()
            print("Investment updated successfully!")
        else:
            print(f"ID {update_id} does not exist! Cannot update.")

    elif choice == "3":
        # Delete
        delete_id = int(input("Enter ID to delete: "))
        cur.execute("SELECT * FROM investments WHERE id=%s", (delete_id,))
        record = cur.fetchone()

        if record:
            cur.execute("DELETE FROM investments WHERE id=%s", (delete_id,))
            conn.commit()
            print("Investment deleted successfully!")
        else:
            print(f"ID {delete_id} does not exist! Cannot delete.")

    elif choice == "4":
        # View
        cur.execute("SELECT * FROM investments")
        rows = cur.fetchall()
        print("\n----- All Investments -----")
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Monthly: {row[2]}, Years: {row[3]}, Total: {row[4]}")
        else:
            print("No records found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice! Try again.")

cur.close()
conn.close()
print("Program exited. ")