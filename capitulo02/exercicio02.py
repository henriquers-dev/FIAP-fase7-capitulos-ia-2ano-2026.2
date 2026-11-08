import pandas as pd
import pm4py

# Construção do dataset completo de event log
data = [
[1001, "Create Order", "2024-01-01 10:00:00", "System"],
[1001, "Approve Payment", "2024-01-01 10:05:00", "Gateway"],
[1001, "Pick Items", "2024-01-01 10:20:00", "Warehouse"],
[1001, "Ship Order", "2024-01-01 11:00:00", "Logistics"],
[1001, "Deliver Order", "2024-01-02 14:00:00", "Carrier"],

[1002, "Create Order", "2024-01-01 10:02:00", "System"],
[1002, "Approve Payment", "2024-01-01 10:06:00", "Gateway"],
[1002, "Cancel Order", "2024-01-01 10:10:00", "Customer"],

[1003, "Create Order", "2024-01-01 10:10:00", "System"],
[1003, "Approve Payment", "2024-01-01 10:15:00", "Gateway"],
[1003, "Pick Items", "2024-01-01 10:40:00", "Warehouse"],
[1003, "Ship Order", "2024-01-01 11:30:00", "Logistics"],
[1003, "Deliver Order", "2024-01-02 16:00:00", "Carrier"]
]

columns = ["case_id", "activity", "timestamp", "resource"]

# Criação do DataFrame
log_df = pd.DataFrame(data, columns=columns)

# Conversão do timestamp para formato datetime
log_df["timestamp"] = pd.to_datetime(log_df["timestamp"])

# Ordenação dos eventos por caso e tempo
log_df = log_df.sort_values(by=["case_id", "timestamp"])

# Visualização do log estruturado
print("Event Log Estruturado:\n")
print(log_df)

# Conversão para formato compatível com mineração de processos
event_log = pm4py.format_dataframe(
log_df,
case_id="case_id",
activity_key="activity",
timestamp_key="timestamp"
)

# Exportação para XES
pm4py.write_xes(event_log, "event_log_example.xes")

print("\nArquivo XES gerado com sucesso.")
