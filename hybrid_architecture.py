
from auto_scale_system import AutoScaler
from MainIntegrationLogic_QuantumSystemIntegrator import QuantumSystemIntegrator
from quantum_monitor import QuantumMonitor
import logging

class SelfHealingAI:
    def __init__(self):
        self.integrator = QuantumSystemIntegrator()
        self.auto_scaler = AutoScaler()
        self.quantum_monitor = QuantumMonitor()
        logging.info("Self-healing AI system initialized.")

    def start(self):
        logging.info("Starting self-healing AI system with hybrid architecture.")
        self.integrator.integrate()
        self.auto_scaler.scale_resources()
        self.quantum_monitor.monitor_quantum_system()
