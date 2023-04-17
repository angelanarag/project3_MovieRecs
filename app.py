from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/movies')
def get_movies():
    # Establish a connection to the database
    conn = sqlite3.connect('movies.db')

    # Create a cursor object
    c = conn.cursor()

    # Execute a SELECT statement on the movies table
    # We can join the two tables below using the SQL script
    c.execute('SELECT * FROM movies')

    # Fetch all the rows in the result set
    rows = c.fetchall()

    # Convert the results to a list of dictionaries
    result = []
    for row in rows:
        result.append({
            'id': row[0],
            'title': row[1],
            'genre': row[2],
            'language': row[3],
            'release_date': row[4],
            'budget': row[5],
            'revenue': row[6],
            'rating': row[7],
            'vote_count': row[8],
            'director': row[9],
            'dir_gender': row[10],
            'dir_popularity': row[11],
            'certification': row[12],
            'runtime': row[13],
            'movie_popularity': row[14]
        })
        
        # id,title,genre,language,release_date,budget,revenue,rating,vote_count

    # Close the connection
    conn.close()

    # Return the results as JSON
    response=jsonify(result)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)