CREATE USER areopuertos_user WITH PASSWORD 'admin123';
CREATE DATABASE areopuertos_db OWNER areopuertos_user;

\c areopuertos_db

ALTER SCHEMA public OWNER TO areopuertos_user;
GRANT ALL ON SCHEMA public TO areopuertos_user;
GRANT CREATE ON SCHEMA public TO areopuertos_user;

ALTER DEFAULT PRIVILEGES FOR USER areopuertos_user IN SCHEMA public
GRANT ALL ON TABLES TO areopuertos_user;

ALTER DEFAULT PRIVILEGES FOR USER areopuertos_user IN SCHEMA public
GRANT ALL ON SEQUENCES TO areopuertos_user;

ALTER DEFAULT PRIVILEGES FOR USER areopuertos_user IN SCHEMA public
GRANT ALL ON FUNCTIONS TO areopuertos_user;
