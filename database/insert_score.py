from database.db_connection import conn

def insert_score(
        candidate_name,
        job_title,
        ats_score,
        matched_skills,
        missing_skills):

    cursor = conn.cursor()

    query = """
    INSERT INTO candidate_scores
    (
        candidate_name,
        job_title,
        ats_score,
        matched_skills,
        missing_skills
    )
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            candidate_name,
            job_title,
            ats_score,
            ",".join(matched_skills),
            ",".join(missing_skills)
        )
    )

    conn.commit()

    print("Score Saved Successfully!")