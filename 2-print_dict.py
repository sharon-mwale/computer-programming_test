from bs4 import BeautifulSoup

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
    	<td>B</td>
	</tr>
</table>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the table element
table = soup.find('table', class_='grades')

# Create an empty dictionary to store the student data
student_grades = {}

# Extract the student names and their corresponding grades
rows = table.find_all('tr')
for row in rows[1:]:  # Exclude the header row
    cells = row.find_all('td')
    student = cells[0].text
    grade = cells[1].text
    student_grades[student] = grade

# Print the dictionary of student grades
print(student_grades)
