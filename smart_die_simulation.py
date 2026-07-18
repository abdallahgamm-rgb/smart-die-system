# smart_die_simulation.py
import random
import time

class ToolSimulator:
    def __init__(self, tool_id="DIE_001"):
        self.tool_id = tool_id
        self.force = 100.0
        self.temperature = 50.0
        self.wear = 0.0
        
    def read_sensors(self):
        # Simuler des données de capteurs
        self.force = random.uniform(80, 160)
        self.temperature = random.uniform(30, 100)
        self.wear = self.wear + random.uniform(0.5, 2.0)
        
        return {
            "tool_id": self.tool_id,
            "force": round(self.force, 1),
            "temperature": round(self.temperature, 1),
            "wear": round(self.wear, 1)
        }

if __name__ == "__main__":
    tool = ToolSimulator()
    print("🔧 Smart Die System - Simulation démarrée")
    for i in range(20):
        data = tool.read_sensors()
        print(f"🔧 {data['tool_id']} - Force: {data['force']}N, Temp: {data['temperature']}°C, Usure: {data['wear']}%")
        
        if data['wear'] > 80:
            print("🚨 ALERTE ROUGE: Usure > 80% - REMPLACER L'OUTIL IMMÉDIATEMENT!")
        elif data['wear'] > 60:
            print("⚠️ ALERTE ORANGE: Usure > 60% - Prévoir remplacement")
        
        time.sleep(1)
    print("✅ Simulation terminée")
