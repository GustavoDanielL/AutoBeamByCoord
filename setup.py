from cx_Freeze import setup, Executable

setup(
    name="BeamAuto",
    version="1.0",
    description="Descrição do seu programa",
    executables=[Executable("VerificaBeam.py", icon="brasil.ico")],
)
