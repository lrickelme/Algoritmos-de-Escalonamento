from Scheduler import Scheduler
import random

class Scheduler_LOT(Scheduler):
    def get_random_process(self, ready_processes):
        return random.choice(ready_processes)
    
    def LOT(self):
        while any(not process["executado"] for process in self.process):
            ready_processes = self.put_list_process()
            
            if len(ready_processes) == 0:
                self.current_time += 1
                self.idle_time += 1
            else:
                job = self.get_random_process(ready_processes)
                self.idle_time += self.switch_time
                self.current_time += self.switch_time
                job["tempo_retorno"] = self.current_time + job["tempo_execucao"]
                job["tempo_espera"] = self.current_time - job["tempo_chegada"]
                job["executado"] = True
                self.current_time += job["tempo_execucao"]
                
                print("Processo Executado:", job, sep=" ")

process_number = int(input("Digite o número de processos que deseja executar: "))

sc = Scheduler_LOT()
sc.create_process(process_number)
sc.LOT()
sc.show_logs()