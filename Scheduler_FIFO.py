from Scheduler import Scheduler

class Scheduler_FIFO(Scheduler):
  def FIFO(self):
    while any([process["executado"] == False for process in self.process]):
      queue_process = self.put_list_process()
      if len(queue_process) == 0 :
        self.current_time += 1
        self.idle_time += 1
      else:
        for job in queue_process:
          self.idle_time += self.switch_time
          self.current_time += self.switch_time
          job.update({"tempo_retorno" : self.current_time + job.get("tempo_execucao")})
          job.update({"tempo_espera": self.current_time - job.get("tempo_chegada")})
          job.update({"tempo_restante": job.get("tempo_restante") - job.get("tempo_execucao")})
          job.update({"executado" : True})
          self.current_time += job.get("tempo_execucao")
          print("Processo Executado:", job ,sep=" ")
    
sc = Scheduler_FIFO()
sc.create_process(5)
sc.FIFO()
sc.show_logs()