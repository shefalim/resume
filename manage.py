from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    skip = Professor(name='Clinton White', department='Accounting & MIS')
    sharma = Professor(name='Pratyush Nidhi Sharma', department='Accounting & MIS')
    bambach = Professor(name='Mark Bambach', department='Business Administration')
    anu = Professor(name='Anu Sivvaraman', department='Business Administration')
    course1 = Course(course_number= 'MISY430', title='Systems Analysis', description='Covers the challenges of developing and managing systems analysis and design projects. Students learn to determine systems requirements, analyze systems problems, model potential solutions and design and implement these solutions. Other current topics will be included to reflect the changing information systems environment')
    course2 = Course(course_number='MISY 330', title='Database Design & Implementation', description='Covers the design and implementation of enterprise databases in the business environment. A networked setting and its effect on database management will be emphasized')
    course3 = Course(course_number='BUAD 301', title='Introduction to Marketing', description='Management of the marketing functions, marketing research, product planning, distribution channels, pricing, personal selling, and advertising. Emphasis on consumer and industrial markets')
    course4 = Course(course_number='MISY 302', title='Market Research', description='Focuses on the marketing research process as an aid in marketing decision making. Defining marketing problems, identifying marketing information needs, developing methods to gather information, and applying research results to marketing problems')
    db.session.add(skip)
    db.session.add(sharma)
    db.session.add(bambach)
    db.session.add(anu)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
