SELECT  u.id user_id,
        u.first_name,
        u.last_name,
        u.email user_email,
        u.is_admin,
        p.id product_id,
        p.title product_title,
        p.meta_title product_meta_title,
        p.description,
        p.price,
        p.old_price,
        p.is_active product_is_active,
        pi.id image_id,
        pi.file path_to_image,
        pi.alt,
        c.id category_id,
        c.title category_title,
        c.image category_image,
        c.meta_title category_meta_title,
        c.description category_description,
        c.is_active category_is_active
FROM users u 
INNER JOIN products p 
    ON u.id = p.user_id 
INNER JOIN product_images pi 
    ON p.id = pi.product_id 
INNER JOIN categories_products cp 
    ON p.id = cp.product_id
INNER JOIN categories c 
    on c.id = cp.category_id;