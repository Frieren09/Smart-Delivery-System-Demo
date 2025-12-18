import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        os.environ["DATABASE_URL"],
        sslmode="require"
    )



def create_order(customer_id, items):

    conn = get_connection()

    cur = conn.cursor()


    cur.execute(

        "INSERT INTO orders (customer_id, status) VALUES (%s, %s) RETURNING order_id",

        (customer_id, "Pending")

    )

    order_id = cur.fetchone()[0]


    for item in items:

        cur.execute(

            """

            INSERT INTO order_items (order_id, product_id, quantity)

            VALUES (%s, %s, %s)

            """,

            (order_id, item["product_id"], item["quantity"])

        )


    conn.commit()

    cur.close()

    conn.close()


    return order_id



def get_order_items(order_id):

    conn = get_connection()

    cur = conn.cursor()


    cur.execute("""

        SELECT 

            p.name,

            oi.quantity

        FROM order_items oi

        JOIN products p ON oi.product_id = p.product_id

        WHERE oi.order_id = %s

    """, (order_id,))


    rows = cur.fetchall()

    cur.close()

    conn.close()


    return [

        {

            "product_name": r[0],

            "quantity": r[1]

        }

        for r in rows

    ]




def get_all_riders():

    conn = get_connection()

    cur = conn.cursor()


    cur.execute("SELECT rider_id, name FROM riders")

    rows = cur.fetchall()


    cur.close()

    conn.close()


    return [

        {"rider_id": r[0], "name": r[1]}

        for r in rows

    ]



def assign_rider(order_id, rider_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE orders
        SET rider_id = %s,
            status = 'Assigned'
        WHERE order_id = %s
    """, (rider_id, order_id))

    conn.commit()
    cur.close()
    conn.close()




def update_order_status(order_id, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE orders
        SET status = %s
        WHERE order_id = %s
    """, (status, order_id))

    conn.commit()
    cur.close()
    conn.close()

def get_all_orders():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT 

            o.order_id,

            o.status,

            o.created_at,

            c.name AS customer_name,

            r.name AS rider_name

        FROM orders o

        JOIN customers c ON o.customer_id = c.customer_id

        LEFT JOIN riders r ON o.rider_id = r.rider_id

        ORDER BY o.created_at DESC

    """)

    rows = cur.fetchall()

    cur.close()

    conn.close()


    orders = []

    for r in rows:

        orders.append({

            "order_id": r[0],

            "status": r[1],

            "created_at": r[2],

            "customer_name": r[3],

            "rider_name": r[4]  # None if not assigned

        })

    return orders


def get_all_products():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""

        SELECT product_id, name, price, stock

        FROM products

        ORDER BY name

    """)

    rows = cur.fetchall()

    cur.close()

    conn.close()


    return [

        {

            "product_id": r[0],

            "name": r[1],

            "price": float(r[2]),

            "stock": r[3]

        }

        for r in rows

    ]


def delete_order(order_id):

    conn = get_connection()

    cur = conn.cursor()


    # IMPORTANT: delete child records first

    cur.execute("DELETE FROM order_items WHERE order_id = %s", (order_id,))

    cur.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))


    conn.commit()

    cur.close()

    conn.close()

def get_rider_orders(rider_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT order_id, status
        FROM orders
        WHERE rider_id = %s
        AND status IN ('Assigned', 'On Delivery')
        ORDER BY created_at
    """, (rider_id,))

    rows = cur.fetchall()
    cur.close()
    conn.close()

    # return list of dicts
    return [
        {"order_id": r[0], "status": r[1]}
        for r in rows
    ]

