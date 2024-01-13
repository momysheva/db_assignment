from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey,LargeBinary,Float,Enum, Date, DateTime, Boolean,TIMESTAMP, MetaData,  and_
from decimal import Decimal
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import date, time, datetime
from sqlalchemy.orm import joinedload, aliased
from sqlalchemy import func
from sqlalchemy.sql.expression import true


Base = declarative_base()
db_url = 'postgresql://postgres:202078586@localhost/assignment2'
engine = create_engine(db_url)

class PlatformUser(Base):
    __tablename__ = 'platform_user'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    given_name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    city = Column(String(50))
    phone_number = Column(String(15))
    profile_description = Column(Text)
    password = Column(String(255), nullable=False)
    caregivers = relationship("Caregiver", uselist=False, back_populates="user")
    family_member = relationship("FamilyMember", uselist=False, back_populates="user")


class Caregiver(Base):
    __tablename__ = 'caregiver'
    caregiver_user_id = Column(Integer, ForeignKey('platform_user.user_id', ondelete='CASCADE'),primary_key=True)
    photo = Column(LargeBinary)
    gender = Column(String(10))
    caregiving_type = Column(Enum('babysitter', 'caregiver for elderly', 'playmate for children', name='caregiving_type_enum'))
    hourly_rate = Column(Float(10, 2))
    user = relationship("PlatformUser", back_populates="caregivers")
    Job_application=relationship("Job_application")
    appoitments=relationship("Appointment")


class FamilyMember(Base):
    __tablename__ = 'family_member'
    member_user_id = Column(Integer, ForeignKey('platform_user.user_id', ondelete='CASCADE'),primary_key=True)
    house_rules = Column(Text)
    user = relationship('PlatformUser', back_populates='family_member')
    address = relationship("Address", uselist=False, back_populates="family_member")
    jobs = relationship("Job")
    appoitments=relationship("Appointment")


class Address(Base):
    __tablename__ = 'address'
    member_user_id = Column(Integer, ForeignKey('family_member.member_user_id', ondelete='CASCADE'), primary_key=True)
    house_number = Column(String(20), primary_key=True)
    street = Column(String(100))
    town = Column(String(50))
    family_member = relationship("FamilyMember", back_populates="address")

class Job(Base):
    __tablename__ = 'job'
    job_id = Column(Integer, primary_key=True)
    member_user_id = Column(Integer, ForeignKey('family_member.member_user_id',ondelete='CASCADE' ))
    required_caregiving_type = Column(Enum('babysitter', 'caregiver for elderly', 'playmate for children', name='caregiving_type_enum'))
    other_requirements = Column(Text)
    date_posted = Column(Date)
    Job_application=relationship("Job_application")


class Job_application(Base):
    __tablename__ = 'job_application'
    caregiver_user_id = Column(Integer, ForeignKey('caregiver.caregiver_user_id', ondelete='CASCADE'), primary_key=True)
    job_id = Column(Integer, ForeignKey('job.job_id', ondelete='CASCADE'), primary_key=True)
    date_applied = Column(Date)


class Appointment(Base):
    __tablename__ = 'appointment'
    appointment_id = Column(Integer, primary_key=True)
    caregiver_user_id = Column(Integer, ForeignKey('caregiver.caregiver_user_id', ondelete='CASCADE'))
    member_user_id = Column(Integer, ForeignKey('family_member.member_user_id', ondelete='CASCADE'))
    appointment_date = Column(Date)
    appointment_time = Column(TIMESTAMP)
    work_hours = Column(Integer)
    status = Column(Boolean)

session = Session(engine)

insert_caregivers = [
    {'caregiver_user_id': 2, 'photo': open('man-avatar-profile-vector-21372065.jpg', 'rb').read(), 'gender': 'Male', 'caregiving_type': 'playmate for children', 'hourly_rate': 7.50},
    {'caregiver_user_id': 3, 'photo': open('woman-avatar-profile-vector-21372074.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'caregiver for elderly', 'hourly_rate': 20.00},
    {'caregiver_user_id': 5, 'photo': open('woman-avatar-profile-vector-21372074.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'babysitter', 'hourly_rate': 25.00},
    {'caregiver_user_id': 8, 'photo': open('woman-avatar-profile-vector-21372074.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'babysitter', 'hourly_rate': 15.00},
    {'caregiver_user_id': 9, 'photo': open('man-avatar-profile-vector-21372065.jpg', 'rb').read(), 'gender': 'Male', 'caregiving_type': 'caregiver for elderly', 'hourly_rate': 8.00},
    {'caregiver_user_id': 11, 'photo': open('man-avatar-profile-vector-21372065.jpg', 'rb').read(), 'gender': 'Male', 'caregiving_type': 'babysitter', 'hourly_rate': 8.00},
    {'caregiver_user_id': 12, 'photo': open('young-and-elegant-woman-avatar-profile-vector-9685441.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'caregiver for elderly', 'hourly_rate': 21.00},
    {'caregiver_user_id': 13, 'photo': open('man-avatar-profile-vector-21372065.jpg', 'rb').read(), 'gender': 'Male', 'caregiving_type': 'playmate for children', 'hourly_rate': 18.00},
    {'caregiver_user_id': 16, 'photo': open('young-and-elegant-woman-avatar-profile-vector-9685441.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'caregiver for elderly', 'hourly_rate': 11.50},
    {'caregiver_user_id': 18, 'photo': open('young-and-elegant-woman-avatar-profile-vector-9685441.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'babysitter', 'hourly_rate': 6.50},
    {'caregiver_user_id': 19, 'photo': open('young-and-elegant-woman-avatar-profile-vector-9685441.jpg', 'rb').read(), 'gender': 'Female', 'caregiving_type': 'playmate for children', 'hourly_rate': 10.00},
    {'caregiver_user_id': 20, 'photo': open('man-avatar-profile-vector-21372065.jpg', 'rb').read(), 'gender': 'Male', 'caregiving_type': 'playmate for children', 'hourly_rate': 19.00}
]

for caregiver_data in insert_caregivers:
    new_caregiver = Caregiver(**caregiver_data)
    session.add(new_caregiver)

session.commit()

insert_members=[
    {'member_user_id':1, 'house_rules': 'No pets'},
    {'member_user_id':4, 'house_rules': 'No smoking'},
    {'member_user_id':6, 'house_rules': 'Clean after yourself'},
    {'member_user_id':7, 'house_rules': 'Should pay attention to hygiene'},
    {'member_user_id':10, 'house_rules': 'No guests'},
    {'member_user_id':14, 'house_rules': 'No pets'},
    {'member_user_id':15, 'house_rules': 'Turn off lights and appliances when not in use'},
    {'member_user_id':17, 'house_rules': 'No loud music'},
    {'member_user_id':21, 'house_rules': 'No pets'},
    {'member_user_id':22, 'house_rules': 'No pets'}
]

for member_data in insert_members:
    new_member = FamilyMember(**member_data)
    session.add(new_member)
session.commit()


insert_address=[
    {'member_user_id':1, 'house_number':'45','street':'Panfilov ','town':'Almaty'},
    {'member_user_id':4, 'house_number':'7','street':'Turkistan','town':'Astana'},
    {'member_user_id':6, 'house_number':'12','street':'Panfilov','town':'Almaty'},
    {'member_user_id':7, 'house_number':'63','street':'Turan','town':'Astana'},
    {'member_user_id':10, 'house_number':'64','street':'Panfilov','town':'Almaty'},
    {'member_user_id':14, 'house_number':'72','street':' Almaty','town':'Astana'},
    {'member_user_id':15, 'house_number':'93','street':'Turkistan','town':'Astana'},
    {'member_user_id':17, 'house_number':'25','street':'Turan','town':'Astana'},
    {'member_user_id':21, 'house_number':'48','street':'Almaty','town':'Astana'},
    {'member_user_id':22, 'house_number':'2','street':'Kabanbay batyr','town':'Astana'}

]

for address_data in insert_address:
    new_address = Address(**address_data)
    session.add(new_address)
session.commit()

job_insertion=[
    {'job_id':1021,'member_user_id':1,'required_caregiving_type':'playmate for children','other_requirements':'preferred time intervals 12:00-15:00','date_posted':date(2023, 1, 15)},
    {'job_id':1022,'member_user_id':4,'required_caregiving_type':'playmate for children','other_requirements':'be gentle','date_posted':date(2022, 12, 15)},
    {'job_id':1023,'member_user_id':6,'required_caregiving_type':'caregiver for elderly','other_requirements':'preferred time intervals 09:00-12:00','date_posted':date(2023, 3, 27)},
    {'job_id':1024,'member_user_id':7,'required_caregiving_type':'babysitter','other_requirements':'preferred time intervals 09:00-16:00 daily','date_posted':date(2023, 2, 14)},
    {'job_id':1025,'member_user_id':10,'required_caregiving_type':'playmate for children','other_requirements':'younger 30 years, weekly','date_posted':date(2023, 8, 20)},
    {'job_id':1026,'member_user_id':14,'required_caregiving_type':'caregiver for elderly','other_requirements':'experience 5 years','date_posted':date(2023, 3, 27)},
    {'job_id':1027,'member_user_id':15,'required_caregiving_type':'babysitter','other_requirements':'Older than 20 yers. Weekly','date_posted':date(2021, 2, 14)},
    {'job_id':1028,'member_user_id':17,'required_caregiving_type':'playmate for children','other_requirements':'preferred time intervals 09:00-18:00','date_posted':date(2023, 8, 20)},
    {'job_id':1029,'member_user_id':21,'required_caregiving_type':'caregiver for elderly','other_requirements':'preferred time intervals 10:00-12:00 weekly. Have gentle service','date_posted':date(2023, 11, 1)},
    {'job_id':1030,'member_user_id':22,'required_caregiving_type':'caregiver for elderly','other_requirements':'preferred time intervals 14:00-18:00 daily','date_posted':date(2023, 11, 10)}
]

for job_data in job_insertion:
    new_job = Job(**job_data)
    session.add(new_job)

session.commit()

insert_applications = [
    {'caregiver_user_id': 2, 'job_id':1021, 'date_applied':date(2023, 1, 16)},
     {'caregiver_user_id': 2, 'job_id':1028 , 'date_applied':date(2023, 8, 25)},
    {'caregiver_user_id': 3, 'job_id': 1026, 'date_applied':date(2023, 3, 29)},
    {'caregiver_user_id': 5, 'job_id': 1024, 'date_applied': date(2023, 2, 14)},
    {'caregiver_user_id': 8, 'job_id': 1024, 'date_applied':date(2023, 2, 15)},
    {'caregiver_user_id': 9, 'job_id':1023, 'date_applied':date(2023, 1, 15)},
    {'caregiver_user_id': 11, 'job_id':1027, 'date_applied':date(2023, 1, 15)},
    {'caregiver_user_id': 12, 'job_id': 1023, 'date_applied':date(2023, 3, 29)},
    {'caregiver_user_id': 13, 'job_id': 1025, 'date_applied': date(2023, 8, 22)},    
    {'caregiver_user_id': 16, 'job_id':1026, 'date_applied':date(2023, 3, 30)},
    {'caregiver_user_id': 18, 'job_id':1027, 'date_applied':date(2021, 2, 21)},
    {'caregiver_user_id': 19, 'job_id': 1021, 'date_applied':date(2023, 1, 18)},
    {'caregiver_user_id': 20, 'job_id':1022, 'date_applied':date(2022, 12, 17)},
    {'caregiver_user_id': 3, 'job_id':1029, 'date_applied':date(2023, 11, 2)},
    {'caregiver_user_id': 12, 'job_id':1029, 'date_applied':date(2023, 11, 3)},
    {'caregiver_user_id': 9, 'job_id':1030, 'date_applied':date(2023, 11, 15)}
]

for application_data in insert_applications:
    new_application = Job_application(**application_data)
    session.add(new_application)

session.commit()


insert_appointments = [
    {'appointment_id': 2021, 'caregiver_user_id': 2, 'member_user_id': 1, 'appointment_date': date(2023, 1, 19), 'appointment_time': datetime.combine(date(2023, 1, 19), time(12, 30)), 'work_hours': 5, 'status': True},
    {'appointment_id': 2022, 'caregiver_user_id': 2, 'member_user_id': 17, 'appointment_date': date(2023, 8, 28), 'appointment_time': datetime.combine(date(2023, 8, 28), time(13, 30)), 'work_hours': 6, 'status': False},
    {'appointment_id': 2023, 'caregiver_user_id': 3, 'member_user_id': 14, 'appointment_date': date(2023, 3, 30), 'appointment_time': datetime.combine(date(2023, 3, 30),time(11, 00)), 'work_hours': 4, 'status': False},
    {'appointment_id': 2024, 'caregiver_user_id': 5, 'member_user_id': 7, 'appointment_date': date(2023, 2, 15), 'appointment_time':  datetime.combine(date(2023, 2, 15),time(15, 30)), 'work_hours': 5, 'status': True},
    {'appointment_id': 2025, 'caregiver_user_id': 8, 'member_user_id': 7, 'appointment_date': date(2023, 2, 16), 'appointment_time':  datetime.combine(date(2023, 2, 16),time(16, 00)), 'work_hours': 2, 'status': False},
    {'appointment_id': 2026, 'caregiver_user_id': 9, 'member_user_id':6, 'appointment_date': date(2023, 2, 18), 'appointment_time':  datetime.combine(date(2023, 1, 15),time(14, 30)), 'work_hours': 10, 'status': True},
    {'appointment_id': 2027, 'caregiver_user_id': 11, 'member_user_id': 15, 'appointment_date': date(2023, 1, 15), 'appointment_time': datetime.combine(date(2023, 1, 15),time(12, 30)), 'work_hours': 8, 'status': True},
    {'appointment_id': 2028, 'caregiver_user_id': 12, 'member_user_id': 6, 'appointment_date': date(2023, 3, 30), 'appointment_time':  datetime.combine(date(2023, 3, 30), time(15, 00)), 'work_hours': 3, 'status': False},
    {'appointment_id': 2029, 'caregiver_user_id': 13, 'member_user_id': 10, 'appointment_date': date(2023, 8, 25), 'appointment_time':  datetime.combine(date(2023, 8, 25),time(10, 00)), 'work_hours': 5, 'status': True},
    {'appointment_id': 2030, 'caregiver_user_id': 16, 'member_user_id': 14, 'appointment_date': date(2023, 4, 1), 'appointment_time':  datetime.combine(date(2023, 4, 1), time(11, 30)), 'work_hours': 4, 'status': True},
    {'appointment_id': 2031, 'caregiver_user_id': 18, 'member_user_id': 15, 'appointment_date': date(2021, 2, 21), 'appointment_time': datetime.combine(date(2021, 2, 21), time(17, 30) ), 'work_hours': 7, 'status': False},
    {'appointment_id': 2032, 'caregiver_user_id': 19, 'member_user_id': 1, 'appointment_date': date(2023, 1, 20), 'appointment_time':  datetime.combine(date(2023, 1, 20), time(18, 30)), 'work_hours': 2, 'status': False},
    {'appointment_id': 2033, 'caregiver_user_id': 20, 'member_user_id': 4, 'appointment_date': date(2022, 12, 19), 'appointment_time': datetime.combine(date(2022, 12, 19),time(15, 00)), 'work_hours': 4, 'status': True},
    {'appointment_id': 2034, 'caregiver_user_id': 3, 'member_user_id': 21, 'appointment_date': date(2023, 11, 19), 'appointment_time': datetime.combine(date(2023, 11, 3),time(11, 00)), 'work_hours': 5, 'status': False},
    {'appointment_id': 2035, 'caregiver_user_id': 9, 'member_user_id': 21, 'appointment_date': date(2022, 12, 19), 'appointment_time': datetime.combine(date(2023, 11, 3),time(14, 00)), 'work_hours': 6, 'status': True},
     {'appointment_id': 2036, 'caregiver_user_id': 12, 'member_user_id': 22, 'appointment_date': date(2022, 12, 19), 'appointment_time': datetime.combine(date(2023, 11, 16),time(12, 00)), 'work_hours': 3, 'status': False}

]

for appointment_data in insert_appointments:
    new_appointment = Appointment(**appointment_data)
    session.add(new_appointment)

session.commit()

3.1
user_to_update = session.query(PlatformUser).filter_by(given_name='Askar',surname='Askarov' )
if user_to_update:
    user_to_update.phone_number = '+77771010001'
    session.commit()


3.2
caregivers = session.query(Caregiver).all()
for caregiver in caregivers:
    if caregiver.hourly_rate< 9.00:
        caregiver.hourly_rate += Decimal('0.50')
    else:
        caregiver.hourly_rate= caregiver.hourly_rate*Decimal('1.1')

session.commit()

#4.1
subquery = session.query(PlatformUser.user_id).filter(and_(PlatformUser.given_name == 'Bolat', PlatformUser.surname == 'Bolatov'))
session.query(Job).filter(Job.member_user_id.in_(subquery)).delete(synchronize_session=False)
session.commit()

# #4.2
subquery = session.query(Address.member_user_id).filter(Address.street == 'Turan')
session.query(FamilyMember).filter(FamilyMember.member_user_id.in_(subquery)).delete(synchronize_session=False)
session.commit()

#5.1
query = (
    session.query(PlatformUser.given_name)
    .filter(PlatformUser.user_id.in_(
        session.query(Appointment.caregiver_user_id)
        .filter(Appointment.status == 'true')  
    ))
    .all()
)

for row in query:
    print(row)

#5.2
query = session.query(Job.job_id).filter(Job.other_requirements.like('%gentle%'))

result = query.all()
print(result)


job_applications_query = (
    session.query(Job_application, PlatformUser)
    .join(PlatformUser, Job_application.caregiver_user_id == PlatformUser.user_id)
    .all()
)

#5.3
query = session.query(Appointment.work_hours).join(Caregiver).filter(Caregiver.caregiving_type=='babysitter')

result = query.all()
print(result)

#5.4
query = (
    session.query(FamilyMember)
    .join(Address)
    .filter(FamilyMember.jobs.any(Job.required_caregiving_type == 'caregiver for elderly'))
    .filter(Address.town == 'Astana')
    .filter(FamilyMember.house_rules.like('%No pets%'))
)

result = query.all()
for family_member in result:
    print(f"Member User ID: {family_member.member_user_id}")
    print(f"Given Name: {family_member.user.given_name}")
    print(f"Surname: {family_member.user.surname}")
    print(f"House Rules: {family_member.house_rules}")

#6.1
query = (
    session.query(
        FamilyMember.member_user_id,
        Job.job_id,
        func.count(Job_application.caregiver_user_id).label("applicant_count")
    )
    .join(Job, FamilyMember.member_user_id == Job.member_user_id)
    .outerjoin(Job_application, Job.job_id == Job_application.job_id)
    .group_by(FamilyMember.member_user_id, Job.job_id)
)
results = query.all()
for result in results:
    print(f"Member User ID: {result.member_user_id}, Job ID: {result.job_id}, Applicant Count: {result.applicant_count}")

#6.2
query = (
    session.query(
        func.sum(Appointment.work_hours).label("total_hours")
    )
    .join(Caregiver, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
    .filter(Appointment.status=='true') 
)

result = query.scalar()
print(f"Total Hours Spent by Caregivers for Accepted Appointments: {result}")

#6.3
average_pay_query = (
    session.query(func.avg(Caregiver.hourly_rate))
    .join(Appointment, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
    .filter(Appointment.status == 'true')
)

print(f"Average pay of caregivers based on accepted appointments: {average_pay_query.scalar()}")

#6.4
above_average_pay_query = (
    session.query(Caregiver)
    .join(Appointment, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
    .filter(and_(Appointment.status == 'true', Caregiver.hourly_rate > average_pay_query.scalar()))
)

for c in above_average_pay_query:
    print(f"{c.user.given_name} {c.user.surname} is paid above average pay")

#7
total_cost_query = (
    session.query(func.sum(Caregiver.hourly_rate * Appointment.work_hours).label('total_cost'))
    .join(Appointment, Appointment.caregiver_user_id == Caregiver.caregiver_user_id)
    .filter(Appointment.status == 'true')
)

print(f"Total cost to pay for caregivers for all accepted appointments: {total_cost_query.scalar()}")

#8
job_applications_query = (
    session.query(Job_application, PlatformUser)
    .join(PlatformUser, Job_application.caregiver_user_id == PlatformUser.user_id)
    .all()
)

for job_application, applicant in job_applications_query:
    print(f"Job Application ID: {job_application.caregiver_user_id}")
    print(f"Job Title: {job_application.job_id}")
    print(f"Applicant: {applicant.given_name} {applicant.surname}")
    print("\n")

session.close()