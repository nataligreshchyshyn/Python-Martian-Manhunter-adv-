SELECT
    a.*,
    c.title AS category
FROM
    articles a
LEFT JOIN
    article_categories ac
    ON a.id = ac.article_id
LEFT JOIN
    category c
    ON c.id = ac.category_id;