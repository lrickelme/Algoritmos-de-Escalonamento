from Scheduler import Scheduler

class Scheduler_SJF(Scheduler):

  def get_shortest_process(self,list):
    short = list[0]
    for process in list:
      if short["tempo_execucao"] > process["tempo_execucao"]:
        short = process
    
    return short

  def SJF(self):
    while any([process["executado"] == False for process in self.process]):
      queue_process = self.put_list_process()
      if len(queue_process) == 0 :
        self.current_time += 1
        self.idle_time += 1
      else:
          job = self.get_shortest_process(queue_process)
          self.idle_time += self.switch_time
          self.current_time += self.switch_time
          job.update({"tempo_retorno" : self.current_time + job.get("tempo_execucao")})
          job.update({"tempo_espera": self.current_time - job.get("tempo_chegada")})
          job.update({"tempo_restante": job.get("tempo_restante") - job.get("tempo_execucao")})
          job.update({"executado" : True})
          self.current_time += job.get("tempo_execucao")
          print("Processo Executado:", job ,sep=" ")
          self.SJF()

process_number = int(input("Digite o número de processos que deseja executar: "))

sc = Scheduler_SJF()
sc.create_process(process_number)
sc.SJF()
sc.show_logs()