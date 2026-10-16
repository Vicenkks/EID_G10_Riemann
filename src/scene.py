import subprocess
import sys
import shutil

def check_command(cmd):
    """Verifica si un comando está disponible"""
    # Usar shutil.which es más confiable
    if not shutil.which(cmd):
        print(f"❌ {cmd} NO está en el PATH")
        return False
    
    try:
        # FFmpeg usa -version, no --version
        result = subprocess.run(
            [cmd, "-version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✅ {cmd}: {version_line}")
            return True
        else:
            print(f"⚠️ {cmd} retornó código {result.returncode}")
            return False
    except Exception as e:
        print(f"⚠️ Error verificando {cmd}: {e}")
        return False

print("=" * 60)
print("Verificando dependencias del sistema...")
print("=" * 60)

system_ok = [
    check_command("ffmpeg"),
    check_command("pdflatex"),
]

print("\n" + "=" * 60)
print("Verificando dependencias de Python...")
print("=" * 60)

python_ok = []

try:
    import manim
    print(f"✅ manim {manim.__version__}")
    python_ok.append(True)
except ImportError:
    print("❌ manim NO está instalado")
    python_ok.append(False)

try:
    import pydub
    print("✅ pydub instalado")
    python_ok.append(True)
except ImportError:
    print("❌ pydub NO está instalado")
    python_ok.append(False)

print("\n" + "=" * 60)
all_ok = system_ok + python_ok

if all(all_ok):
    print("🎉 ¡Todo listo! Puedes renderizar con Manim.")
else:
    print("⚠️ Faltan algunas dependencias.")
print("=" * 60)