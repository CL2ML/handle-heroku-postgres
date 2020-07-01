"""
Collection of SQL commands that can be imported by the main scripts
"""

create_table_cmd = """CREATE TABLE plant_specs 
            (id SERIAL PRIMARY KEY,
	        botanical_name VARCHAR (100) NOT NULL,
	        common_name VARCHAR (100) NOT NULL,
	        light_requirements VARCHAR (50),
	        water_requirements VARCHAR (50),
	        additional_characteristics VARCHAR,
	        blossom_color VARCHAR (50),
	        best_time_to_plant VARCHAR (50),
	        fragrance VARCHAR (25),
	        mature_size VARCHAR (25),
	        fertilizing_need VARCHAR (355),
	        air_humidity VARCHAR (50),
	        direct_sunlight BOOLEAN,
	        at_window BOOLEAN,
	        avg_temperature VARCHAR (25),
	        toxic BOOLEAN,
	        cats BOOLEAN,
	        dogs BOOLEAN,
	        children BOOLEAN,
	        climate_origin VARCHAR (50),
	        repotting_need VARCHAR (100))"""


check_tables_cmd = """SELECT *
        FROM pg_catalog.pg_tables
        WHERE schemaname != 'pg_catalog'
        AND schemaname != 'information_schema';"""


check_table_columns_cmd = """SELECT	COLUMN_NAME, DATA_TYPE 
                FROM information_schema.COLUMNS
                WHERE TABLE_NAME = 'plant_specs';
               """
