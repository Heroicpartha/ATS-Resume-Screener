from database.db_connection import conn

def get_job(job_id):

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT job_title,
               required_skills
        FROM jobs
        WHERE job_id = %s
        """,
        (job_id,)
    )

    result = cursor.fetchone()

    return result