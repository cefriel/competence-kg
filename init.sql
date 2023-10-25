CREATE TABLE employees (
  id VARCHAR(80) PRIMARY KEY,
  name VARCHAR(50),
  surname VARCHAR(50),
  unit VARCHAR(50)
);
CREATE TABLE competences (
  id VARCHAR(80) PRIMARY KEY,
  dimension INT,
  competence TEXT,
  description TEXT
);
CREATE TABLE assignment (
  employee_id VARCHAR(80),
  competence_id VARCHAR(80),
  level VARCHAR(50),
  interest VARCHAR(50),
  PRIMARY KEY (employee_id, competence_id),
  FOREIGN KEY (employee_id) REFERENCES employees(id),
  FOREIGN KEY (competence_id) REFERENCES competences(id)
);

COPY employees (id, name, surname, unit)
FROM '/data/employees.csv' DELIMITER ',' CSV HEADER;
COPY competences (id, dimension, competence, description)
FROM '/data/competences.csv' DELIMITER ',' CSV HEADER;
COPY assignment (employee_id, competence_id, level, interest)
FROM '/data/assignment.csv' DELIMITER ',' CSV HEADER;