# Sagar Sahu
# Walmart Global Tech Advanced SWE Virtual Job- Task 4

import csv
import sqlite3


def insertShippingData_1(cursor):
    with open('/Desktop/Walmart\ Advanced\ Virtual\ SWE/src/data/shipping_data_0.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            origin, destination, product, on_time, product_quantity, driver_identifier = row
            cursor.execute("INSERT INTO shipping_data_0 (origin, destination, product, on_time, product_quantity, driver_identifier) VALUES (?, ?, ?, ?, ?, ?)",
                           (origin, destination, product, on_time, product_quantity, driver_identifier))


def insertShippingData_2(cursor):
    with open('/Desktop/Walmart\ Advanced\ Virtual\ SWE/src/data/shipping_data_2.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        shipping_data_2_rows = [row for row in csv_reader]

    with open('/Desktop/Walmart\ Advanced\ Virtual\ SWE/src/data/shipping_data_1.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            shipment_identifier, product, on_time = row
            matching_rows = [r for r in shipping_data_2_rows if r[0] == shipment_identifier]
            if matching_rows:
                origin, destination, driver_identifier = matching_rows[0][1], matching_rows[0][2], matching_rows[0][3]
                cursor.execute("INSERT INTO shipping_data_1 (shipment_identifier, product, on_time, origin, destination) VALUES (?, ?, ?, ?, ?)",
                               (shipment_identifier, product, on_time, origin, destination))
                

def getData(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_0 (
            origin TEXT,
            destination TEXT,
            product TEXT,
            on_time TEXT,
            product_quantity INTEGER,
            driver_identifier TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipping_data_1 (
            shipment_identifier TEXT,
            product TEXT,
            on_time TEXT,
            origin TEXT,
            destination TEXT
        )
    """)
    insertShippingData_1(cursor)
    insertShippingData_2(cursor)


if __name__ == "__main__":
    database = sqlite3.connect('/Desktop/Walmart\ Advanced\ Virtual\ SWE/src/shipment_database.db')
    cursor = database.cursor()
    getData(cursor)
    database.commit()
    database.close()