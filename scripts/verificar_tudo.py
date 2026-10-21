"""Executa os verificadores do projeto, pesquisa e formatação, sem publicar."""
from pathlib import Path
import importlib.util
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    python = sys.executable
    if not importlib.util.find_spec('PIL'):
        candidates = [ROOT/'.venv/Scripts/python.exe', ROOT/'.venv/bin/python']
        python = next((str(p) for p in candidates if p.is_file()), None)
        if python is None:
            raise SystemExit('Os testes de imagens requerem Pillow no Python ou no ambiente .venv.')
    commands = [[python, str(ROOT/'scripts/verificar.py')]]
    commands += [[python, str(p)] for p in sorted((ROOT/'testes').glob('verificar_*.py'))]
    node = shutil.which('node')
    prettier = ROOT/'node_modules/prettier/bin/prettier.cjs'
    if not node or not prettier.is_file():
        raise SystemExit('Node.js e Prettier são necessários. Execute npm ci antes de verificar.')
    commands += [[node, '--test', 'testes/pesquisa.test.cjs'],
                 [node, str(prettier), '--check', '**/*.html']]
    for command in commands:
        subprocess.run(command, cwd=ROOT, check=True)
    print('OK: verificações técnicas, pesquisa e formatação concluídas.')

if __name__ == '__main__':
    main()
