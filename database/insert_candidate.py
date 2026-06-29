from database.db_connection import conn

def insert_candidate(name, email, phone, resume_text):

    try:
        cursor = conn.cursor()

        query = """
        INSERT INTO candidates
        (name, email, phone, resume_text)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (name, email, phone, resume_text)
        )

        conn.commit()

        print("Candidate Inserted Successfully!")

    except Exception as e:
        print("Error:", e)