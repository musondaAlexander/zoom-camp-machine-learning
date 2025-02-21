import PyInstaller.__main__

PyInstaller.__main__.run([
    'calculator_usage.py',
    '--onefile',
    '--windowed',
    '--name=AdvancedCalculator'
]) 