-- Sample user
INSERT INTO users (email, password_hash) VALUES
('demo@rivalscan.ai', 'hashed_password_123');

-- Sample product
INSERT INTO products (user_id, name, our_price)
VALUES (
    (SELECT id FROM users WHERE email = 'demo@rivalscan.ai'),
    'Smart Sensor X',
    149.99
);

-- Sample competitor price
INSERT INTO competitor_prices (user_id, product_name, competitor_price)
VALUES (
    (SELECT id FROM users WHERE email = 'demo@rivalscan.ai'),
    'Smart Sensor X',
    139.99
);
