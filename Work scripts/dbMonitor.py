# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:43:44 2020

@author: Gerardo

    SQL DB monitoring script
        Thi is an adhoc script that will run queries on the specified DB providing necessary health status of the DB
"""

import pyodbc
import sys
from collections import OrderedDict


# Defining Variables

connection = OrderedDict()
connection[""] = ""
connection[""] = ""


queries = list()
# query.append("Select top 1 * from trade")
queries.append("SELECT es.session_id ,es.login_name ,es.host_name ,er.blocking_session_id ,er.wait_type ,er.command, "
             "CASE es.transaction_isolation_level "
             "WHEN 0 THEN 'Unspecified' "
             "WHEN 1 THEN 'ReadUncommitted' "
             "WHEN 2 THEN 'ReadCommitted' "
             "WHEN 3 THEN 'Repeatable' "
             "WHEN 4 THEN 'Serializable' "
             "WHEN 5 THEN 'Snapshot' END AS transaction_isolation_level "
             ",OBJECT_NAME(st.objectid, er.database_id) as object_name "
             "FROM sys.dm_exec_connections ec LEFT OUTER JOIN sys.dm_exec_sessions es ON ec.session_id = es.session_id "
             "LEFT OUTER JOIN sys.dm_exec_requests er ON ec.connection_id = er.connection_id "
             "OUTER APPLY sys.dm_exec_sql_text(sql_handle) st "
             "OUTER APPLY sys.dm_exec_query_plan(plan_handle) ph "
             "WHERE ec.session_id <> @@SPID AND es.status = 'running'ORDER BY es.session_id;")
queries.append("SELECT db_name(b.database_id) as DbName,"
             "case b.type_desc when 'ROWS' then 'DATA' else type_desc end as Space_Type, "
             "cast(CAST(sum(CAST(FILEPROPERTY(a.name, 'SpaceUsed')/131072.0 AS DECIMAL(10,2)))/"
             "sum(CAST(a.size/131072.0 AS DECIMAL(10,2)))*100 AS DECIMAL(10,2)) as varchar(10))+'%' AS Percent_Used,"
             "cast(100 - CAST(sum(CAST(FILEPROPERTY(a.name, 'SpaceUsed')/131072.0 AS DECIMAL(10,2)))/"
             "sum(CAST(a.size/131072.0 AS DECIMAL(10,2)))*100 AS DECIMAL(10,2)) as varchar(10))+'%' AS Percent_Free "
             "FROM sysfiles a join master.sys.master_files b on a.fileid = b.file_id "
             "where db_name(b.database_id) = DB_NAME() "
             "group by b.database_id, b.type_desc order by b.database_id desc, b.type_desc desc;")
queries.append("SELECT ar.replica_server_name, adc.database_name,drs.is_primary_replica, drs.synchronization_state_desc,"
             "drs.synchronization_health_desc, redo_queue_size_KB, drs.last_commit_time, drs.recovery_lsn "
             "FROM sys.dm_hadr_database_replica_states AS drs "
             "INNER JOIN sys.availability_databases_cluster AS adc "
             "ON drs.group_id = adc.group_id "
             "AND drs.group_database_id = adc.group_database_id INNER JOIN sys.availability_groups AS ag "
             "ON ag.group_id = drs.group_id INNER JOIN sys.availability_replicas AS ar "
             "ON drs.group_id = ar.group_id AND drs.replica_id = ar.replica_id "
             "ORDER BY ag.name, ar.replica_server_name, adc.database_name;")


sleepTimeMinutes = 30  # Minutes to wait between calls
threshold = 0.5  # percentage threshold for queues


# Do not change this values
sleepTime = sleepTimeMinutes * 60


while True:
    for srv, db in connection.items():
        # Connecting to server
        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=" + srv + ";"
                              "Database=" + db + ";"
                              "Trusted_Connection=yes;")
        # Creating cursor and executing query
        cursor = cnxn.cursor()
        print(queries[0])
        cursor.execute(queries[0])


        for row in cursor:
            print('row = %r' % (row,))

