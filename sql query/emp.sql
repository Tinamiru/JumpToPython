CREATE TABLE emp(
	e_id INT,
	e_name VARCHAR(20),
	sex VARCHAR(1),
	addr VARCHAR(200)
);

INSERT into emp (
	e_id,
	e_name,
	sex,
	addr
)
VALUE (
	3,
	3,
	3,
	3
);emp

UPDATE emp
	SET e_name = 4,
		 sex = 4,
		 addr = 4
 WHERE e_id = 4;
 
 DELETE FROM emp
 WHERE e_id = 3;