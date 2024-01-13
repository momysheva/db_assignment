CREATE TABLE PLATFORM_USER (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    given_name VARCHAR(50),
    surname VARCHAR(50),
    city VARCHAR(100),
    phone_number VARCHAR(20),
    profile_description TEXT,
    password VARCHAR(255) NOT NULL
);
CREATE TYPE caregiving_type_enum AS ENUM ('babysitter', 'caregiver for elderly', 'playmate for children');

CREATE TABLE CAREGIVER (
    caregiver_user_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE,
    photo BYTEA, 
    gender VARCHAR(10),
    caregiving_type caregiving_type_enum,
    hourly_rate DECIMAL(10, 2),
    FOREIGN KEY (caregiver_user_id) REFERENCES PLATFORM_USER(user_id) ON DELETE CASCADE
);

CREATE TABLE FAMILY_MEMBER (
    member_user_id SERIAL PRIMARY KEY,
    user_id INT UNIQUE,
    house_rules TEXT,
    FOREIGN KEY (user_id) REFERENCES PLATFORM_USER(user_id) ON DELETE CASCADE
);

CREATE TABLE ADDRESS (
    member_user_id INT PRIMARY KEY,
    house_number VARCHAR(10),
    street VARCHAR(100),
    town VARCHAR(100),
    FOREIGN KEY (member_user_id) REFERENCES FAMILY_MEMBER(member_user_id) ON DELETE CASCADE
);


CREATE TABLE JOB (
    job_id SERIAL PRIMARY KEY,
    member_user_id INT,
    required_caregiving_type caregiving_type_enum,
    other_requirements TEXT,
    date_posted DATE,
    FOREIGN KEY (member_user_id) REFERENCES FAMILY_MEMBER(member_user_id) ON DELETE CASCADE
);


CREATE TABLE JOB_APPLICATION (
    caregiver_user_id INT,
    job_id INT,
    date_applied DATE,
    PRIMARY KEY (caregiver_user_id, job_id),
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES JOB(job_id) ON DELETE CASCADE
);


CREATE TABLE APPOINTMENT (
    appointment_id SERIAL PRIMARY KEY,
    caregiver_user_id INT,
    member_user_id INT,
    appointment_date DATE,
    appointment_time TIME,
    work_hours INT,
    status VARCHAR(50),
    FOREIGN KEY (caregiver_user_id) REFERENCES CAREGIVER(caregiver_user_id) ON DELETE CASCADE,
    FOREIGN KEY (member_user_id) REFERENCES FAMILY_MEMBER(member_user_id) ON DELETE CASCADE
);

INSERT INTO platform_user(user_id, email, given_name, surname, city, phone_number, profile_description, password)
VALUES
('1', 'bolat.bolatov@gmail.com', 'Bolat', 'Bolatov', 'Almaty', '+77015678234', '25 years old. Seeking a playful and responsible babysitter for my 4-year-old twin boys who love outdoor activities and creative play.', '*bb8745*'),
('2', 'askar.askarov@gmail.com', 'Askar', 'Askarov', 'Astana', '+77759812345', '28 years old. Experienced educator looking for opportunities to provide academic support and tutoring for school-aged children.', 'TeachAbdul789*'),
('3', 'layla.ospanova@gmail.com', 'Layla', 'Ospanova', 'Almaty', '+77271239876', '30 years old. Compassionate caregiver with 5 years of experience in elderly care. Seeking a position to provide companionship and assistance.', 'CompassionLayla*'),
('4', 'daniyar.polat@gmail.com', 'Daniyar', 'Polat', 'Astana', '+77019876567', '26 years old. Looking for a fun and energetic playmate for my 6-year-old daughter who enjoys games, crafts, and outdoor adventures.', 'FunTimeDani*'),
('5', 'zhuldyz.ahmet@gmail.com', 'Zhuldyz', 'Ahmet', 'Astana', '+77751239876', '35 years old. Highly experienced caregiver with a background in child development. Seeking a rewarding role in childcare and early education.', 'ExperiencedZhul123*'),
('6', 'nargiza.maratova@gmail.com', 'Nargiza', 'Maratova', 'Almaty', '+77278876543', '23 years old. Seeking a reliable and trustworthy babysitter for occasional evenings to care for my 2-year-old son.', 'TrustNargiza*'),
('7', 'bakyt.bakytov@gmail.com', 'Bakyt', 'Bakytov', 'Astana', '+77015678901', '29 years old. Looking for a playmate for my 5-year-old daughter who enjoys imaginative play, storytelling, and arts and crafts.', 'PlayWithBakyt*'),
('8', 'ainura.alisher@gmail.com', 'Ainura', 'Alisher', 'Almaty', '+77759823456', '32 years old. Experienced educator passionate about fostering a love for learning in children. Seeking opportunities for tutoring and academic support.', 'LearnAinura789*'),
('9', 'amir.amirov@gmail.com', 'Amir', 'amirov', 'Astana', '+77271234567', '27 years old. Compassionate caregiver with a focus on elderly care. Available for part-time or full-time caregiving positions.', 'CaringAmir2023*'),
('10', 'aigerim.tulegenova@gmail.com', 'Aigerim', 'Tulegenova', 'Almaty', '+77019876543', '24 years old. Seeking a fun and enthusiastic playmate for my 3-year-old son who loves exploring, games, and creative activities.', 'PlayTimeAig*'),
('11', 'serik.serikov@gmail.com', 'Serik', 'Serikov', 'Astana', '+77751234567', '30 years old. Dedicated educator with a background in child psychology. Seeking a role to inspire and support children in their educational journey.', 'InspireSerik123*'),
('12', 'gaukhar.abay@gmail.com', 'Gaukhar', 'Abay', 'Almaty', '+77278856789', '28 years old. Experienced caregiver with a focus on providing compassionate support for the elderly. Open to both short-term and long-term caregiving positions.', 'SupportGaukhar*'),
('13', 'askar.dauletov@gmail.com', 'Askar', 'Dauletov', 'Astana', '+77015678901', '26 years old. Professional with a background in child development and early education. Seeking a challenging and fulfilling role in the field of childcare.', 'ChildProAskar789*'),
('14', 'naina.serik@gmail.com', 'Naina', 'Serik', 'Almaty', '+77759876543', '31 years old. Seeking a playful and engaging babysitter for my 7-year-old daughter who enjoys outdoor sports, games, and creative activities.', 'FunNaina*'),
('15', 'almas.zhaksylyk@gmail.com', 'Almas', 'Zhaksylyk', 'Astana', '+77271239876', '29 years old. Passionate about education with a focus on individualized learning. Seeking opportunities to provide academic support and mentorship for children.', 'TeachAlmas2023*'),
('16', 'aydana.medenova@gmail.com', 'Aydana', 'Medenova', 'Almaty', '+77019876567', '34 years old. Compassionate caregiver with extensive experience in elderly care. Available for part-time caregiving with a focus on companionship and support.', 'CompanionAydana*'),
('17', 'danat.zholdas@gmail.com', 'Danat', 'Zholdas', 'Astana', '+77751239876', '25 years old. Energetic and fun-loving individual seeking a playmate role for my 5-year-old son who enjoys outdoor adventures, games, and storytelling.', 'FunDanat2023*'),
('18', 'ayaz.kuben@gmail.com', 'Ayaz', 'Kuben', 'Almaty', '+77278876543', '27 years old. Experienced educator with a passion for fostering creativity and critical thinking in children. Seeking a role to inspire and engage young minds.', 'InspireAyaz*'),
('19', 'nargiz.momysheva@gmail.com', 'Nargiz', 'Momysheva', 'Astana', '+77015678901', '33 years old. Dedicated caregiver with a focus on elderly care. Available for full-time caregiving positions with a commitment to providing compassionate and personalized support.', 'DedicateNargiz*'),
('20', 'aslan.aslanov@gmail.com', 'Aslan', 'Aslanov', 'Almaty', '+77759823456', '30 years old. Professional with a background in child development and early education. Seeking a challenging and fulfilling role in the field of childcare.', 'ChildProAslan123*'),
('21', 'amina.serikova@gmail.com', 'Amina', 'Serikova', 'Astana', '+77025412396', '35 years old. Seeking a person who can take care of my grandfather.', '*Amina78*'),
('22', 'miras.zhumagulov@gmail.com', 'Miras', 'Zhumagulov', 'Astana', '+77756984123', '29 years old. Have 70 years old grandmother', 'MirasGrand*')
