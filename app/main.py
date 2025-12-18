from flask import (
    Flask, request, jsonify,
    render_template, redirect, session
)


from app.dao import (
    create_order,
    get_all_orders,
    get_order_items,
    update_order_status,
    get_all_riders,
    assign_rider,
    get_all_products,
    delete_order,
    get_rider_orders
)


# ---------------------------
# APP SETUP
# ---------------------------
app = Flask(__name__)
app.secret_key = "super-secret-admin-key"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

print("🔥 SMART DELIVERY API STARTED 🔥")


# ---------------------------
# HOME
# ---------------------------
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to SmartDelivery API</h1><p>Visit /order or /admin</p>"


# ---------------------------
# ORDER PAGE (CUSTOMER)
# ---------------------------
@app.route("/order", methods=["GET"])
def order_page():
    products = get_all_products()
    return render_template("order.html", products=products)


# ---------------------------
# CREATE ORDER (API)
# ---------------------------
@app.route("/orders", methods=["POST"])
def place_order():
    data = request.get_json()

    order_id = create_order(
        data["customer_id"],
        data["items"]
    )

    return jsonify({
        "orderId": order_id,
        "status": "Pending"
    }), 201


# ---------------------------
# GET ORDERS (JSON)
# ---------------------------
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(get_all_orders())


# ---------------------------
# ADMIN DASHBOARD
# ---------------------------
@app.route("/admin")
def admin_dashboard():
    if not session.get("admin_logged_in"):
        return redirect("/login")

    orders = get_all_orders()
    riders = get_all_riders()

    for o in orders:
        o["items"] = get_order_items(o["order_id"])

    return render_template("admin.html", orders=orders, riders=riders)



# ---------------------------
# UPDATE ORDER STATUS (FLOW)
# ---------------------------

# ---------------------------
# ASSIGN RIDER
# ---------------------------
@app.route("/admin/orders/<int:order_id>/assign", methods=["POST"])
def assign_order_rider(order_id):
    rider_id = request.form["rider_id"]
    assign_rider(order_id, rider_id)
    return redirect("/admin")


@app.route("/admin/orders/<int:order_id>/delete", methods=["POST"])
def delete_order_admin(order_id):
    if not session.get("admin_logged_in"):
        return redirect("/login")

    delete_order(order_id)
    return redirect("/admin")

# ---------------------------
# LOGIN
# ---------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (
            request.form["username"] == ADMIN_USERNAME
            and request.form["password"] == ADMIN_PASSWORD
        ):
            session["admin_logged_in"] = True
            return redirect("/admin")

        return render_template(
            "login.html",
            error="Invalid credentials"
        )

    return render_template("login.html")


# ---------------------------
# LOGOUT
# ---------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/track", methods=["GET", "POST"])
def track_order():
    order = None
    items = []

    if request.method == "POST":
        order_id = request.form["order_id"]

        orders = get_all_orders()
        order = next((o for o in orders if str(o["order_id"]) == order_id), None)

        if order:
            items = get_order_items(order["order_id"])

    return render_template("track.html", order=order, items=items)
@app.route("/rider/<int:rider_id>")
def rider_dashboard(rider_id):
    orders = get_rider_orders(rider_id)
    return render_template("rider.html", orders=orders, rider_id=rider_id)

@app.route("/rider/orders/<int:order_id>/start", methods=["POST"])
def rider_start(order_id):
    update_order_status(order_id, "On Delivery")
    return redirect(request.referrer)

@app.route("/rider/orders/<int:order_id>/complete", methods=["POST"])
def rider_complete(order_id):
    update_order_status(order_id, "Completed")
    return redirect(request.referrer)


@app.route("/api/admin/orders")
def api_admin_orders():
    orders = get_all_orders()

    for order in orders:
        order["items"] = get_order_items(order["order_id"])

    return jsonify(orders)

# ---------------------------
# START SERVER
# ---------------------------
if __name__ == "__main__":
    app.run()

