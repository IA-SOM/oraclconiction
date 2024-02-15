#!/bin/bash

# Wait for Oracle Database to start up
sleep 30s

# Set environment variables
ORACLE_SID=FREE
ORACLE_PDB=FREEPDB1
ORACLE_USER=sys
ORACLE_PASSWORD=samir5636123

# SQL script to create user and grant privileges
sqlplus / as sysdba <<EOF
CREATE USER samir IDENTIFIED BY samir;
GRANT CREATE SESSION TO samir;
GRANT CREATE TABLE TO samir;
GRANT DROP TABLE TO samir;
GRANT ALTER ANY TABLE TO samir;
EXIT;
EOF