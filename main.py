from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_untitledtts import Ui_UntitledTTS
from threading import Thread
from threading import Timer
import sys
import pyttsx3
import time
import tempfile
import atexit
import os
import pyaudio
import wave


def update_devices():
    devices = []
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device = p.get_device_info_by_index(i)
        if device["hostApi"] == 0 and device["maxInputChannels"] == 0:
            devices.append(device)
    return devices, p.get_default_output_device_info()


class UntitledTTS(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_UntitledTTS()
        self.ui.setupUi(self)
        
        self.version = "0.1.0"
        
        self.temp = tempfile.mktemp(suffix=".wav")
        
        get_output_name = lambda o: o["name"]
        self.output_list, self.output = update_devices()
        self.output_name = list(map(get_output_name, self.output_list))
        self.output_index = self.output_name.index(self.output["name"])
        
        self.CHUNK = 1024
        
        self.engine = pyttsx3.init()
        
        self.voices_list = self.engine.getProperty("voices")
        get_voice_name = lambda v: v.name
        get_voice_id = lambda v: v.id
        self.voices_name = list(map(get_voice_name, self.voices_list))
        self.voices_id = list(map(get_voice_id, self.voices_list))
        
        self.wait_time = 0
        self.rate = 200
        self.volume = 1.0
        self.voice = self.engine.getProperty("voice")
        self.voice_index = self.voices_id.index(self.voice)
        self.voice_index_default = self.voice_index
        self.property_update()
        
        self.is_saying = False
        
        self.ui.voicesComboBox.addItems(self.voices_name)
        self.ui.voicesComboBox.setCurrentIndex(self.voice_index)
        self.ui.outputComboBox.addItems(self.output_name)
        self.ui.outputComboBox.setCurrentIndex(self.output_index)
        
        self.ui.rateSlider.valueChanged.connect(self.rate_value_update)
        self.ui.rateSlider.sliderReleased.connect(self.property_update)
        self.ui.volumeSlider.valueChanged.connect(self.volume_value_update)
        self.ui.volumeSlider.sliderReleased.connect(self.property_update)
        self.ui.voicesComboBox.currentIndexChanged.connect(self.voice_update)
        self.ui.outputComboBox.currentIndexChanged.connect(self.output_update)
        self.ui.waitTimeSpinBox.valueChanged.connect(self.wait_time_update)
        self.ui.sayButton.clicked.connect(self.say_button_pressed)
        self.ui.resetButton.clicked.connect(self.reset_tts)
        self.ui.aboutButton.clicked.connect(self.about)
    
    def reset_tts(self):
        self.wait_time = 0
        self.rate = 200
        self.volume = 1.0
        self.voice = self.engine.getProperty("voice")
        self.voice_index = self.voice_index_default
        self.voice = self.voices_list[self.voice_index]
        self.property_update()
        
        self.ui.waitTimeSpinBox.setValue(self.wait_time)
        self.ui.rateSlider.setValue(self.rate)
        self.ui.volumeSlider.setValue(int(self.volume * 100))
        self.ui.voicesComboBox.setCurrentIndex(self.voice_index)
        
        self.ui.outputComboBox.clear()
        get_output_name = lambda o: o["name"]
        self.output_list, device = update_devices()
        self.output_name = list(map(get_output_name, self.output_list))
        self.ui.outputComboBox.addItems(self.output_name)
        self.output = device
        self.output_index = self.output_name.index(self.output["name"])
        self.ui.outputComboBox.setCurrentIndex(self.output_index)
    
    def status_change(self, enable):
        self.ui.outputComboBox.setEnabled(enable)
        self.ui.voicesComboBox.setEnabled(enable)
        self.ui.rateSlider.setEnabled(enable)
        self.ui.volumeSlider.setEnabled(enable)
        self.ui.waitTimeSpinBox.setEnabled(enable)
        self.ui.resetButton.setEnabled(enable)
        self.ui.aboutButton.setEnabled(enable)
        self.ui.sayButton.setText("说话" if enable else "暂停")
    
    def say_button_pressed(self):
        text = self.ui.readTextEdit.toPlainText()
        if text:
            if self.is_saying:
                self.is_saying = False
            else:
                self.is_saying = True
                t = Thread(target=self.tts, args=(text,))
                t.start()
    
    def tts(self, text):
        self.status_change(False)
        
        time_start = time.time()
        
        self.engine.save_to_file(text, self.temp)
        self.engine.runAndWait()

        p = pyaudio.PyAudio()
        wf = wave.open(self.temp)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True,
                        output_device_index=self.output["index"])
        
        time_end = time.time()
        delta_time = time_end - time_start
        sleep_time = 0
        if delta_time < self.wait_time:
            sleep_time = self.wait_time - delta_time
        timer = Timer(sleep_time, self.play_wav, (wf, stream))
        timer.start()
        
        while self.is_saying:
            pass
        timer.cancel()
        
        stream.close()
        p.terminate()
        
        self.status_change(True)
        self.is_saying = False
    
    def play_wav(self, wf, stream):
        data = wf.readframes(self.CHUNK)
        while len(data) and self.is_saying:
            stream.write(data)
            data = wf.readframes(self.CHUNK)
        self.is_saying = False
    
    def property_update(self):
        self.engine.setProperty("rate", self.rate)
        self.engine.setProperty("volume", self.volume)
        self.engine.setProperty("voice", self.voice)
    
    def rate_value_update(self):
        self.rate = self.ui.rateSlider.value()
        self.ui.rateLabel.setText(f"{self.rate}字/min")
    
    def volume_value_update(self):
        self.volume = self.ui.volumeSlider.value() / 100
        self.ui.volumeLabel.setText(f"{self.ui.volumeSlider.value()}%")
    
    def voice_update(self):
        self.voice_index = self.ui.voicesComboBox.currentIndex()
        self.voice = self.voices_id[self.voice_index]
        self.property_update()
    
    def output_update(self):
        self.output_index = self.ui.outputComboBox.currentIndex()
        self.output = self.output_list[self.output_index]
    
    def wait_time_update(self):
        self.wait_time = self.ui.waitTimeSpinBox.value()
    
    def about(self):
        QMessageBox.about(self, "关于UntitledTTS", "只是一个TTS软件。\n"
                                                   "......\n"
                                                   f"version {self.version}")
    
    def closeEvent(self, event):
        self.is_saying = False
        event.accept()
    
    def remove_temp(self):
        try:
            os.remove(self.temp)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    utts = UntitledTTS()
    atexit.register(utts.remove_temp)
    utts.show()
    sys.exit(app.exec())
