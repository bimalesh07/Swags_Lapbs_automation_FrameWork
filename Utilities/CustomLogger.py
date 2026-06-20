import logging
import os

class LogGen:

    # 1.THIS IS FOR UI TESTING 
    @staticmethod
    def loggen():
        # Yeh line automatic tumhare project ka main absolute path nikalega
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_dir = os.path.join(base_dir, "Logs")
        log_file_path = os.path.join(log_dir, "automation.log")

        # Agar Logs folder nahi hai toh sahi jagah banao
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logger = logging.getLogger("SwagLabsAutomation")
        
        if logger.hasHandlers():
            logger.handlers.clear()
            
        logger.setLevel(logging.INFO)
        
        # Sahi absolute path ka use karo
        file_handler = logging.FileHandler(log_file_path, mode='a', encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        return logger  # 👈 Aur haan, iske aage jo 'this corrent na' text box mein likha tha use hata dena 😜