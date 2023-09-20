from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Function to fetch data from the database
def get_data_from_database():
    con = pymysql.connect(host="_", user="_", password="_", database= "_")
    cursor = con.cursor()
    
    # Execute an SQL query to fetch data (replace with your query)
    cursor.execute("SELECT * FROM patients")
    
    # Fetch all rows from the query result
    data = cursor.fetchall()
    
    con.close()
    return data

@app.route('/')
def display_data():
    data = get_data_from_database()
    return render_template('doctor.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
