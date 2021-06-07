SELECT * FROM users
WHERE is_developer = 1;


INSERT INTO phone_companies (name) 
VALUES ('xiaomi'), ('apple'), ('samsung');


INSERT INTO phones (phone_name, company_id, user_id)
VALUES  ('Xiaomi Redmi Note 9', 1, 3),
        ('IPhone 8', 2, 4),
        ('Galaxy S21 Ultra', 3, 1);


SELECT * FROM phones
WHERE company_id =
    (SELECT c.id
    FROM phone_companies c
    WHERE c.name = 'xiaomi');


SELECT * FROM users
WHERE id IN 
    (SELECT user_id
    FROM phones);
