import random

class Scheduler:
  
  def __init__(self):
    self.process = [];
    self.initial_time = 0;
    self.switch_time = 1;
    self.current_time = 0;
    self.idle_time = 0

  def create_process(self, number_process):
    for i in range(number_process):
      self.process.append({
          'id': i + 1,
          'tempo_chegada': random.randint(1, 20),
          'tempo_execucao': random.randint(1, 20),
          'tempo_retorno': 0,
          'tempo_espera': 0,
          'executado': False
      })
    for j in range(len(self.process) - 1):
      for k in range(len(self.process) - j - 1):
        if self.process[k]['tempo_chegada'] > self.process[k + 1]['tempo_chegada']:
            self.process[k], self.process[k + 1] = self.process[k + 1], self.process[k]
  
  def calculate_avarage(self):
    arrival_time = 0
    return_time = 0
    wait_time = 0
    for process in self.process:
      arrival_time += process["tempo_chegada"]
      return_time += process["tempo_retorno"]
      wait_time += process["tempo_espera"]
    
    return {"av_arrival_time": arrival_time / len(self.process),
            "av_return_time": return_time / len(self.process), 
            "av_wait_time": wait_time / len(self.process) }


  def show_logs(self):
    for i in self.process:
      print(i)

    results = self.calculate_avarage()

    print(f"Tempo médio de chegada: {results['av_arrival_time']:.2f}")
    print(f"Tempo médio de retorno: {results['av_return_time']:.2f}")
    print(f"Tempo médio de espera: {results['av_wait_time']:.2f}")
    print(f"Tempo de ociosidade do processador: {self.idle_time}")
    print(f"Tempo total de troca de processos: {self.switch_time}")