from dataclasses import dataclass

@dataclass(slots=True)
class Project:
    name: str      
    payment: int    
    client: str

    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}...")