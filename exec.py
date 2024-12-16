from cx_Freeze import setup, Executable
# pour fournir un exécutable python necessite cx_Freeze pip install cx_Freeze
build_exe_options = {
    "packages": ["socket", "time", "subprocess", "platform", "os"],
    "excludes": ["tkinter", "unittest"],  
}

setup(
    name="MonProgramme",
    version="1.0",
    description="Programme avec des fonctionnalitÃ©s rÃ©seau et systÃ¨me",
    options={"build_exe": build_exe_options},
    executables=[Executable("client.py", base="Win32GUI")],  
)
