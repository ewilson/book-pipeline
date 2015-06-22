CREATE TABLE book_staging (
  id INT NOT NULL,
  section_id INT,
  author VARCHAR(50),
  title VARCHAR(50),
  section_title VARCHAR(200),
  para_text TEXT,
  section_text MEDIUMTEXT,
  PRIMARY KEY (id)
);
