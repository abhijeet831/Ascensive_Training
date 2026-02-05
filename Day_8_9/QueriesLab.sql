-- table creation
CREATE TABLE departments (
	dept_id SERIAL PRIMARY KEY,
	dept_name VARCHAR(50)
	
);

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY,
	emp_name VARCHAR(50),
	salary INT,
	dept_id INT REFERENCES departments(dept_id)
);






-- insert query
INSERT INTO departments (dept_name) Values ('HR'),('IT'),('Finances');



INSERT INTO employees (emp_name , salary , dept_id) VALUES ('Amit',50000,1),('Riya','70000',2),('Karan',60000,2),('Neha',55000,3);





--select query
SELECT * FROM employees

SELECT * FROM departments

SELECT * FROM employees ;

SELECT emp_name , salary FROM employe




-- where

SELECT * FROM employees WHERE salary > 60000 ;

SELECT * FROM employees WHERE dept_id = 2 ;





-- order by

SELECT * FROM employees ORDER BY salary DESC ;


-- limit

SELECT * FROM employees ORDER BY salary DESC LIMIT 2;


--- update

UPDATE employees
SET salary = 75000
WHERE emp_name = 'Riya';

SELECT * FROM employees WHERE emp_name = 'Riya' ;



-- Delete

DELETE FROM employees 
WHERE emp_name = 'Neha';

SELECT * FROM employees ;



-- Joins

-- inner join
Select e.emp_name ,e.salary ,d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id ;




-- left join

SELECT e.emp_name,d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id


--right join

SELECT e.emp_name , d.dept_name
FROM employees e
RIGHT JOIN departments d
ON e.dept_id = d.dept_id


--AGREGATE FUNCTIONS
SELECT dept_id , AVG(salary)
FROM employees
GROUP BY dept_id;

SELECT COUNT(*) FROM employees ;

SELECT dept_id , MAX(salary)
FROM employees
GROUP BY dept_id ;


--normal join
SELECT e.emp_name , d.dept_name 
FROM employees e , departments d
WHERE e.dept_id = d.dept_id ;
















