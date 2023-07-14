CREATE TABLE employees (
  id TEXT PRIMARY KEY,
  name TEXT,
  surname TEXT,
  unit TEXT
);
CREATE TABLE competences (
  id TEXT PRIMARY KEY,
  dimension TEXT,
  competence TEXT,
  description TEXT
);
CREATE TABLE assignment (
  employee_id TEXT,
  competence_id TEXT,
  level TEXT,
  interest TEXT,
  FOREIGN KEY (employee_id) REFERENCES employees(id),
  FOREIGN KEY (competence_id) REFERENCES competences(id)
);

COPY employees (id, name, surname, unit)
FROM '/data/employees.csv' DELIMITER ',' CSV HEADER;
COPY competences (id, dimension, competence, description)
FROM '/data/competences.csv' DELIMITER ',' CSV HEADER;
COPY assignment (employee_id, competence_id, level, interest)
FROM '/data/assignment.csv' DELIMITER ',' CSV HEADER;