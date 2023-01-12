-- creates a trigger that decreases quantity of an item
-- after adding a new order
CREATE TRIGGER dec_quantity 
AFTER INSERT ON orders
FOR EACH ROW 
UPDATE items 
SET quantity = quantity-New.number
WHERE name=New.item_name;