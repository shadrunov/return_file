from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.students', 
          'https://www.googleapis.com/auth/classroom.courses.readonly']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('classroom', 'v1', credentials=creds)


def get_courses(service, name):  # course_id
    # Call the Classroom API
    results = service.courses().list(teacherId = "onlineeducation@miem.hse.ru").execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
        return 404
    else:
        for course in courses:
            print(course['id'], course['name'])
            if course['name'] == name:
                id = course['id']
                return id
        return 404


def create_coursework(course_id, name, service=service):
    """ Creates a coursework. """
    coursework = {
        'title': name,
        'description': '',
        'materials': [],
        'maxPoints': 100,
        'workType': 'ASSIGNMENT',
        'state': 'DRAFT',
    }
    coursework = service.courses().courseWork().create(
        courseId=course_id, body=coursework).execute()
    print('Assignment created with ID {%s}' % coursework.get('id'))

print("Вы хотите создать новое задание")
x = 404
while x == 404:
    print("Введите название курса: ")
    c = input()
    x = get_courses(service, c)
    if x == 404:
        print("Не найден такой курс! ")
    else:
        print("id курса: ", x)

print(f"Введите название задания в курсе {c}: ")
c = input()
create_coursework(course_id=x, name=c)

input("Press any key to continue...")