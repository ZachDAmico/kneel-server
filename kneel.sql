-- CREATE TABLE `Metals`
-- (
--     `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `metal` NVARCHAR(160) NOT NULL,
--     `price` NUMERIC(5,2) NOT NULL
-- );

-- CREATE TABLE `Styles`
-- (
--     `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
--     `style` NVARCHAR(160) NOT NULL,
--     `price` NUMERIC(3,2) NOT NULL
-- );
-- with NUMERIC, 10 is total number of digits, and 2 is the number of digits after decimal
-- similar to FLOAT, but more exact being a fixed decimal
CREATE TABLE styles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  style VARCHAR,
  price NUMERIC(10, 2)
);

CREATE TABLE sizes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  carets NUMERIC(10, 2),
  price NUMERIC(10, 2)
);

CREATE TABLE metals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  metal VARCHAR,
  price NUMERIC(10, 2)
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  styleId INT,
  metalId INT,
  sizeId INT,
  FOREIGN KEY (styleId) REFERENCES styles(id),
  FOREIGN KEY (metalId) REFERENCES metals(id),
  FOREIGN KEY (sizeId) REFERENCES sizes(id)
);

INSERT INTO styles (style, price) VALUES ('Solitaire', 149.99);
INSERT INTO styles (style, price) VALUES ('Halo', 199.99);
INSERT INTO styles (style, price) VALUES ('Vintage', 179.99);
INSERT INTO styles (style, price) VALUES ('Modern', 159.99);
INSERT INTO styles (style, price) VALUES ('Three-Stone', 169.99);


INSERT INTO sizes (carets, price) VALUES (0.5, 19.99);
INSERT INTO sizes (carets, price) VALUES (1.0, 29.99);
INSERT INTO sizes (carets, price) VALUES (1.5, 39.99);
INSERT INTO sizes (carets, price) VALUES (2.0, 49.99);
INSERT INTO sizes (carets, price) VALUES (2.5, 59.99);


INSERT INTO metals (metal, price) VALUES ('Gold', 99.99);
INSERT INTO metals (metal, price) VALUES ('Silver', 59.99);
INSERT INTO metals (metal, price) VALUES ('Platinum', 149.99);
INSERT INTO metals (metal, price) VALUES ('Titanium', 69.99);
INSERT INTO metals (metal, price) VALUES ('Stainless Steel', 39.99);

INSERT INTO orders (styleId, metalId, sizeId) VALUES (1, 3, 2);
INSERT INTO orders (styleId, metalId, sizeId) VALUES (4, 2, 4);
INSERT INTO orders (styleId, metalId, sizeId) VALUES (2, 1, 1);
INSERT INTO orders (styleId, metalId, sizeId) VALUES (5, 5, 3);
INSERT INTO orders (styleId, metalId, sizeId) VALUES (3, 4, 5);


-- all selects are for testing purposes
SELECT 
styles.id,
styles.style,
styles.price,
o.id orderId,
o.styleId,
o.customerId,
o.metalId,
o.sizeId
FROM styles 
JOIN orders o
ON styles.id = o.styleId;

SELECT 
sizes.id,
sizes.carets,
sizes.price,
o.id orderId,
o.styleId,
o.customerId,
o.metalId,
o.sizeId
FROM sizes
JOIN orders o
ON sizes.id = o.sizeId;

SELECT 
metals.id,
metals.metal,
metals.price,
o.id orderId,
o.styleId,
o.customerId,
o.metalId,
o.sizeId
FROM metals
JOIN orders o 
ON metals.id = o.metalId;

SELECT 
id,
styleId,
metalId,
sizeId,
timestamp
FROM orders;

SELECT
                    o.id,
                    o.metalId,
                    o.styleId,
                    o.sizeId,
                    o.timestamp,
                    m.id AS metalId,
                    m.metal,
                    m.price as metal_price,
                    s.id AS sizeId,
                    s.carets,
                    s.price as size_price,
                    st.id AS styleId,
                    st.style,
                    st.price as style_price
                    FROM Orders o
                    LEFT JOIN Metals m ON o.metalId = m.id
                    LEFT JOIN Sizes s ON o.sizeId = s.id
                    LEFT JOIN Styles st ON o.styleId = st.id
                    WHERE o.id = 3;




