nofnof = "NöfNöf"
import simpleaudio, math

class KlinoffMath:
    wave_obj = simpleaudio.WaveObject.from_wave_file("nofnof.wav")
    
    @staticmethod
    def add(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a + b}\nAdded!! {nofnof}")

    @staticmethod
    def subtract(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a - b}\nSubtracted!! {nofnof}")

    @staticmethod
    def multiply(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a * b}\nMultiplied!! {nofnof}")

    @staticmethod
    def divide(a, b):
        if b == 0:
            play_obj = KlinoffMath.wave_obj.play()
            play_obj.wait_done()
            raise ValueError(f"Division by zero is not allowed... {nofnof} I am displeased {nofnof}")
        return print(f"{a / b}\nDivided!! {nofnof}")
    
    @staticmethod
    def power(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a ** b}\nPowered!! {nofnof}")
    
    @staticmethod
    def root(a, b):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{a ** (1/b)}\nRooted!! {nofnof}")
    
    @staticmethod
    def factorial(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.factorial(a)}\nFactorialized!! {nofnof}")
    
    @staticmethod
    def sin(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.sin(a)}\nSined!! {nofnof}")
    
    @staticmethod
    def cos(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.cos(a)}\nCosined!! {nofnof}")
    
    @staticmethod
    def tan(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.tan(a)}\nTanned!! {nofnof}")
    
    @staticmethod
    def asin(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.asin(a)}\nAsined!! {nofnof}")
    
    @staticmethod
    def acos(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.acos(a)}\nAcosed!! {nofnof}")
    
    @staticmethod
    def atan(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.atan(a)}\nAtaned!! {nofnof}")
    
    @staticmethod
    def log(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.log(a)}\nLogged!! {nofnof}")
    
    @staticmethod
    def lg(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.log10(a)}\nLogged10!! {nofnof}")
    
    @staticmethod
    def ln(a):
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.log1p(a)}\nLogged1p!! {nofnof}")
    
    @staticmethod
    def π():
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.pi}\nπ!! {nofnof}")
    
    @staticmethod
    def e():
        play_obj = KlinoffMath.wave_obj.play()
        play_obj.wait_done()
        return print(f"{math.e}\ne!! {nofnof}")
    