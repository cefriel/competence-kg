
Other employees having same competences
MATCH (e:Employee {name:"Jane", surname:"Taylor"})-[:HAS_COMPETENCE]->(c:Competence)<-[:HAS_COMPETENCE]-(oe:Employee) RETURN c.competence, collect(oe.employeeId)

More "similar" employees
MATCH (e:Employee {name:"Jane", surname:"Taylor"})-[:HAS_COMPETENCE]->(c:Competence)<-[:HAS_COMPETENCE]-(oe:Employee) RETURN oe.employeeId, count(c) as num ORDER BY num DESC

docker exec -it corso-kg-postgres psql -U postgres corso-kg-postgres

WITH jane_competences AS (
  SELECT competence_id
  FROM employees
  JOIN assignment ON employees.id = assignment.employee_id
  WHERE employees.name = 'Jane' AND employees.surname = 'Taylor'
)
SELECT employees.id, employees.name, employees.surname, COUNT(assignment.competence_id) AS num_competences
FROM employees
JOIN assignment ON employees.id = assignment.employee_id
WHERE assignment.competence_id IN (SELECT competence_id FROM jane_competences) AND NOT(employees.name = 'Jane' AND employees.surname = 'Taylor')
GROUP BY employees.id, employees.name, employees.surname
ORDER BY num_competences DESC;