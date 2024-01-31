
# `competence-kg`: a tutorial on Knowledge Graphs

This repository contains the material for the "Knowledge Graphs Course" erogated by [Cefriel](https://cefriel.com/). An example scenario (`Competence Registry`) is considered to implement and discuss modelling and querying over relational databases, graph databases and triplestores. The main topics are:
- **Relational Databases** using [Postgres](https://www.postgresql.org/) (CSV import and SQL queries)
- **Graph Database** using [Neo4j](https://neo4j.com/) (Graph modelling, CSV import and Cypher queries)
- **RDF Database** using [RDFLib](https://pypi.org/project/rdflib/) (KG construction from CSV file, SPARQL queries)
- [_Bonus_] **Natural language QA** using [LangChain](https://www.langchain.com/) (querying different databases using the OpenAI API)

If you are interested in the course associated with this repository get in contact or send an email to [info@cefriel.com](mailto:info@cefriel.com).

## The `Competence Registry` scenario

A company would like to keep a record of the digital competences possessed by each employee. Each employee is described by their first name, last name, and the department they belong to.
Each competence defined by the [DigComp](https://joint-research-centre.ec.europa.eu/digcomp/digcomp-framework_en) framework is described through four main fields: identifier, dimension, name, and description.
Each employee can be associated with one or more competences. For each competence association, the following information can be provided: competence level (from 1 to 5) and the person's interest in gaining/increasing the skill.

## How to run the code
The repository defines a `docker-compose.yml` file to run all the databases and the Jupyter notebooks as containers via Docker. The containers can be run all at once or separately.

The notebooks can be executed running the `competence-kg-notebook` container with the command:
```bash
docker-compose up --force-recreate competence-kg-notebook
```

## Data
The data are randomly generated via the script available in the `notebooks/competence-kg-generate.ipynb` notebook. A constant `seed` is currently defined to always generate the default data contained in the `data` folder.

The files `employees.csv`, `assignment.csv` and `competences.csv` contain the data. The `*-iri.csv` files are generated to support the discussion on the RDF graph.

## Relational Database
The relational database is modelled according to the ER diagram defined in the `model` folder. The diagram can be edited using the `draw.io` webapp.

An `init.sql` file is defined to initialise a `Postgres` database from the CSV files in the `data` folder. The database can be executed using the command:
```bash
docker-compose up --force-recreate competence-kg-postgres
```
Note that if the option `--volumes` is not used with the command `docker-compose down` the status of the database is automatically persisted by Docker.

The `competence-kg-postgres.ipynb` notebook contains the code to inspect and query the database using the `SQL` syntax.

## Graph Database
The graph database is modelled according to the diagram defined in the `model` folder. The diagram can be edited using the [arrows.app](https://arrows.app/) webapp.

The `competence-kg-neo4j.ipynb` notebook contains the code to import the data and to inspect and query the database. A `Neo4j` database is instantiated using the CSV files in the `data` folder and according to the graph model defined. The `Cypher` language is used to query the database.

The database can be executed using the command:
```bash
docker-compose up --force-recreate competence-kg-neo4j
```

The status of the database is automatically persisted in the `neo4j` folder as defined in the `docker-compose.yml` file. The folder can be deleted to erase all the data in the database.

## RDF Database
The graph database is modelled according to the ontology `ontology.ttl` defined in the `model` folder and available online at [https://knowledge.c-innovationhub.com/competence-kg/schema](https://knowledge.c-innovationhub.com/competence-kg/schema). The ontology reuses the `foaf` vocabulary and adds further classes and properties. The ontology can be visualised using the [WebVOWL](http://vowl.visualdataweb.org/webvowl.html) webapp. In the `model` folder the file `content-negotiation.sh` shows how different cURL requests return different representations of the ontology.

The `competence-kg-rdf.ipynb` notebook contains the code to construct the knowledge graph and to inspect and query the it. An in-memory database is instantiated using the [RDFLib](https://pypi.org/project/rdflib/) library and the CSV files in the `data` folder. In this case, the `*-iri.csv` files are considered instead of the `assignment.csv` and `competences.csv` files. Indeed, we leverage the SKOS vocabulary describing the DigComp framework (already [available online](http://publications.europa.eu/resource/dataset/digital-competence-framework)) to enrich the company's graph without having to instantiate from the CSV all the data about the competences. 

The mappings from the CSV files to the ontology are defined using YARRRML, compiled to RML using the [yatter](https://github.com/oeg-upm/yatter) tool and executed using the [morph-kgc](https://github.com/morph-kgc/morph-kgc) processor. The mappings are available in `mappings` folder. The `SPARQL` language is used to query the database.

The generated RDF graphs are serialised in the Turtle format and saved in the `rdf` folder together with a dump of the DigComp SKOS vocabulary.

## LangChain QA
The `competence-kg-langchain.ipynb` notebook provides the code to execute QA (i.e., natural language querying) over the three databases leveraging the `langchain` library and the OpenAI GPT models. The `SQLDatabaseChain`, `GraphCypherQAChain`, `GraphSPARQLQAChain` are used in the code.

A `credentials.json` file should be provided in the main folder with a valid key for the OpenAI API.
```
{
    "OPENAI_API_KEY": "PUT_HERE_YOUR_KEY"
}
```
