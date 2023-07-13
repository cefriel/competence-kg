# tag::import[]
# Import the neo4j dependency
from neo4j import GraphDatabase
# end::import[]


uri = "neo4j://corso-kg-neo4j:7687"

"""
Example Authentication token.
You can pass the username and password as a tuple.
"""
username = 'neo4j'
password = 'kgCefriel'

# tag::auth[]
auth = (username, password)
# end::auth[]

# tag::driver[]
# Create a new Driver instance
driver = GraphDatabase.driver(uri,auth=auth)
# end::driver[]

# tag::verifyConnectivity[]
# Verify the connection details
driver.verify_connectivity()
# end::verifyConnectivity[]

from os import listdir
from os.path import abspath, basename, isfile, join, dirname

local_folder = dirname(abspath(__file__))
import_path = join(local_folder, "data")

# tag::driver.session[]
with driver.session() as session:
# end::driver.session[]

    def create_constraint_competences(tx):
        return tx.run("""
            CREATE CONSTRAINT CompetenceId IF NOT EXISTS ON (c:Competence) ASSERT c.competenceId IS UNIQUE
            """)
    def create_constraint_users(tx):
        return tx.run("""
            CREATE CONSTRAINT EmployeeId IF NOT EXISTS ON (e:Employee) ASSERT e.employeeId IS UNIQUE
            """)
    print("Create constraints")
    session.execute_write(create_constraint_competences)
    session.execute_write(create_constraint_users)

    def create_competences(tx):
        return tx.run("""
            LOAD CSV WITH HEADERS
            FROM "file:///competences.csv"
            AS row
            MERGE (c:Competence {competenceId: row.id})
            ON CREATE SET
            c.dimension = row.dimension,
            c.source = row.source,
            c.competence = row.competence,
            c.description = row.description
            """)
    print("Create competences")
    session.execute_write(create_competences)

    def create_units(tx):
        return tx.run("""
            LOAD CSV WITH HEADERS
            FROM "file:///employees.csv"
            AS row
            MERGE (u:Unit {unitName: row.unit})
            """)
    print("Create units")
    session.execute_write(create_units)

    def create_employees(tx):
        return tx.run("""
            LOAD CSV WITH HEADERS
            FROM "file:///employees.csv"
            AS row
            MERGE (e:Employee {employeeId: row.id})
            ON CREATE SET
            e.name = row.name,
            e.surname = row.surname
            WITH e, row
            MATCH (u:Unit {unitName: row.unit})
            MERGE (e)-[r:IN_UNIT]->(u)
            """)
    print("Create employees")
    session.execute_write(create_employees)

    def load_assignments(tx):
        cypher = """
            LOAD CSV WITH HEADERS
            FROM "file:///assignment.csv"
            AS row
            MATCH (e:Employee {employeeId: row.employee_id})
            MATCH (c:Competence {competenceId: row.competence_id})
            MERGE (e)-[r:HAS_COMPETENCE]->(c)
            ON CREATE SET r.level = row.level
        """
        return tx.run(cypher)
    print("Load assignments")
    session.execute_write(load_assignments)
    
    def load_interest(tx):
        cypher = """
            LOAD CSV WITH HEADERS
            FROM "file:///assignment.csv"
            AS row
            WITH row WHERE row.interest = "1"
            MATCH (e:Employee {employeeId: row.employee_id})
            MATCH (c:Competence {competenceId: row.competence_id})
            MERGE (e)-[r:INTERESTED_IN]->(c)
        """
        return tx.run(cypher)
    print("Load interest")
    session.execute_write(load_interest)

driver.close()
