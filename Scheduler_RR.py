from Scheduler import Scheduler

class Scheduler_RR(Scheduler):
  def get_queue_process(self):
    queue_process = self.put_list_process()
    while len(queue_process) == 0:
      self.current_time += 1
      self.idle_time += 1
      queue_process = self.put_list_process()
    return queue_process

  def Round_Robin(self, quantum):
      queue_process = self.get_queue_process()
      count = 0
      while any([process["executado"] == False for process in self.process]):
        job = queue_process[count]
        self.idle_time += self.switch_time
        self.current_time += self.switch_time
        if job.get("tempo_espera") == 0 and job.get("tempo_restante") == job.get("tempo_execucao"): 
          job.update({"tempo_espera": self.current_time - job.get("tempo_chegada")})
        job.update({"tempo_restante": job.get("tempo_restante") - quantum if job.get("tempo_restante") - quantum >= 0 else 0})
        if job["tempo_restante"] == 0:
          job.update({"executado" : True})
          job.update({"tempo_retorno" : self.current_time + job.get("tempo_execucao")})
          print("Processo Executado:", job ,sep=" ")
          count -= 1
        self.current_time += quantum
        queue_process = self.put_list_process()
        if count + 1 >= len(queue_process):
          count = 0
        else: 
          count += 1

sc = Scheduler_RR()
sc.create_process(5)
sc.Round_Robin(4)
sc.show_logs()