log=fr"D:\Indixpert 2025\Indixpert_Dec_Batch_2024_Restaurant_Management_System\Src\Logs\logs.txt"

def writelogs(logs):
    with open(log, "a") as file:
        file.write(logs + "\n")