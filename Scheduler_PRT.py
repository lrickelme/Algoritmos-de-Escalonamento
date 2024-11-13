from Scheduler import Scheduler

class Scheduler_Priority(Scheduler):

  def get_highest_priority_process(self, ready_list):
    highest_priority_process = ready_list[0]
    for process in ready_list:
        if process["prioridade"] < highest_priority_process["prioridade"]:
            highest_priority_process = process
    return highest_priority_process
  
  def Priority(self):
    while any([process["executado"] == False for process in self.process]):
      ready_process = self.put_list_process()
      if len(ready_process) == 0 :
        self.current_time += 1
        self.idle_time += 1
      else:
          process = self.get_highest_priority_process(ready_process)
          self.idle_time += self.switch_time
          self.current_time += self.switch_time
          process.update({"tempo_retorno" : self.current_time + process.get("tempo_execucao")})
          process.update({"tempo_espera": self.current_time - process.get("tempo_chegada")})
          process.update({"tempo_restante": process.get("tempo_restante") - process.get("tempo_execucao")})
          process.update({"executado" : True})
          self.current_time += process.get("tempo_execucao")
          print("Processo Executado:", process ,sep=" ")


process_number = int(input("Digite o número de processos que deseja executar: "))

sc = Scheduler_Priority()
sc.create_process(process_number)
sc.Priority()
sc.show_logs()