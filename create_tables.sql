CREATE TABLE CUSTOMER   (   C_ID            INTEGER NOT NULL, 
                            C_ADDRESS       VARCHAR(40) NOT NULL,
                            C_NAME          CHAR(25) NOT NULL,
                            C_EMAIL         CHAR(40) NOT NULL,
				    		C_MONEY_SPENT   DECIMAL(15,2) NOT NULL);
 
CREATE TABLE ORDERS     (   O_NUM_ITEMS  INTEGER NOT NULL,
                            C_ID         INTEGER NOT NULL,
                            P_ID         INTEGER NOT NULL,
                            O_SHIPDATE    DATE NOT NULL,
                            O_DELIVERDATE  DATE NOT NULL,
                            O_ORDERDATE DATE NOT NULL);
 
CREATE TABLE PRODUCTS   (   P_ID          INTEGER,
                            P_NAME        VARCHAR(152),
							P_BRAND       VARCHAR(50),
                            P_DESCRIPTION VARCHAR(300),
							p_IMG_URL     VARCHAR(152),
							P_COST        DECIMAL(15,2),
                            P_QUANTITY    INTEGER,
				    		P_INSTOCK     BOOLEAN);

CREATE TABLE CART       (   CART_ID       INTEGER,
                            P_ID          INTEGER,
                            C_ID          INTEGER);