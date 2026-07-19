#REQUIRED STRUCTURES
users = {
    'jperez':   {'password': '1234', 'rol': 'student', 'name': 'Juan Pérez'},
    'dromo':    {'password': '1234', 'rol': 'student', 'name': 'Daniela Romo'},
    'mjuarez':  {'password': '1234', 'rol': 'student', 'name': 'Mauricio Juárez'},
    'mlopez':   {'password': '1234', 'rol': 'student', 'name': 'María López'},
    'euc':      {'password': '1234', 'rol': 'student', 'name': 'Ernesto Uc'},
    'cbalam':   {'password': '1234', 'rol': 'student', 'name': 'Carlos Balam'},
    'jpedrozo': {'password': '1234', 'rol': 'professor', 'name': 'Jorge Pedrozo'},
    'dgamboa':  {'password': '1234', 'rol': 'coordinator', 'name': 'Didier Gamboa'}
}

subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)

notes = {
    'jperez': {
        'Discrete Mathematics': 8.5, 'Programming': 9.2, 'English II': 9.0, 'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3, 'Computer and Server Architecture': 6.8, 'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0, 'Programming': 6.7, 'English II': 9.4, 'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1, 'Computer and Server Architecture': 6.5, 'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5, 'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8, 'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2, 'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6, 'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8, 'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4, 'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5, 'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9, 'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

#LOGIN
logged_in = False

while not logged_in:
    username = input('User: ')
    password = input('Password: ')
    
    if username in users and users[username]['password'] == password:
        logged_in = True
        print('Bienvenid@,', users[username]['name'], f'({users[username]['rol']})')
        print('==========================================')
    else:
        print('Invalid username or password. Try again.')
#ROLE
user_role = users[username]['rol']

if user_role =='student':
    print('School Report\n')
    
    approved = set()
    pending = set()
    
    for subject in subjects:
        grade = notes[username][subject]
        print(subject, ':', grade)
        
        if grade >= 8.0:
            approved.add(subject)
        else:
            pending.add(subject)
            
    print('Approved:', approved)
    print('Pending:', pending)
# 2. Proffesor menu
elif user_role == 'professor':
    print("Students")
    for u_id in users:
        if users[u_id]['rol'] =='student':
            print("User:", u_id, "| Student:", users[u_id]['name'])
    print()
    
    # ask which student to grade
    username_to_grade = input("Student to grade (username): ")
    
    # verify if students exist in the records
    if username_to_grade in notes:
        # ask subject name
        subject_to_grade = input("Subject to grade: ")
        
        # check if subject is valid
        if subject_to_grade in subjects:
            new_grade = float(input("New grade: "))
            old_grade = notes[username_to_grade][subject_to_grade]
            
            # ask for confirmation
            print("Do you confirm (yes/no)?")
            confirm = input(f" {subject_to_grade}: {old_grade} ==> {new_grade}\n")
            
            if confirm == 'yes':
                # update the grade directly inside the dictionary
                notes[username_to_grade][subject_to_grade] = new_grade
                print("Grade updated!")
                print(notes[username_to_grade])
            else:
                print("Cancelled.")
        else:
            print("Invalid subject")
    else:
        print("Invalid student")
        
#Coordinator menu
elif user_role == 'coordinator':
    print("Professors")
    # loop
    for u_id in users:
        if users[u_id]['rol'] == 'professor':
            print("User:", u_id, "| Professor:", users[u_id]['name'])
            
    print("\nStudents")
    
    for u_id in users:
        if users[u_id]['rol'] == 'student':
            print("User:", u_id, "| Student:", users[u_id]['name'])
            
    print("\nRecords\n")
    
    for u_id in notes:
        print("Grades for", users[u_id]['name'], ":")
        print(notes[u_id])
        print("--------------------")