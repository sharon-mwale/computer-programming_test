from bs4 import BeautifulSoup

def get_highest_grade(table):
    # Create an empty dictionary to store the student data
    student_grades = {}

    # Extract the student names and their corresponding grades
    rows = table.find_all('tr')
    for row in rows[1:]:  # Exclude the header row
        cells = row.find_all('td')
        student = cells[0].text
        grade = cells[1].text
        student_grades[student] = grade

    # Find the student with the highest grade
    highest_grade = max(student_grades.values())
    highest_student = [student for student, grade in student_grades.items() if grade == highest_grade][0]

    return highest_student, highest_grade

# HTML structure of the table
html = '''
<table class="grades">
	<tr>
    	<th>Student</th>
    	<th>Grade</th>
	</tr>
	<tr>
    	<td>John</td>
    	<td>A</td>
	</tr>
	<tr>
    	<td>Jane</td>
    	<td>A</td>
	</tr>
</table>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the table element
table = soup.find('table', class_='grades')

# Call the get_highest_grade function
result = get_highest_grade(table)

# Print the student with the highest grade
print(f"Highest grade: {result[0]} for student: {result[1]}")
