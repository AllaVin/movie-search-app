from db_connection import execute_query

# Search for movies by a keyword in the title or description
def search_movies_by_keyword(keyword):
    # SQL query to find movies where the title or description contains the keyword
    query = f"""
    SELECT title, release_year, description
    FROM film
    WHERE title LIKE '%{keyword}%' OR description LIKE '%{keyword}%'
    LIMIT 10;
    """
    # Execute the query, fetching results from the 'sakila' database (use_app_db=False)
    return execute_query(query, use_app_db=False, fetch=True)

# Search for movies by a specific genre and release year
def search_movies_by_genre_and_year(genre, year):
    # SQL query to join 'film', 'film_category', and 'category' tables
    # and filter by selected genre and year
    query = f"""
    SELECT f.title, f.release_year, f.description
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = '{genre}' AND f.release_year = {year}
    LIMIT 10;
    """
    # Execute the query, fetching results from the 'sakila' database
    return execute_query(query, use_app_db=False, fetch=True)

# Save a user's search query into the search_logs table
def save_search_query(search_type, search_text):
    # SQL query to insert a new search log or update the count if the entry already exists
    query = f"""
    INSERT INTO search_logs (search_type, search_text)
    VALUES ('{search_type}', '{search_text}')
    ON DUPLICATE KEY UPDATE search_count = search_count + 1;
    """
    # Execute the query, committing changes to the application database (use_app_db=True)
    execute_query(query, use_app_db=True, commit=True)

# Retrieve the most popular search queries based on their search count
def get_popular_queries():
    # SQL query to select top 10 most frequent search logs
    query = """
    SELECT search_type, search_text, search_count
    FROM search_logs
    ORDER BY search_count DESC
    LIMIT 10;
    """
    # Execute the query, fetching results from the application database
    return execute_query(query, use_app_db=True, fetch=True)

# Get the list of all available movie genres
def get_valid_categories():
    # SQL query to retrieve genre names from the 'category' table
    query = f"""
    SELECT name 
    FROM category 
    ORDER BY name ASC;
    """
    # Execute the query, fetching results from the 'sakila' database
    return execute_query(query, use_app_db=False, fetch=True)
    return [category[0] for category in categories]