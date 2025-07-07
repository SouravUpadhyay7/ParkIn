from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from datetime import datetime

app = Flask(__name__)

# PostgreSQL DB connection
conn = psycopg2.connect(
    host="localhost",
    database="db_name",
    user="postgres",
    password="your_own_password"  # change this
)
cur = conn.cursor()

# Total parking slots in ground floor
TOTAL_SLOTS = 10

@app.route('/')
def index():
    # Count bookings
    cur.execute("SELECT COUNT(*) FROM bookings")
    booked_count = cur.fetchone()[0]
    available_slots = TOTAL_SLOTS - booked_count
    return render_template('index.html', available=available_slots, total=TOTAL_SLOTS)

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    car_number = request.form['car_number']
    in_time = datetime.strptime(request.form['in_time'], "%Y-%m-%dT%H:%M")
    out_time = datetime.strptime(request.form['out_time'], "%Y-%m-%dT%H:%M")

    # Check if slots are available
    cur.execute("SELECT COUNT(*) FROM bookings")
    booked_count = cur.fetchone()[0]
    if booked_count >= TOTAL_SLOTS:
        return render_template('index.html', available=0, total=TOTAL_SLOTS, error='No slots available!')

    # Find the next available slot (1 to TOTAL_SLOTS)
    cur.execute("SELECT slot FROM bookings ORDER BY slot")
    booked_slots = [row[0] for row in cur.fetchall()]
    for slot_num in range(1, TOTAL_SLOTS + 1):
        if slot_num not in booked_slots:
            assigned_slot = slot_num
            break

    # Insert booking
    cur.execute(
        "INSERT INTO bookings (name, car_number, in_time, out_time, slot) VALUES (%s, %s, %s, %s, %s)",
        (name, car_number, in_time, out_time, assigned_slot)
    )
    conn.commit()

    # Redirect with details
    return redirect(url_for('success', name=name, car=car_number, checkin=in_time, checkout=out_time, slot=assigned_slot))

@app.route('/success')
def success():
    name = request.args.get('name')
    car = request.args.get('car')
    checkin = request.args.get('checkin')
    checkout = request.args.get('checkout')
    slot = request.args.get('slot')
    return render_template('success.html', name=name, car=car, checkin=checkin, checkout=checkout, slot=slot)

if __name__ == '__main__':
    app.run(debug=True)
