import pymysql
from db import get_db_connection
from ai_agents import assessment_agent

def test_assessment_agent():
    """Test the assessment agent for employee ID 1"""
    print("Testing Assessment Agent for Employee ID 1")
    print("=" * 50)
    
    # Test the assessment agent
    result = assessment_agent(1)
    
    print("Assessment Agent Result:")
    print(f"Summary: {result.get('summary', 'N/A')}")
    print(f"Error: {result.get('error', 'None')}")
    
    if 'recent_assessments' in result:
        print(f"\nRecent Assessments ({len(result['recent_assessments'])}):")
        for i, assessment in enumerate(result['recent_assessments'], 1):
            print(f"  {i}. Course: {assessment['course_name']}")
            print(f"     Marks: {assessment['marks_obtained']}")
            print(f"     Date: {assessment.get('attempt_date', 'N/A')}")
            print()
    
    if 'completed_courses' in result:
        print(f"Completed Courses ({len(result['completed_courses'])}):")
        for course in result['completed_courses']:
            print(f"  - {course}")
    
    # Also check the database directly
    print("\n" + "=" * 50)
    print("Direct Database Query:")
    
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT course_name, marks_obtained, attempt_date, assessment_id
                FROM assessment_marks 
                WHERE emp_id = 1 
                ORDER BY assessment_id DESC 
                LIMIT 5
            """)
            assessments = cursor.fetchall()
            
            print(f"Found {len(assessments)} assessment records:")
            for assessment in assessments:
                print(f"  ID: {assessment['assessment_id']}, Course: {assessment['course_name']}, Marks: {assessment['marks_obtained']}, Date: {assessment['attempt_date']}")
                
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if conn and conn.open:
            conn.close()

if __name__ == "__main__":
    test_assessment_agent()
