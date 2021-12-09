create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl2;
''')

create_table_movie_list = ('''
    DROP SCHEMA IF EXISTS petl2 CASCADE;
    
    CREATE SCHEMA IF NOT EXISTS petl2;
    
    DROP TABLE IF EXISTS petl2.movie_list;
    
    CREATE TABLE IF NOT EXISTS petl2.movie_list (
        title TEXT,
        rated TEXT,
        released DATE, 
        runtime INT,
        genre TEXT[],
        director TEXT,
        writers TEXT[],
        actors TEXT[],
        plot TEXT,
        awards TEXT,
        poster TEXT
    );
''')

insert_movie = ('''
    INSERT INTO petl2.movie_list
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
''')