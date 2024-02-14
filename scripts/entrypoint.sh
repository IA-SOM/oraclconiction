#!/bin/bash

# Wait for Oracle Database to start up
sleep 30s

# Set environment variables
ORACLE_SID=FREE
ORACLE_PDB=FREEDB1
ORACLE_USER=sys
ORACLE_PASSWORD=samir5636123

# SQL script to create user and grant privileges
sqlplus / as sysdba <<EOF
CREATE USER ml_user IDENTIFIED BY ml_password;
GRANT CREATE SESSION TO ml_user;
GRANT CREATE TABLE TO ml_user;
GRANT DROP TABLE TO ml_user;
GRANT ALTER ANY TABLE TO ml_user;
EXIT;
EOF